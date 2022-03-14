class environment:
    def __init__(self):
        self.lum = 0

    def modify_lum(self,pMod):
        if pMod == 1:
            self.lum =+ 10
        elif pMod ==-1:
            self.lum =+ -10
              
    def set_lum(self,pLum):
        self.lum = pLum

    def get_lum(self):
        return self.lum