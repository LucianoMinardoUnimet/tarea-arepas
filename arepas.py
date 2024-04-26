#calcular la masa de las arepas que quieras hacer :D
print("Introduzca la cantidad en gramos que va a usar de cada ingrediente")
#inputs para las cantidades
harina = round(float(input("introduzca los gramos de harina: ")), 2)
agua = round(float(input("introduzca los ml de agua: ")), 2)
aceite = round(float(input("introduzca los ml de aceite: ")), 2)
sal = round(float(input("introduzca los gramos de sal: ")), 2)
#imprimir las cantidades y la masa final
cantidades = ["cantidad de harina: {}g".format(harina), "cantidad de agua: {}ml".format(agua), 
              "cantidad de aceite: {}ml".format(aceite), "cantidad de sal: {}g".format(sal)]
masaFinal = round(float(harina + agua + aceite + sal), 2)
print("Las cantidades que usted coloco son: ", cantidades)
print("La masa final de su arepa es: ", masaFinal)

