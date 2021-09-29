from icecream  import ic

l = ['a','b','c','d']
def l_to_s(l) :
    res = ''
    for e in l:
        res = res + str(e)
    return res

ic(l_to_s(l))
ic("abcd")