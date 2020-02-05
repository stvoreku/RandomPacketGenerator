import numpy as np
import matplotlib.pyplot as plt

LAMBDA = 13
PAC_NUM_1 = 100000
PAC_NUM_2 = 100000

k1 = np.random.poisson(LAMBDA, PAC_NUM_1)
k2 = np.random.poisson(LAMBDA, PAC_NUM_2)
plt.hist(k1)
plt.show()
plt.hist(k2)
plt.show()

with open("input_gen.txt", "w") as file:
    file.write("{} {}\n".format(PAC_NUM_1 + k1.sum(), PAC_NUM_2 + k2.sum()))
    for num in k1:
        for a in range(0, num):
            file.write('0 ')
        file.write("1 ")
    file.write("\n")
    for num in k2:
        for a in range(0,num):
            file.write('0 ')
        file.write("1 ")
    file.write("\n")
print("generating done. mediana k1: {} mediana k2: {}".format(k1.mean(), k2.mean()))

