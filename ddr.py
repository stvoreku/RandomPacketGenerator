import matplotlib.pyplot as plt



with open("input_gen.txt", "r") as file:
    out = file.readlines()
    kolejka_1 = out[1].split()
    kolejka_2 = out[2].split()

print(len(kolejka_2))

bufor_1 = []
bufor_2 = []
b1 = 4
b2 = 4
Q1 = 0
Q2 = 0
Q1delta = 0.2
Q2delta = 0.8
Q1sent = {}
Q2sent = {}
allsent_Q1 = 0
allsent_Q2 = 0
sending = 0
for num in range(0, 500):
    print("TIME: {} Q1: {:.2f} Q2: {:.2f} sending: {} B1: {} B2: {}".format(num, Q1, Q2, sending, len(bufor_1), len(bufor_2)))
    try:
        if kolejka_1[num] == '1':
            bufor_1.append(b1)
    except IndexError:
        pass
    try:
        if kolejka_2[num] == '1':
            bufor_2.append(b2)
    except IndexError:
        pass
    if len(bufor_1) != 0:
        Q1 += Q1delta
        if Q1 > bufor_1[0]:
            if sending == 0:
                sending = bufor_1[0]
                bufor_1.pop(0)
                Q1 = 0
                allsent_Q1 += 1
                Q1sent[num] = allsent_Q1 / (allsent_Q1 + allsent_Q2)
                print(allsent_Q1 / (allsent_Q1 + allsent_Q2))

    if len(bufor_2) != 0:
        Q2 += Q2delta
        if Q2 > bufor_2[0]:
            if sending == 0:
                sending = bufor_2[0]
                bufor_2.pop(0)
                Q2 = 0
                allsent_Q2 += 1
                Q2sent[num] = allsent_Q2 / (allsent_Q1 + allsent_Q2)
                print(allsent_Q2 / (allsent_Q1 + allsent_Q2))
    if sending > 0:
        sending-=2


print(Q1sent, Q2sent)

lists = sorted(Q1sent.items()) # sorted by key, return a list of tuples
x1, y1 = zip(*lists) # unpack a list of pairs into two tuples
lists = sorted(Q2sent.items()) # sorted by key, return a list of tuples
x2, y2 = zip(*lists) # unpack a list of pairs into two tuples
plt.plot(x2, y2)
plt.plot(x1, y1)
plt.show()