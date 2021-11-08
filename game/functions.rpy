init python:
    def battlefieldPoints(pos):
        if (pos == 4):
            return 5
        elif (pos == 1 or pos == 2 or pos == 6 or pos == 7):
            return 1
        else:
            return 3

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
            return "ERROR"

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

    def passtring(id):
        if (id == ACE):
            return "A wasted turn. I need to avoid those."
        elif (id == KROOS):
            return "Eh? Are we taking a nap on the battlefield? That might be a bit too much, even for me."
        else:
            return "ERROR"

    #ai is an int that is used to determine the ai's priority. None exists so far
    def prioritize(ai):
        #can I deploy
        for op in otherOps:#for every enemy operator
            for i, square in enumerate(battlefield):#for every square on the battlefield
                if (op.getparameter(COST) + (8 - i) * 10 <= otherdp and square == None):#if you have enough dp to deploy there and the square is unoccupied
                    return ("deploy", op, i)#return "deploy", the enemy operator being deployed, and the cell they're being deployed to

        print("can't deploy")

        #can I use a tech
        for tech in actor.getparameter(TECHS):#for every tech of the active actor
            if (tech.getparameter(POINTS) >= tech.getparameter(COST)):#if that tech has enough points to use
                for i in reversed(range(actorpos - tech.getparameter(MAXRANGE), actorpos - tech.getparameter(MINRANGE) + 1)):#look at every cell within those points
                    op = battlefield[i]
                    if (op != None and op.getparameter(ALLY)):#if that cell isn't empty, and contains an ally
                        return ("tech", tech, [op])#return "tech", the tech being used, and the ally operator being targeted by the tech

        print("can't use tech")

        #can I use an attack
        for i in reversed(range(actorpos - actor.getparameter(MAXRANGE), actorpos - actor.getparameter(MINRANGE) + 1)):#look at every cell within the actor's range
            op = battlefield[i]
            if (op != None and op.getparameter(ALLY)):#if that cell isn't empty, and contains an ally
                return ("attack", [op])#return "attack" and the operator being targeted

        print("can't use attack")

        #can I move
        if (actor.getparameter(MOVEPOINTS) >= 1):
            for i in range(actorpos - int(math.floor(actor.getparameter(MOVEPOINTS))), actorpos):
                if (battlefield[i] == None):
                    return ("move", i)

        print("can't use move, passing")

        return ("pass")
