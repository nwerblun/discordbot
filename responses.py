import discord
import random

class Responses:
    def random_gm_response():
        return random.choice(Responses.good_morning_responses)

    def random_gm_warning():
        return random.choice(Responses.good_morning_warnings)

    def random_gm_post_max():
        return random.choice(Responses.good_morning_post_max_responses)

    def random_hype_reaction():
        return random.choice(Responses.emojis["hype"])

    good_morning_responses = [
        "gm gaymer",
        "gm",
        "Good Morning",
        "Have a lovely morning, beautiful <:homiekissh:1367947655875137547>",
        "Sup bby get out there and have a good day *towel whips your booty* <:angelman:1367947736535793695>",
        "Good morning, don't let me catch you down in the dumps king",
        "Good morning to everyone except people who don't say good morning",
        "Luv u bby <3"
    ]

    good_morning_warnings = [
        "Bruh, go say good morning right now",
        "Ain't no way you out here typing without saying good morning <:ShrekStare:1368622841112821821>",
        "Dude, how can you just come out here and start your day without a good morning?",
        "Bots have feelings too, go say good morning right now",
        "What, you homophobic or something? Go say gm right now and get your kiss <:homiekissh:1367947655875137547>"
    ]

    good_morning_post_max_responses = [
        "Dawg that's it, I ain't playing no more. Message deleted, go say good morning NOW <:low_tier_god:1369725986748235797>",
        "Thine word be silenced til thee sow thine seed of pleasentry to the world",
        "I'm just gonna keep deleting your messaged bro, go say good morning",
        "You think this is a game? I can do this all day, go say good morning RIGHT NOW"

    ]

    emojis = {
        "hype": {
            "letsgo" : 1368313034883334236,
            "nut" : 1369390342700404918
        },
        "misc" : {
            "homiekiss" : 1367947655875137547,
            "ltg" : 1369725986748235797

        }
    }
