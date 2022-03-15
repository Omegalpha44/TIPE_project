from numpy.lib.npyio import BagObj
import pandas

class Utilitaire(object):
    '''les programmes dont l'utilisation ne sert qu'� la mise en forme'''
    def ptov(file) :
        a = open(file,"r")
        b = open("informations/res.csv",'w')
        c= 0
        for e in a:
            b.write(e.replace(';',','))
            c+=1
        a.close()
        b.close()

Utilitaire.ptov("informations/resultat_etude.csv")
column_name = ["auteur","year","type de blessure analysée","taille de l'étude", "pas de casque blessé", "casque blessé","pas de casque non blessé","casque non blessé","loc","setting","colletion des informations","obligatoire", "type d'obligation", "âge", "pourcentage de masculin", "tête", "face", "neck"]
dataset = pandas.read_csv("informations/res.csv",names=column_name)
data_features = dataset.copy()

def popper(l):
    c=0
    x=[0,9,10,15,16,17]
    for e in l:
        if x.count(c) !=0:
            data_features.pop(e)
        c+=1

popper(column_name)

A = data_features.pop("casque blessé")
B = data_features.pop("pas de casque blessé")
D = A.pop(0)
E =B.pop(0)
print(A)
print(D)
A = A.astype(int)
B=B.astype(int)
#A.loc[-1] = [D]
#B.loc[-1] = [E]
#A.index = A.index + 1
#B.index = B.index + 1
#A.sort_index(inplace = True)
#B.sort_index(inplace = True)
data_label = A + B #On prend le total de personne blessé lors des expériences.
print(data_label)
C = pandas.concat([data_features,data_label],axis=1)
print(C)
C.to_csv("informations/res2.csv")


#comment transformer la base de donnée pour qu'elle soit utilisable par la machine : on fait tourner 
# successivement les différents bouts de code se trouvant dans ce fichier en particulier.