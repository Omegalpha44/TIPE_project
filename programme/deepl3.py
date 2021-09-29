import tensorflow as tf
import tensorboard
import pandas
from icecream import ic 
#définition du dataset
class Utilitaire(object):
    '''les programmes dont l'utilisation ne sert qu'� la mise en forme'''
    def ptov(file) :
        a = open(file,"r")
        b = open("informations/res.csv",'w')
        c= 0
        for e in a:
            if c >0:
                b.write(e.replace(';',','))
            c+=1
        a.close()
        b.close()

    def l_to_s(l) :
        '''Retourne une string en se basant sur une liste'''
        res = ''
        for e in l:
            res = res + str(e)
        return res


    # def string_to_num(file):
    #     a = open(file)
    #     b = open ("informations/res2.csv",'w')
    #     L = []
    #     c = 0
    #     buffer  = []
    #     buffer2 = ""
    #     bool = True
    #     for e in a : # pour chaque ligne
    #         buffer = ""
    #         buffer2 = ""
    #         for x in e : # pour chaque element dans la ligne
    #             if type(x) == str :
    #                 buffer = buffer + x
    #             else:
    #                 if L.count(buffer) != 0 :
    def no_more_string(x):
        global l
        global c
        l = []
        c = 0
        for e in x :
            print(type(e))
            print(e)
            if isinstance(e,str) and l.count(x) !=0:
                l.append(e)
                c+=1
                return c
            elif isinstance(e,str) :
                l.append(x)
                return l.index(e)



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
data_label = A + B
print(data_label)

data_label = tf.convert_to_tensor(data_label, dtype=tf.float32)

data_features.apply(Utilitaire.no_more_string)
print(data_features)


model = tf.keras.Sequential([
    tf.keras.layers.Dense(24),
    tf.keras.layers.Dense(12),
    tf.keras.layers.Dense(6),
    tf.keras.layers.Dense(1)
])