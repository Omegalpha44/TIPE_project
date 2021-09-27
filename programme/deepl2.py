import tensorflow as tf
from icecream import ic
import pandas
import tensorboard
import os

os.environ['CUDA_VISIBLE_DEVICES'] = '-1' #défini si on utilise le CPU ou le GPU, ici le CPU pour une plus grande vitesse de calcul brute

class Utilitaire(object):
    def ptov(file) :
        a = open(file,"r")
        b = open("informations/valeur_inter.csv",'w')
        for e in a:
            b.write(e.replace(';',','))
        a.close()
        b.close()

Utilitaire.ptov("informations/valeur2.csv")

column_names = ["début d'étude" , "fin d'étude" , "nombre de véhicule" , "pays" , "loi" , "population" , "accidenté"]
data_train = pandas.read_csv("informations/valeur_inter.csv",names = column_names)
data_features = data_train.copy()
data_labels = data_features.pop("accidenté")
ic(data_features)
data_features = tf.convert_to_tensor(data_features, dtype= tf.float32)
data_labels = tf.convert_to_tensor(data_labels, dtype=tf.float32)
model = tf.keras.Sequential([
    tf.keras.layers.Dense(24),
    tf.keras.layers.Dense(12),
    tf.keras.layers.Dense(6),
    tf.keras.layers.Dense(1)
])
model.compile(loss = tf.keras.losses.MeanSquaredError(),
optimizer=tf.optimizers.Adam())
log_dir = "logs/fit/"
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)
model.fit(data_features,data_labels,epochs=10000, callbacks=[tensorboard_callback])

