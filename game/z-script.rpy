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

    doctor = 0
    killer = 0

    party = [aceop]

    inventory = []

    rocksickspared = None

    swearing = True

define who = Character("???")
define a = DynamicCharacter("playerfirstname")
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
image ace = "chars/ace/ace.png"
image ace shadow = "chars/ace/shadowace.png"
image rocksick = "chars/rocksick/rocksick.png"
image rocksick left = Transform("chars/rocksick/rocksick.png", xzoom=-1)

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



    # These display lines of dialogue.

    a "You've created a new Ren'Py game."

    a "Once you add a story, pictures, and music, you can release it to the world!"


    nvl show dissolve

    "And now, the requisite credits. I'll move these to the main menu later."

    "The Forest and the Trees by Kevin MacLeod. Link: https://incompetech.filmmusic.io/song/4494-the-forest-and-the-trees. License: https://filmmusic.io/standard-license"

    # This ends the game.

    return
