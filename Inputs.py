print("Dime lo que sea...")
anything = input()
print("Hmm...", anything, "... ¿en serio?")

anything = input("Dime lo que sea...")
print("Hmm...", anything, "...¿en serio?")

anything = float(input("Ingresa un número: "))#convertir a float  o a int()
something = anything ** 2.0
print(anything, "a la potencia de 2 es", something)

#programa para calcular el largo de una hipotenusa
leg_a = float(input("Ingresa la longitud del primer cateto: "))
leg_b = float(input("Ingresa la longitud del segundo cateto: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("La longitud de la hipotenusa es:", hypo)
print("La longitud de la hipotenusa es " + str((leg_a**2 + leg_b**2) ** .5))# convertido el resultado a string


#imprime un cuadro
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")
