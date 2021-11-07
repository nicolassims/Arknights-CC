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
