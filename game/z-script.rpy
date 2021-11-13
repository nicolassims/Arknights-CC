# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init 3 python:
    import copy

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
image safehouse = Transform("bgs/safehouse.png", xsize=1920, ysize=1080)
image road = Transform("bgs/road.jpg", xsize=1920, ysize=1080)

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
image blaze shadow = scaleportrait("chars/blaze/shadowblaze.png", 172, True)

#Transitions
transform moveleft:
    linear 0.5 xpos 0.15

transform mymovein(timing, start, destination):
    yalign 1.0 xanchor 0.5 xpos start
    linear timing xpos destination

# The game starts here.

label start:

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

    scene change road

    a "...Pretty out here."

    chiave "Yeah, and I haven't seen the sunrise in {i}months{/i}, so thanks for breaking that streak by waking us up at the crack of dawn. Damn old people sleep schedules."

    a "I have a hammer."

    chiave "Big deal, I've got a wrench."




    #$ Call("title", title="Chapter 1", subtitle="Dustbreaking Footfalls")

    # These display lines of dialogue.

    "{b}END OF DEMO! Thanks for playing!{/b}"

    nvl show dissolve

    nvl clear

    "And now, the requisite credits. I'll move these to the main menu later."

    "The Forest and the Trees by Kevin MacLeod. Link: https://incompetech.filmmusic.io/song/4494-the-forest-and-the-trees. License: https://filmmusic.io/standard-license"

    "Welcome to the Show by Kevin MacLeod. Link: https://incompetech.filmmusic.io/song/4614-welcome-to-the-show. License: https://filmmusic.io/standard-license"

    "Rains Will Fall by Kevin MacLeod. Link: https://incompetech.filmmusic.io/song/4262-rains-will-fall. License: https://filmmusic.io/standard-license"

    "Kawai Kitsune by Kevin MacLeod. Link: https://incompetech.filmmusic.io/song/4990-kawai-kitsune. License: https://filmmusic.io/standard-license"

    "Basic Implosion by Kevin MacLeod. Link: https://incompetech.filmmusic.io/song/3420-basic-implosion. License: https://filmmusic.io/standard-license"

    # This ends the game.

    return
