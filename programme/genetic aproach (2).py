#main program

import pygad # le module permettant la programmation génétique
import numpy # calcul des matrices et tenseurs
from source import principal as pr # le programme que l'on veut obtimiser avec le ML
from source import psychologie as ps # une autre partie de ce programme, se basant sur l'aspect psychologique
from icecream import ic # pour afficher les valeurs, debugging
import matplotlib.pyplot as plt # afficher la courbe de la fitness le long de l'entraînement

def gen1():
    '''Etude ml des résultats de l'étude faite dans le Rhône entre 1998 et 2008'''
    couple = []
    asso = []
    #Etude 1 : provenance de France, donc on pose loi à 0 (casque non obligatoire) 

    pr.loi = 0
    pr.risk = 1 #la population étudié est la population de cycliste s'étant blessé en faisant du vélo

    #1.on définit le ground truth

    function_input = 8373 # nombre de cyclistes blessés dans le rhône entre 1998 et 2008
    desired_output = [0] #on vise 0 blessé

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
        output = [sum(res)/4]
        ic(output)
        couple.append(output)
        fitness1 = 1/numpy.abs(output[0] - desired_output[0])
        fitness = abs(fitness1)
        ic(fitness)
        asso.append([fitness,solution])
        return fitness
    fitness_function = fitness_func

    # paramètre de l'algorithme génétique

    num_generations = 50 # nombre de générations

    num_parents_mating = 4 # nombre de parents qui se mènent à la reproduction

    sol_per_pop = 20 # nombre de solutions par population
    num_genes = 7 # nombre de paramètres

    init_range_low = 0 # valeur minimale de chaque paramètre
    init_range_high = 1 # age en pourcentage, on considère que au dela de 100 ans la personne ne fait plus de vélo

    parent_selection_type = "sss" # type de sélection des parents
    keep_parents = 4 # nombre de parents conservés
    gene_space = numpy.arange(0,1,0.00001) # espace des paramètres
    crossover_type = "single_point" # type de croisement

    mutation_type = "random" # type de mutation
    mutation_percent_genes = 20 # pourcentage de mutation des paramètres

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


    ga_instance.run() # lancement de l'algorithme

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


    def mx():  # la fonction qui va chercher la fitness la plus élevée
        '''Récupération des 5 valeurs ayant obtenues la plus haute fitness dans l'ensemble des générations'''
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
# [2250.925] soit 2250,925/8373*100 = 22,5% de la population blessée
# ic| max: [0.00044426180348079117,
#           array([0.0145 , 0.06186, 0.00328, 0.83399, 0.00558, 0.69183, 0.79491])]
# 70% de port de casque, qui réduit de 80% le risque de blessure
gen1()
