import numpy as np
import matplotlib.pyplot as plt
data = np.load("C:\\Users\\charl\\Source\\Repos\\Omegalpha44\\TIPE_project\\resultat etude\\light_res_helmeted\\results\\injury_predictions.npy")

X = [i for i in range(0,101)]

plt.plot(X,data)
plt.title("nb blesse casque france non obligatoire")
plt.xlabel("pourcentage de port de casque de velo")
plt.ylabel("pourcentage de blesse")
plt.show()
