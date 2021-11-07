init python:
    def battlefieldPoints(pos):
        if (pos == 4):
            return 5
        elif (pos == 1 or pos == 2 or pos == 6 or pos == 7):
            return 1
        else:
            return 3
