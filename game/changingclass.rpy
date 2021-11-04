init python:
    #Implemented by classes Operator and Skill
    class ChangingClass:
        def setparameter(self, num, newvalue):
            self.parameters[num] = newvalue
            
        def setparameters(self, parameters):
            self.parameters = parameters
            
        def getparameter(self, num):
            return self.parameters[num]