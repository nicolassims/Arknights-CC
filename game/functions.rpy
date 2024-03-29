init python:
    def battlefieldPoints(pos):
        if (pos == 4):
            return 3
        elif (pos == 1 or pos == 2 or pos == 6 or pos == 7):
            return 1
        else:
            return 2

    def hitsStrings(hits):
        if (hits == 1):
            return ""
        elif (hits == 2):
            return " with two hits"
        elif (hits == 3):
            return " with three hits"
        elif (hits == 4):
            return " with four hits"
        elif (hits == 5):
            return " with five hits"
        else:
            return " with " + str(hits) + " hits"

    def effectiveness(offensetypes, defensetypes):
        effect = 1
        for atktype in offensetypes:
            for deftype in defensetypes:
                if (atktype == "Shoot"):
                    if (deftype == "Shield"):
                        effect *= 0.5
                    elif (deftype == "Strike"):
                        effect *= 2
                elif (atktype == "Shield"):
                    if (deftype == "Shoot"):
                        effect *= 2
                    elif (deftype == "Strike"):
                        effect *= 0.5
                elif (atktype == "Strike"):
                    if (deftype == "Shield"):
                        effect *= 2
                    elif (deftype == "Shoot"):
                        effect *= 0.5
                elif (atktype == "Arts"):
                    if (deftype == "Power"):
                        effect *= 2
                    elif (deftype == "Wit"):
                        effect *= 0.5
                elif (atktype == "Power"):
                    if (deftype == "Wit"):
                        effect *= 2
                    elif (deftype == "Arts"):
                        effect *= 0.5
                elif (atktype == "Wit"):
                    if (deftype == "Arts"):
                        effect *= 2
                    elif (deftype == "Power"):
                        effect *= 0.5
        return effect

    def effectivestring(effectiveness, atkelements, defelements):
        if (effectiveness == 1):
            return ""

        fullstring = ""
        atkelement = ""
        defelement = ""

        for i, element in enumerate(atkelements):
            atkelement += ("/" if i != 0 else "") + element

        for i, element in enumerate(defelements):
            defelement += ("/" if i != 0 else "") + element

        fullstring += atkelement + " style is "
        fullstring += ("resisted by " if effectiveness < 1 else "strong against ")
        fullstring += defelement + " style"
        fullstring += ("... " if effectiveness < 1 else "! ")

        return fullstring

    #ai is an int that is used to determine the ai's priority. None exists so far
    def prioritize(ai):
        #can I deploy
        for op in otherOps:#for every enemy operator
            for i, square in enumerate(battlefield):#for every square on the battlefield
                if (ownedfield[i] == False and op.getparameter(COST) + (8 - i) * 10 <= otherdp and square == None):#if you have enough dp to deploy there and the square is unoccupied
                    return ("deploy", op, i)#return "deploy", the enemy operator being deployed, and the cell they're being deployed to

        #can I use a tech
        for tech in actor.getparameter(TECHS):#for every tech of the active actor
            if (tech.getparameter(POINTS) >= tech.getparameter(COST)):#if that tech has enough points to use
                for i in reversed(range(actorpos - tech.getparameter(MAXRANGE), actorpos - tech.getparameter(MINRANGE) + 1)):#look at every cell within those points
                    op = battlefield[i]
                    if (op != None and op.getparameter(ALLY)):#if that cell isn't empty, and contains an ally
                        return ("tech", tech, [op])#return "tech", the tech being used, and the ally operator being targeted by the tech

        #can I use an attack
        for i in reversed(range(actorpos - actor.getparameter(MAXRANGE), actorpos - actor.getparameter(MINRANGE) + 1)):#look at every cell within the actor's range
            op = battlefield[i]
            if (op != None and op.getparameter(ALLY)):#if that cell isn't empty, and contains an ally
                return ("attack", [op])#return "attack" and the operator being targeted

        #can I move
        if (actor.getparameter(MOVEPOINTS) >= 1):
            for i in range(actorpos - int(math.floor(actor.getparameter(MOVEPOINTS))), actorpos):
                if (battlefield[i] == None):
                    return ("move", i)

        return ("pass")

    def orderstring(ind):
        if (ind == 0):
            return "Current"
        elif (ind == 1):
            return "Next"
        elif (ind == 2):
            return "3rd Up"
        else:
            return str(ind + 1) +"th Up"

    def gettechblurb(id):
        if (id == 0):#doubletapauto
            return "After two attacks, hit 1.4 times as hard, twice in one turn. Shoot style."
        elif (id == 1):#hammerdown
            return "After being hit twice, retaliate at 2.5 times your normal strength. Power style."
        elif (id == 2):#rocklaw
            return "A desperate, clumsy swipe that's slightly weaker than a regular attack, but drains a foe's blood, healing you by as much damage as you deal. Strike style."
        elif (id == 3):#coltellata
            return "A cutting stab that strikes twice, once while going in, and once while coming out. Wit style."
        elif (id == 4):#blazing wire stripper
            return "An incredibly powerful Arts blast. Hits yourself, and everyone around you, by 3.5 times your Arts power. Arts style."
        elif (id == 5):#wolf's fist
            return "A blindingly-fast flurry of ten punches, each hitting at 20% strength. Can shove a foe back. Strike style."
        elif (id == 6):#wolf's eye
            return "An Arts-infused charged shot that does 1.5 times your Arts power. Reduces the hit target's defense to zero for three turns. Shoot style."
        else:
            return "This shouldn't show up."

    def passtring(id):
        if (id == ACE):
            return "Discretion is the better part of valor. Let them come to me."
        elif (id == KROOS):
            return "Eh? Are we taking a nap on the battlefield? That might be a bit too much, even for me."
        elif (id == ROCKSICK):
            return "Grrahhh... Grrhh... Garrrr...?"
        elif (id == HEADHUNTER or id == SKULLHUNTER):
            return "I'm just getting warmed up, {i}cazzone.{/i}"
        elif (id == CHIAVE):
            return "Come on already! What's this \"standing around\" junk?"
        elif (id == GAMBINO):
            return "You want me to hang back? Grrr... there's nothin' that survives getting between me and the most direct route to my prey."
        elif (id == CAPONE):
            return "The key to winning a battle is patience. I see you know this."
        else:
            return "This shouldn't show up."

    def gettalentblurb(id):
        if (id == ACE):
            return "A sturdy and no-nonsense soldier with decades of experience, even if you don't remember it. Your combat training has taught you the importance of not losing ground; in battle, nothing on Terra can move you back even one step."
        elif (id == KROOS):
            return "A seemingly lazy and flippant young sniper whose skill is unparalleled... at avoiding work. Still, her desire to get back to bed as soon as possible means she prioritizes headshots, hitting for 160% damage 20% of the time."
        elif (id == ROCKSICK):
            return "A moaning, shambling figure. Its constant cries of pain are the only sign it's still alive. However, its unterran endurance works well in battle, regenerating 10% of its max health at the end of each of its turns."
        elif (id == HEADHUNTER):
            return "A ruthless, or perhaps just desperate, hunter armed with little but a knife and his wits. A keen opportunist, against foes with less than half health, all his attacks and skills will have double the amount of hits."
        elif (id == CHIAVE):
            return "A hotheaded youth that's known to throw himself out into battle with wild abandon. His powerful explosive arts clear the way for allies. Upon becoming incapacitated, he returns up to twice your current DP gain."
        elif (id == SKULLHUNTER):
            return "A ruthless hunter armed with a collection of throwing knives and his wits. A keen opportunist, against foes with less than half health, all his attacks and skills will have double the amount of hits. Can make ranged attacks at 80% power."
        elif (id == GAMBINO):
            return "A reckless mafia Don who charges into battle, gaining territory quickly. After incapacitating a foe, his momentum carries him one square forward."
        elif (id == CAPONE):
            return "A patient mafia Don who relies on coordinated strikes to bring down even the biggest foes. When attacking a foe that is being blocked by an ally, will hit at 150% of his normal power."
        else:
            return "This shouldn't show up."

    #height is an int in centimeters
    def scaleportrait(picture, height, flip=False):
        return Transform(picture, ysize=int(5.08 * height), fit="contain", xzoom=(-1 if flip else 1))

    def censor(who, what):
        if (not swearing):
            swearlist = ["shit", "fuck", "damn", "piss", "bastard", "bitch", "ass"]

            for swear in swearlist:
                censor = "*" * len(swear)
                what = what.replace(swear, censor).replace(swear.upper(), censor).replace(swear.title(), censor)

        renpy.say(who, what)

    def fibonacci(ind):
        if (ind == 0):
            return 0
        elif (ind < 3):
            return 1
        else:
            return fibonacci(ind-1) + fibonacci(ind-2)

    def statstring(stat):
        if (stat == ATK):
            return "attack"
        elif (stat == DEF):
            return "defense"
        elif (stat == ARTS):
            return "arts power"
        elif (stat == ARTSDEF):
            return "arts defense"
        elif (stat == MOV):
            return "movement"
        else:
            return "ERROR"

    def addxp(ops, amount):
        for op in ops:
            op.setparameter(EXPERIENCE, op.getparameter(EXPERIENCE) + amount)

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

    def bufftext(buff):
        stat = buff[1]
        amount = buff[2]
        multiplication = buff[3]

        bufftext = ""

        if (stat == ATK):
            bufftext += "ATK"
        elif (stat == DEF):
            bufftext += "DEF"
        elif (stat == ARTS):
            bufftext += "ARTS"
        elif (stat == ARTSDEF):
            bufftext += "ARTSDEF"
        elif (stat == MOV):
            bufftext += "MOV"
        elif (stat == MAXHEALTH):
            bufftext += "HEALTH"

        if (multiplication):
            bufftext += " x"
        elif (amount > 0):
            bufftext += " +"
        else:
            bufftext += " -"

        bufftext += str(amount)

        return bufftext
