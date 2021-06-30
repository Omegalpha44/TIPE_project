import pygad
import numpy
from tensorflow.python.ops.gen_array_ops import where
from source import principal as pr
from source import psychologie as ps
from icecream import ic
import matplotlib.pyplot as plt

def gen1():
    '''Etude ml des résultats de l'étude faite dans le Rhône entre 1998 et 2008'''
    couple = []
    asso = []
    #Etude 1 : provenance de France, donc on pose loi à 0 (casque non obligatoire) 

    pr.loi = 0
    pr.risk = 1 #la population étudié est la population de cycliste s'étant blessé en faisant du vélo

    #1.on définit le ground truth

    function_input = 8373
    desired_output = [1471,529] 

    #2. on définit la fonction fitness

    def fitness_func(solution,solution_idx):
        pr.head = solution[0]
        pr.sportif = solution[1]
        pr.neck = solution[2]
        ps.aging = solution[3]
        ps.commoner = solution[4]
        ps.sport = solution[5]
        ps.helmet_risk_reducing = solution[6]
        res = pr.mass_simulation_moyennée(function_input)
        output = [res[0],res[4]]
        ic(output)
        couple.append(output)
        fitness1 = 1/numpy.abs(output[0] - desired_output[0])
        fitness2 = 1/numpy.abs(output[1] - desired_output[1])
        fitness = (abs(fitness1) + abs(fitness2))/2
        ic(fitness)
        asso.append([fitness,solution])
        return fitness
    fitness_function = fitness_func

    # paramètre de l'algorithme génétique

    num_generations = 50

    num_parents_mating = 4

    sol_per_pop = 20
    num_genes = 7

    init_range_low = 0
    init_range_high = 1 # age en pourcentage, on considère que au dela de 100 ans la personne ne fait plus de vélo

    parent_selection_type = "sss"
    keep_parents = 4
    gene_space = numpy.arange(0,1,0.00001)
    crossover_type = "single_point"

    mutation_type = "random"
    mutation_percent_genes = 20

    #création de l'instance

    ga_instance = pygad.GA(num_generations=num_generations,
                            num_parents_mating=num_parents_mating,
                            fitness_func=fitness_function,
                            sol_per_pop=sol_per_pop,
                            num_genes=num_genes,
                            init_range_low=init_range_low,
                            init_range_high=init_range_high,
                            parent_selection_type=parent_selection_type,
                            keep_parents=keep_parents,
                            crossover_type=crossover_type,
                            mutation_type=mutation_type,
                            mutation_percent_genes=mutation_percent_genes,
                            gene_space=gene_space)


    ga_instance.run()

    #affichage des résultats

    solution, solution_fitness, solution_idx = ga_instance.best_solution()
    print("Parameters of the best solution : {solution}".format(solution=solution))
    print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
    pr.head = solution[0]
    pr.sportif = solution[1]
    pr.neck = solution[2]
    ps.aging = solution[3]
    ps.commoner = solution[4]
    ps.sport = solution[5]
    res = pr.mass_simulation_moyennée(function_input)
    output = [res[0],res[4]]
    prediction = output
    print("Predicted output based on the best solution : {prediction}".format(prediction=prediction))

    #recherche de la fit la plus élevé sur l'intégralité du parcours et non pas uniquement sur la dernière époque


    def mx():
        max = [0,[]]
        c = 0
        for elem in asso:
            if max[0]<= elem[0]:
                max = elem
        c = asso.index(max)
        asso.pop(c)
        ic(couple[c])
        couple.pop(c)
        ic(max)
    mx()
    mx()
    mx()
    mx()
    mx()
    X=[i for i in range(0,len(couple))]
    Y=[asso[i][0] for i in range(0,len(couple))]
    plt.plot(X,Y)
    plt.show()
    #résultat : 
    # [0.23082 0.2418  0.05785 0.30925 0.238   0.30175 0.89066] fit = inf
    # [0.35392 0.00703 0.05203 0.15667 0.21758 0.88732 0.49523] fit = 0.50
    # [0.38125 0.549   0.05497 0.75923 0.69725 0.06841 0.58737] fit = 0.055
    # [0.13751 0.31678 0.05947 0.38065 0.07699 0.15622 0.28947] fit = 0.500
    # [0.19888 0.963   0.0419  0.52166 0.39168 0.98445 0.4281 ] fit = 0.509
gen1()
