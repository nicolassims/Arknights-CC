init python:
    def battlefieldPoints(pos):
        if (pos == 1 or pos == 7):
            return 1
        elif (pos == 3 or pos == 6):
            return 5
        elif (pos == 4):
            return 7
        else:
            return 3
