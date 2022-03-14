class environment:
    def __init__(self):
        self.lum = 0

    def modify_lum(self,pLum):
        self.lum += pLum

              
    def set_lum(self,pLum):
        self.lum = pLum

    def get_lum(self):
        return self.lum

    def __str__(self):
        status = 'la luz ambiental es: ' + str(self.lum)+ '%'
        return status