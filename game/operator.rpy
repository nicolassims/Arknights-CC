init python:
    import math
    
    #ID,firstname,lastname,codename,health,atk,def,arts,artsdef,mov,cost,class,subclass,element,minrange,maxrange,talent,portraits,ally
    class Operator(ChangingClass):
        def __init__(self, id, level, ally):
            self.parameters = []
            id -= 1
            for x in range(PORTRAITS + 1):
                print(x)
                if (HEALTH <= x <= ARTSDEF):
                    self.parameters.append(math.ceil(opdex[id][x] * (10 + level)))
                elif (x == PORTRAITS):
                    newarray = []
                    for y in opdex[id][x]:
                        newarray.append("chars/" + y)
                    self.parameters.append(newarray)
                else:
                    self.parameters.append(opdex[id][x])
            self.parameters.append(ally)# set ALLY

    #define specific Operators here.
    aceop = Operator(ACE, 1, True)
    enemyaceop = Operator(ACE, 1, False)