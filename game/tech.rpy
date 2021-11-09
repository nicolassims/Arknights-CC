init 1 python:
    import math

    #ID,name,damage,hits,aoe,dmgtype,dmgto,gaintype,start,gainper,cost,icon,charges,element,minrange,maxrange,effect,effectPower1,effectPower2,effectPower3,points
    class Tech(ChangingClass):
        def __init__(self, id):
            id -= 1
            self.parameters = []
            for x in range(EFFECTPOWER3 + 1):
                if (x != ICON):
                    self.parameters.append(techdex[id][x])
                else:
                    self.parameters.append("ui/techicons/" + techdex[id][x])
            self.parameters.append(techdex[id][START])# add points as basic starting value

    #define specific Techs here.
    doubletapauto = Tech(1)
    hammerdown = Tech(2)
    rocklaw = Tech(3)
