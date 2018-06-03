import os

list = os.listdir()
i = -1
nume = input()
for every in list:
    i += 1
    os.rename(every, str(nume) + " " + str(i))