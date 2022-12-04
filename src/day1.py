from elves import Elf
from itertools import groupby
import types
from collections import OrderedDict

def get_input(fileinfo):
    f_input = open(fileinfo)
    return f_input

def get_food_per_elf(textfile):
    input_lines = []

    # populate input_lines
    for line in textfile:
        input_lines.append(line.strip())

    # separate food_per_elf by empty list items
    food_per_elf = [list(sub) for ele, sub in groupby(input_lines, key = bool) if ele]

    return food_per_elf
    
def feed_elves(food):
    # create an empty elves list
    elves = []

    # create an Elf for every food_per_elf
    for i in range(len(food)):
        elves.append(Elf(i))

    # give each Elf in elves their food
    for l in range(len(food)):
        elves[l].foods = food[l]

    return elves

def get_most_prepared_elf(elves):
    # find the elf with the most food
    most_cals = 0
    most_prepared_elf = types.SimpleNamespace()
    for elf in elves:
        if elf.get_total_cals() > most_cals:
            most_cals = elf.get_total_cals()
            most_prepared_elf = elf

    return most_prepared_elf

def build_elf_dict(these_elves):
    elf_db = {}
    for elf in these_elves:
        elf_db.update({elf.id: elf.get_total_cals()})

    return elf_db

def get_top_3_elves(this_elf_db):
    total_cals = 0
    for i in range(3):
        total_cals += list(this_elf_db.values())[i]
    
    return total_cals

def main():

    day1_file = get_input("inputs/day_1_input.txt")

    food_per_elf = get_food_per_elf(day1_file)

    my_elves = feed_elves(food_per_elf)

    my_most_prepared_elf = get_most_prepared_elf(my_elves)

    sorted_elf_db = dict(sorted(build_elf_dict(my_elves).items(), key=lambda item: item[1], reverse=True))

    print("Elf " + str(my_most_prepared_elf.id) + " is the most prepared elf with " + 
    str(my_most_prepared_elf.get_total_cals()) + " calories!")

    print("The top 3 elves have " + str(get_top_3_elves(sorted_elf_db)) + " calories of food!")

    day1_file.close()
    

if __name__ == "__main__":
    main()







    


    
# for e in elves:
#     print(e.get_total_cals())

# print(res)
# print(len(res))

# for elf in elves:
#     print(elf.get_total_cals())


#print(elf_counter)

# print(input_lines)


