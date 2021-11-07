label Battle(ops, otherOps):
    window hide#Ren'Py function that hides the built-in gui

    show tactics with dissolve

    python:
        actionlist = []
        battlefield = [None, otherOps[0], None, None, None, None, None, None, None]

        renpy.show_screen("frontman")#display the prompt to select the frontman for the battle
        first = renpy.call_screen("setup")#select the frontman
        battlefield[0] = first#assign the chosen frontman to square 1
        battlefield[8] = otherOps[0]#assign the enemy's frontman to square 9
        myCost = first.getparameter(COST)#get the DP saved by choosing this frontman
        otherCost = otherOps[0].getparameter(COST)#get the DP saved by the enemy
        #It's your turn if you saved less than the foe, or if you saved the same amount, but got lucky
        actionlist.append(first)
        if (myCost < otherCost or (myCost == otherCost and renpy.random.random() <= .5)):
            actionlist.append(otherOps[0])
        else:
            actionlist.insert(0, otherOps[0])

    hide tactics with dissolve

    while(True):
        label badmove:
            python:
                actor = actionlist[0]
                actorpos = battlefield.index(actor)
                if actor.getparameter(ALLY):
                    action = renpy.call_screen("battleui")
                    if (action == 'attack'):
                        targetpos = renpy.call_screen("targeting", location=actorpos, minrange=actor.getparameter(MINRANGE), maxrange=actor.getparameter(MAXRANGE), aoe=False, target="op")
                        targets = []
                        for i in targetpos:
                            targets.append(battlefield[i])

                        incapacitated = renpy.call_screen("useattack", source=actor, targets=targets)
                        for op in incapacitated:
                            battlefield[battlefield.index(op)] = None
                            actionlist.remove(op)
                            del op

                    elif (action == 'tech'):
                        print("chose a tech")

                    elif (action == 'move'):
                        #this list should always only have one element, so just pull the first element from the list for the targetpos
                        targetpos = renpy.call_screen("targeting", location=actorpos, minrange=0, maxrange=math.floor(actor.getparameter(MOVEPOINTS)), aoe=False, target="empty")[0]
                        actor.setparameter(MOVEPOINTS, actor.getparameter(MOVEPOINTS) - abs(actorpos-targetpos))
                        battlefield[actorpos] = None
                        battlefield[targetpos] = actor

                    elif (action == 'item'):
                        print("chose an item")

                    elif (action == 'pass'):
                        renpy.say(a, "A wasted turn. Poor strategy on my part.")

                else:
                    print("foe's turn happened")

                if (actor.getparameter(MOVEPOINTS) < 1):#if this unit can't move at least one square yet...
                    actor.setparameter(MOVEPOINTS, actor.getparameter(MOVEPOINTS) + actor.getparameter(MOV))#increase their move points by the requisite amount

                actionlist.pop(0)
                actionlist.append(actor)
