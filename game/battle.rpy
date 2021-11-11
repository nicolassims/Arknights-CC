label Battle(ops, otherOps):
    window hide#Ren'Py function that hides the built-in gui

    show tactics with dissolve

    python:
        actionlist = []
        battlefield = [None, None, None, None, None, None, None, None, None]
        ownedfield = [True, None, None, None, None, None, None, None, False]#cycles through None, True, and False
        mydp = 0
        otherdp = 0
        exiting = False

        enemyxp = 0#the amount of experience these enemies will grant
        for enemyop in otherOps:
            enemyxp = max(enemyop.getparameter(LEVEL), 1)#get the maximum of 1 and the foe's level
        enemyxp = int(enemyxp * (1 + len(otherOps) / 10.0))#increase total enemyxp based on the number of foes

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
        ops.remove(battlefield[0])#remove your frontman from your party
        otherOps.remove(battlefield[8])#remove your enemy's frontman from your enemy's party
        battlefield[0].setparameter(MOVEPOINTS, 1)#set movement to 1, so you don't have to skip your first turn
        battlefield[8].setparameter(MOVEPOINTS, 1)#set movement to 1, so you don't have to skip your first turn




    hide tactics with dissolve

    while (not exiting):
        label badmove:
            python:
                actor = actionlist[0]
                actorpos = battlefield.index(actor)
                incapacitated = []
                if actor.getparameter(ALLY):
                    action = renpy.call_screen("battleui")
                    if (action == 'attack'):
                        targetpos = renpy.call_screen("targeting", location=actorpos, minrange=actor.getparameter(MINRANGE), maxrange=actor.getparameter(MAXRANGE), aoe=False, target="op", deploying=0)
                        targets = []
                        for i in targetpos:
                            targets.append(battlefield[i])

                        incapacitated = renpy.call_screen("useattack", source=actor, targets=targets, hits=1, atkbuff=1, elements=[None], effect=0)

                    elif (action == 'tech'):
                        techchoice = renpy.call_screen("usetech", op=actor)
                        targetpos = renpy.call_screen("targeting", location=actorpos, minrange=techchoice.getparameter(MINRANGE), maxrange=techchoice.getparameter(MAXRANGE), aoe=techchoice.getparameter(AOE), target="op", deploying=0)
                        targets = []

                        for i in targetpos:
                            targets.append(battlefield[i])

                        incapacitated = renpy.call_screen("useattack", source=actor, targets=targets, hits=techchoice.getparameter(HITS), atkbuff=techchoice.getparameter(DAMAGE), elements=[techchoice.getparameter(ELEMENT)], effect=techchoice)

                        techchoice.setparameter(POINTS, techchoice.getparameter(POINTS) - techchoice.getparameter(COST))

                    elif (action == 'move'):
                        #this list should always only have one element, so just pull the first element from the list for the targetpos
                        targetpos = renpy.call_screen("targeting", location=actorpos, minrange=0, maxrange=math.floor(actor.getparameter(MOVEPOINTS)), aoe=False, target="empty", deploying=0)[0]
                        actor.setparameter(MOVEPOINTS, actor.getparameter(MOVEPOINTS) - abs(actorpos-targetpos))
                        battlefield[actorpos] = None
                        battlefield[targetpos] = actor
                        ownedfield[targetpos] = True
                        actorpos = targetpos#make actorpos accurate again, in case of use later

                    elif (action == 'item'):
                        techchoice = renpy.call_screen("useitem")

                    elif (action == 'deploy'):
                        operator = renpy.call_screen("deploy")
                        targetpos = renpy.call_screen("targeting", location=0, minrange=0, maxrange=8, aoe=False, target="empty", deploying=operator.getparameter(COST))[0]
                        battlefield[targetpos] = operator
                        actionlist.append(operator)
                        ops.remove(operator)
                        mydp -= operator.getparameter(COST) + targetpos * 10

                    elif (action == 'pass'):
                        renpy.say(actor.getparameter(CODENAME), passtring(actor.getparameter(ID)))

                else:
                    action = prioritize(0)
                    actiontype = action[0]

                    if (actiontype == 'attack'):#("attack", [op])
                        incapacitated = renpy.call_screen("useattack", source=actor, targets=action[1], hits=1, atkbuff=1, elements=[None], effect=0)

                    elif (actiontype == 'tech'):#("tech", tech, [op])
                        techchoice = action[1]
                        incapacitated = renpy.call_screen("useattack", source=actor, targets=action[2], hits=techchoice.getparameter(HITS), atkbuff=techchoice.getparameter(DAMAGE), elements=[techchoice.getparameter(ELEMENT)], effect=techchoice)
                        techchoice.setparameter(POINTS, techchoice.getparameter(POINTS) - techchoice.getparameter(COST))

                    elif (actiontype == 'move'):#("move", i)
                        #this list should always only have one element, so just pull the first element from the list for the targetpos
                        targetpos = action[1]
                        actor.setparameter(MOVEPOINTS, actor.getparameter(MOVEPOINTS) - abs(actorpos-targetpos))
                        battlefield[actorpos] = None
                        battlefield[targetpos] = actor
                        ownedfield[targetpos] = False
                        actorpos = targetpos#make actorpos accurate again, in case of use later

                    elif (actiontype == 'deploy'):#("deploy", op, i)
                        operator = action[1]
                        targetpos = action[2]
                        battlefield[targetpos] = operator
                        actionlist.append(operator)
                        otherOps.remove(operator)
                        otherdp -= operator.getparameter(COST) + (8 - targetpos) * 10

                    elif (actiontype == 'pass'):#("pass")
                        renpy.say(a, "Looks like they're just watching and waiting...")

                #run end of turn clean-up
                for op in incapacitated:
                    battlefield[battlefield.index(op)] = None
                    actionlist.remove(op)
                    del op

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

                actionlist.pop(0)#this might become a problem someday if an operator can incapacitate themself
                actionlist.append(actor)

                oneAlly = False
                oneEnemy = False
                for op in actionlist:
                    if op.getparameter(ALLY):
                        oneAlly = True
                    else:
                        oneEnemy = True

                if (not oneEnemy):
                    renpy.say(a, "...Secured the battlefield. That looks like a victory to me.")
                    exiting = True

                if (not oneAlly):
                    renpy.say(a, "...Cut off and surrounded by enemies. Time for another last stand.")
                    renpy.say("", "Doctor, surely, you're not going to leave it at that, will you? Go on, reload your save. Fight for the dawn.")
                    MainMenu(confirm=False)()

    python:
        for op in battlefield:
            if (op != None and op.getparameter(ALLY)):
                ops.append(op)

        for op in ops:
            op.setparameter(EXPERIENCE, op.getparameter(EXPERIENCE) + enemyxp * 20)

            while (op.getparameter(EXPERIENCE) >= fibonacci(op.getparameter(LEVEL))):
                op.setparameter(EXPERIENCE, op.getparameter(EXPERIENCE) - fibonacci(op.getparameter(LEVEL)))
                op.setparameter(LEVEL, op.getparameter(LEVEL) + 1)

                statgains = []
                opid = op.getparameter(ID) - 1
                for stat in range(HEALTH, ARTSDEF + 1):
                    statgained = 0
                    odds = opdex[opid][stat]

                    while (odds > 1):
                        statgained += 1
                        odds -= 1.0

                    if (renpy.random.random() <= odds):
                        statgained += 1

                    statgains.append(statgained)

                for i, statgain in enumerate(statgains):
                    op.setparameter(i + HEALTH, op.getparameter(i + HEALTH) + statgains[i])

                renpy.call_screen("levelup", op=op, statgains=statgains)
