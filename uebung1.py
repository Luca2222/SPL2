zahl1 = input("1.te Zahl eingeben")
zahl2 = input("2.te Zahl eingeben")
zahl3 = input("3.te Zahl eingeben")

if(zahl1 < zahl2 < zahl3):
    print(zahl1,zahl2,zahl3)

if(zahl2 < zahl3 < zahl1):
    print(zahl2,zahl3,zahl1)

if(zahl3 < zahl2 < zahl1):
    print(zahl3,zahl2,zahl1)

if(zahl1 < zahl3 < zahl2):
    print(zahl1,zahl3,zahl2)

if(zahl2 < zahl1 < zahl3):
    print(zahl2,zahl1,zahl3)

if(zahl3 < zahl1 < zahl2):
    print(zahl3,zahl1,zahl2)