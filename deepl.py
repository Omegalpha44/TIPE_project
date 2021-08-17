import os
from numpy.lib.nanfunctions import nancumsum
import tensorflow as tf
from icecream import ic
import numpy
from tensorflow.python.keras import activations
from tensorflow.python.keras.engine import input_layer
import pandas

# Présentation du modèle : on prend en entrée un vecteur à 5 dimensions, chacune représentant une information nécessaire pour résoudre le problème
#ensuite, on le fait passer dans la suite de neurone (10 neurones pour l'instant)
#enfin, on demande le trie pour savoir cb de

model = tf.keras.Sequential(
    [
    tf.keras.layers.Dense(100), # 5 en entrée, dans notre tenseur. Cf .csv pour se référer aux différentes caractéristiques
    tf.keras.layers.Dense(60,activation='relu'), # la couche du milieu
    tf.keras.layers.Dense(30,activation="relu"),
    tf.keras.layers.Dense(5,activation="relu")
    ])
column_names = ["début d'étude" , "fin d'étude" , "nombre de véhicule" , "pays" , "loi" , "population" , "accidenté" , "portait un casque" , "tête" , "nuque" , "visage"]

data_train = pandas.read_csv("valeur.csv",names = column_names)
data_features = data_train.copy()
label_names = column_names[6:]
data_labels = pandas.read_csv("label.csv",names = label_names)
ic( data_features)
ic( data_labels)
data_features = numpy.array(data_features)
data_labels = numpy.array(data_labels)

data_features = numpy.asarray(data_features).astype(numpy.float32)

data_labels = numpy.asarray(data_labels).astype(numpy.float32)



model.compile(loss=tf.losses.MeanSquaredError(),
                optimizer=tf.optimizers.Adam())

model.fit(data_features,data_labels,epochs=1000)