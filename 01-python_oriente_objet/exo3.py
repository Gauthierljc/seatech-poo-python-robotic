from abc import ABC, abstractmethod
from ast import Return


class weapons():
    "an usefull tool in everyday life =)"
    def tirer(self):
        print("une balle est tirée")
    def recharger(self):
        print("votre arme est chargée")
    def netoyer(self):
        print("votre arme est propre")    
    print("vous avez choisis de vivre librement")
    
class SelectAmmunition(ABC):
    
    @abstractmethod
    def Ammochoice (self):
        pass

class Uses(ABC):

    @abstractmethod
    def utility(self):
        pass


class LongRange(weapons):
    def tirer(self):
        print("une balle de gros calibre est tirée")
    

class ShortRange(weapons):
    def tirer(self):
        print("une balle  de petit calibre est tirée")
    

class Midlerange(weapons):
    def tirer(self):
        print("une balle standart est tirée")
   
    

class ForHuman(weapons,Uses):

    def utility(self):
        print("votre arme est efficasse contre les bipeds")
    

class ForMaterial(weapons,Uses):

    def utility(self):
        print("votre arme est efficasse contre les vehicules/batiments")
    

class ForHomeSecurity(weapons,Uses):

    def utility(self):
        print("votre arme vous sera tres utile pour abatre le biped qui s'aventure sur votre territoir")
    


class guns(ShortRange,ForHuman,ForHomeSecurity,SelectAmmunition,Uses):
    def utility(self):
        print("an carriable wepon for short range fight or homesecurity")
    def Ammochoice (self):
        print("munition 9mm choisis")

class AssaultRifles(Midlerange,ForHomeSecurity,ForHuman,SelectAmmunition,Uses):
    
    def utility(self):
        print("an good polyvalent weapon wich can permite to do urban or forest fight but also used for homesecurity")
    def Ammochoice (self):
        print("munition 5.56mm choisis")

class Shotguns(ShortRange,ForHuman,ForHomeSecurity,SelectAmmunition,Uses):

    def utility(self):
        print("an good wepon verry efficient for short and urban fight")
    def Ammochoice (self):
        print("munition 12.cal choisis")

class Machineguns(Midlerange,ForHuman,SelectAmmunition,Uses):
    
    def utility(self):
        print("used in very specific case, use a lot of munition for covering or reposting fire")
    def Ammochoice (self):
        print("munition 308. choisis")

class PMs(ShortRange,ForHuman,ForHomeSecurity,SelectAmmunition,Uses):
    
    def utility(self):
        print("used for urban fight and homesecurity")
    def Ammochoice (self):
        print("munition 9mm choisis")

class DMR(Midlerange,LongRange,ForHuman,SelectAmmunition,Uses):
    
    def utility(self):
        print("used for covering, reposting or precision shot but also for long or midle range fight (including forest fight)")
    def Ammochoice (self):
        print("munition 308. choisis")

class PrecisionRifles(LongRange,ForHuman,SelectAmmunition,Uses):
    
    def utility(self):
        print("used for long range fight and precision shot (but more eficiantly than the DMR")
    def Ammochoice (self):
        print("munition 12.7mm choisis")

class GrenadeLauncher(Midlerange,ForHuman,ForMaterial,SelectAmmunition,Uses):
    
    def utility(self):
        print("used to blow up material or human at mid or short range")
    def Ammochoice (self):
        print("munition 40mm choisis")

class RocketLauncher(Midlerange,LongRange,ForMaterial,SelectAmmunition,Uses):
    
    def utility(self):
        print("used to destroy vehicles at mid or long range more efficiently than grenadelaucher")
    def Ammochoice (self):
        print("munition rocket choisis")

def retour(self):
    return self

rl=RocketLauncher()
