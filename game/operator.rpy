init 2 python:
    import math

    #ID,firstname,lastname,codename,health,atk,def,arts,artsdef,mov,cost,class,subclass,element,minrange,maxrange,talent,portraits,usesArts,ally,techs,level,movepoints
    class Operator(ChangingClass):
        def __init__(self, id, level, ally):
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
            self.parameters[HEALTH] *= 5# increase health by proper amount
            self.parameters[ATK] = math.ceil(self.parameters[ATK] * 2.5)# increase dmg by proper amount
            self.parameters[ARTS] = math.ceil(self.parameters[ARTS] * 2.5)# increase dmg by proper amount
            self.parameters.append(ally)# set ALLY
            self.parameters.append([])# set TECHS
            self.parameters.append(level)# set LEVEL
            self.parameters.append(0)# set MOVEPOINTS

    #define specific Operators here.
    aceop = Operator(ACE, 1, True)
    aceop.setparameter(TECHS, [ hammerdown ])

    kroosop = Operator(KROOS, 2, True)
    kroosop.setparameter(TECHS, [ doubletapauto ])

    enemyaceop = Operator(ACE, 1, False)
    enemyaceop.setparameter(TECHS, [ hammerdown ])

    enemykroosop = Operator(KROOS, 2, False)
    enemykroosop.setparameter(TECHS, [ doubletapauto ])
