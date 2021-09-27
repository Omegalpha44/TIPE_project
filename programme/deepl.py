import os
import tensorflow as tf
from icecream import ic
import numpy
import pandas

# Présentation du modèle : on prend en entrée un vecteur à 5 dimensions, chacune représentant une information nécessaire pour résoudre le problème
#ensuite, on le fait passer dans la suite de neurone (10 neurones pour l'instant)
#enfin, on demande le trie pour savoir cb de

#le dataset
column_names = ["début d'étude" , "fin d'étude" , "nombre de véhicule" , "pays" , "loi" , "population" , "accidenté"]
data_train = pandas.read_csv("valeur.csv",names = column_names)
data_features = data_train.copy()
data_labels = data_features.pop("accidenté")

#traitage des informations non numérique : 
inputs = {}
for name,column in data_features.items():
    dtype = column.dtype
    if dtype == object :
        dtype = tf.string
    else :
        dtype = tf.float32

    inputs[name] = tf.keras.Input(shape=(1,),name=name,dtype=dtype)

numeric_inputs = {name:input for name,input in inputs.items()
                  if input.dtype == tf.float32}
x = tf.keras.layers.Concatenate()(list(numeric_inputs.values()))
norm = tf.keras.layers.experimental.preprocessing.Normalization()
norm.adapt(numpy.array(data_train[numeric_inputs.keys()])) # erreur provenant uniquement de intellisense : le programme tourne très bien malgré l'avertissement.
all_numeric_inputs = norm(x)
ic(all_numeric_inputs)

preprocessed_inputs = [all_numeric_inputs]

for name, input in inputs.items():
    if input.dtype == tf.float32:
        continue
    lookup = preprocessing.StringLookup(vocabulary=numpy.unique(data_features[name]))
    one_hot = preprocessing.CategoryEncoding(max_tokens=lookup.vocab_size())
    x = lookup(input)
    x = one_hot(x)
    preprocessed_inputs.append(x)
    
preprocessed_inputs_cat = tf.keras.layers.Concatenate()(preprocessed_inputs)
data_preprocessing = tf.keras.Model(inputs,preprocessed_inputs_cat)
#tf.keras.utils.plot_model(model = data_preprocessing, rankdir='LR', dpi=72, show_shapes=True)

data_features_dict = {name:numpy.array(value)
                      for name,value in data_features.items()}

#on définie le modèle

def data_model(preprocessing_head, inputs):
    body = tf.keras.Sequential([
        tf.keras.layers.Dense(64),
        tf.keras.layers.Dense(1)
        ])
    preprocessed_inputs = preprocessing_head(inputs)
    result = body(preprocessed_inputs)
    model = tf.keras.Model(inputs,result)
    model.compile(loss=tf.losses.MeanSquaredError(),
                optimizer=tf.optimizers.Adam())
    return model
model = data_model( data_preprocessing, inputs)
model.fit(x = data_features_dict,y=  data_labels, batch_size=256, epochs = 20000)

#hey


