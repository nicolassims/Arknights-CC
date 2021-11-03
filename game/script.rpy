# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
    # Declare positions used by this game
    midleft = Position(xpos = 0.25)
    midright = Position(xpos = 0.75)
        
    # Declare variables used by this game
    playerfirstname = "You"
    playerlastname = "The Operator"

define who = Character("???")
define a = DynamicCharacter("playerfirstname")
define narrator = nvl_narrator

# Backgrounds
image black = "#000000"
image white = "#ffffff"
image ruinedTent = im.Scale("ruinedtent.png", 1920, 1080)
image forest = im.Scale("forest.png", 1920, 1080)

# Characters
image ace = "ace.png"
image ace shadow = "shadowace.png"

#Transitions
transform moveleft:
    linear 0.5 xpos 0.15

#CC == Contingency Contract && Catastrophe Caller

# The game starts here.

label start:

    scene black with Dissolve(2)
    
    a "...Ow."
    
    a "...Where am I?"
    
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
    
    nvl clear
    
    window hide dissolve
    
    show ruinedTent behind ace with Dissolve(2)
    
    show ace with dissolve
    
    a "...Hm. I'm in some shit, huh? A hammer, a shield, a whole lot of carbon-fiber body armor, and everything around me's torn to shreds."
    
    a "Don't know who I am, don't know where I am, and I don't know why I'm kitted out like this... but all this points to me having just walked out of a pretty tough fight."
    
    a "...Aw, shit, I don't know who I am. I don't even remember my name? What the hell happened?"
    
    a "Guess I better make something up..."
    
    $ playerfirstname = renpy.input("My first name'll be...", allow='QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890-.', length=12).strip().title()
       
    $ playerlastname = renpy.input("Sure, sure. And my last name'll be...", allow='QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890-.', length=12).strip().title()
    
    a "Huh. This uniform's got a patch that says \"Ace\" on it. And... Rhodes Island? Is that who I work with?"
    
    a "...Ugh. I better find someone who can point me in the right direction. And maybe tell me what the right direction is, too."
    
    show ace at midleft with ease
    
    call Crawl(guerroforest, 6, 3, guerroknowledge)

    

    # These display lines of dialogue.

    a "You've created a new Ren'Py game."

    a "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
