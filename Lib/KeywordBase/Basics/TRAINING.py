from Lib.KeywordBase.Config.Constants import *

class TRAINING():
    def __init__(self, **kwargs):
        self.constants = 540
        super().__init__(**kwargs)

    def MAXIMIZE(self, var1, var2):
        if var1 > self.constants:
            return var1
        elif var2 > self.constants:
            return  var2
        else:
            return var1, var2

#TRAINING = TRAINING()