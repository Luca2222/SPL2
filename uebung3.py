import random#
zahlen = []
anzahlWuerfe = input("Wie oft soll gewürfelt werden?")
anzahlWuerfe = int(anzahlWuerfe)

for i in range (0,anzahlWuerfe):
  wurf = random.randint(1,6)
  zahlen.append(wurf)
  # print(wurf, end="..")

print ()
print ("Ergebnis: ")
#print (zahlen)

for z in range(1,7):
    print (z,"er :", zahlen.count(z))


