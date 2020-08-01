# Mensagens para datas

f = open("conversas.txt", "r", encoding="utf8")

dates = open("dates.txt", "w")

for line in f:
    date = line[0:8]
    if date.find('/') != -1:
        print(date)
        dates.write(date +'\n')

dates.close()

# Datas únicas

f = open("dates.txt", "r")
n = open("d.txt", "w")

last = f.readline()

for line in f:
    print(line)
    if "(" in line or "h" in line or "[" in line:
        continue
    else:
        if(line != last):
            n.write(line)
            last = line
    last = line

n.close()

# Alg Final

import datetime

dates = open("d.txt", "r")


vet = dates.readline().replace("\n", "").split('/')
print("a" + dates.readline())
lastDate = datetime.date(int(vet[2]), int(vet[1]), int(vet[0]))
nextDate = ""
auxDate = ""

maxDays = 1
dateMax = ""

for line in dates:
    maxDays +=1
    print("\n")
    print(line.replace("\n", ""))
    vet = line.replace("\n", "").split("/")
    nextDate = datetime.date(int(vet[2]), int(vet[1]), int(vet[0]))
    print(str(abs(nextDate - lastDate))[0])
    lastDate = nextDate

print(maxDays)