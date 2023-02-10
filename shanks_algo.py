import numpy as np

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

x = shanks(97010, 13896, 17389)
print(x)
