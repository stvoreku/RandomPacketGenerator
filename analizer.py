import matplotlib.pyplot as plt


SIZES = {}

TAG_I1 = "1.0"
TAG_I2 = "2.0"

SENT_DICT = {}
SENT_DICT[TAG_I1] = {}
SENT_DICT[TAG_I2] = {}

LOST_DICT = {}
LOST_DICT[TAG_I1] = {}
LOST_DICT[TAG_I2] = {}

SIZES[TAG_I1] = 3
SIZES[TAG_I2] = 4

ALL_BYTES = {}
ALL_BYTES[TAG_I1] = 0
ALL_BYTES[TAG_I2] = 0

ALL_LOST = {}
ALL_LOST[TAG_I1] = 0
ALL_LOST[TAG_I2] = 0

with open("output.txt", "r") as file:
    for line in file.readlines():
        line_split = line.split()
        try:
            if line_split[0] != 'obecny':
                print("pass")
            elif len(line_split) > 5:
                t = int(line_split[3])
                i = 0
                cmd = ""
                current_tag = ""
                packet_num = ""
                for word in line_split:
                    print(cmd, packet_num, current_tag)
                    i+=1
                    if word in ["Obsluzono","Rozpoczecie","Odrzucono"]:
                        cmd = word
                    if word == "i:":
                        current_tag = line_split[i]
                    elif word == "j:":
                        packet_num = line_split[i]
                    if cmd != "" and current_tag != "" and packet_num != "":
                        if cmd == "Obsluzono":
                            for tag in SENT_DICT.keys():
                                if current_tag == tag:
                                    ALL_BYTES[tag] = float(packet_num) * SIZES[tag]
                                    SENT_DICT[tag][t] = float(packet_num) * SIZES[tag]  / (ALL_BYTES[TAG_I2] + ALL_BYTES[TAG_I1])
                        elif cmd == "Odrzucono":
                            for tag in LOST_DICT.keys():
                                print("LOSS")
                                print(tag)
                                if current_tag == tag:
                                    LOST_DICT[tag][t] = (ALL_LOST[tag] + 1)
                                    ALL_LOST[tag] = LOST_DICT[tag][t]

                        cmd = ""
                        current_tag = ""
                        packet_num = ""

            else:
                print("Nothing to parse")
        except:
            print("Bad parse")


print(SENT_DICT)
print(LOST_DICT)
lists = sorted(SENT_DICT[TAG_I1].items()) # sorted by key, return a list of tuples
x1, y1 = zip(*lists) # unpack a list of pairs into two tuples

lists = sorted(SENT_DICT[TAG_I2].items()) # sorted by key, return a list of tuples
x2, y2 = zip(*lists) # unpack a list of pairs into two tuples

plt.plot(x2, y2)
plt.plot(x1, y1)
plt.show()

lists = sorted(LOST_DICT[TAG_I1].items()) # sorted by key, return a list of tuples
x3, y3 = zip(*lists) # unpack a list of pairs into two tuples
plt.plot(x3, y3)
plt.show()