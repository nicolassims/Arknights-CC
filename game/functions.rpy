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
