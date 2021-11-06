label Battle(ops, otherOps):
    window hide#Ren'Py function that hides the built-in gui

    show tactics with dissolve

    python:
        import random

        battlefield = [None, None, None, None, None, None, None, None, None]

        renpy.show_screen("frontman")#display the prompt to select the frontman for the battle
        first = renpy.call_screen("setup")#select the frontman
        battlefield[0] = first#assign the chosen frontman to square 1
        battlefield[8] = otherOps[0]#assign the enemy's frontman to square 9
        myCost = first.getparameter(COST)#get the DP saved by choosing this frontman
        otherCost = otherOps[0].getparameter(COST)#get the DP saved by the enemy
        #It's your turn if you saved less than the foe, or if you saved the same amount, but got lucky
        myTurn = myCost < otherCost or (myCost == otherCost and random.randrange(10) <= 5)

    hide tactics with dissolve

    while(True):
        if myTurn:
            $ action = renpy.call_screen("battleui")

            if (action == 'attack'):
                $ print("chose an attack")

            elif (action == 'tech'):
                $ print("chose a tech")

            elif (action == 'move'):
                $ print("chose to move")

            elif (action == 'item'):
                $ print("chose an item")
        else:
            $ print("foe's turn happened")


        myTurn = !myTurn

    pause(5.0)
