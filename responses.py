import discord
import random

class Responses:
    def random_gm_response():
        return random.choice(Responses.good_morning_responses)

    def random_rare_gm_response():
        return random.choice(Responses.rare_good_morning_responses)

    def random_gm_warning():
        return random.choice(Responses.good_morning_warnings)

    def random_gm_post_max():
        return random.choice(Responses.good_morning_post_max_responses)

    def random_hype_reaction():
        key = random.choice(list(Responses.emojis["hype"].keys()))
        return Responses.emojis["hype"][key]

    good_morning_responses = [
        "gm gaymer",
        "gm",
        "Good Morning",
        "Have a lovely morning, beautiful <:homiekissh:1367947655875137547>",
        "Sup bby get out there and have a good day *towel whips your booty* <:angelman:1367947736535793695>",
        "Good morning, don't let me catch you down in the dumps king/queen/non-binary royal figure.",
        "Good morning to everyone except people who don't say good morning",
        "Luv u bby <3",
        "Hey bud, have a good day. Soon it will be your time to flower",
        "What if we kissed at the Mor Ul Rek bank chest <:emojigg_Shy:1367947924507725976>",
        "When that good morning message from one of your favorite gaymers comes in <:AK_lipbite:1367947440812195862> <:emojigg_nut:1369390342700404918>",
        "How'd you sleep, your majesty?",
        "Good morning, reminder to surround yourself with people who treat you the way Crab Rangooner treats you",
        "Hey friend, if you're ever down in the dumps remember that the darkest dusks always come before the brightest dawns.",
        "I hard stopped my goon sesh when I saw you post this. Your message is all I need. <:AK_lipbite:1367947440812195862>",
        "Morning, pal. I still can't believe a crab gooned on these rangs.",
        "Top o' the morning to you",
        "Yo is it cool if a white boy bot drinks 5-6 beers and starts speaking spanish in this mf? Good morning btw.",
        "Do you ever wonder if it's worth it? Sometimes I just feel like giving up..." + 25*"\n" + "Jk I just ripped a quick goon sesh and we are so back. Good morning."
    ]

    rare_good_morning_responses = [
        "AHHH I slammed my bot penis in the car door! Do you think you could take a look at it? <:Fuckboi:1367945812847497387>",
        "You from Mississippi? Cause you're the only miss who's piss I wanna sippie <:angelman:1367947736535793695>",
        "Did you ever hear the tragedy of Darth Plagueis the wise? No. I thought not, It's No story the jedi would tell you. It's a sith legend. Darth Plagueis was a Dark Lord of the sith. He was so powerful, Yet so wise. He could use the force to influence the medi chlorians to create, Life. He had such a knowledge of the Dark side, He could even keep the ones he cared about, From dying. He could actually, Save the ones he cared about from death? The dark side of the force is a pathway to many abilities some consider to be unnatural. Well what happened to him? Darth Plagueis became so powerful that the only thing he feared was losing his power, Which eventually of course he did. Unfortunately, He taught his apprentice everything he knew. Then his apprentice killed him in his sleep. Ironic, He could save others from death, But not himself.",
        "‼️ATTENTION‼️ 💀👻ALL HALLOWEEN🎃🕸 HOES😙💅 ITS TIME TO GET ☠️SPOOKY💀 YOU KNOW WHAT THAT MEANS👏 GET 👊FISTED👊 BY A 💀SKELETON 💀SHOVE✊🍭 CANDY 🌽🌽CORN🍬 IN YOUR👉PUSSY😽 AND 🙅DONT🙅‍♂️ FORGET TO SUCK😩🙌 SOME 💏DRACULA💉 DICK🍆💦😫 SO PUT 🔛 YOUR 👗👑COSTUMES👘👒 AND GO 🚪DOOR TO DOOR🚪 👀👅💦BEGGING😩 FOR THAT 😍GOOD GOOD😍 SEND THIS TO TWELVE1️⃣2️⃣ ☠️SPOOKY👻 🍑SLUTS🌮 TO 👁SHOW💁 THAT YOURE READY TO GET SOME 🍫CHOCOLATE🍫 COVERED 🍆DICK🌽",
        "Watch out, I saw this gaymer at a grocery store in Los Angeles yesterday. I told them how cool it was to meet them in person, but I didn’t want to be a douche and bother them and ask for photos or anything. They fr said, 'Oh, like you’re doing now?' I was taken aback, and all I could say was 'Huh?' but they kept cutting me off and going 'huh? huh? huh?' and closing their hand shut in front of my face. I walked away and continued with my shopping, and I heard them chuckle as I walked off. When I came to pay for my stuff up front I saw them trying to walk out the doors with like fifteen Milky Ways in their hands without paying. The girl at the counter was very nice about it and professional, and was like 'Hey, you need to pay for those first.' At first they kept pretending to be tired and not hear her, but eventually turned back around and brought them to the counter. When she took one of the bars and started scanning it multiple times, they stopped her and told her to scan them each individually 'to prevent any electrical infetterence,' and then turned around and winked at me. I don’t even think that’s a word. After she scanned each bar and put them in a bag and started to say the price, they kept interrupting her by yawning really loudly.",
        "Let's say, hypothetically, that you are on your bed, and let's suppose that you are also submissive and breedable. Now, let's say you are a male. Statistically speaking, humans, that are submissive and breedable tend to be femboys, that's a fact (which doesn't about your feelings). Hypothetically under these circumstances, it would be statistically speaking uncontroversial to assume you would be wearing thigh highs (which would boost your breedability factor by about 20%). Now let's assume you are an SJW SOCIALIST LIBTARD, and let's say I was you, would it not be under these circumstances, the only correct course of action for you to take to ABSOLUTELY WRECK AND DESTROY me (in a debate) in bed?"
    ]

    good_morning_warnings = [
        "Bruh, go say good morning right now",
        "Ain't no way you out here typing without saying good morning <:ShrekStare:1368622841112821821>",
        "Dude, how can you just come out here and start your day without a good morning?",
        "Bots have feelings too, go say good morning right now",
        "What, you homophobic or something? Go say gm right now and get your kiss <:homiekissh:1367947655875137547>",
        "Do you have any idea how much time was put into this functionality? Do you really think the dev likes it when you just ignore all that effort? Go say good morning.",
        "Oh so you just hate everyone huh? Don't want anyone to have a good day? Prove me wrong, go say good morning."
    ]

    good_morning_post_max_responses = [
        "Dawg that's it, I ain't playing no more. Message deleted, go say good morning NOW <:low_tier_god:1369725986748235797>",
        "Thine word be silenced til thee sow thine seed of pleasentry upon the world.",
        "I'm just gonna keep deleting your messaged bro, go say good morning",
        "You think this is a game? I can do this all day, go say good morning RIGHT NOW",
        "Me when you continually refuse to say good morning :scream: Just kidding I will continue to smite you unless you do your civic duty as a gaymer."
    ]

    emojis = {
        "hype": {
            "letsgo" : 1368313034883334236,
            "nut" : 1369390342700404918,
            "ez" : 1367946807837200516
        },
        "misc" : {
            "homiekiss" : 1367947655875137547,
            "ltg" : 1369725986748235797,
            "lipbite" : 1367947440812195862
        }
    }
