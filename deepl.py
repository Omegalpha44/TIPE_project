import tensorflow as tf
from icecream import ic
import numpy
from tensorflow.python.keras import activations
from tensorflow.python.keras.engine import input_layer

# Présentation du modèle : on prend en entrée un vecteur à 5 dimensions, chacune représentant une information nécessaire pour résoudre le problème
#ensuite, on le fait passer dans la suite de neurone (10 neurones pour l'instant)
#enfin, on demande le trie pour savoir cb de

model = tf.keras.Sequential([
    tf.keras.layers.InputLayer(5), # 5 en entrée, dans notre tenseur : le pays, la pop totale, le nb d'accidenté au total, si présence de véhicule et la loi
    tf.keras.layers.Dense(10,activation='relu'),
    tf.keras.layers.Dense(5,activation="relu") # homme (femme obtenu par calcul), cycliste touché, tête, visage, neck
]
)


