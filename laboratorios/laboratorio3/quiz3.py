x= input("> ")
agua = 0
fuego = 0

while x != 'salir':

    if x.find("agua") >= 0 :
         agua=agua+1


    elif x.find("fuego") >= 0:
        fuego = fuego +1

    x = input("> ")

print("agua = " + str(agua) + "\n" + "fuego = " + str(fuego) )

