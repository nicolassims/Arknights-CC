# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init 3 python:
    # Declare positions used by this game
    midleft = Position(xpos = 0.25)
    midright = Position(xpos = 0.75)

    # Declare variables used by this game
    playerfirstname = "You"
    playerlastname = "The Operator"

    aostaname = "Nervous Albino"
    brocaname = "Scowly Brunette"
    chiavename = "Shouty Redhead"

    doctor = 0
    killer = 0

    party = [aceop]

    inventory = []

    rocksickspared = None

    swearing = True

define who = Character("???")
define a = DynamicCharacter("playerfirstname")
define aosta = DynamicCharacter("aostaname")
define broca = DynamicCharacter("brocaname")
define chiave = DynamicCharacter("chiavename")
define narrator = nvl_narrator

# Backgrounds
image black = "#000000"
image white = "#ffffff"
image ruinedTent = im.Scale("bgs/ruinedtent.png", 1920, 1080)
image forest = im.Scale("bgs/forest.png", 1920, 1080)
image outcounty = im.Scale("bgs/outcounty.png", 1920, 1080)
image tactics = Transform("bgs/tactics.png", matrixcolor=SaturationMatrix(0), xsize=1920, ysize=1080)
image village = Transform("bgs/village.png", xsize=1920, ysize=1080)
image innervillage = Transform("bgs/village2.png", xsize=1920, ysize=1080)

# Characters
image ace = scaleportrait("chars/ace/ace.png", 190)
image ace shadow = scaleportrait("chars/ace/shadowace.png", 190)
image rocksick = scaleportrait("chars/rocksick/rocksick.png", 210)
image rocksick left = scaleportrait("chars/rocksick/rocksick.png", 210, True)
image chiave = scaleportrait("chars/chiave/chiave.png", 182)
image chiave shocked = scaleportrait("chars/chiave/shockedchiave.png", 182)
image chiave confused = scaleportrait("chars/chiave/confusedchiave.png", 182)
image chiave happy = scaleportrait("chars/chiave/happychiave.png", 182)
image broca = scaleportrait("chars/broca/broca.png", 189)
image broca angry = scaleportrait("chars/broca/angrybroca.png", 189)
image broca surprised = scaleportrait("chars/broca/surprisedbroca.png", 189)
image aosta left = scaleportrait("chars/aosta/aosta.png", 177, True)
image aosta nervous left = scaleportrait("chars/aosta/nervousaosta.png", 177, True)
image aosta surprised left = scaleportrait("chars/aosta/surprisedaosta.png", 177, True)
image aosta eyesclosed left = scaleportrait("chars/aosta/eyesclosedaosta.png", 177, True)

#Transitions
transform moveleft:
    linear 0.5 xpos 0.15

#CC == Contingency Contract && Catastrophe Caller

# The game starts here.

label start:

    scene black with Dissolve(2)

    a "...Ow."

    a "...Where am I?"

    play sound "audio/footstep.mp3"

    who "..."

    a "A noise! Hostiles? Damn it, where's my squad?"

    a "...Wait. Squad? Hostiles? What does any of that mean...?"

    show ace shadow with dissolve

    a "Agh. My head hurts like a son of a bitch. Don't tell me, I was out drinking too hard last night with..."

    a "With...?"

    nvl show dissolve

    "You scrape at the insides of your mind. You know this name. Of course you do. You've fought side by side a hundred times."

    "You have shared tears, laughter, rage, and despair. And, occasionally, a drink."

    "It would be ridiculous for you to forget her name."

    "And yet."

    nvl clear

    nvl show dissolve

    "{i}And yet.{/i}"

    nvl clear

    window hide dissolve

    a "Damn it... Where am I?"

    nvl show dissolve

    "You open your eyes."

    play music "audio/forest.mp3" loop

    nvl clear

    window hide dissolve

    show ruinedTent behind ace with Dissolve(2)

    show ace with dissolve

    a "...Hm. I'm in some shit, huh? A hammer, a shield, a whole lot of carbon-fiber body armor, and everything around me's torn to shreds."

    a "Don't know who I am, don't know where I am, and I don't know why I'm kitted out like this... but all this points to me having just walked out of a pretty tough fight."

    a "...Aw, shit, I don't know who I am. I don't even remember my name? What the hell happened?"

    a "Guess I better make something up..."

    label namechoice1:

    $ playerfirstname = renpy.input("My first name'll be...", allow='QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890-.', length=12).strip().title()

    if (playerfirstname == ""):
        a "I can't just say my name is nothing. If a man's got nothing else, he's got his name."

        jump namechoice1

    label namechoice2:

    $ playerlastname = renpy.input("Sure, sure. And my last name'll be...", allow='QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890-.', length=12).strip().title()

    if (playerlastname == ""):
        a "I can't just say my name is nothing. If a man's got nothing else, he's got his name."

        jump namechoice2

    a "%(playerfirstname)s %(playerlastname)s, huh?"

    a "...Looks like this uniform's got a patch that says \"Ace\" on it. What's that, a callsign?"

    a "And... \"Rhodes Island?\" Is that who I work with?"

    a "...Ugh. I better find someone who can point me in the right direction. And maybe tell me what the right direction is, too."

    show ace at midleft with ease

    call Crawl(guerroforest, 6, 3, guerroknowledge, True)

    show ace at center with ease

    show outcounty behind ace with dissolve

    a "Finally an end to all that grass and smoke. It's a miracle the whole forest didn't burn down from whatever caused... that."

    a "Looks like there's a village ahead. With any luck, they'll have a way to get in contact with these \"Rhodes Island\" people. Maybe they'll be able to tell me why I'm wearing their getup.\n...Maybe they'll have a paycheck for me."

    a "...What the hell is that running towards me?"

    hide ace with dissolve

    call Battle(party, [Operator(ROCKSICK, -5, False, [ rocklaw ])])

    show ace at midleft with dissolve

    window show

    a "...But what the hell did I just win against?"

    show rocksick left at midright with dissolve

    who "Aaaargh... Graaahh... Gurghh..."

    a "Seems like it's not in any further mood to fight... Or it can't, anyway. Those are some nasty wounds."

    a "...They're closing fast, though. I need to make a choice."

    menu:
        "{color=FF0000}Finish it.{/color}":
            show ace shadow with dissolve

            a "Can't risk this thing getting back up behind me."

            nvl show dissolve

            "Your hammer swings down."

            "And nothing gets back up."

            "{color=FF0000}Your heart shifts towards the path of a killer.{/color}"

            $ killer += 1

        "{color=27C4CC}Spare it.{/color}":
            $ rocksickspared = True

            a "It wasn't hard to beat the first time. If there's a second, it should be even easier."

            nvl show dissolve

            "The creature seems unable to comprehend your mercy. It continues to moan and writhe pitifully on the ground."

            "...You quickly move on."

            "{color=27C4CC}Your heart shifts towards the path of a doctor.{/color}"

            $ doctor += 1

    nvl clear

    hide rocksick with moveoutright

    show ace at center with ease

    "You continue moving toward the village. As you come closer, you can see that village may be too generous a term."

    "It's really more of a hamlet. A small, dilapidated little township with houses composed mostly of wood and old vehicles."

    window hide dissolve

    a "I'm not expecting much from the kind of folk you find out in the boonies like this, but maybe they'll be able to tell me what that thing was."

    a "..."

    show ace shadow with dissolve

    nvl show dissolve

    "You stop in your tracks. Walking into an unfamiliar situation like this could be suicide."

    "...You've had training that told you as much. Even if you don't remember it, your body does."

    nvl clear

    "You get into a cautious pose, ready for more combat, as you walk up to the village gates. They're small, wooden, and unguarded."

    scene village with dissolve

    show ace shadow with dissolve

    a "Damn. Where is everyone? Don't tell me that thing got to them before I did..."

    nvl show dissolve

    "The air is deathly silent in the village. Even the dust seems unwalked in."

    nvl clear

    "Still, as you gaze around at the architecture, you can't help but marvel at the ingenuity on display."

    "Yes, it looks like it was put together by children with only a rudimentary understanding of how power tools work..."

    "But the sheer breadth of materials used in the construction of the village is impressive, to say the least."

    window hide dissolve

    nvl clear

    show ace with dissolve

    a "...Huh. That building's door is a car's hood. I'm mostly just surprised to see that there are autos here."

    a "...Oh, we're here."

    nvl clear

    scene innervillage with dissolve

    show ace at midleft with dissolve

    nvl show dissolve

    "You came here with low expectations, and even those seem to have been dashed."

    "The village's silence is absolute. Not a peep can be heard from any of the buildings, and the level of disrepair they are unilaterally in is a strong indicator as to how utterly abandoned this place is."

    nvl clear

    "Now, on an unrelated subject, this game will occasionally delve into some grim material. Perhaps even moreso than {i}Arknights{/i} proper."

    "Sometimes, people will respond to this grim material through... inelegant means."

    "To wit: swearing."

    "Would you like this game to censor such swear words for you?"

    nvl clear

    menu:
        "Yes, please.":
            $ swearing = False

        "No, thanks.":
            $ swearing = True

    "Understood."

    $ renpy.say(a, "Fuck." if swearing else "****.")

    hide ace with dissolve

    a "Well... if there's nothing left here, I guess I might as well grab what I can and keep moving. Maybe there'll be a cannibalized refrigerator somewhere that still has rations."

    who "...Now."

    a "Huh!?"

    show chiave at center with vpunch

    chiave "{i}Prendilo!{/i}"

    show broca angry at midleft with hpunch

    broca "{b}{i}Prendilo!{/i}{/b}"

    show aosta nervous left at midright with dissolve

    aosta "Prendilo... wait, no, guys, this isn't him."

    show chiave shocked

    $ swearword = "fucking" if swearing else "****ing"

    menu:
        "Prendilo?":
            show aosta surprised left

            aosta "It means... well, it's impolite."

            show aosta eyesclosed left

            aosta "Sorry, sir. We thought you were someone else."

        "Prepare to %(swearword)s die, kiddos.":
            show aosta surprised left

            aosta "...Wait. Let's not do anything rash here. Chiave, that means you."

            $ chiavename = "Chiave"

            show chiave confused

            chiave "Hey, why are you looking at me like that?"

            show aosta eyesclosed

            aosta "It was your idea to jump an armed militant, since he, and I quote, \"was tall.\" Everything else about this guy makes it clear he's not our target."

        "Who am I not?":
            broca "...What kinda dumb question is that? You trying to be funny?"

            show aosta surprised left

            aosta "Calm down, Broca."

            $ brocaname = "Broca"

            show broca

            broca "...Nnrgh."

            show aosta eyesclosed left

            aosta "Sorry, sir. We thought you were someone else."

    show chiave confused

    $ renpy.say(chiavename, "Well, shit. If he's not {i}him{/i}, who is he, Aosta?" if swearing else "Well, ****. If he's not {i}him{/i}, who is he, Aosta?")

    $ aostaname = "Aosta"

    show aosta left

    aosta "Based on his clothing, a member of some low-level mercenary gang?"

    a "{size=20}Low level? This brat...{/size}"

    a "Who are you three? And who's your target?"

    chiave "Wait? You don't know us?"

    a "...Should I?"

    show chiave happy

    chiave "You will. Intros, guys!"

    show chiave with vpunch

    chiave "Chiave the chainbreaker! Leader of the premier Siracusan {i}famiglia{/i}, the freedom-fighting four!"

    show broca with vpunch

    broca "Broca the brusier. Enforcer and muscle of the 4F. I can bite through tires."

    show aosta eyesclosed left with vpunch

    aosta "Aosta. Tactician and strategist of the... {i}ugh...{/i} freedom-fighting four."

    $ aostaname = "Aosta"
    $ brocaname = "Broca"
    $ chiavename = "Chiave"

    menu:
        "Where's your fourth?":
            show chiave shocked

            aosta "I told you that was the first thing anyone would ask."

            show chiave happy

            chiave "Well... we fight like four people! Each!"

            a "Oh, yeah? Who are you fighting?"

        "I repeat. Who's your target?":
            show chiave shocked

            chiave "{size=20}He just... ignored us...{/size}"

            aosta "I told you that freedom fighters don't actually have intros."

            show chiave happy

        "Freedom fighters?":
            show chiave happy

            chiave "Yeah, the best in Siracusa!"

            a "...Okay, who are you kids fighting?"

    chiave "Our enemies are injustice and imperialism! Everything that ties a people down and makes them slaves to {b}the man!{/b}"

    a "You were going to try and kill injustice with some oversized construction equipment?"

    show broca surprised

    broca "No-one's tried it before."

    show aosta left

    aosta "We're still... getting started on the whole freedom-fighter thing. We thought you were an infected."

    scene white with vpunch

    nvl clear

    nvl show dissolve

    "Your head, almost in an instant, is split, stabbed through with excrutiating pain."

    "{b}Infected...{/b}"

    "You know this word. It means so much to you. And yet you can't remember {i}what{/i}."

    nvl hide dissolve

    scene innervillage with dissolve

    show broca surprised at midleft with dissolve

    show aosta surprised left at midright with dissolve

    show chiave confused at center with dissolve

    chiave "{size=15}...alr{/size}{size=20}ight? Hey, man, can{/size} you hear me?"

    a "...Just a headache. What's this \"infected\" you're talking about?"

    show chiave shocked

    chiave "You don't know what the infected are? Oh, man, lucky."

    show chiave

    chiave "The infected are these, like... ghouls. They've got these gross black crystals growing off of them, and they totally lose their minds. They try to eat people, y'know? We think that's what happened here."

    nvl clear

    nvl show dissolve

    "It seems clear that Chiave is referring to the beast you met in the woods."

    "You don't know why, but you feel, strongly, like you need to defend the infected."

    "However, since you called that creature in the forest \"it\", multiple times, you have little ground to stand on."

    "Still, you wonder..."

    nvl hide dissolve

    a "Right. How many infected have you met?"

    show chiave happy

    show aosta nervous left

    show broca

    $ renpy.say("Freedom-Fighting {s}Four{/s} Three", "One.")

    a "(Yeah, that's what I thought.)"

    if (rocksickspared):
        a "Well, you don't need to worry about that infected in the forest anymore. I dealt with it."

        show chiave shocked

        chiave "What? By yourself? Impressive!"

    a "You said you think that the people here were attacked by the infected. Where is here?"

    show chiave

    chiave "Like I told you, man. Siracusa."

    a "No, I mean this village."

    show chiave confused

    chiave "...Siracusa. {i}Comprende{/i}?"

    nvl clear

    nvl show dissolve

    "You look to your right. There's a sign posted on the fence. Though well-worn, it clearly reads... \"Siracusa.\""

    scene white with vpunch

    "Siracusa? A tiny abandoned village? No."

    "Siracusa was a... it {i}is{/i} a..."

    "..."

    nvl clear

    "Scratches on the walls of empty memories. Nothing comes to you."

    nvl hide dissolve

    scene innervillage with dissolve

    show broca surprised at midleft with dissolve

    show aosta surprised left at midright with dissolve

    show chiave confused at center with dissolve

    chiave "{size=15}...eed{/size}{size=20}a nap? That{/size} headache looks nasty!"

    a "N-no. Ugh. I'm fine. So this tiny village is Siracusa. And you're fighting to free it from...?"

    show broca angry

    $ renpy.say(brocaname, "Those Lateran bastards." if swearing else "Those Lateran *******s.")

    a "{size=20}That doesn't sound right, but{/size} what has Lateran done that's so heinous?"

    show chiave shocked at center

    chiave "You don't know this, either!? What rock have you been sleeping under!?"

    $ renpy.say(a, "A pretty fucking big one, evidently." if swearing else "A pretty ****ing big one, evidently.")

    show aosta nervous left

    aosta "Wait. {size=20}It's possible this guy is a Lateran spy who's playing dumb to get us to confess to heresy...{/size}"

    menu:
        "You got me.":
            show chiave confused

            broca "I'll kill you."

            a "You could try, kid. You could try."

            a "(...These guys talk big, but they all flinched when I said that.)"

        "I'm not.":
            broca "That's exactly what I'd say, too."

            show chiave happy

            chiave "Well, that's good enough for me!"

    a "Enough talk. Who is Lateran, why are you fighting them, and how does Siracusa--the tiny village, apparently--fit into this?"

    show chiave

    a "Alright. But if you're going to keep falling over, you might want to sit down. Come to our place?"











    # These display lines of dialogue.

    "{b}END OF DEMO! Thanks for playing!{/b}"

    nvl show dissolve

    "And now, the requisite credits. I'll move these to the main menu later."

    "The Forest and the Trees by Kevin MacLeod. Link: https://incompetech.filmmusic.io/song/4494-the-forest-and-the-trees. License: https://filmmusic.io/standard-license"

    # This ends the game.

    return
