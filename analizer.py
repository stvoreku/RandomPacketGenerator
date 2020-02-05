import matplotlib.pyplot as plt

FILE = "l13_1500B_VC.txt"

SIZES = {}

TAG_I1 = "1.0"
TAG_I2 = "2.0"

LICZ_PUSTE = True

SENT_DICT = {}
SENT_DICT[TAG_I1] = {}
SENT_DICT[TAG_I2] = {}

LOST_DICT = {}
LOST_DICT[TAG_I1] = {}
LOST_DICT[TAG_I2] = {}

SIZES[TAG_I1] = 1500
SIZES[TAG_I2] = 1500

ALL_BYTES = {}
ALL_BYTES[TAG_I1] = 0
ALL_BYTES[TAG_I2] = 0

ALL_LOST = {}
ALL_LOST[TAG_I1] = 0
ALL_LOST[TAG_I2] = 0

LAST_SEND = {}
LAST_SEND[TAG_I1] = 0
LAST_SEND[TAG_I2] = 0

LAST_PACKETS = [] #to bedzie lista z jakiej kolejki jest ostatnie 10 pakietów
WINDOW_SIZE = 10 #ile ostatnich pakietow jest liczonych
with open(FILE, "r") as file:
    for line in file.readlines():
        line_split = line.split()
        try:
            if line_split[0] != 't0:':
                print("pass")
            elif len(line_split) > 3:
                t = int(line_split[1])
                i = 0
                cmd = ""
                current_tag = ""
                packet_num = ""
                for word in line_split:
                    #print(cmd, packet_num, current_tag)
                    i+=1
                    if word in ["Obsluzono","Rozpoczecie","Odrzucono"]:
                        cmd = word
                        print(t, cmd)
                    if word == "i:":
                        current_tag = line_split[i]
                    elif word == "j:":
                        packet_num = line_split[i]
                    if cmd != "" and current_tag != "" and packet_num != "":
                        if cmd == "Obsluzono":
                            if len(LAST_PACKETS) == WINDOW_SIZE:
                                LAST_PACKETS.pop(0)
                            for tag in SENT_DICT.keys():
                                if current_tag == tag:
                                    ALL_BYTES[tag] = float(packet_num) * SIZES[tag]
                                    LAST_SEND[tag] += SIZES[tag]
                                    LAST_PACKETS.append(tag)
                                    #print(LAST_PACKETS)                                      #LAST_SEND daje nam surowe dane ile wyslano. Obecny dzielnik zlicza stosunek pakietów do wszystkich
                                    SENT_DICT[tag][t] = LAST_PACKETS.count(tag) / WINDOW_SIZE #LAST_SEND[tag]
                        elif cmd == "Odrzucono":
                            for tag in LOST_DICT.keys():
                                print("LOSS")
                                print(tag)
                                if current_tag == tag:
                                    LOST_DICT[tag][t] = (ALL_LOST[tag] + 1)
                                    ALL_LOST[tag] = LOST_DICT[tag][t]
                        elif LICZ_PUSTE:
                            LAST_PACKETS.pop(0)
                            LAST_PACKETS.append('NONE')

                        cmd = ""
                        current_tag = ""
                        packet_num = ""

            else:
                pass
        except:
            print("Bad parse")


#print(SENT_DICT)
#print(LOST_DICT)
try:
    lists = sorted(SENT_DICT[TAG_I1].items()) # sorted by key, return a list of tuples
    x1, y1 = zip(*lists) # unpack a list of pairs into two tuples
except:
    pass
try:
    lists = sorted(SENT_DICT[TAG_I2].items()) # sorted by key, return a list of tuples
    x2, y2 = zip(*lists) # unpack a list of pairs into two tuples
except:
    pass

try:
    lists = sorted(LOST_DICT[TAG_I1].items()) # sorted by key, return a list of tuples
    x3, y3 = zip(*lists) # unpack a list of pairs into two tuples
except:
    pass


fig = plt.figure()
ax1 = fig.add_subplot()
ax1.set_ylabel('Dane')
ax1.set_xlabel("Czas")
ax1.set_title('Ilość wysłanych Danych')
try:
    ax1.plot(x1, y1, color='tab:blue', label='Zrodlo 1')
    ax1.plot(x2, y2, color='tab:orange', label='Zrodlo 2')
    leg = plt.legend()
except:
    pass


fig2 = plt.figure()
ax1 = fig2.add_subplot()
ax1.set_ylabel('Utracone Pakiety')
ax1.set_xlabel("Czas")
ax1.set_title('Ilość utraconych Pakietów')
try:
    ax1.plot(x3, y3, color='tab:red', label = 'stracone pakiety z Zrodla 2')
    leg = plt.legend()
except:
    pass

plt.show()