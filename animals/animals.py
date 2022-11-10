#!/usr/bin/env python3
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

for animal in farms[0]["agriculture"]:
    print(animal)

choice = input("Choose a farm to see what animals and crops are grown (NE Farm, W Farm, SE Farm)\n>")
for farm in farms:
    if farm["name"].lower() == choice.lower():
        print(f"{choice} has these plants and/or animals: ")
        for items in farm["agriculture"]:
            print(items)
        yuck = ["carrots", "celery"]
        for items in farm["agriculture"]:
            if items not in yuck:
                print("\nWe excluded anything that is not an animal")
                print(items)

