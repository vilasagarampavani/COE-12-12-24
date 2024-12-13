Basic = int(input('Ehter the salary:'))
if Basic  < 10000:
     HRA = (67 *Basic)/100
     DA = (67 *Basic)/100
elif Basic > 10000 and Basic <20000 :
     HRA = (69*Basic)/100
     DA = (76*Basic)/100
elif Basic > 20000:
     HRA = (73*Basic)/100
     DA = (89*Basic)/100
print(HRA)
print(DA)
GS = HRA +  DA + Basic
print(GS)