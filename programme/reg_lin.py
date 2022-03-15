import pandas as pd
import numpy as np
import tensorflow as tf
import tensorflow.keras as ker
import tensorboard
import datetime

# On charge le dataset que l'on souhaite utiliser
df = pd.read_csv("informations/res6(comprehension)(ex)(csv).csv")


# alorithme usant de pandas permettant de convertir des valeurs str en valeurs int suivant l'usage d'un dictionnaire
def categorize(column):
    """permet de catégoriser les valeurs d'une même colonne étant des strings en des valeurs numériques"""
    D = {}
    L = []
    j = 0
    for i in range(len(column)):
        if column[i] in D.keys():
            L.append(D[column[i]])
        else:
            D[column[i]] = j
            L.append(j)
            j += 1
    return L, D


# on catégorise les deux colonnes représentant des catégories
df["mandatory"], D1 = categorize(df['mandatory'])
df["location"], D2 = categorize(df["location"])

"""
Indice de dictionnaire pour analyse des résultats finaux :
{'N': 0, 'Y': 1}
{'USA': 0, 'Australia': 1, 'UK': 2, 'USA/Canada': 3, 'Canada': 4, 'Norway': 5, 'Singapore': 6, 'UAE': 7, 'Hong Kong': 8, 'Finland': 9, 'France': 10, 'Germany': 11, 'Sweden': 12}
"""

# création de l'algorithme de machine learning reposant sur les modules numpy, tensorflow et tensorboard
column_name = ["location", "mandatory", "helmeted", "car_2"]
target = df.pop('injury')  # la colonne des valeurs que l'on souhaite trouver
column_features = df[column_name]
column_features.head()
tf.convert_to_tensor(column_features)
normalizer = ker.layers.Normalization(axis=1)
normalizer.adapt(column_features)
print(df)

def get_basic_model():
    model = tf.keras.Sequential([
#        normalizer, #Cause des problèmes liés au fait que mes données ne sont pas assez diversifié en permier lieu.
        tf.keras.layers.Dense(94,activation='tanh'),
        tf.keras.layers.Dense(32,activation="relu"),
        tf.keras.layers.Dense(16,activation='relu'),
        tf.keras.layers.Dense(1)
    ])
    model.compile(optimizer='Adam',
                loss=tf.keras.losses.MeanAbsoluteError(),
                metrics = ['mse'])
    return model


log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
model_dir = "logs/models/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

model = get_basic_model()
model.fit(column_features, target, epochs=2000, batch_size=25, callbacks=[tensorboard_callback])
model.save(model_dir)