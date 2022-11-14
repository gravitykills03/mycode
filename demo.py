greeting = {
        0: "Hello!",
        1: "Good",
        2: "morning,",
        3: "and welcome",
        4: "back to class."
        }
for i in range(len(greeting)):
    print(greeting[i], end=" ")
age = int(input("How old are you?"))

if age >= 30:
    print("a")
elif age >= 40:
    print("b")
else:
    print("Pfft")
