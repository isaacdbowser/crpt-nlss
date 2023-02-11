import numpy as np
import time

def shanks(g, h, mod):
    g = g % mod # in case g is not given as 0 <= g < mod

    # calculate order of g
    test = g
    order = 1
    while test != 1:
        test = (test * g) % mod
        order +=1

    n = int(np.floor(np.sqrt(order)) + 1)

    list1 = [1]
    list2 = [h]
    for i in range(n):
        list1.append((list1[i] * g) % mod)
        list2.append((list2[i] * pow(g**n, -1, mod) % mod))


    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                break
        else:
            continue
        break

    x = i + j*n

    return x
def brute(g, h, mod):
    test = g % mod
    count = 1
    while test % mod != h:
        test = (test * g) % mod
        count += 1
    return count


g = 13919
h = 219382
mod = 15485863


beg = time.time()
xs = shanks(g, h, mod)
end = time.time()
s_time = end-beg
print(f'SHANKS: log is {xs}, time to run {s_time:.5f}')

beg = time.time()
xb = brute(g, h, mod)
end = time.time()
b_time = end-beg
print(f'BRUTE: log is {xb}, time to run {b_time:.5f}')