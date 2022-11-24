""" name = input("Introduce your name")
print("Hello %s" %(name))

height = int(input("Introduce height value"))
width = int(input("Introduce width value"))

perimeter = 2*height + 2*width
area = height*width

print(perimeter, area) """

""" import math

a = int(input("Catet A:"))
b = int(input("Catet B:"))

hipotenuse = math.sqrt(a**2 + b**2)

print(hipotenuse) """

""" val1 = int(input("Introduce first value: "))
val2 = int(input("Introduce second value: "))

sumOfValues = val1 + val2
subtractValues = val1 - val2
multiplyValues = val1 * val2
divideValues = val1 / val2

print("Sum: %d" %(sumOfValues))
print("Substract: %d" %(subtractValues))
print("Multiply: %d" %(multiplyValues))
print("Divide: %d" %(divideValues)) """

""" celsius = int(input("Introduce your temperature in celcius: "))

farenheit = celsius*1.8+ 32

print("Your temperature in Farenheit is: %d" %(farenheit)) """

farenheit = int(input("Introduce your temperature in farenheit: "))

celsius = (farenheit-32)*5/9

print("Your temperature in Celsius is: %d" %(celsius))