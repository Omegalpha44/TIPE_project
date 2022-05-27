import time
import tkinter as tk
from tkinter import ttk
import threading as th
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.figure as fg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tensorflow as tf
import datetime
import tensorflow.keras as ker
"""
Programme d'interface pour les mesures et les vérifications des informations reçus par les programmes
"""


class App(object): # Classe de l'interface
    def __init__(self):
        self.root = tk.Tk() # Création de la fenêtre principale
        self.root.title("pour visualiser le modèle") # Titre de la fenêtre
        self.counter = 0 # Compteur pour les figures
        self.can = tk.Canvas(self.root,width=500,height=400) # Création d'un canvas
        self.entry = ttk.Entry(self.root) # Création d'une zone de texte
        self.can.create_text(250,100,text="Plotting tool", justify='center',font='Cascada 26 bold') # Création d'un texte
        self.can.create_window(250,200,window=self.entry,width=400) # Création d'une zone de texte
        self.button = ttk.Button(self.root,command=self.update,text='plot') # Création d'un bouton
        self.can.create_window(250, 300, window=self.button) # Création d'un bouton dans le canvas
        self.can.create_text(250,350,text="vert = lois, jaune = pays, rouge = casques, bleu = voitures",justify='center') # Création d'un texte
        self.can.pack() # Affichage du canvas
        self.root.mainloop() # Boucle infinie

    def update(self): # Fonction qui permet de mettre à jour le canvas
        a = "_helmeted"
        rep = self.entry.get() # Récupération de la valeur de la zone de texte
        top = tk.Toplevel(self.root) # Création d'une fenêtre secondaire
        top.title(rep) # Titre de la fenêtre secondaire
        b = fg.Figure((5, 5), dpi=100) # Création d'une figure
        d2 = {'USA': 0, 'Australia': 1, 'UK': 2, 'USA/Canada': 3, 'Canada': 4, 'Norway': 5, 'Singapore': 6, 'UAE': 7,
              'Hong Kong': 8, 'Finland': 9, 'France': 10, 'Germany': 11, 'Sweden': 12} # Dictionnaire pour les pays
        d2_reverse = {k: i for i, k in d2.items()} # Dictionnaire inverse pour les pays
        countries = [d2_reverse[i] for i in range(13)] # Liste des pays

        def rg(a, b): # Fonction qui permet de créer une liste de valeurs numériques
            return [str(i) for i in range(a, b + 1)]

        def rgp(a, b, p): # Fonction qui permet de créer une liste de valeurs numériques
            return [str(i) for i in range(a, b + 1, p)]

        plot1 = b.add_subplot(111) # Création d'un sous-plot
        Y = self.tester(a, ["France"], ['N', 'Y'], ['50'], ['50'],rep)
        plot1.plot(Y,'g') # Trace du graphique
        plot1.plot(self.tester(a, countries, ["N"], ["50"], ["50"],rep),"y")
        plot1.plot(self.tester(a, ['France'], ["N"], rg(0, 100), ["50"],rep),'r')
        plot1.plot(self.tester(a, ['France'], ["N"], ["50"], rg(0, 100),rep),'b')
        canvas = FigureCanvasTkAgg(b, top)
        self.counter += 1
        canvas.draw()
        canvas.get_tk_widget().pack()

    def tester(self,ind, location, mandatory, helmeted, car, rep): # Fonction qui permet de tester les données
        model = tf.keras.models.load_model(rep)
        def pred_2(ind, size, location, mandatory, car, helmeted): # Fonction qui permet de prédire les casques
            a = open("prediction_tableau/prediction" + ind + ".csv", "w")
            a.write("size,location,mandatory,helmeted,car_2," + "\n")
            v = ","
            for k in size:
                for l in location:
                    for m in mandatory:
                        for o in car:
                            for p in helmeted:
                                a.write(k + v + l + v + m + v + p + v + o + v + "\n")

        def rg(a, b):
            return [str(i) for i in range(a, b + 1)]

        def rgp(a, b, p):
            return [str(i) for i in range(a, b + 1, p)]

        # pred_2(a, ["100"],['France'], ["N"], ["50"], rg(0,100))
        pred_2(ind, ['100'], location, mandatory, car, helmeted)

        df = pd.read_csv("Prediction_tableau/prediction_helmeted.csv")
        df.drop(df.columns[len(df.columns) - 1], axis=1, inplace=True)
        df.drop(df.columns[0], axis=1, inplace=True)
        X = []

        def categorize(column, k):
            """permet de catégoriser les valeurs d'une même colonne étant des strings en des valeurs numériques"""
            D1 = {'N': 0, 'Y': 1}
            D2 = {'USA': 0, 'Australia': 1, 'UK': 2, 'USA/Canada': 3, 'Canada': 4, 'Norway': 5, 'Singapore': 6,
                  'UAE': 7,
                  'Hong Kong': 8, 'Finland': 9, 'France': 10, 'Germany': 11, 'Sweden': 12}
            L = []
            j = 0
            if k == 0:
                D = D1
            else:
                D = D2
            for i in range(len(column)):
                L.append(D[column[i]])
            return L

        df["mandatory"] = categorize(df['mandatory'], 0)
        df["location"] = categorize(df["location"], 1)
        columns_titles = ["location", "mandatory", "helmeted", "car_2"]
        df = df.reindex(columns=columns_titles)
        print(df)
        tf.convert_to_tensor(df)
        Y = model.predict(df)
        Y = Y[:, 0]
        # if len(Y) == 13:
        #    X = [D2_reverse[i] for i in range(len(Y))]
        # else:
        X = [i for i in range(len(Y))]
        return Y


class Training(object):
    def __init__(self):
        self.fen = tk.Tk()
        self.can = tk.Canvas(self.fen,width=500,height=400)
        self.entry = ttk.Entry(self.fen)
        self.can.create_window(250,150,window=self.entry)
        self.can.create_text(250,120,text='choose a number of epochs', font='calibri 24')
        self.button = ttk.Button(self.fen,command=self.train,text='train')
        self.can.create_window(250,200,window=self.button)
        self.can.pack()
        x = th.Thread(target=App, args=())

        x.start()
        self.fen.mainloop()

    def train(self):
        ep = self.entry.get()
        self.can.pack()
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
                tf.keras.layers.Dense(94, activation='relu'),
                tf.keras.layers.Dense(32, activation="relu"),
                tf.keras.layers.Dense(16, activation='relu'),
                tf.keras.layers.Dense(1)
            ])
            model.compile(optimizer='Adam',
                          loss=tf.keras.losses.MeanAbsoluteError(),
                          metrics=['mse'])
            return model

        log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        model_dir = "logs/models/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)
        model = get_basic_model()
        model.fit(column_features, target, epochs=int(ep), batch_size=25, callbacks=[tensorboard_callback])
        model.save(model_dir)


y = th.Thread(target=Training, args=())
y.start()
