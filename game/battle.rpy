label Battle(myOps, otherOps, passedbattlefield=None, passedownedfield=None):
    window hide#Ren'Py function that hides the built-in gui

    play music "audio/battle.mp3" loop

    show tactics with dissolve

    python:
        renpy.suspend_rollback(True)

        ops = copy.deepcopy(myOps)

        buffs = []#format is [operator, stat, amount, multiplication, turnsleft, originalstat]. that's [object, int, float/int, bool/float, int, int]
        actionlist = []
        if (passedbattlefield == None):
            battlefield = [None, None, None, None, None, None, None, None, None]
        else:
            battlefield = passedbattlefield
        if (passedownedfield == None):
            ownedfield = [True, None, None, None, None, None, None, None, False]#cycles through None, True, and False
        else:
            ownedfield = passedownedfield
        mydp = 0
        otherdp = 0
        mydpgain = 2
        otherdpgain = 2
        exiting = False

        enemyxp = 0#the amount of experience these enemies will grant
        for enemyop in otherOps:
            enemyxp = max(enemyop.getparameter(LEVEL), 1)#get the maximum of 1 and the foe's level
        enemyxp = int(enemyxp * (1 + len(otherOps) / 10.0))#increase total enemyxp based on the number of foes

        renpy.show_screen("frontman")#display the prompt to select the frontman for the battle
        first = renpy.call_screen("setup", back=False)#select the frontman
        battlefield[0] = first#assign the chosen frontman to square 1
        myCost = first.getparameter(COST)#get the DP saved by choosing this frontman
        if (len(otherOps) != 0):
            otherCost = otherOps[0].getparameter(COST)#get the DP saved by the enemy
            #It's your turn if you saved less than the foe, or if you saved the same amount, but got lucky
            actionlist.append(first)
            if (myCost < otherCost or (myCost == otherCost and renpy.random.random() <= .5)):
                actionlist.append(otherOps[0])
            else:
                actionlist.insert(0, otherOps[0])
            battlefield[8] = otherOps[0]#assign the enemy's frontman to square 9
            otherOps.remove(battlefield[8])#remove your enemy's frontman from your enemy's party
            battlefield[8].setparameter(MOVEPOINTS, 1)#set movement to 1, so you don't have to skip your first turn
        else:
            otherCost = 99
            for op in battlefield:
                if (op != None):
                    actionlist.append(op)

        battlefield[0].setparameter(MOVEPOINTS, 1)#set movement to 1, so you don't have to skip your first turn
        ops.remove(battlefield[0])#remove your frontman from your party


        renpy.suspend_rollback(False)

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

                #RUN END OF TURN CLEAN-UP
                actorMaxHealth = actor.getparameter(MAXHEALTH)
                if (actor.getparameter(ID) == ROCKSICK and actor.getparameter(HEALTH) < actorMaxHealth):#ROCKSICK TALENT, Rocksick's talent
                    healthgained = min(actorMaxHealth - actor.getparameter(HEALTH), actorMaxHealth / 10)
                    actor.setparameter(HEALTH, actor.getparameter(HEALTH) + healthgained)
                    damagereport = "{b}Rocksick regenerates, gaining " + str(healthgained) + " health!{/b} "
                    talentblurb = renpy.call_screen("showmessage", message=damagereport)

                mydpgain = 0
                otherdpgain = 0
                for i, claim in enumerate(ownedfield):
                    points = battlefieldPoints(i)
                    if (claim == True):
                        mydpgain += points
                    elif (claim == False):
                        otherdpgain += points

                for op in incapacitated:
                    if (op.getparameter(ID) == CHIAVE):#CHIAVE Talent, Chiave's talent
                        if (op.getparameter(ALLY)):
                            dpreport = "{b}Chiave lets out a rallying cry as he falls! Gained " + str(mydpgain * 2) + " DP!{/b} "
                            mydp = min(mydp + mydpgain * 2, 99)
                        else:
                            dpreport = "{b}Foe Chiave lets out a rallying cry as he falls! Foes gained " + str(otherdpgain * 2) + " DP!{/b} "
                            otherdp = min(otherdp + otherdpgain * 2, 99)
                        talentblurb = renpy.call_screen("showmessage", message=dpreport)

                    if (op == actor):
                        actor = None

                    if (actor != None and actor.getparameter(ID) == GAMBINO):#GAMBINO TALENT, Gambino's talent
                        battlefield[battlefield.index(op)] = actor
                        battlefield[actorpos] = None
                        actorpos = battlefield.index(actor)
                        ownedfield[actorpos] = actor.getparameter(ALLY)
                        talentblurb = renpy.call_screen("showmessage", message="{b}Gambino keeps charging forward!{/b}")
                    else:
                        battlefield[battlefield.index(op)] = None

                    actionlist.remove(op)
                    del op

                if (actor != None):
                    actor.setparameter(MOVEPOINTS, min(max(actor.getparameter(MOV), 1), actor.getparameter(MOVEPOINTS) + actor.getparameter(MOV)))#increase their move points by the requisite amount

                    for tech in actor.getparameter(TECHS):
                        if (tech.getparameter(GAINTYPE) == "Waiting"):
                            tech.setparameter(POINTS, min(tech.getparameter(COST) * tech.getparameter(CHARGES), tech.getparameter(POINTS) + tech.getparameter(GAINPER)))

                    for i, claim in enumerate(ownedfield):
                        if (actor.getparameter(ALLY) and claim == True):
                            mydp = min(99, mydp + battlefieldPoints(i))
                        elif (not actor.getparameter(ALLY) and claim == False):
                            otherdp = min(99, otherdp + battlefieldPoints(i))

                    if (len(actionlist) > 1):
                        actionlist.pop(0)
                        actionlist.append(actor)

                oneAlly = False
                oneEnemy = False
                for op in actionlist:
                    if op.getparameter(ALLY):
                        oneAlly = True
                    else:
                        oneEnemy = True

                if (not oneAlly):
                    renpy.say(a, "...Cut off and surrounded by enemies. Time for another last stand.")
                    renpy.say("", "Doctor, surely, you're not going to leave it at that, are you? Go on, reload your save. Fight for the dawn.")
                    MainMenu(confirm=False)()

                if (not oneEnemy):
                    renpy.say(a, "...Secured the battlefield. That looks like a victory to me.")
                    exiting = True

                #format is [operator, stat, amount, multiplication, turnsleft, originalstat]. that's [object, int, float/int, bool, int, int]
                for i, buff in enumerate(buffs):
                    if (buff[0] != None):
                        buff[4] -= 1#increment the buff
                        if (buff[4] < 0):#revert the buff
                            if (buff[3]):
                                if (buff[2] == 0):
                                    buff[0].setparameter(buff[1], buff[5])
                                else:
                                    buff[0].setparameter(buff[1], buff[0].getparameter(buff[1]) / buff[2])
                            else:
                                buff[0].setparameter(buff[1], buff[0].getparameter(buff[1]) - buff[2])

                            del buff

                    else:
                        #remove it
                        del buff

    python:#end of battle
        for op in myOps:
            op.setparameter(EXPERIENCE, op.getparameter(EXPERIENCE) + enemyxp)

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

                if (i == 0):#also increase maxhp
                    op.setparameter(MAXHEALTH, op.getparameter(MAXHEALTH) + statgains[0])

                renpy.call_screen("levelup", op=op, statgains=statgains)
