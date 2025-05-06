import discord
from discord.ext import tasks
import datetime
import os
from pickledb import AsyncPickleDB
from reaction_map import ReactionMap

class GoonClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tree = discord.app_commands.CommandTree(self)
        self._register_commands()
        if not kwargs["db"] is None:
            self.db = AsyncPickleDB(kwargs["db"])
        self.verbosity = int(os.getenv("VERBOSITY"))

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print("--------")
        print("Registering commands...")
        print("--------")

    async def on_message(self, msg: discord.Message):
        if (await self._user_has_role(msg.author, "guest")) or \
        (await self._user_has_role(msg.author, "Bots")):
            return

        if msg.author.id != self.user.id:
            if msg.channel.name == "good-morning":
                await self._assign_gm_role(msg)
            else:
                await self._reply_with_gm_response_or_clear(msg)
            if msg.channel.name == "are-we-up":
                await self._letsgo(msg)


    @tasks.loop(time=datetime.time(hour=0))
    async def revoke_gm_roles(self):
        gm_role = await self._fetch_role("said gm")
        async for mem in gd.fetch_members():
            await mem.remove_roles(r)
        if self.verbosity > 0:
            print("Removed gm roles")

    async def _letsgo(self, msg: discord.Message):
        await msg.add_reaction(await msg.guild.fetch_emoji(ReactionMap.emojis["letsgo"]))

    async def _fetch_role(self, role_name: str):
        gd = await self.fetch_guild(int(os.getenv("GUILD_ID")))
        roles = await gd.fetch_roles()
        desired_role = None
        for r in roles:
            if r.name == role_name:
                desired_role = r
        return desired_role

    async def _user_has_role(self, user: discord.Member, role_name: str):
        has_role = await self._fetch_role(role_name) in user.roles
        if self.verbosity > 1:
            print("checking if user ", user, " has role ", role_name, "....", has_role)
        return has_role

    async def setup_hook(self):
        gd = await self.fetch_guild(int(os.getenv("GUILD_ID")))
        self.tree.copy_global_to(guild=gd)
        await self.tree.sync()

    async def _assign_gm_role(self, msg):
        gm_role = await self._fetch_role("said gm")
        if not (await self._user_has_role(msg.author, "said gm")):
            await msg.author.add_roles(gm_role)
            await msg.reply("gm gaymer")
            await msg.add_reaction(await msg.guild.fetch_emoji(ReactionMap.emojis["homiekiss"]))
            await self._reply_with_gm_response_or_clear(msg)
            if self.verbosity > 0:
                print("added gm role to " + msg.author.name)

    async def _reply_with_gm_response_or_clear(self, msg):
        if self.db is None:
            raise discord.ClientException("Could not open database while checking gm responses")

        exepmts = await self.db.aget("gm_exempts")
        if (not exepmts is None) and (msg.author.id in exepmts):
            if self.verbosity > 0:
                print("user", msg.author, " is exempted. Skipping")
            return

        main_dict = await self.db.aget("gm_resps")
        key = str(msg.author.id) + "_gm_responses"
        if main_dict is None:
            main_dict = {}
        if not (key in main_dict.keys()):
            main_dict[key] = []
        resps = main_dict[key]

        if not (await self._user_has_role(msg.author, "said gm")):
            resp = await msg.reply("Bruh, go say good morning right now")
            resps += [(resp.channel.id, resp.id)]
            main_dict[key] = resps
        elif (await self._user_has_role(msg.author, "said gm")):
            if not len(resps):
                return  # nothing to delete
            if self.verbosity > 1:
                print("Deleting ", len(resps), " gm messages to ", msg.author)
            for chan_id, msg_id in resps:
                if self.verbosity > 1:
                    print("In channel...", chan_id)
                chan_to_del = await self.fetch_channel(int(chan_id))
                if chan_to_del is not None:
                    if self.verbosity > 1:
                        print("message...", msg_id)
                    msg_to_del = await chan_to_del.fetch_message(int(msg_id))
                    if msg_to_del is not None:
                        if self.verbosity > 1:
                            print("Deleting msg ", msg_to_del)
                        await msg_to_del.delete()
                main_dict.pop(key, None)
        await self.db.aset("gm_resps", main_dict)
        if not await self.db.asave():
            print("WARNING: Failed to save db")

    def _register_commands(self):
        @self.tree.command(description="Clears a database entry by key. Requires admin perms.")
        @discord.app_commands.describe(
            db_key="Key of the database entry"
        )
        async def db_wipe_key(interaction: discord.Interaction, db_key: str):
            if interaction.permissions.administrator:
                await self.db.aremove(db_key)
                succeeded = await self.db.asave()
                if succeeded:
                    await interaction.response.send_message("Cleared DB Key " + db_key)
                else:
                    await interaction.response.send_message("Failed to clear db")
            else:
                await interactionl.response.send_message("Must be admin to use this command")

        """
        @self.tree.command(description="Clears the ENTIRE db.")
        async def purge_db(interaction: discord.Interaction):
            if interaction.permissions.administrator:
                await self.db.apurge()
                succeeded = await self.db.asave()
                if succeeded:
                    await interaction.response.send_message("Cleared DB")
                else:
                    await interaction.response.send_message("Failed to clear db")
            else:
                await interaction.response.send_message("Must be admin to use this command")
        """

        @self.tree.command(description="Exempt a user from gm")
        async def exempt_from_gm(interaction: discord.Interaction, mem: discord.Member):
            if interaction.permissions.administrator:
                if await self.db.aget("gm_exepmts") is None:
                    await self.db.aset("gm_exempts", [str(mem.id)])
                else:
                    await self.db.aset("gm_exempts",
                                       await self.db.aget("gm_exempts") + [str(mem.id)])
                succeeded = await self.db.asave()
                if succeeded:
                    await interaction.response.send_message("User @" + mem.name + " exempted from gm rules")
                else:
                    print("FAILED TO WRITE TO DB")

        @self.tree.command(description="Clear all user's gm status")
        async def wipe_gm_roles(interaction: discord.Interaction):
            if interaction.permissions.administrator:
                r = await self._fetch_role("said gm")
                async for mem in gd.fetch_members():
                    await mem.remove_roles(r)
                if self.verbosity > 0:
                    print("Removed gm roles")
                await interaction.response.send_message("best get into that gm channel my guy, I'll be watching.")
