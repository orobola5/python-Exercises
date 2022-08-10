firstName = "mustapha"
surname = "maruf"
print("hello" + firstName, surname)
print("what do you call a bear with no teeth?\n A gummy bear")


def addition(x, y):
    add = x + y
    return add


print(addition(20, 30))

number1 = int(input("enter first number"))
number2 = int(input("enter number"))
number3 = int(input("enter the last number"))
total = number1 + number2
var = total * number3
print(var)


def refactor():
    x = int(input("enter the number"))
    y = int(input("enter another number"))
    z = int(input("enter another number"))
    add = x + y
    multiply = add * z
    return multiply


print("the answer is",refactor())

slices = int(input("how many slices of pizza the user started with?\n"))
EatenSlice = int(input("How many slices have they eaten"))
slicesLeft = slices - EatenSlice
print(f"we have {slicesLeft} slices of pizza left")

name = str(input("hello my friend can i know  your name\n"))
age = int(input("how old are you?"))
newAge = age + 1
print(f"{name}  next birthday you will be  {newAge}")

Total = int(input("whats the total price of the bill\n"))
diners = int(input("how many diners there are"))
paymentForEach = diners / Total
print("each person must pay", paymentForEach)

days = int(input("enter the numbers of day :"))
hour = days * 24
minutes = hour * 60
seconds = minutes * 60
print("in", days, "days there are...")
print(hour, "hours")
print(seconds, "seconds")

kilo = int(input("enter a weight in kilograms"))
pounds = kilo * 2.204
print("there are ", pounds, "pounds in ", kilo, "kilogram")

larger = int(input("enter a number over 100"))
smaller = int(input("enter a number under 10"))
answer = larger // smaller
print(smaller, "goes into", larger, answer, "times")
