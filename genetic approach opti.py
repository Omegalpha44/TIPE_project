#Not working for now ; error with the type of entry for the program. Need investigating.

from datetime import date
from source import principal as pr
from source import psychologie as ps
import numpy
import matplotlib.pyplot as plt
import tensorflow.keras as ker
from icecream import ic
import pygad.kerasga as py
import pygad
input_layer = ker.layers.InputLayer(1)
dense_layers1 = ker.layers.Dense(14,activation = 'softmax')
output_layer = ker.layers.Dense(1,activation="linear")

model = ker.Sequential()
model.add(input_layer)
model.add(dense_layers1)
model.add(output_layer)

couple = []
asso = []

data_inputs = numpy.array([[6423.0],
[1940.0],
[8373.0]])
data_outputs = numpy.array([[1463.0],
[257.0],
[1671.0]])

def fitness_func(solution,solution_idx):
    global data_inputs,data_outputs,keras_ga,model
    predictions = py.predict(model = model, solution = solution, data = data_inputs)
    mae = ker.losses.mean_absolute_error(data_outputs,predictions)
    abs_error = mae.numpy() + 0.0000001
    solution_fitness = 1.0/abs_error
    return solution_fitness
    

def callback_generation(ga_instance):
    print("Generation = {generation}".format(generation=ga_instance.generations_completed))
    print("Fitness    = {fitness}".format(fitness=ga_instance.best_solution()[1]))

keras_ga = py.KerasGA(model=model,
                     num_solutions=10)

num_generations = 250 # Number of generations.
num_parents_mating = 2 # Number of solutions to be selected as parents in the mating pool.
initial_population = keras_ga.population_weights # Initial population of network weights
gene_space = numpy.arange(0,1,0.00001)
ga_instance = pygad.GA(num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       initial_population=initial_population,
                       fitness_func=fitness_func,
                       on_generation=callback_generation,
                       gene_space=gene_space)

ga_instance.run()

ga_instance.plot_fitness(title="PyGAD & Keras - Iteration vs. Fitness", linewidth=4)
