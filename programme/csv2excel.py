def excel2csv(file):
    a = open(file + ".csv", "r")
    b = open(file + "(csv).csv", 'w')
    c = open("informations/alt.csv", 'w')
    for e in a:
        c.write(e.replace(',', '.'))
    c.close()
    d = open("informations/alt.csv", 'r')
    for e in d:
        b.write(e.replace(';', ','))
    a.close()
    b.close()
    d.close()


def csv2excel(file):
    a = open(file + ".csv", "r")
    b = open(file + "(ex).csv", 'w')
    c = open("informations/alt.csv", 'w')
    for e in a:
        c.write(e.replace(',', ';'))
    c.close()
    d = open("informations/alt.csv", 'r')
    for e in d:
        b.write(e.replace('.', ','))
    a.close()
    b.close()
    d.close()

excel2csv("informations/res6(comprehension)(ex)")
