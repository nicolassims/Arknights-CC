init 2 python:
    import math

    #ID,firstname,lastname,codename,health,atk,def,arts,artsdef,mov,cost,class,subclass,element,minrange,maxrange,talent,portraits,usesArts,ally,techs,level,movepoints,experience, maxhealth
    class Operator(ChangingClass):
        def __init__(self, id, level, ally, techs=[]):
            self.parameters = []
            id -= 1
            for x in range(USESARTS + 1):
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
            self.parameters.append(techs)# set TECHS
            self.parameters.append(level)# set LEVEL
            self.parameters[HEALTH] *= 5 #set health properly
            self.parameters.append(0)# set MOVEPOINTS
            self.parameters.append(0)# set EXPERIENCE
            self.parameters.append(self.parameters[HEALTH])#set MAXHEALTH

    #define specific Operators here.
    aceop = Operator(ACE, 1, True, [ hammerdown ])

    rocksickop = Operator(ROCKSICK, 1, False, [ rocklaw ])
