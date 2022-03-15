
import numpy as np
def pred():
    a = open("prediction_tableau//prediction.csv",'w')
    a.write("size,location,mandatory,car,helmeted,"+"\n")
    injury = ["head","serious.head","face","fatal","head"]
    location = ["Australia","Canada","Finland","France","Germany","Hong Kong","Norway","Singapore","Sweden","UAE","UK","USA","USA/Canada"]
    mandatory = ["N","Y"," "]
    mandatory_category = ["all","child","N"]
    o = "all"
    v = ","
    z = 0
    for k in range(1000,10000,1000):
         for l in location:
               for m in mandatory:
                     for p in np.arange(0,10000,1000):
                            for q in np.arange(0,100,5):
                                a.write(str(k)+v+l+v+m+v+str(p)+v+str(q)+v+"\n")
                                print(z)
                                z+=1
    a.close()
pred()