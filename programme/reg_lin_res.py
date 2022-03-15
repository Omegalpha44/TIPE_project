import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
"""
liste de bon modèle :
'logs/models/20220111-172351'

"""


model = tf.keras.models.load_model('logs/models/20220301-171910')

#injury_default = ["head", "serious.head", "face", "fatal", "head"]
#location_default = ["Australia", "Canada", "Finland", "France", "Germany", "Hong Kong", "Norway", "Singapore", "Sweden",
#                    "UAE", "UK", "USA", "USA/Canada"]
#mandatory_default = ["N", "Y", " "]
#mandatory_category_default = ["all", "child", "N"]
D2 = {'USA': 0, 'Australia': 1, 'UK': 2, 'USA/Canada': 3, 'Canada': 4, 'Norway': 5, 'Singapore': 6, 'UAE': 7,
          'Hong Kong': 8, 'Finland': 9, 'France': 10, 'Germany': 11, 'Sweden': 12}
D2_reverse = {k: i for i, k in D2.items()}
countries = [D2_reverse[i] for i in range(13)]
a = "_helmeted"


def rg(a, b):
    return [str(i) for i in range(a, b + 1)]


def rgp(a, b, p):
    return [str(i) for i in range(a, b + 1, p)]


def tester(ind, location, mandatory, helmeted, car):

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



    # pred_2(a, ["100"],['France'], ["N"], ["50"], rg(0,100))
    pred_2(ind, ['100'], location, mandatory, car, helmeted)
    df = pd.read_csv("Prediction_tableau/prediction_helmeted.csv")
    df.drop(df.columns[len(df.columns) - 1], axis=1, inplace=True)
    df.drop(df.columns[0], axis=1, inplace=True)
    X = []

    def categorize(column, k):
        """permet de catégoriser les valeurs d'une même colonne étant des strings en des valeurs numériques"""
        D1 = {'N': 0, 'Y': 1}
        D2 = {'USA': 0, 'Australia': 1, 'UK': 2, 'USA/Canada': 3, 'Canada': 4, 'Norway': 5, 'Singapore': 6, 'UAE': 7,
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
    #if len(Y) == 13:
    #    X = [D2_reverse[i] for i in range(len(Y))]
    #else:
    X = [i for i in range(len(Y))]
    plt.plot(X, Y)


tester(a,["France"], ['N','Y'],['50'],['50']) # bleu
tester(a, countries, ["N"], ["50"], ["50"]) # orange
tester(a, ['France'], ["N"], rg(0,100), ["50"]) # vert
tester(a, ['France'], ["N"], ["50"], rg(0,100)) # rouge
plt.title("multianalyse")
plt.ylabel("nb de blessé")
plt.show()
