import matplotlib.pyplot as plt

# FILE = "output.txt"
#
# EVENT_DICT_K1 = {}
# EVENT_DICT_K2 = {}
#
# with open(FILE, 'r') as file:
#     lines=file.readlines();
#
# for line in lines:
#     tab = line.split()
#     try:
#         if tab[0] == 't0':
#             print(tab)
#     except IndexError:
#         print('wrong')


tab = []
size = 10
for i in range(0,100):
    if len(tab) > 10:
        tab.pop(0)
    tab.append(i)

    print(tab)