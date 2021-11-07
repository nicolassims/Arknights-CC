label Battle(ops, otherOps):
    window hide#Ren'Py function that hides the built-in gui

    show tactics with dissolve

    python:
        actionlist = []
        battlefield = [None, otherOps[0], None, None, None, None, None, None, None]
        ownedfield = [True, False, None, None, None, None, None, None, False]#cycles through None, True, and False
        mydp = 0
        otherdp = 0

        renpy.show_screen("frontman")#display the prompt to select the frontman for the battle
        first = renpy.call_screen("setup", back=False)#select the frontman
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

                        incapacitated = renpy.call_screen("useattack", source=actor, targets=targets, hits=1, atkbuff=1, elements=[None])
                        for op in incapacitated:
                            battlefield[battlefield.index(op)] = None
                            actionlist.remove(op)
                            del op

                    elif (action == 'tech'):
                        techchoice = renpy.call_screen("usetech", op=actor)
                        targetpos = renpy.call_screen("targeting", location=actorpos, minrange=techchoice.getparameter(MINRANGE), maxrange=techchoice.getparameter(MAXRANGE), aoe=techchoice.getparameter(AOE), target="op")
                        targets = []

                        for i in targetpos:
                            targets.append(battlefield[i])

                        incapacitated = renpy.call_screen("useattack", source=actor, targets=targets, hits=techchoice.getparameter(HITS), atkbuff=techchoice.getparameter(DAMAGE), elements=[techchoice.getparameter(ELEMENT)])

                        techchoice.setparameter(POINTS, techchoice.getparameter(POINTS) - techchoice.getparameter(COST))

                        for op in list(set(incapacitated)):
                            battlefield[battlefield.index(op)] = None
                            actionlist.remove(op)
                            del op

                    elif (action == 'move'):
                        #this list should always only have one element, so just pull the first element from the list for the targetpos
                        targetpos = renpy.call_screen("targeting", location=actorpos, minrange=0, maxrange=math.floor(actor.getparameter(MOVEPOINTS)), aoe=False, target="empty")[0]
                        actor.setparameter(MOVEPOINTS, actor.getparameter(MOVEPOINTS) - abs(actorpos-targetpos))
                        battlefield[actorpos] = None
                        battlefield[targetpos] = actor
                        ownedfield[targetpos] = True
                        actorpos = targetpos#make actorpos accurate again, in case of use later

                    elif (action == 'item'):
                        techchoice = renpy.call_screen("useitem")

                    elif (action == 'deploy'):
                        operator = renpy.call_screen("deploy")

                    elif (action == 'pass'):
                        renpy.say(actor.getparameter(CODENAME), passtring(actor.getparameter(ID)))

                else:
                    print("foe's turn happened")

                #run end of turn clean-up
                if (actor.getparameter(MOVEPOINTS) < 1):#if this unit can't move at least one square yet...
                    actor.setparameter(MOVEPOINTS, actor.getparameter(MOVEPOINTS) + actor.getparameter(MOV))#increase their move points by the requisite amount

                for tech in actor.getparameter(TECHS):
                    if (tech.getparameter(GAINTYPE) == "Waiting"):
                        tech.setparameter(POINTS, min(tech.getparameter(COST) * tech.getparameter(CHARGES), tech.getparameter(POINTS) + tech.getparameter(GAINPER)))

                for i, claim in enumerate(ownedfield):
                    if (claim == True):
                        mydp = min(99, mydp + battlefieldPoints(i))
                    elif (claim == False):
                        otherdp = min(99, otherdp + battlefieldPoints(i))
                actionlist.pop(0)
                actionlist.append(actor)
