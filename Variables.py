PalabrasClavesPython = ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

var = "3.8.5"
account_balance = 1000.0
client_name = 'John Doe'
print("Python version: " + var)

a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c) # para concatenar varialbe string con entero es con la ,

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")


x = 0
x = float(x) # aquí se debe de incluir de manera explicita. Nota como se cambia el tipo de dato para asegurarnos de que x es del tipo float.
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

a = 6
b = 3
a /= 2 * b
print(a)