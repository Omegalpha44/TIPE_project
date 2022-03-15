#############################################
# ludwig prediction visualizer              #
#############################################

#############################################
# What to change :                          #
# - a = number of the experience            #
# - p = suffix of the dataset               #
# - pred-2 = what to change                 #
#############################################
import numpy as np
import os
import matplotlib.pyplot as plt

injury_default = ["head", "serious.head", "face", "fatal", "head"]
location_default = ["Australia", "Canada", "Finland", "France", "Germany", "Hong Kong", "Norway", "Singapore", "Sweden",
                    "UAE", "UK", "USA", "USA/Canada"]
mandatory_default = ["N", "Y", " "]
mandatory_category_default = ["all", "child", "N"]


def pred_2(ind, size, location, mandatory, car, helmeted):
    a = open("prediction_tableau/prediction" + ind + ".csv", "w")
    a.write("size,location,mandatory,car_2,helmeted," + "\n")
    v = ","
    for k in size:
        for l in location:
            for m in mandatory:
                for o in car:
                    for p in helmeted:
                        a.write(k + v + l + v + m + v + o + v + p + v + "\n")


def rg(a, b):
    return [str(i) for i in range(a, b + 1)]


def rgp(a, b, p):
    return [str(i) for i in range(a, b + 1, p)]


a = "_helmeted"
n = 7
pred_2(a, ["8000"], ["France"], ["N"], rg(0,200), ["50"])

os.system("cd C:\\Users\\charl\\Source\\Repos\\Omegalpha44\\TIPE_project\\Prediction_tableau")
os.system(
    "ludwig predict --output_directory C:\\Users\\charl\\Source\\Repos\\Omegalpha44\\TIPE_project\\Prediction_tableau\\results --model C:\\Users\\charl\\Source\\Repos\\Omegalpha44\\TIPE_project\\results\\experiment_run_" + str(
        n) + "\\model --dataset C:\\Users\\charl\\Source\\Repos\\Omegalpha44\\TIPE_project\\Prediction_tableau\\prediction" + a + '.csv')

data = np.load(
    "C:\\Users\\charl\\Source\\Repos\\Omegalpha44\\TIPE_project\\Prediction_tableau\\results\\injury_predictions.npy")

X = [i for i in range(len(data))]

plt.title("pourcentage de blessé en fonction du pourcentage de voiture par personne")
plt.xlabel("pourcentage de voiture par personne")

plt.ylabel("pourcentage de blessé")
plt.plot(X, data)
plt.show()
