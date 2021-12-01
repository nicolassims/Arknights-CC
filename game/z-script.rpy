# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
    import copy

    # Declare positions used by this game
    midleft = Position(xpos = 0.25)
    midright = Position(xpos = 0.75)

define narrator = nvl_narrator
define who = Character("???")
define a = DynamicCharacter("playerfirstname")
define aosta = DynamicCharacter("aostaname")
define broca = DynamicCharacter("brocaname")
define chiave = DynamicCharacter("chiavename")
define headhunter = DynamicCharacter("headhuntername")
define gambino = DynamicCharacter("gambinoname")
define capone = DynamicCharacter("caponename")
define rangers = DynamicCharacter("rangersname")

# Backgrounds
image black = "#000000"
image white = "#ffffff"
image ruinedTent = im.Scale("bgs/ruinedtent.png", 1920, 1080)
image forest = im.Scale("bgs/forest.png", 1920, 1080)
image outcounty = im.Scale("bgs/outcounty.png", 1920, 1080)
image tactics = Transform("bgs/tactics.png", matrixcolor=SaturationMatrix(0), xsize=1920, ysize=1080)
image village = Transform("bgs/village.png", xsize=1920, ysize=1080)
image innervillage = Transform("bgs/village2.png", xsize=1920, ysize=1080)
image safehouse = Transform("bgs/safehouse.png", xsize=1920, ysize=1080)
image road = Transform("bgs/road.jpg", xsize=1920, ysize=1080)
image sunsetroad = Transform("bgs/roadsunset.jpg", xsize=1920, ysize=1080)
image city = Transform("bgs/city/city.png", xsize=1920, ysize=1080)
image raincity = Transform("bgs/city/raincity.png", xsize=1920, ysize=1080)
image kidhouse = Transform("bgs/kidhouse.png", xsize=1920, ysize=1080)

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
image broca scowl = scaleportrait("chars/broca/scowlbroca.png", 189)
image aosta left = scaleportrait("chars/aosta/aosta.png", 177, True)
image aosta nervous left = scaleportrait("chars/aosta/nervousaosta.png", 177, True)
image aosta surprised left = scaleportrait("chars/aosta/surprisedaosta.png", 177, True)
image aosta eyesclosed left = scaleportrait("chars/aosta/eyesclosedaosta.png", 177, True)
image aosta smile left = scaleportrait("chars/aosta/smileaosta.png", 177, True)
image blaze shadow = scaleportrait("chars/blaze/shadowblaze.png", 172)
image headhunter = scaleportrait("chars/headhunter/headhunter.png", 184)
image gambino shadow = scaleportrait("chars/gambino/shadowgambino.png", 189)
image gambino happy = scaleportrait("chars/gambino/happygambino.png", 189)
image gambino = scaleportrait("chars/gambino/gambino.png", 189)
image gambino angry = scaleportrait("chars/gambino/angrygambino.png", 189)
image gambino nervous = scaleportrait("chars/gambino/nervousgambino.png", 189)
image capone shadow left= scaleportrait("chars/capone/shadowcapone.png", 181, True)
image capone happy left = scaleportrait("chars/capone/happycapone.png", 181, True)
image capone shout left = scaleportrait("chars/capone/shoutingcapone.png", 181, True)
image capone angry left = scaleportrait("chars/capone/angrycapone.png", 181, True)
image capone left = scaleportrait("chars/capone/capone.png", 181, True)
image rangers = scaleportrait("chars/rangers/rangers.png", 179)
image rangers thinking = scaleportrait("chars/rangers/thinkingrangers.png", 179)
image suzuran = scaleportrait("chars/suzuran/suzuran.png", 137)
image suzuran happy = scaleportrait("chars/suzuran/happysuzuran.png", 137)
image suzuran surprised = scaleportrait("chars/suzuran/surprisedsuzuran.png", 137)
image shamare = scaleportrait("chars/shamare/shamare.png", 138)
image vermeil = scaleportrait("chars/vermeil/vermeil.png", 153)
image kroos = scaleportrait("chars/kroos/kroos.png", 154)
image kroos surprised = scaleportrait("chars/kroos/surprisedkroos.png", 154)
image kroos happy = scaleportrait("chars/kroos/happykroos.png", 154)

#Transitions
transform moveleft:
    linear 0.5 xpos 0.15

transform mymovein(timing, start, destination):
    yalign 1.0 xanchor 0.5 xpos start
    linear timing xpos destination

# The game starts here.

label start:

    jump mapsetup

    label aftermaps:

    # Declare variables used by this game
    python:
        playerfirstname = "You"
        playerlastname = "The Operator"

        aostaname = "Nervous Albino"
        brocaname = "Scowly Brunette"
        chiavename = "Shouty Redhead"
        headhuntername = "Headhunter"
        gambinoname = "Chappy Wolf"
        caponename = "Wolfy Chap"
        rangersname = "Albino Savra"

        doctor = 0
        killer = 0

        party = [Operator(ACE, 1, True, [ hammerdown ])]

        inventory = []

        rocksickspared = None
        headhunterspared = None
        sneakyway = None
        gambinoalive = None
        caponealive = None

        swearing = True

        cash = 0

    scene black with Dissolve(2)

    a "...Ow."

    a "...Where am I?"

    play sound "audio/footstep.mp3"

    who "..."

    a "A noise! Hostiles? Where's my squad?"

    a "...Wait. Squad? Hostiles? Who would those even be...?"

    show ace shadow with dissolve

    a "Agh. My head hurts like I just tried to wrestle a metal crab. Don't tell me, I was out drinking too hard last night with..."

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

    a "Ugh... Where am I?"

    nvl show dissolve

    "You open your eyes."

    play music "audio/forest.mp3" loop

    nvl clear

    window hide dissolve

    show ruinedTent behind ace with Dissolve(2)

    show ace with dissolve

    a "...Hm. A hammer, a shield, a whole lot of carbon-fiber body armor, and everything around me's torn to shreds."

    a "Don't know who I am, don't know where I am, and I don't know why I'm kitted out like this... but all this points to me having just walked out of a pretty tough fight."

    a "...Aw, I don't know who I am. I don't even remember my name. What the hell happened?"

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

    call Crawl(guerroforest, 6, 3, guerroknowledge, True) from _call_Crawl

    show ace at center with ease

    show outcounty behind ace with dissolve

    a "Finally an end to all that grass and smoke. It's a miracle the whole forest didn't burn down from whatever caused... that."

    a "Looks like there's a village ahead. With any luck, they'll have a way to get in contact with these \"Rhodes Island\" people. Maybe they'll be able to tell me why I'm wearing their getup.\n...Maybe they'll have a paycheck for me."

    a "...What the hell is that running towards me?"

    hide ace with dissolve

    call Battle(party, [Operator(ROCKSICK, -5, False, [ rocklaw ])]) from _call_Battle

    show ace at midleft with dissolve

    window show

    a "...But what the hell did I just win against?"

    show rocksick left at midright with dissolve

    play music "audio/sad.mp3" loop

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

    play music "audio/forest.mp3" loop

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

    stop music fadeout 2.0

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

    "Would you like this game to censor such swear words for you? This decision can be changed at any time in the Preferences menu."

    nvl clear

    menu:
        "Yes, please.":
            $ swearing = False

        "No, thanks.":
            $ swearing = True

    "Understood."

    $ censor(a, "Fuck.")

    hide ace with dissolve

    a "Well... if there's nothing left here, I guess I might as well grab what I can and keep moving. Maybe there'll be a cannibalized refrigerator somewhere that still has rations."

    play music "audio/chiave.mp3" loop

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

    $ censor(chiave, "Well, shit. If he's not {i}him{/i}, who is he, Aosta?")

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

    if (rocksickspared):
        "However, since you called that creature in the forest \"it\", multiple times, you have little ground to stand on."
    elif (rocksickspared):
        "However, since you killed that creature in the forest, you have little ground to stand on."

    "Still, you wonder..."

    nvl hide dissolve

    a "Right. How many infected have you met?"

    show chiave happy

    show aosta nervous left

    show broca

    $ renpy.say("Freedom-Fighting {s}Four{/s} Three", "One.")

    a "(Yeah, that's what I thought.)"

    if (not rocksickspared):
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

    chiave "{size=15}...eed{/size}{size=20} a nap? That{/size} headache looks nasty!"

    a "N-no. Ugh. I'm fine. So this tiny village is Siracusa. And you're fighting to free it from...?"

    show broca angry

    $ censor(broca, "Those Lateran bastards.")

    a "{size=20}That doesn't sound right, but{/size} what has Lateran done that's so heinous?"

    show chiave shocked at center

    chiave "You don't know this, either!? What rock have you been sleeping under!?"

    $ censor(a, "A pretty fucking big one, evidently.")

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

    chiave "Alright. But if you're going to keep falling over, you might want to sit down. Come to our place?"

    pause(2.0)

    a "Fine."

    scene safehouse with dissolve

    nvl clear

    nvl show dissolve

    "Chiave leads you back to his gang's safehouse, a dinky little collapsed building that looks like it might have once been a restaurant."

    "He sits you down and begins to talk freely, Broca standing guard in the corner. Aosta wandered off somewhere."

    "Chiave explains that the village of Siracusa is in the nation of Sconfitto, a vassal state of the ruthless and expansionist Lateran Empire."

    "Ever since firearms were invented in Laterano two decades ago, the primarily-Sankta nation had been on the warpath, imposing their Thirteen Absolutes on their neighbours."

    nvl clear

    "As the closest geographical nation to Laterano, Sconfitto was conquered in the opening year of the war."

    "Many of the Sconfittian people accepted their new subservient role without protest. Their own government at the time was corrupt and plagued by infighting."

    "Besides mass conscription into the Laterano army, which every adult Sconfittian was automatically enrolled into, Laterano had left the pridebroken nation alone."

    "Most Sconfittians only encountered one daily reminder of their subservience--the true name of their nation was forbidden to speak, under penalty of death."

    nvl hide dissolve

    show chiave confused at center with dissolve

    a "So... you don't know what this place used to be called?"

    chiave "Nah. We don't call it the Lateran name either, though. We don't know what our home is really called, but we know it's not that disgusting slur."

    nvl clear

    nvl show dissolve

    "Chiave continues to explain how he and his gang ended up here."

    "Apparently, they were formerly a street gang in a city further inland. A company of Lateran soldiers descended on the city one day, searching for a man who'd apparently escaped conscription."

    "They wanted to fight the Laterans, but were outnumbered forty-to-one."

    "So it was Chiave who made the call to retreat and come back later."

    nvl clear

    "When they did, the city was empty, save for the children."

    nvl hide dissolve

    a "...What happened to them?"

    show chiave at center

    chiave "What d'ya think? We grabbed as many as we could carry and got them out of there!"

    a "You... carried the children?"

    show broca surprised at midleft with moveinleft

    broca "I carried at least seven, myself."

    hide broca with moveoutleft

    show chiave happy at center

    chiave "He sure did! Aosta talked them into coming with us, and I rigged up a car to get us as far away from the city as possible. We found an empty village--Siracusa--and set up shop here."

    show aosta left at midright with dissolve

    aosta "Don't forget the help we had."

    show chiave at center

    chiave "How could I?"

    show chiave happy at center

    chiave "This super-hot chick helped us out, too! She had these crazy gravity Arts that helped us push the car the last half of the journey when it broke down."

    a "...Where are these kids, then? Or this \"super-hot chick?\""

    show chiave confused at center

    chiave "Well... I mean, I'd love to tell you, but... uh... thing is, we still can't trust you, really."

    a "You've already told me about your rebellion, your anti-Laterano sentiments. What more could you possibly reveal that would be incriminating?"

    show aosta nervous left

    aosta "...Good question."

    show chiave happy at center

    chiave "Well, you don't know where all the kids are hiding!"

    a "But I {i}do{/i} know that you're hiding a bunch of kids in this village."

    show aosta eyesclosed left

    aosta "Chiave, please stop talking."

    show aosta surprised left

    aosta "On a practical note, though... hiding children isn't illegal underneath Laterano's standard vassal edicts. And we're all under the age of majority, too."

    broca "..."

    a "(...The big guy just looked away. Only for half a second, but there was definitely something there...)"

    a "Well, legal or not, it doesn't matter. I'm not reporting you kids. Hell, I might as well join you."

    show broca surprised at midleft

    show chiave shocked at center with vpunch

    chiave "WHAT!?"

    a "(\"WHAT!?\" is right. Why'd I say that? It just came out, like...)"

    a "(Like I need to be part of something.)"

    show chiave confused

    chiave "Man, we don't even know your name. It's a bit soon to be pledging yourself to joining the freedom fighters, isn't it?"

    a "%(playerfirstname)s %(playerlastname)s. My uniform says my callsign was \"Ace,\" which sounds a bit self-aggrandizing. I actually know how to fight. Do you need anything more?"

    chiave "...Well, uh..."

    show broca

    broca "You came from the south. Only thing that way is Rim Billiton, Laterano, and the sea. You don't look like a Cautus or Seaborn."

    a "Yeah, well, I'm obviously not a Sankta, either. And I don't know where I came from. I woke up in that forest two hours ago with a bunch of memories that I can't remember, but everything you've told me is telling me they're wrong."

    show aosta eyesclosed left

    aosta "Even given your obvious uninformed state, that doesn't seem likely."

    $ censor(chiave, "Yeah, calling bullshit on that one.")

    show broca scowl

    broca "...He isn't lying."

    show chiave shocked

    show aosta surprised left

    $ censor(chiave, "No shit? Huh, sorry for doubting you, then, man.")

    aosta "Yes, apologies for my suspicion. I'm sure you understand, given the stakes."

    a "(That was all it took...?)"

    a "Alright. I'd like to make it clear that I'll only chaperone you kids until I find something that tells me more about who I am, and who I belong with, but until then, I'm at your disposal."

    show chiave happy

    chiave "Glad to have you onboard!"

    stop music fadeout 2.0

    scene black with Dissolve(2.0)

    nvl clear

    nvl show

    "Chiave leads you to a side room, where there's several mattresses on the floor. In spite of the early hour, your throbbing head makes sleep seem a very appealing prospect."

    "You express concern that you're stealing one of the kids' beds, but you're assured that there's plenty more to go around."

    "You try to stay awake, but your mind, still wracked with waves of pain, gets the better of you, and you eventually slip into a fitful sleep."

    "As your heavy eyelids close, the last thing you see is a tube of lime-flavored lip balm sitting on the floor next to the mattress."

    nvl clear

    "In your dreams, you see..."

    nvl hide dissolve

    show blaze shadow with dissolve

    $ censor(who, "Alright, you old bastard, you'd better get back to me soon or I'll kick your ass so hard you'll have to find your way back in a wheelchair! I already lost you once. It's not happening again, got it!?")

    hide blaze with dissolve

    nvl show

    "...Incomprehensible memories of a life you never lived."

    "But they do not wake you, and the night passes peacefully."

    #show title with dissolve

    window hide dissolve

    $ renpy.transition(Dissolve(2.0))
    $ renpy.show_screen("title", title="Chapter 1", subtitle="Dustbreaking Footfalls")

    pause 6.0

    $ renpy.transition(dissolve)
    $ renpy.hide_screen("title")

    scene safehouse with dissolve

    play music "audio/forest.mp3" loop

    a "Rise and shine, kids! Up and at 'em! The early bird gets the worm!"

    show chiave confused at mymovein(2.5, 1.5, 0.5)

    chiave "...What the hell, man...?"

    show broca angry at mymovein(1.5, -0.5, 0.25)

    broca "There better be a dead body. And if there isn't, there will be."

    show aosta eyesclosed left at mymovein(1.5, 1.5, 0.75)

    aosta "...There are a number of benefits associated with early waking hours, not the least of which is..."

    a "..."

    chiave "......"

    aosta "........."

    show broca angry with vpunch

    broca "WAKE UP!"

    show aosta surprised left

    aosta "...improved cognitive function!"

    chiave "I don't think any of us are feeling very coglike right now, Aosta."

    a "Hey! Snap to attention, you three."

    show aosta smile left

    show chiave

    show broca

    a "(Huh, they actually did...)"

    a "I'm glad to see you all have your weapons on you. Never go to sleep without an obvious weapon at your side, and a hidden weapon under your pillow."

    chiave "Yeah, yeah. We know all that. We're kinda tough as nails, you know."

    a "..."

    chiave "Anyway, since you got us up at this {i}empio{/i} hour, I hope you're prepared to pull your weight!"

    a "Mine and more."

    chiave "Cool. 'Cause we're heading back to the city and getting more kids."

    a "Fine."

    show chiave confused

    chiave "...You're really okay just taking orders from me? You're like fifty years older than me."

    a "Firstly, watch your mouth. I'm barely double your age."

    a "Secondly, you're the leader of your men. They're clearly loyal to you. I want you to show me why. So, yeah, tell me where you want me."

    chiave "...Huh. Well, okay. But, actually, why are you guys...?"

    show broca surprised

    broca "Who else would I follow?"

    aosta "I ask myself this every day, but you've never lead us so wrong that we didn't recover. I mean, look at this. You had us attack the wrong guy, and now he's joined us. That's just the way you are."

    show chiave happy

    chiave "Cool!"

    show chiave

    chiave "Alright. Everyone grab one of those space food packets from the cooler and let's discuss the mission."

    scene tactics with dissolve

    nvl clear

    nvl show dissolve

    "Chiave explains the day's mission to you. Your target is a city about a three-hour drive northwest known as Piccino."

    "The city is mostly abandoned, aside from a sparse population of children and old people."

    "Your goal is to go the city and rescue as many children as you can--primarily older teens, as they're in the most danger if the Laterans come back."

    nvl hide dissolve

    show chiave happy with dissolve

    chiave "Alright, any questions?"

    label missionquestions:

    menu:
        "What resistance do you expect?":
            chiave "None. Worst that might happen is we get attacked by some wolves on the way there."

            show aosta smile left at midright with moveinright

            aosta "It doesn't make much sense for Lateran to station a permanent guard in Piccino, so we should be fine."

            hide aosta with moveoutright

            jump missionquestions

        "How will we bring the kids back?":
            chiave "I can rig up another car! There are hundreds left around the city. Actually, I should go for a van this time."

            jump missionquestions

        "Do you have enough resources here to take care of the kids?":
            chiave "Yeah. We've got years' worth of dry food, and the water and gas are still running. A few buildings even have electricity left, not to mention the car batteries, which are mostly full."

            jump missionquestions

        "How long will this take?":
            chiave "Three hours there, three hours rescuing, and three hours back."

            jump missionquestions

        "Is your helper from last time coming?":
            show chiave

            chiave "...Well, she was technically one of the people we rescued last time. If any of our rescues volunteered, we wouldn't turn them down, but we don't want to ask any of them to help. 'Cause how could they say no? Even if they were really scared?"

            a "(...I think, maybe, I see what Broca and Aosta see in him.)"

            jump missionquestions

        "Let's go.":
            show chiave happy

            chiave "Hell yeah. {i}Prendilo!{/i}"

    scene sunsetroad with dissolve

    a "...Pretty out here."

    chiave "Yeah, and I haven't seen the sunrise in {i}months{/i}, so thanks for breaking that streak by waking us up at the crack of dawn. Damn old people sleep schedules."

    a "I have a hammer."

    chiave "Big deal, I've got a wrench."

    a "(These kids... how the hell have they managed to stay alive so long?)"

    a "On that topic, if fighting becomes necessary, you all stay behind. I'll handle it."

    broca "Not going to happen."

    chiave "Broca, chill. Let's at least hear why he said that."

    a "You haven't seen me fight before. I've barely seen me fight before. All I know is that I can. It'd be best if you kids got an understanding of what I can do before we started working together, so we don't get in each other's way."

    aosta "Your logic is sound. But what if you become overwhelmed?"

    a "Well, I'm not proud. You can jump in, then."

    broca "Your call, boss."

    chiave "Makes sense. Let's let him show off."

    a "Good call."

    a "(...But, really, the reason I said that was...)"

    nvl clear

    nvl show dissolve

    "A memory flashes in your mind..."

    "An argument, with someone that you respected, feared, thanked, and despised in equal measure..."

    "\"Children don't fight, Doctor.\""

    "\"On the contrary. When told to, no-one will fight more obediently and instantly than a child. Perhaps you meant to say that a child {i}shouldn't{/i} fight... but this is clearly not a world that privileges us with what {i}should{/i} be.\""

    nvl clear

    "You continue to drive down the road. Somehow, you ended up in the driver's seat. Chiave is riding shotgun, his boots up on the dashboard."

    "Broca and Aosta are riding in the back, with Broca's head slightly poking out of the missing sunroof."

    "You consider mentioning his vulnerability to snipers, but decide to keep the thought to yourself. You're just being paranoid."

    "...In this way, dawn turns to day."

    scene road with Dissolve(2.0)

    chiave "Eighty-seven słoma sodas on the wall! Eighty-seven słoma sodas! Take one down, pass it around, eighty-six słoma sodas on the wall!"

    nvl clear

    nvl show dissolve

    "In this way, dawn turns to day... {i}excrutiatingly slowly.{/i}"

    nvl hide dissolve

    a "(I'm going to kill him. I swear I'll kill him and join the Laterans as soon as he hits eighty-five słoma sodas--)"

    show broca surprised at mymovein(0.2, -0.5, 0.5) with vpunch

    broca "STOP THE CAR!"

    nvl clear

    nvl show dissolve

    "Without question, you slam on the brakes!"

    hide broca with vpunch

    "The car skids to a halt, but at the very end of its slide, you hear a characteristic ripping, tearing, popping sound..."

    "You instantly recognize the sound of a tire being ruined."

    "You grit your teeth and leave the car to examine the damage, along with Chiave."

    show chiave confused at midleft with dissolve

    chiave "Well, the good news is that Aosta packed a spare tire, just in case."

    chiave "The bad news is that this is a caltrop chain. And the people who use these things are..."

    hide chiave with dissolve

    show headhunter with Dissolve(2.0)

    who "Ciao."

    chiave "{i}Headhunters.{/i}"

    nvl clear

    nvl show dissolve

    "The contempt in Chiave's voice is clear."

    nvl hide dissolve

    show aosta left at midright with vpunch

    aosta "Traitor! You'd betray your country just to get into those fascists' good books?"

    who "I'd betray my country to make enough money to not starve to death, yeah. But this doesn't have to involve you kids."

    show chiave confused at midleft with dissolve

    chiave "I mean, you attacked our car, man..."

    who "Look, just keep grandpa still, let me get these plastic ties on him, and you kids can go."

    a "I'm not a Sconfittian."

    who "That's for the Lateran recruiting office to figure out. You're a body, so I'll get paid."

    a "Where're your allies?"

    who "{i}Stai zitto.{/i}"

    aosta "Well, sir, you said you wanted a chance to fight. Show us what you can do."

    a "Gladly."

    hide chiave with moveoutleft

    hide aosta with moveoutright

    show ace at mymovein(0.5, -0.5, 0.12)

    show headhunter at mymovein(0.5, 0.5, 0.88)

    call Battle(party, [Operator(HEADHUNTER, 2, False, [ coltellata ])]) from _call_Battle_3

    show headhunter at mymovein(0.8, 0.88, 0.75)

    show ace at mymovein(0.4, 0.12, 0.25)

    who "...{i}Accidenti.{/i}"

    a "What's your name, Headhunter?"

    who "Guido. Guido Testa. What's it to you?"

    $ headhuntername = "Guido"

    menu:
        "{color=FF0000}I should know the name of the man I'm going to kill.{/color}":
                $ headhunterspared = False

                show ace shadow with dissolve

                nvl clear

                nvl show dissolve

                "The headhunter sneers at you, head held high."

                "Your hammer swings down."

                "And nothing gets back up."

                hide headhunter with dissolve

                nvl show dissolve

                "{color=FF0000}Your heart shifts towards the path of a killer.{/color}"

                $ killer += 1

                show chiave confused at midright with Dissolve(2.0)

                chiave "...So that's how you fight, huh?"

                a "He forfeited his right to mercy when he attacked you."

                hide chiave with dissolve

        "I want to talk. I want to know where your allies are.":
            headhunter "Yeah, so do I. Guess those {i}codardi{/i} ran away as soon as they saw you."

            a "Who would they be running to?"

            headhunter "The Dons of Piccino, probably. Two real nasty pieces of work. Capone and Gambino."

            show chiave confused with dissolve

            chiave "What? Dons? I haven't heard about this."

            headhunter "They moved in recently. Organized up all the scum like me. They're trying to bring back the {i}famiglie.{/i}"

            show chiave happy

            chiave "What!? That's fantastic!"

            headhunter "Hah. You just say that 'cause you don't know how bad the families ruined our country even before the war. Lateran's no worse."

            show chiave confused

            chiave "I... I refuse to believe that!"

            headhunter "Believe whatever you want. It's no skin off my nose. Now, look, I've got a broken leg here, probably, so if you're going to leave me here, I'd prefer if you just finished me off. Better your hammer than the wolves."

            menu:
                "{color=FF0000}Finish him.{/color}":
                    $ headhunterspared = False

                    show ace shadow with dissolve

                    a "As you wish."

                    nvl clear

                    nvl show dissolve

                    "The headhunter bows his head."

                    "Your hammer swings down."

                    "And nothing gets back up."

                    hide headhunter with dissolve

                    nvl show dissolve

                    "{color=FF0000}Your heart shifts towards the path of a killer.{/color}"

                    $ killer += 1

                    chiave "...Well, he literally asked for it."

                    hide chiave with dissolve

                "{color=27C4CC}Help him.{/color}":
                    $ headhunterspared = True

                    a "Nah, we're not leaving you. Can we fit him in the car?"

                    show chiave shocked

                    show aosta surprised left at right

                    show broca surprised at left with vpunch

                    chiave "WHAT!?"

                    a "You recruited me after attacking me. I'm going to recruit him."

                    hide aosta with dissolve

                    hide broca with dissolve

                    headhunter "Appreciate the thought, but you guys--"

                    show chiave happy

                    chiave "Freedom Fighters!"

                    headhunter "Yeah, I'm guessing freedom fighters don't make a whole lot of moolah. Your ideals are great and all, but I'm starving."

                    a "We have food. Piccino should have plenty of abandoned stores and homes, too."

                    headhunter "...What, you want to loot them? Someday this war will be over, and people'll come back to those homes and stores, you know."

                    a "At the very least, we'll take you to Piccino. Like you said, leaving you out here in the wilds is just another death sentence, and I'm not going to kill you."

                    headhunter "...Eh, whatever. Sure, load me up."

                    nvl clear

                    nvl show dissolve

                    "You and Broca work to put the headhunter in the backseat of the car, squishing Aosta up next to the door. Broca's help was likely not needed, as you realize immediately after putting your hand on Guido."

                    "Underneath his starched and worn suit, he is deathly thin."

                    "...You mentally make a note to get this man a cheeseburger."

                    "{color=27C4CC}Your heart shifts towards the path of a doctor.{/color}"

                    $ doctor += 1

                    $ headhunterop = Operator(HEADHUNTER, 2, True, [ coltellata ])
                    $ renpy.call_screen("Newmember", op=headhunterop)
                    $ party.append(headhunterop)

    nvl clear

    "You all pile back into the car after replacing the popped tire, and continue onward toward the city."

    "It's quiet inside the car, and everyone is keenly on the lookout for ambushes."

    if (headhunterspared):
        "Your new guest falls asleep almost immediately, head pressed against the window as he snores lightly."

    "Without further ado... you make it to Piccino."

    scene city with dissolve

    show chiave happy with dissolve

    chiave "Alright. Everyone remember where the car's parked. Everyone try to bring back a car, as well."

    show aosta nervous left at midright with dissolve

    aosta "I recommend splitting into two distinct groups. Each team should have a member who's good at being stealthy, and one who's good at hitting hard."

    chiave "Sounds good. I'll go with %(playerfirstname)s."

    if headhunterspared:
        show chiave

        chiave "Oh, and Guido. I guess."

        headhunter "Yeah, I'm going with the big guy."

    show broca at midleft with dissolve

    broca "Hrmmm. Be safe, Chiave."

    chiave "No problems! We'll be in and out in a flash. Hey, %(playerfirstname)s, be careful when cutting through alleyways. There might be more headhunters around, and they like to hide in narrow spaces."

    nvl clear

    nvl show dissolve

    "And so, with those words that tempted fate like nothing else, your first official mission with Chiave the Chainbreaker's Freedom-Fighting Famiglia begins."

    hide aosta

    hide chiave

    hide broca

    $ piccinokills = 0
    $ chiaveop = Operator(CHIAVE, 1, True, [ Tech(5) ])
    $ renpy.call_screen("Newmember", op=chiaveop)
    $ party.append(chiaveop)

    call Crawl(piccinocity, 1, 5, piccinoknowledge, True) from _call_Crawl_3

    #killer: 3
    #doctor: 2

    scene city with dissolve

    a "It's quieter out there than I thought it'd be."

    if (piccinokills > 0):
        a "Mostly just headhunters."

    a "No kids."

    show chiave confused with dissolve

    chiave "Yeah, I don't get it. Last time I was here, kids were running all over the place. Oldies, too. But there's a lot more adults just walking around openly now. I guess everyone's becoming a headhunter to avoid conscription."

    if (headhunterspared):
        headhunter "Yeah, it's a great deal. Since everyone's taking advantage of it, we all know the Laterans are going to revoke the deal any day now, but it gets us by today."

    nvl clear

    nvl show dissolve

    "The air suddenly seems struck by an intense stillness, as though everyone in this city block is holding their breath."

    "Your tail twitches, and, were you capable of forming goosebumps, you'd have them."

    hide chiave

    show ace shadow with vpunch

    a "Show yourself!"

    show capone shadow left at midright with dissolve
    show gambino shadow at midleft with dissolve

    gambino "Heh heh heh..."

    capone "Hah hah hah..."

    if (headhunterspared):
        $ censor(headhunter, "Ah, crap, it's the Dons.")

    show capone happy left with dissolve
    show gambino happy with dissolve

    capone "Well, look at this, Gambino! Seems we've got an outsider in our little city."

    gambino "I've got eyes, Capone. Let's ask him what he wants, huh?"

    $ gambinoname = "Gambino"
    $ caponename = "Capone"

    capone "Oooh, too direct, Gambino. Besides, I think it's clear what he wants."

    if (headhunterspared):
        capone "After all, he's got dear Guido with him. Clearly, Guido's bringing him into our {i}famiglia.{/i}"

    elif (piccinokills > 1):
        show capone angry left

        capone "After all, he killed more than %(piccinokills)s of our crew."

        gambino "Eh. They were just grunts. Now this guy, he looks like something."

    a "What do you want with us?"

    show capone happy left

    capone "Why, we want to help you, {i}compagno{/i}."

    show gambino

    gambino "We saw you digging through the trash. Looking in dumpsters. Picking up worthless {i}garbage{/i}."

    if (headhunterspared):
        a "(He was definitely looking at Guido when he said that.)"

    capone "So I figures you're looking for something, eh? Well, maybe my Family can do you a favor, and help you find it."

    a "(I don't need to be told what a Family's favor means...)"

    menu:
        "I don't need your help.":
            show gambino angry

            $ censor(gambino, "We're {i}offering{/i} our help. Don't be fucking rude.")

            capone "Now, Gambino, I'm sure he just doesn't understand what's in it for him."

            show capone left

            capone "Why don't you explain what you're looking for, and we'll tell you how we can help you?"

        "I would appreciate your help.":
            capone "Ah, you're very sensible. I like that."

            show capone left

            capone "Why don't you explain what you're looking for, and we'll tell you how we can help you?"

    a "I'm looking for people who will be in danger of conscription when the Laterans come back."

    show capone happy left

    capone "Ah. I guess you haven't heard, then."

    show gambino happy

    gambino "Y'see, me and my blood brother, we went ahead and solved that problem."

    capone "Sure, the Laterans would sweep in every few months and capture anyone they felt could serve the war effort."

    gambino "But we figured somethin' out. Y'see, the Laterans won't come here as long as they get two \"volunteers\" per week. And that's easy, in a city this big."

    capone "Every week, like clockwork, right before the deadline, two of our crew \"volunteers\" for the frontlines."

    gambino "This keeps the Laterans off our back, and minimizes the drain to the city. A few of the boys have been getting busy with all the free time they're getting, and Piccino's population is actually rising again."

    capone "{i}Perfetto.{/i}"

    a "You're giving your own men to the Laterans?"

    show capone angry left

    capone "Hey, no, no. Don't go accusing us of anything untoward. Like I said, they \"volunteered.\""

    show gambino

    gambino "Which brings us to our problem. Y'see, these headhunters you've seen all around the place aren't actually recruiting for the Laterans. Nah, they're recruiting for us."

    capone "And our numbers have been down recently..."

    if (piccinokills > 0):
        capone "See, you're just one man, but we've already spent more men tryin' to get you than you're worth."

        gambino "It's bad math."

    show capone happy left

    capone "So, look, we'd like to invite you to work with us. Join our {i}famiglia{/i}, eh?"

    gambino "You're a big guy. You bring in a few dozen more guys, and the books'll be open for you."

    a "...You sell your own men off to your nation's oppressor. What guarantee do I have that you won't do the same to me?"

    show capone angry left

    capone "Stop saying that, {i}compagno{/i}."

    gambino "Here's your guarantee. Mafia's honor, if you do one little job for us, we'll help you find what you were looking for and let you go back home."

    a "I'll listen to your offer, then decide whether I want to do it."

    show gambino nervous

    gambino "So, here's the thing. Pretty much all the men and women in this city were conscripted. Leaves it nice and open for my Family to move in, you dig?"

    capone "Yeah. But the former Don--former as in before the war--has her own little family that stays on the West side of the city."

    show gambino

    gambino "Now, we're good with working together. As you know, two's company."

    show capone happy left

    capone "But three's a crowd."

    a "You want me to kill the former Don."

    capone "Hah, no, I don't think you could. Her Arts would turn you inside-out before you could blink."

    gambino "But the Don's got a husband, and that husband's got a daughter, and that daughter has a daughter, and we know where that daughter is."

    show capone left

    capone "Of course, she's an innocent child. We're not going to hurt her. But her family wants open war with the Laterans."

    gambino "I like taking the direct route, but even I know that's suicide."

    capone "We don't want the West side thinking we're weak just 'cause we're not charging at the Laterans, crossbows drawn."

    show capone happy left

    capone "So, if you could grab little Lisa for us, that'd be... insurance."

    a "...Little Lisa. She's a child?"

    gambino "Yeah. Most of the kids and old folks in town fled West when we moved in."

    a "(Well, that explains why there's only been headhunters here on the East side...)"

    a "(It might be best to go along with them for now. At the very least, they'll be able to get me to the kids. Once I have them, I can decide if the Dons get Lisa. Either way, all the other kids will come home with me.)"

    show ace

    a "Fine."

    a "Point me in the right direction."

    capone "That's what I like to hear! Knew I had a good feeling about you. Glad our headhunters didn't get you before we could negotiate this deal."

    if (headhunterspared):
        a "I'll need Guido."

        show capone angry left

        show gambino angry

        pause 2.0

        show capone happy left

        show gambino happy

        capone "Sure, sure. Usually, we have a very specific consequence for failure, but we'll just give him to you."

        headhunter "...Thanks, %(playerfirstname)s."

    nvl clear

    nvl show dissolve

    "Gambino and Capone show you on a map of the city where Lisa's safehouse is. Security should be minimal. It's essentially a straight line there and back."

    "...In a way, this irritates you. You were hoping you'd have more time to think about what you'll do."

    "They walk you to the border to the West Side and give you a hearty slap on the back, with some friendly parting words."

    show gambino happy

    show capone happy left

    capone "So, hey, it'd be great if you could get in there and get out without anyone seeing, but if you need to rough up some of their men, we won't get mad at you."

    gambino "Yeah, and... well, Capone said that you couldn't kill the Don, but if you happen to come across her... get creative, eh?"

    $ renpy.say("The Dons", "Don't fail. {i}Arrivederci!{/i}")

    hide gambino with dissolve

    hide capone with dissolve

    hide ace with dissolve

    $ gatedown = False
    $ sawstation = False

    call Crawl(piccinocityeast, 13, 14, piccinoknowledgeeast, True) from _call_Crawl_4

    nvl clear

    nvl show dissolve

    "You make your way to the storehouse the Dons had pointed you to."

    "You hear many high-pitched chattering voices coming from inside. There's definitely some children here, even if Lisa isn't."

    "You take a deep breath and reach toward the doorknob--but before you make contact, the door opens."

    show rangers with dissolve

    rangers "Oh. Hello, young man. Can I help you?"

    a "I--"

    show chiave shocked at midleft with vpunch

    chiave "Grandpa Rangers!? You're here!? I thought the Laterans had snatched you up!"

    $ rangersname = "Rangers"

    rangers "Eeeh hee hee. No, they passed right over an old sack of bones like me. And quite right, too. I'd never be able to wrap my head around their new-fangled firearm devices."

    show chiave happy

    $ censor(chiave, "That's bullshit, Gramps! Everyone knows that you're still an ace shot with that bow.")

    show rangers thinking

    rangers "Language, m'boy."

    $ censor(chiave, "Shit, sorry.")

    rangers "Well, please, Chiave, come in."

    show rangers

    rangers "You too, young man."

    if (headhunterspared):
        rangers "And you too, Guido. How's that arrow wound healing up?"

        headhunter "Still infected."

        rangers "Oh, dear. Well, perhaps someone inside can do something about that."

    scene kidhouse with dissolve

    nvl clear

    nvl show dissolve

    "As you make your way into the safehouse, two things strike you."

    "Firstly: someone, or perhaps many someones, has tried very hard to make this place accommodatable for children."

    "The walls are covered in baby-blue wallpaper, and handmade dolls and blankets are lying all over the floor."

    "Secondly: You are practically knee-deep in children the moment you walk through the door."

    nvl clear

    "You are barely able to maneuver, as children, seemingly without fear, dart around and between your legs in the middle of their games of tag and hide-and-seek."

    nvl hide

    show rangers thinking with dissolve

    rangers "Pardon them. Given our circumstances, we didn't think it necessary to impress upon them the importance of personal space."

    a "We? Are you part of the family of the former Don, then?"

    show rangers

    rangers "...Hrrm. You've been talking to the East side family, then."

    show rangers thinking

    show chiave confused at midright with dissolve

    chiave "Whaddya mean, gramps?"

    if (headhunterspared):
        rangers "...Guido already knows this. And I thank you for keeping quiet about it."

        show headhunter at midleft with dissolve

        headhunter "Eh, fuggedaboutit."

    show rangers

    rangers "Young man. May I have your name?"

    a "%(playerfirstname)s %(playerlastname)s."

    rangers "I see. Well, %(playerfirstname)s, I imagine the twin Dons of the West Side told you that one or the other of the children we have here is a relative of the East Side's Don? A woman of unparalleled Arts prowess?"

    a "Yes."

    show rangers thinking

    rangers "Pure fiction."

    a "Hm?"

    rangers "We have no Don. We have no family. It's just my apprentice and I taking care of several dozen children. We've taken over a clinic, a grocery store, and a movie theater. That's the sum total strength of the West Side Family."

    show chiave shocked

    chiave "What!? Then you're... you're basically...?"

    show rangers

    rangers "Defenseless, besides my ability to tell stories that lead Gambino and Capone to think we're hiding some great power."

    rangers "They've gotten bolder, though. Even if they're only sending an outsider such as yourself to acquire insurance against us, this is merely a prelude to more aggressive actions later on."

    a "They said you want open war with Laterano."

    show rangers thinking

    rangers "I think, looking at the mighty army we have amassed here, you can draw your own conclusions about the truthfulness of that statement."

    show rangers

    rangers "The West Side Dons claim to be working for the betterment of Piccino by avoiding direct conflict with the Laterans, but they're helping them as much as they're helping Piccino."

    rangers "The Laterans would be content with one conscript a month from a city they've already plundered as much as they have Piccino."

    rangers "Their \"two a week\" policy is purely so that they can justify turning the entire adult population of the city against each other as Headhunters."

    rangers "...Which they do, because when one is running blind and scared of their supposed allies, it's very hard to notice what benefits their superior reaps from them."

    if (headhunterspared):
        rangers "...No offense, Guido."

        $ censor(headhunter, "I knew that already. Why'd you think I never told those bastards about you?")

    show chiave confused

    chiave "But, then... what do we do?"

    rangers "What you came here to do, I imagine. Take as many children from this place as you can. Don't tell me where you're taking them--when we are overrun, I don't want my weakness to betray you."

    rangers "But if we let Gambino and Capone have their way, they'll deplete this city far faster than the Laterans ever could. It's a matter of months before they run out of adults."

    rangers "It's best to get the older children out of here before they start looking like acceptable targets."

    chiave "...We're just supposed to leave you here, gramps?"

    rangers "Oh, I'm one stiff breeze and a bad cough away from dying, anyway. It's the children that deserve a future."

    who "Ra-ng-ers!~ Vermeil stole your bow again!"

    rangers "Ah, excuse me. I think a certain little troublemaker requires my attention."

    hide rangers with moveoutleft

    pause 1.0

    show ace with dissolve

    chiave "We're not just going to let him die, are we? Besides, no way we can transport all these kids to Siracusa."

    if (headhunterspared):
        show headhunter with dissolve

        headhunter "...What'd you say? What was that name you said?"

        chiave "Our home base. It's a little village called Siracusa."

        headhunter "Oh. ...Carry on."

        hide headhunter with dissolve

    chiave "We don't have enough resources to support all these kids. I thought it'd be fine if we brought back twenty or so more kids, but even if we took multiple trips, there's at least two hundred here!"

    chiave "We'd run out of food in weeks. I don't know how quickly we could make more. Aosta would know..."

    a "...We want a more permanent solution, then. Something that makes Gambino and Capone less of a threat."

    if (piccinokills >= 5):
        chiave "...I don't want to kill any more of them."

        a "Noted."

    a "The way I see it, we have two practical options."

    a "A {color=FF0000}messy way{/color} and a {color=27C4CC}sneaky way{/color}."

    if (piccinokills >= 5):
        chiave "I think... maybe... I'm really not cut out to make these decisions. Life and death are... a lot more real than I thought they were."

    else:
        show chiave happy

        chiave "Hey, let's go with the messy way! These traitors deserve it."

        if (headhunterspared):
            chiave "...Er, no offense, Guido."

            headhunter "Nah, I'm scum. No offense taken."

        a "Don't be so hasty. At least hear out my plans, first."

    nvl clear

    nvl show dissolve

    "You explain your two plans to Chiave. He seems to be having some difficulty wrapping his head around them, and wishes that Aosta was here."

    "At the end, Chiave leaves the decisions to you."

    "You're very aware of the monumentous nature of this decision."

    "Think this through. Some roads cannot be unwalked."

    menu:
        "{color=FF0000}Do this the messy way.{/color}":
            $ sneakyway = False

        "{color=27C4CC}Do this the sneaky way.{/color}":
            $ sneakyway = True

    nvl clear

    "A decision is made."

    "You can only hope that the consequences that lie in wait later on are within your acceptable parameters."

    hide ace with dissolve

    hide chiave with dissolve

    "{i}2 Hours Later...{/i}"

    "You're ready to leave Piccino. In your company are several children that you thought might prove useful to the Lateran war effort."

    nvl clear

    "Lisa Tani. At Chiave's recommendation, you've advised her to operate under the codename \"Suzuran.\""

    show suzuran with dissolve

    pause 1.0

    "She greeted you happily as soon as Rangers said Chiave and you could be trusted. You understand that, despite her age, she has incredible talent with Arts."

    "You judged that, given her skillsets could be utilized in a supportive role, and her natural skill at Arts, the Laterans might find a use for her. So it's best if they don't find her."

    nvl clear

    "Poveglia Amare, codename \"Shamare,\" was brought on for very similar reasons. Her voodoo-style arts, which she already had an incredible amount of control over, would make her a useful asset even if not on the frontlines."

    show shamare at midleft with dissolve

    pause 1.0

    "However, in all other aspects, she could be considered the opposite of Suzuran. She scowled at you, and is constantly hiding behind her doll, making clear that \"Morti\" does not like or trust you."

    "You also have some concerns about her outfit, but after lightly threatening Rangers under the assumption he was an old pervert, he maintains that she's just \"weird,\" and chose to dress herself like that."

    nvl clear

    "Your third charge directly asked to join you."

    show vermeil at midright with dissolve

    "Vermeil" "Vermeil, hunter. You won't regret giving work to me."

    a "Vermeil?"

    "Vermeil" "It's the name of the village where this cloak was made. No-one gets my real name. It might let... {i}him{/i} find me..."

    nvl show dissolve

    "Rangers pulls you aside and quietly explains that Vermeil says there's a Lateran agent personally stalking her."

    "Children can have such active imaginations."

    nvl clear

    if (sneakyway):
        "In any case, your new pint-sized companions are not vital to your plan. Except, maybe, for Lisa. But if she couldn't handle what you asked of her, there were plenty of backups."
    else:
        "In any case, your new pint-sized companions are not vital to your plan."

    hide shamare with dissolve

    hide suzuran with dissolve

    show chiave confused at midleft with dissolve

    chiave "Hey, I hope this isn't a rude question, but, uh, why do you and Lisa have rocks growing on your shoulders? They look kind of like... uh... this one {i}very sick{/i} man I knew..."

    "Vermeil" "It's a mark of the infected."

    chiave "Uh... those two-meter people-eating zombies?"

    "Vermeil" "Is that what you think the infected are?"

    chiave "I mean, yeah. I've met one."

    a "Exactly one."

    chiave "Hey, it's not like you've met any more, %(playerfirstname)s!"

    "Vermeil" "Well, now you have. I'm infected, Lisa's infected, even Poveglia's infected."

    chiave "Uh... Povey doesn't have any crystals, though."

    show shamare at left with dissolve

    "Shamare" "If you call me Povey again, I'll place a curse on you."

    hide shamare with dissolve

    "Vermeil" "Crystallization can be internal. Not all infected even reach the point of crystallization. Why didn't you learn any of this? I'm years younger than you."

    show chiave happy

    chiave "The Lateran Educational Board just never thought it was important, I guess! They only wanted to teach us trades and agriculture, and combat."

    "Vermeil" "...I'm sorry."

    chiave "Hey, it could be worse. Sure, they were teaching us to be the perfect future conscripts for their army, but at least I never had to learn history, or anything boring like that."

    "Vermeil" "...I'm {i}really{/i} sorry."

    hide vermeil with dissolve

    show chiave shocked

    chiave "Wait, what did I say?"

    "You were all ready to leave, when..."

    nvl hide dissolve

    who "Here I am!"

    hide shamare

    hide vermeil

    hide chiave

    show kroos at midleft with vpunch

    pause 1.0

    "...A Cautus you had previously assumed was one of the children under Rangers' protection introduced herself."

    "Coco" "Hi-hiii~ I'm Coco~ I might be inexperienced, but I'll do the best I can~"

    $ kroosop = Operator(KROOS, 3, True, [ doubletapauto])
    $ renpy.call_screen("Newmember", op=kroosop)
    $ party.append(kroosop)

    a "...Rangers, what the hell is this?"

    show rangers thinking at midright with dissolve

    rangers "Well, this is my apprentice. I believe I mentioned her before."

    a "She's basically a child herself."

    "Coco" "Oh, that's mean~! I might be small, but that's just because I don't get enough sleep~!"

    show chiave happy with vpunch

    chiave "Tell me about it! This guy woke us up at 6 AM this morning. 6! AM!"

    hide chiave with dissolve

    show kroos surprised

    "Coco" "Oh, no! That's terrible~! Are you a bad guy after all, Mister?"

    a "She just called me Mister. {i}Shamare{/i} didn't even call me Mister. How old is this girl, Rangers?"

    show kroos

    "Coco" "{i}It's not polite to ask a lady's age.{/i}"

    a "(...Why did I just get a chill up my spine?)"

    a "I... alright. I could use someone who knows what this city's been going through over the past few months. But Rangers, how will you...?"

    show rangers

    rangers "Oh, I can always train up another apprentice. There's a certain little kitten I've got my eye on. I think she'll be very impressive, when she's older."

    a "..."

    show rangers thinking

    rangers "I wish you would stop giving me that expression. I'm really not a pervy old man."

    a "...Sorry."

    hide kroos with dissolve

    show rangers at mymovein(0.5, 0.75, 0.5)

    a "I'll take the kids to the car that Chiave got ready, and then we can head out."

    a "If all goes well, Capone and Gambino should be less of a problem. If not... well, Chiave'll make sure the kids get to Siracusa, at the very least."

    "Child" "Ooooh! You said a bad word!"

    a "Hm?"

    "Child" "My Mommy told me you aren't supposed to say that word!"

    a "(Siracusa? Then, could that be...)"

    a "Rangers, do you know what the name of this country used to be?"

    show rangers thinking

    rangers "I'm... well, I'm afraid my memory isn't quite what it used to be."

    if (headhunterspared):
        headhunter "Let's just quit yapping about it. I heard the Laterans can tell when we say it."

    a "...Alright. Something to think about in the future, I guess."

    rangers "Good luck, young man. Walk in the dust."

    a "Hm?"

    show rangers

    rangers "Oh, it's an old saying from when I was younger. I forget its meaning, but I quite like how it sounds."

    scene raincity with dissolve

    nvl clear

    nvl show dissolve

    "By the time you leave Rangers' orphanage, the sky has fully darkened, with a heavy downpour of rain soaking you through to the bones."

    if (headhunterspared):
        "Guido throws his coat over Suzuran's shoulders."

    "Lacking a coat, Chiave spreads his arms like a bat and tries to cover Shamare."

    "You are too focused on what is coming next to worry about saving the children from a bit of water."

    nvl clear

    if (sneakyway):
        "Your plan is complicated, but well-formed."

    else:
        "Your plan is simple."

    "The only thing that remains is whether you can execute it."

    nvl hide dissolve

    show capone shadow left at midright with dissolve
    show gambino shadow at midleft with dissolve
    show ace with dissolve

    gambino "Heh heh heh..."

    capone "Hah hah hah..."

    a "Capone. Gambino."

    show gambino happy
    show capone happy left

    gambino "I see you've got the girl! Nice, nice. Ciao, little Lisa."

    capone "Well done, {i}compagno{/i}. See, Gambino? I told you he wasn't going to betray us. You need to have a bit more faith in my plans."

    gambino "I would, if you didn't have a hard-on for taking the most complicated path to any goal. I could've charged in there myself and gotten Lisa out months ago."

    show capone angry left

    capone "And if you got shot, {i}idiota{/i}? Half the men are loyal to you."

    show gambino angry

    gambino "More than half. You know that they're tired of waiting around for your \"schemes\" to unfold, yeah?"

    capone "Sure, they're impatient and thickheaded, so it's no wonder they'd rather follow you. But you'd get them all killed!"

    gambino "As opposed to you, who'd get them killed slowly, which is {i}better{/i}, eh?"

    a "Ahem."

    capone "What!? Can't you see we're--"

    show gambino happy
    show capone happy left

    capone "Oh, of course. What sort of impression are we giving our guest, hm? Please, hand over Lisa, {i}compagno{/i}, and we'll help you find... whatever you were looking for."

    $ sneakyway = True

    if (sneakyway):
        a "Sure. Just one question."

        capone "Oh, ask away!"

        a "Who do I give Lisa to?"

        show gambino
        show capone left

        gambino "What?"

        capone "I beg your pardon?"

        a "I get you two are doing your \"two-in-one\" deal. But who's calling the shots? Who decided I should nab Lisa?"

        gambino "..."

        capone "..."

        a "(...They see what I'm doing. I need to apply more pressure.)"

        a "Capone, you told me about the old Don. Was this your plan?"

        show capone happy left

        capone "Well, we might as well say it was."

        show gambino angry

        gambino "..."

        a "(...Ooh, Gambino didn't like that.)"

        a "\"Might as well?\" Sorry, I don't think you're being direct with me here."

        show capone left

        capone "I see no reason to be direct with you. You're barely an inductee into the {i}famiglia{/i}."

        a "It's just, if I'm joining you guys, I need to know who I should be listening to. You do most of the talking, so--"

        gambino "Both of us! We're both the Dons, {i}capisce{/i}!?"

        show capone shout left

        capone "Gambino! Calm down. We're having a civilized discussion here."

        gambino "{i}Cazzate!{/i} You're both using a lot of words to say nothing. Listen to him and just be direct!"

        capone "Direct about what!? There's no \"end goal\" to this conversation you can just rush to bull-headedly, like you do with everything else!"

        gambino "Oh, yeah? So you're just going to talk circles around who's actually the boss here, huh?"

        capone "It's both of us! You just said that!"

        gambino "Sure, sure. So completely equal, huh? Fifty-fifty?"

        show capone angry left

        capone "I've told you that we both share absolute control over the Piccino {i}famiglia!{/i} It's one hundred-one hundred!"

        gambino "MATH DOESN'T WORK LIKE THAT!"

        capone "Oh, so now you can {i}count{/i}!?"

        gambino "You shut your mouth, Capone! You know you wouldn't have a single one of the men following you without me to keep them in line!"

        capone "And you wouldn't have a single man alive if it weren't for me coming up with plans that aren't as direly suicidal as yours!"

        gambino "You don't know how my plans would work out, because you never let me run any of 'em! You just keep me around to yell at the men!"

        show capone happy left

        capone "Give the dog a cookie! You get it!"

        gambino "...You... You {i}bastardo{/i}."

        show capone left

        capone "Face it, Gambino. You're dumb muscle. \"Ace\" here could replace you in a heartbeat."

        gambino "Yeah? Well, here's something maybe you didn't consider. You're just a tactician. Disposable brainpower. Ace could replace you, too. The men wouldn't blink twice."

        show capone angry left

        capone "WHAT!? Dis-- disposable BRAINPOWER!? That's not-- you can't-- I'm VITAL to this operation!"

        gambino "Oh, yeah? And what would change tomorrow if you disappeared today? Do the men need to be told to do the same neighborhood shakedowns they've been doing for the past two months? You're through."

        a "(Now's my chance. I've become the kingmaker. I can goad either of them into attacking the other. The only question left is.... who would be a better ally in the future?)"

        a "(Capone is cunning. He can help with strategies and tactical plays. He probably has greater knowledge about the nations of this world, as well as the political situations this Lateran war has caused.)"

        a "(Gambino, though, has the loyalty of his men. Holding Piccino would be easier with his help, and I could probably sway him toward whatever cause I want more easily than I could Capone.)"

        menu:
            "Side with Capone.":
                capone "I've had it, Gambino! You're a useless moron I've shackled myself to for too long!"

                a "Capone, I'm with you."

                show capone left

                capone "I... wait, pardon?"

                gambino "Oh, yeah, {i}you're{/i} the smart one, but you didn't see this mook's obvious plan to turn us against each other? Well, whatever, I've been looking for an opportunity to get rid of you, too! I'll take you all on!"

                show capone angry left

                capone "Urrrghh... fine! Ace, prove yourself to the Piccino {i}famiglia{/i} by taking out this traitor!"

                $ caponeop = Operator(CAPONE, 5, True, [ Tech(7) ])
                $ renpy.call_screen("Newmember", op=caponeop)
                $ party.append(caponeop)
                $ gambinoalive = False
                $ caponealive = True

                hide gambino
                hide capone
                hide ace

                call Battle(party, [Operator(GAMBINO, 10, False, [ Tech(6) ])])

            "Side with Gambino.":
                gambino "Enough, Capone! I'm changing our arrangement. I do all the work, and get none of the credit or respect! I'm not just an enforcer. I'm a Don!"

                a "Gambino, I'm with you."

                show gambino

                gambino "You... what?"

                capone "Credit? Respect? Bah! You couldn't even see this stranger's obvious plan to turn us against each other. You are due nothing but a swift end, delivered promptly by my crossbow!"

                show gambino angry

                gambino "Feh. You could never beat me in a straight fight, Capone. You're just making your mama cry, throwing your life away. Ace, crush this mook's skull."

                $ gambinoop = Operator(GAMBINO, 5, True, [ Tech(6) ])
                $ renpy.call_screen("Newmember", op=gambinoop)
                $ party.append(gambinoop)
                $ gambinoalive = True
                $ caponealive = False

                hide gambino
                hide capone
                hide ace

                call Battle(party, [Operator(CAPONE, 10, False, [ Tech(7) ])])

        if (gambinoalive):
            show ace at center with dissolve

            a "...Well, that's that, then."

            show gambino at midleft with dissolve

            hide ace with dissolve

            gambino "He's really dead, huh? I never thought I'd be free of him."

            gambino "..."

            gambino "Aw, Capone, why'd you have to go and make me hurt ya, huh? I only wanted you to get that I could be more than you let me be."

            capone "...Grrk."

            gambino "Huh? You're still alive?"

            show capone shadow left at midright with Dissolve(3.0)

            capone "Ah, you {i}bastardo{/i}. I always told you that if you killed me, I'd get the last word in."

            show gambino happy at midleft

            gambino "Yeah, but I figured you'd shoot me or somethin', not talk at me some more."

            capone "Yeah, well you always were impatient, brother."

            show gambino

            gambino "...I'm sorry, brother."

            capone "Eh. I attacked first. And I guess... I wasn't as clever as I thought I was. I let a random stranger turn my best friend against me in a matter of hours."

            gambino "You're really an idiot if you think that you \"let\" anything happen. You never had control over any of this."

            capone "Hah hah hah... I'd argue with you, but since I'm dying, I guess you've got a point."

            pause 2.0

            gambino "...Hey. I wouldn't do it again."

        else:
            show ace at center with dissolve

            a "...Well, that's that, then."

            show capone left at midright with dissolve

            hide ace with dissolve

            capone "Gambino, you fool... I never actually thought that you could die. I figured that if I shot you, you'd just get back up."

            capone "..."

            capone "Gambino, why'd you force my hand like this? We had a good deal going. We could've kept at it for another few decades, at least..."

            gambino "...Grrk."

            show capone shouting left

            capone "Gambino!? How on... I shot you through both lungs!"

            show gambino shadow at midleft with Dissolve(3.0)

            capone "...Didya... Ugh... Didya really think I was going to let you pretend this was {i}my{/i} fault, huh?"

            show capone happy left

            capone "Oh, Gambino. You were always stubborn to a fault."

            gambino "Heh. Got that from my brother."

            show capone left

            capone "...I'm sorry, brother."

            gambino "Bah. With my hot temper, I'm just surprised I haven't tried to kill you before now."

            capone "Guess I have to thank you for trying when it's just me and a couple of strangers. If you did this in front of the men... well, I'd still win, but I'd hate to have to take out the guys who joined you."

            gambino "Heh heh heh... Get it straight. If you tried this again... ugh... you wouldn't win."

            pause 2.0

            capone "...Gambino? I wouldn't do it again."

        a "Alright, that's all I needed to hear."

        gambino "Huh?"

        capone "Huh?"

        a "Lisa, if you will, please."

        show suzuran happy with dissolve

        "Suzuran" "Yes, Mr. Ace. I'll do my best!"

        nvl clear

        nvl show dissolve

        "Lisa closes her eyes and focuses her Arts through her staff. As her power flows through the ground, the area around you is illuminated by a bright blue haze."

        "This is not a surprise to you, of course, as during the two hours you spent at Rangers' orphanage, you determined Lisa had a very valuable noncombat proficiency."

        "Namely, she can heal a person back to full health, even when they're almost at the point of death."

        nvl clear

        "As Lisa concentrates, a little bead of sweat running down her diminutive forehead, the fallen mafioso's wounds start to seal, and the dried blood on his clothes starts to dissipate, washed away by Lisa's aura of purity."

        "{color=27C4CC}Your heart shifts towards the path of a doctor.{/color}"

        "...and so does {color=27C4CC}another{/color}."

        $ doctor += 1

        show gambino nervous

        show capone left

        gambino "...Heh, this is awkward."

        capone "Yeah, I don't think we would've been quite so direct if we knew we were both going to survive that encounter."

        gambino "...Well, there's something to be said for bein' direct, heh?"

        capone "Maybe a bit."

        hide suzuran with dissolve

        show ace with dissolve

        a "You're both too valuable for me to let either of you die for some stupid reason. But it better be clear to you both that I could outfight you, Gambino, and outsmart you, Capone."

        show gambino angry
        show capone angry left

        gambino "Yeah, what's your point?"

        a "I want in to the Piccino {i}famiglia{/i}."

        capone "That's what we were offering! You didn't have to kill one of us to get it!"

        a "I thought this way would make the seriousness of my intent clear."

        show gambino nervous

        gambino "...Was that a joke?"

        a "I'll let you continue ruling Piccino. You can do whatever you want as long as you follow three conditions."

        show capone left

        capone "Careful, Ace. You're still neck-deep in our turf. Don't ask too much of us."

        nvl clear

        nvl show dissolve

        "You raise your hammer."

        "They both flinch."

        "Point made."

        a "Condition one: You stop giving away so many Piccinians. The Laterans don't need that many. Let there be some adults in this city that don't work for your family. You need shopkeepers. You need teachers. You need infrastructure."

        a "Right now, you're just burning down the candle, with no plan for what you'll do when the wick reaches your fingers."

        capone "...It'll be difficult to explain to the men our sudden change of strategy."

        $ censor (gambino, "You kidding? They'll be relieved as hell. They won't question anything.")

        a "Condition two: You leave the West side alone. If any of your men fight the West Don's men, enter her territory, or even look too hard at that side of the city, I'm coming back."

        gambino "Well, the Don's granddaughter just brought someone back to life, so, yeah, I don't think I want to tangle with that kind of Arts power anyway. Fine by me."

        a "Condition three: You two are available to me whenever I need you. I'm planning on crossing continents. I'm planning on being a big player in this war. I'll need you to fight by my side once in a while. Think you can do that?"

        capone "...As long as we're not too far away from the city for too long, I suppose that's fine..."

        gambino "We can't both be gone at the same time, but yeah, we could do that. Been tryin' to get out more, anyway..."

        a "Good. And remember, if you break any of these three conditions, I'm coming back to dismantle your {i}famiglia{/i} myself."

        capone "Even from what I've seen, I don't think you could... but I don't want to risk it."

        a "Smart."

        a "...Oh, one more thing."

        gambino "Eh?"

        if (headhunterspared):
            a "Guido's good. You're not killing him."

            show gambino angry
            show capone angry

            $ censor(capone, "Goddamn, I was hoping you'd forgotten about that.")

            headhunter "Dons, seriously, what's your beef? What did I do to make you hate me so much?"

            gambino "Oh, not much, you just brought {i}this{/i} monster directly to us, unraveling the {i}famiglia{/i} that took us months to set up, in a matter of hours."

            headhunter "...Oh, fair."

            a "Water under the bridge. Now, we need a car. Something sporty."

        else:
            a "We need a car. Get us something sporty."

        capone "Agh. This guy's intolerable, huh, Gambino?"

        gambino "Full agreement."

        nvl clear

        nvl show dissolve

        "Though they grumble, the Dons eventually produce a vehicle that fits your criteria, and twenty minutes later, you're at the rendezvous point with Aosta and Broca."

    else:
        a "No."

        show capone angry left
        show gambino angry

        capone "Eh, I must've misheard you. You want to run that by me again?"

        gambino "You're not backing out on our deal now, are you? 'Cause that's a bad idea."

        a "I'm here to kill you. Lisa will be leaving with me. And we'll appoint someone else as the Don of Piccino. Your men will gladly accept a new boss who doesn't sell them to the Laterans."

        capone "..."

        gambino "..."

        show capone happy left
        show gambino happy

        capone "You disappoint me, \"Ace.\" I really thought that you'd make a good addition to our {i}famiglia{/i}. I guess I should've listened to Gambino, eh?"

        gambino "That's what I've been trying to tell you, {i}fratello{/i}. But, eh, a lesson learned late is still a lesson learned, eh?"

        capone "Seems even an old wolf like me can learn some new tricks."

        gambino "Speaking of tricks, I'm sometimes known as the attack dog of the Piccino Famiglia."

        capone "And like every good attack dog, it really just takes a word to set him off."

        gambino "We're a good pair, my blood brother and I. We disagree on a lot, but when we're in sync, we're pretty much unstoppable."

        capone "There's a reason the men follow us. And it's not 'cause we talk pretty."

        gambino "Yeah, see, we know a few ways to keep people in line. Not necessarily the by-the-book ways, nah, but they're effective."

        capone "The men didn't always volunteer for the front lines, y'know. They had to be persuaded, at first."

        gambino "I bet you're wondering how we persuaded them."

        capone "We know a trick or two."

        gambino "Wanna see?"

        show capone angry left
        show gambino angry

        capone "{i}Sic 'em.{/i}"

        hide gambino
        hide capone
        hide ace

        $ gambinoalive = False
        $ caponealive = False

        call Battle(party,
            [],
            [None, None, None, None, None, None, None, Operator(GAMBINO, 5, False, [ Tech(6) ]), Operator(CAPONE, 5, False, [ Tech(7) ])],
            [True, None, None, None, None, None, None, False, False])

        show ace at midleft with dissolve

        a "...Well, that's that, then."

        show chiave confused at midright with dissolve

        chiave "...We really killed them. Both of them. They were... they were just alive, and now..."

        show suzuran surprised with dissolve

        nvl clear

        nvl show dissolve

        "You look back at the rest of your companions. Chiave is shuddering, having developed a fascination with his wrench. Shamare and Vermeil are looking very intently at the ground, glistening pinpricks in the corners of their eyes."

        "Lisa, though... she's hugging her seven tails to her chest, but looking directly at your bloodied hammer. Her big, emerald, eyes stare at you without judgement--with understanding."

        "{color=FF0000}Your heart shifts towards the path of a killer.{/color}"

        "...and so does {color=FF0000}another.{/color}"

        $ killer += 1

        nvl clear

        "The streets seem empty. You can see gangsters rushing out of your way out of the corner of your eye. There's a power vacuum here, ripe and ready to be stepped into. Without problems, you find an abandoned car, and make your way back to the rendezvous point, where Aosta and Broca are waiting."

    "Their discouragement at being unable to find a single child is quickly dispelled as you explain what's happened on your side."

    "They do not believe you even for a moment, though the veracity of your story isn't helped by Chiave's enthusiastic embellishments."

    if (headhunterspared):
        "You allow them to disbelieve. They'll see the truth eventually. For now, the three kids, the three freedom fighters, Guido, and you, all pile into your respective vehicles, and begin the drive back to Siracusa."

    else:
        "You allow them to disbelieve. They'll see the truth eventually. For now, the three kids, the three freedom fighters, and you, all pile into your respective vehicles, and begin the drive back to Siracusa."

    scene sunsetroad with dissolve

    nvl clear

    "Your head is racing with plans. How will you utilize your newly-acquired asset? You wonder..."

    "All that you can be certain of is that you've now shifted the balance of power in this world in a relatively minor way. Certainly not the sort of way the Laterans will notice."

    "But enough. {i}Definitely{/i} enough for one day's work."

    "You sit back with your hand on the steering wheel, and smile grimly. This is going to be a fun war."

    #killer: 4
    #doctor: 3

    nvl clear

    "{b}END OF DEMO! Thanks for playing!{/b}"

    nvl clear

    "And now, the requisite credits. I'll move these to the main menu later."

    "The Forest and the Trees by Kevin MacLeod. Link: https://incompetech.filmmusic.io/song/4494-the-forest-and-the-trees. License: https://filmmusic.io/standard-license"

    "Welcome to the Show by Kevin MacLeod. Link: https://incompetech.filmmusic.io/song/4614-welcome-to-the-show. License: https://filmmusic.io/standard-license"

    "Rains Will Fall by Kevin MacLeod. Link: https://incompetech.filmmusic.io/song/4262-rains-will-fall. License: https://filmmusic.io/standard-license"

    "Kawai Kitsune by Kevin MacLeod. Link: https://incompetech.filmmusic.io/song/4990-kawai-kitsune. License: https://filmmusic.io/standard-license"

    "Basic Implosion by Kevin MacLeod. Link: https://incompetech.filmmusic.io/song/3420-basic-implosion. License: https://filmmusic.io/standard-license"

    # This ends the game.

    return
