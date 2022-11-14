count = 0
with open("dracula.txt", "r") as foo:
    with open("vampytimes.txt", "w") as vamp:
        for line in foo:
            if "vampire" in line.lower():
                print(line)
                count += 1
                vamp.write(line)
print(count)
