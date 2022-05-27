import threading
import threading as th
import time
import asyncio as sync


def sleep_sort(liste):
    res = []

    def f(x):
        time.sleep(x / 10)
        res.append(x)

    for i in liste:
        threading.Thread(target=f, args=(i,)).start()
    while threading.active_count() > 1:
        pass
    return res

