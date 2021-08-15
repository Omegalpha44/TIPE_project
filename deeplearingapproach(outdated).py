import tensorflow as tf
from icecream import ic
import numpy
from tensorflow.python.keras import activations

data_inputs = numpy.array([[6423.0],
[1940.0],
[8373.0]])
data_outputs = numpy.array([[1463.0],
[257.0],
[1671.0]])
data_inputs = tf.convert_to_tensor(data_inputs)
data_outputs = tf.convert_to_tensor(data_outputs)

model = tf.keras.Sequential([
    tf.keras.layers.InputLayer(1),
    tf.keras.layers.Dense(14,activation='relu'),
    tf.keras.layers.Dense(7,activation = 'relu'),
    tf.keras.layers.Dense(2000,activation = 'softmax')
])


prediction = model(data_inputs).numpy()

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy()

model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])

model.fit(data_inputs,data_outputs, epochs=50, use_multiprocessing=True)
model.evaluate(data_inputs, verbose=2,use_multiprocessing=True,)
