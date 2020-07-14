flowers = ("daisy", "rose")
print(flowers.index("rose")) # Output is 1

zoo = ("panda", "polar bear", "giraffe", "llama", "monkey", "kangaroo", "cheetah", "tiger", "sloth", "turtle")
print(zoo.index("tiger"))
print(zoo[7])
if "kangaroo" in zoo:
    print("Animal is present")

(first_animal, second_animal, third_animal, fourth_animal, fifth_animal, sixth_animal, seventh_animal, eigth_animal, ninth_animal, tenth_animal ) = zoo
print(first_animal)
print(second_animal)
print(third_animal)
print(fourth_animal)
print(fifth_animal)
print(sixth_animal)
print(seventh_animal)
print(eigth_animal)
print(ninth_animal)
print(tenth_animal)

# bigger_zoo = zoo + ("jaguar", "gorilla", "peguin")
# print(bigger_zoo)

zoo = list(tuple(zoo))
print("list:", zoo)
more = ["jaguar", "gorilla", "penguin"]
zoo.extend(more)
print("extended list:", zoo)
zoo = tuple(list(zoo))
print("tuple again:", zoo)