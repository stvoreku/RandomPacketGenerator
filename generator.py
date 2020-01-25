import numpy as np
# import matplotlib.pyplot as plt
LAMBDA = 4
PAC_NUM_1 = 100
PAC_NUM_2 = 200

k1 = np.random.poisson(LAMBDA, PAC_NUM_1)
k2 = np.random.poisson(LAMBDA, PAC_NUM_1)
# plt.hist(k1)
# plt.show()

with open("input_gen.txt", "w") as file:
    file.write("{} {}\n".format(PAC_NUM_1, PAC_NUM_2))
    for num in k1:
        for a in range(0,num):
            file.write('0 ')
        file.write("1 ")
    file.write("\n")
    for num in k2:
        for a in range(0,num):
            file.write('0 ')
        file.write("1 ")
    file.write("\n")
print("generating done. mediana k1: {} mediana k2: {}".format(k1.mean(), k2.mean()))

