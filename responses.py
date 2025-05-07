import discord
import random

class Responses:
    def random_gm_response():
        return random.choice(Responses.good_morning_responses)

    def random_gm_warning():
        return random.choice(Responses.good_morning_warnings)

    def random_hype_reaction():
        return random.choice(Responses.emojis["hype"])

    good_morning_responses = [
        "gm gaymer",
        "gm",
        "Good Morning",
        "Have a lovely morning, beautiful :homiekissh:",
        "Sup bby get out there and have a good day *towel whips your booty* :angelman:",
        "Good morning, don't let me catch you down in the dumps king",
        "Good morning to everyone except people who don't say good morning",
        "Luv u bby <3"
    ]

    good_morning_warnings = [
        "Bruh, go say good morning right now",
        "Ain't no way you out here typing without saying good morning :ShrekStare:",
        "Dude, how can you just come out here and start your day without a good morning?",
        "Bots have feelings too, go say good morning right now",
        "What, you homophobic or something? Go say gm right now and get your kiss :homiekissh:"
    ]

    emojis = {
        "hype": {
            "letsgo" : 1368313034883334236
        },
        "misc" : {
            "homiekiss" : 1367947655875137547
        }
    }
