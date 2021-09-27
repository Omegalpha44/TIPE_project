import tensorflow as tf
import tensorboard
import pandas

#définition du dataset
class Utilitaire(object):
    '''les programmes dont l'utilisation ne sert qu'à la mise en forme'''
    def ptov(file) :
        a = open(file,"r")
        b = open("informations/res.csv",'w')
        for e in a:
            b.write(e.replace(';',','))
        a.close()
        b.close()

    def string_to_num(file):
        a = open(file)
        b = open ("informations/res2.csv",'w')
        L = []
        c = 0
        for e in a :
            

dataset = pandas.read_csv("informations/res.csv")

dataset.replace()
