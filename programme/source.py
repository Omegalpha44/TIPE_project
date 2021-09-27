#Source program, used for the main aspect.

#Etape 1 : Définition des poids que l'on va utiliser pour résoudre le problème
import random as rand
import numpy as np
from icecream import ic
from numpy.ma.extras import average
#complexité totale: O(n) (on parcourt la liste des individus, et on les teste tous individuellement)
class psychologie(object):
    helmet_risk_reducing = 0.70 # ne fonctionne que pour les dégâts envers la tête et le visage
    behaving_risk_augmenting = 1.20 
    behave_mod = 0.80
    aging=0.2
    law = 9
    sport = 0.86
    commoner = 0.07

    def comportement(age,port): #on définit la nature de la personne en fonction de son âge. On définit différentes natures : raisonnable, ou dangereux, en se basant sur l'étude montrant que porter un casque entraîne un risque lié à la prise de risque
        if rand.randrange(0,100,1)/100 <psychologie.behave_mod and age>=psychologie.aging and port == psychologie.helmet_risk_reducing: # on pose un pourcentage arbitraire de 80 %  de personnes ne présentant pas le caractère dangereux avec un casque au vu de l'absence d'info plus précis
            return psychologie.behaving_risk_augmenting # comportement dangereux
        else:
            return 1 # comportement normal

    def is_wearing_an_helmet(mandatory,sportif): # si la personne porte un casque ou pas
        if mandatory :
            if rand.randint(0,10) <=psychologie.law:
                return psychologie.helmet_risk_reducing
            else:
                return 0
        elif sportif:
            if rand.randrange(0,100,1)/100<=psychologie.sport:
                return psychologie.helmet_risk_reducing
            else:
                return 0
        else:
            if rand.randrange(0,100,1)/100<=psychologie.commoner:
                return psychologie.helmet_risk_reducing
            else:
                return 0  
                      
class principal(object):
    risk = 0.45
    head = 0.169
    arm = 0.475
    legs = 0.326
    face = 0.233
    sportif = 0.45
    neck = 0.233
    loi = 1
    def mass_simulation(n): # on prend comme argument la population de personnes à tester pour vérifier si la simulation est cohérente.
        individual_list = []
        def individu():
            age = rand.randint(18,60) #on définit l'âge de la personne comme le risque augmente en fonction de l'âge
            casque=0
            if principal.loi ==1 and rand.randrange(0,100,1)/100<=principal.sportif :
                casque = psychologie.is_wearing_an_helmet(True,True)
            elif principal.loi ==1:
                casque = psychologie.is_wearing_an_helmet(True,False)

            if rand.randrange(0,100,1)/100<=principal.sportif and principal.loi == 0:
                casque = psychologie.is_wearing_an_helmet(False,True)
            elif principal.loi == 0:
                casque = psychologie.is_wearing_an_helmet(False,False)
            comp = psychologie.comportement(age,casque)
            return [comp,casque]
        result = [0,0,0,0,0] # empl : 0 = la tête ; 1 = les bras ; 2 = les jambes ; 3 = le visage : 4 = la nuque
        for i in range(0,n):
            individual_list.append(individu()) # on créé autant d'individu que de personne dans la liste
        for j in range(0,n): # Pour chaque individu, on lui fait passer les tests d'accidents
            if (rand.randrange(0,100)/100) <=principal.risk*individual_list[j][0]: # si 
                if (rand.randrange(0,100)/100)<=principal.head*individual_list[j][0]:
                    result[0]+=1
                if (rand.randrange(0,100)/100)<=principal.face*individual_list[j][0]:
                    result[3]+=1
                if (rand.randrange(0,100)/100)<=principal.neck*individual_list[j][0]:
                    result[4]+=1
                if (rand.randrange(0,100)/100)<=principal.arm:
                    result[1]+=1
                if (rand.randrange(0,100)/100)<=principal.legs:
                    result[2]+=1
        return result
    def mass_simulation_moyennée(n):
        '''version moyennée 10 fois de mass_simulation, permettant d'avoir des résultats plus précis'''
        res = []
        sum = [0,0,0,0,0]
        for i in range(10):
            res.append(principal.mass_simulation(n))
        (res)
        for i in range(5):
            for j in range(10):
                sum[i]+=res[j][i]/10
                (sum)
        return sum  
#14 paramètres à faire varier pour résoudre le problème
