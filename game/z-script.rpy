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

    party = [aceop, kroosop]

    inventory = []

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

# Characters
image ace = "chars/ace/ace.png"
image ace shadow = "chars/ace/shadowace.png"

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

    a "Huh. This uniform's got a patch that says \"Ace\" on it. And... Rhodes Island? Is that who I work with?"

    a "...Ugh. I better find someone who can point me in the right direction. And maybe tell me what the right direction is, too."

    show ace at midleft with ease

    call Crawl(guerroforest, 6, 3, guerroknowledge, True)

    show ace at center with ease

    show outcounty behind ace with dissolve

    a "Finally an end to all that grass and smoke. It's a miracle the whole forest didn't burn down from whatever caused... that."

    a "Looks like there's a village ahead. With any luck, they'll have a way to get in contact with these \"Rhodes Island\" people. Maybe they'll be able to tell me why I'm wearing their getup.\n...Maybe they'll have a paycheck for me."

    a "...What the hell is that running towards me?"

    hide ace with dissolve

    call Battle(party, [enemyaceop, enemykroosop])



    # These display lines of dialogue.

    a "You've created a new Ren'Py game."

    a "Once you add a story, pictures, and music, you can release it to the world!"


    nvl show dissolve

    "And now, the requisite credits. I'll move these to the main menu later."

    "The Forest and the Trees by Kevin MacLeod. Link: https://incompetech.filmmusic.io/song/4494-the-forest-and-the-trees. License: https://filmmusic.io/standard-license"

    # This ends the game.

    return
