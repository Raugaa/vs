weight = float(input("Let's convert your weight. How much do you weigh? "))
mass = input("Is that in (K)g or (L)bs? ")
if mass.upper() == "K":
    print("In Pounds, you weigh: ", weight * 2.21)
elif mass.upper() == "L":
    print("In Kilograms, you weigh: ", weight * 0.45)
else:
    print("U r confused.")
print("Have a nice day!")