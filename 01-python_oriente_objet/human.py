import time

class Human():   
    # Human class content here
    __name = '<unnamed>'
    __faim =0
    __fatigue = 99
    __sexe='<none>'
    __etat='vivant'

    def __init__(self,name,sexe):
        self.__name=name
        self.__sexe=sexe

    def nom(self):
        return self.__name
        pass

    def nouurrir (self,nourriture):
        for i in range (round(nourriture/10)):
            if self.__fatigue <100:
                self.__fatigue+=1
            elif self.__etat=='vivant':
                self.__mort("fatigue")
            if self.__faim>2:
                self.__faim-=2
            else:
                self.faim=0
            time.sleep(1)

    def dormir(self,temps):
        if temps >0 and temps<11 :
            for i in range (temps):
                if self.__fatigue>10:
                    self.__fatigue-=10
                else:
                    self.__fatigue= 0
                if self.__faim <100:
                    self.__faim+=2
                elif self.__etat=='vivant':
                    self.__mort('faim')


    def __mort(self,__cause):
        self.__etat='mort'
        print("%s est mort de %s"%(self.nom(),__cause) )



    
    
    pass


bannane= 10
steak= 30
chocolat= 20



humain1=Human('Bob','homme')
humain1.nouurrir(steak)
