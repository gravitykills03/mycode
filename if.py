import emoji

guess = int(input("What's the magic number? "))

secret_num = 42

if secret_num == guess:
    print("Correct!")
elif secret_num-5 < guess < secret_num+5:
    print("Close!")
else:
    answer = emoji.emojize("That is the :bomb:")
    print(answer)


