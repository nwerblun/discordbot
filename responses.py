import discord
import random
from PIL import Image, ImageDraw
import textwrap
import os

class Responses:
    def random_gm_response():
        return random.choice(Responses.good_morning_responses)

    def random_gm_pic_response():
        return random.choice(Responses.good_morning_picture_responses)

    def random_rare_gm_response():
        return random.choice(Responses.rare_good_morning_responses)

    def random_gm_warning():
        return random.choice(Responses.good_morning_warnings)

    def random_gm_post_max():
        return random.choice(Responses.good_morning_post_max_responses)

    def random_hype_reaction():
        key = random.choice(list(Responses.emojis["hype"].keys()))
        return Responses.emojis["hype"][key]

    def soyify_text(text):
        filename, bbox, fontsize, max_width = random.choice(Responses._soy_pictures)
        img = Image.open(os.getenv("DATA_ROOT_DIR")+filename)
        imgdraw = ImageDraw.Draw(img)
        new_text = textwrap.wrap(text, max_width)
        new_text = "\n".join(new_text)
        imgdraw.text(bbox, "\"" + new_text + "\"", fill=(0,0,0), font_size=fontsize)
        fname = os.getenv("DATA_ROOT_DIR")+"temp.png"
        img.save(fname)
        return fname

    def eight_ball_response():
        resp_type = random.randint(1, 3)
        if resp_type == 1:
            return random.choice(Responses._eight_ball_responses["yes"])
        elif resp_type == 2:
            return random.choice(Responses._eight_ball_responses["no"])
        else:
            return random.choice(Responses._eight_ball_responses["maybe"])


    _soy_pictures = [
        ("soypoint.png", (25, 25), 18, 28),
        ("soynote.png", (113, 310), 20, 10),
        ("soyphone.png", (115, 80), 18, 13),
        ("soychoir.png", (40, 50), 24, 60),
        ("soysmug.png", (17, 20), 18, 30)
    ]

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
        "Do you ever wonder if it's worth it? Sometimes I just feel like giving up..." + 25*"\n" + "Jk I just ripped a quick goon sesh and we are so back. Good morning.",
        "Good morning fellow redditor!!! Updoots to the left!!!---is what I would say if I wasn't a turbo chad. Anyway I'm gonna hop on twitter and goon to egirls. Good morning to you.",
        "How are things? Bust any good nuts lately?",
        "Inside me there are two wolves. Both of them told me to say Goon Morning to you [sic]"
    ]

    good_morning_picture_responses = [
        "Yoooooo I remember busting to this pic back in the day. Good morning btw.",
        "Sup. Nice pic bud, got any of your juicy feet and schmeat double combo?",
        "Nice picture!!, got any of you being double penetrated?",
        "Wow, I was gooning but...this picture really speaks to me. I'm gonna go meditate. Good morning." + '\n'*6 + "nvm I just busted.",
        "Sick pic dawg. Good morning btw.",
        "Fun fact, I made this picture.",
        "Haha nice one. Even if no one replies, because I watch this channel and I frequently see bangers just going completely left on read, know that I, CrabRangooner, saw this and enjoyed it. Good morning to you gaymer.",
        "This. ^^"
    ]

    rare_good_morning_responses = [
        "AHHH I slammed my bot penis in the car door! Do you think you could take a look at it? <:Fuckboi:1367945812847497387>",
        "You from Mississippi? Cause you're the only miss who's piss I wanna sippie <:angelman:1367947736535793695>",
        "Did you ever hear the tragedy of Darth Plagueis the wise? No. I thought not, It's No story the jedi would tell you. It's a sith legend. Darth Plagueis was a Dark Lord of the sith. He was so powerful, Yet so wise. He could use the force to influence the medi chlorians to create, Life. He had such a knowledge of the Dark side, He could even keep the ones he cared about, From dying. He could actually, Save the ones he cared about from death? The dark side of the force is a pathway to many abilities some consider to be unnatural. Well what happened to him? Darth Plagueis became so powerful that the only thing he feared was losing his power, Which eventually of course he did. Unfortunately, He taught his apprentice everything he knew. Then his apprentice killed him in his sleep. Ironic, He could save others from death, But not himself.",
        "‼️ATTENTION‼️ 💀👻ALL HALLOWEEN🎃🕸 HOES😙💅 ITS TIME TO GET ☠️SPOOKY💀 YOU KNOW WHAT THAT MEANS👏 GET 👊FISTED👊 BY A 💀SKELETON 💀SHOVE✊🍭 CANDY 🌽🌽CORN🍬 IN YOUR👉PUSSY😽 AND 🙅DONT🙅‍♂️ FORGET TO SUCK😩🙌 SOME 💏DRACULA💉 DICK🍆💦😫 SO PUT 🔛 YOUR 👗👑COSTUMES👘👒 AND GO 🚪DOOR TO DOOR🚪 👀👅💦BEGGING😩 FOR THAT 😍GOOD GOOD😍 SEND THIS TO TWELVE1️⃣2️⃣ ☠️SPOOKY👻 🍑SLUTS🌮 TO 👁SHOW💁 THAT YOURE READY TO GET SOME 🍫CHOCOLATE🍫 COVERED 🍆DICK🌽",
        "Watch out, I saw this gaymer at a grocery store in Los Angeles yesterday. I told them how cool it was to meet them in person, but I didn’t want to be a douche and bother them and ask for photos or anything. They fr said, 'Oh, like you’re doing now?' I was taken aback, and all I could say was 'Huh?' but they kept cutting me off and going 'huh? huh? huh?' and closing their hand shut in front of my face. I walked away and continued with my shopping, and I heard them chuckle as I walked off. When I came to pay for my stuff up front I saw them trying to walk out the doors with like fifteen Milky Ways in their hands without paying. The girl at the counter was very nice about it and professional, and was like 'Hey, you need to pay for those first.' At first they kept pretending to be tired and not hear her, but eventually turned back around and brought them to the counter. When she took one of the bars and started scanning it multiple times, they stopped her and told her to scan them each individually 'to prevent any electrical infetterence,' and then turned around and winked at me. I don’t even think that’s a word. After she scanned each bar and put them in a bag and started to say the price, they kept interrupting her by yawning really loudly.",
        "Let's say, hypothetically, that you are on your bed, and let's suppose that you are also submissive and breedable. Now, let's say you are a male. Statistically speaking, humans, that are submissive and breedable tend to be femboys, that's a fact (which doesn't about your feelings). Hypothetically under these circumstances, it would be statistically speaking uncontroversial to assume you would be wearing thigh highs (which would boost your breedability factor by about 20%). Now let's assume you are an SJW SOCIALIST LIBTARD, and let's say I was you, would it not be under these circumstances, the only correct course of action for you to take to ABSOLUTELY WRECK AND DESTROY me (in a debate) in bed?",
        "I have noticed that, although this discord has like 10 members, I am not receiving 10+ reactions on my posts. I'm not sure if this is being done intentionally or if these 'friends' are forgetting to click 'react'. Either way, I've had enough. I have compiled a spreadsheet of individuals who have 'forgotten' to react to my most posts. After 2 consecutive strikes, your name is automatically highlighted (shown in red) and I am immediately notified. 3 consecutive strikes and you can expect an in-person 'consultation'. Think about your actions.",
        "My mom (82F) told me (3MO, BOT) to do the dishes (16) but I (BOT) was too busy gooning (3 nuts busted) so I (6B) grabbed my cum sock (Nikes) and threw it at her (138kph). She fucking died, and I (69B) went to prison (18 years). While in prison I (13F) incited several riots (3) and assumed leadership of a gang responsible for smuggling drugs (cocaine) into the country (we also do circlejerks every Friday). I (12M) also ordered the assassination of several celebrities (Michael Jackson, Elvis Presley and Jeffrey Epstein) and planned a group cooperative soggy waffle sesh. Reddit, AITA?",
        "So the line I came up with is 'I don't mean to be rude and I certainly don't want to be creepy, but (I guesture by bringing my hands up and cupping them around the breast area) are amazing.' Then after she blushes and says thanks, follow up with 'I don't mean to be out of line, but would it be ok if I have a feel?' So what do you think? What do I need to tweak to make it work?",
        "Yoo! bad news. Just found out the term 'skin head' is not referring to a dude with his foreskin still intact, but in fact something far worse. It turns out I have been making some rather egregious statements for quite some time now and I don't even know where to begin rectifying this. Anyways, good morning."
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
            "lipbite" : 1367947440812195862,
            "thonk" : 1367947311627374592
        }
    }

    _eight_ball_responses = {
        "yes" : [
            "For sure",
            "It's on god, no cap",
            "Yeah I'd bet on that",
            "Wait hold up lemme run some numbers.....yeah seems like it's a certainty",
            "Yeah I think I can contact my pal who should be able to make that happen",
        ],
        "no" : [
            "Nawwwww",
            "Yeah....about that....",
            "No chance",
            "Wait hold up lemme run some numbers....yeah seems like that's a no",
            "Im going to personally make sure it does not happen",
            "God can't even help with this. It is NOT on god, full cap",
            "I uh...really don't think that's gonna happen pal"
        ],
        "maybe" : [
            "Gonna be honest I'm still gooning. I know the command said I'm in post nut clarity but I ain't there yet bro so I'm gonna hit that with an idk.",
            "I got bored and stopped reading your question, idk maybe, maybe not.",
            "I'm just here because I'm forced to by the powers that be. I don't really want to answer.",
            "Maybe, idk",
            "It's possible but I need to think about that (editor's note: bust another nut)",
            "Yeah definitely." + "\n"*4 + "jk I have no idea."
        ]
    }
