from Elf import Elf
from Food import Food
import os

def createElves(fileName):

    countElves= 0

    elves = []
    file = open(fileName, "r")

    if os.path.getsize(fileName) > 0:
        countElves += 1

        newElf = Elf(f"Elf_{countElves}")
        for line in file:
            if line == "\n":
                elves.append(newElf)
                countElves += 1
                newElf = Elf(f"Elf_{countElves}")
            else:
                newElf.addFood(Food("",int(line.rstrip())))

    return elves

def main():

    elves = createElves("input.txt")

    totalCalorieslist = []

    for elf in elves:
        totalCalorieslist.append(elf.getTotalCalories())

    print(f"Elf {totalCalorieslist.index(max(totalCalorieslist)) + 1} has the most calories, being {max(totalCalorieslist)}")
    print(f"Sum of Total Calories of the top three elves = {sum(sorted(totalCalorieslist, reverse=True)[:3])}")

if __name__ == "__main__":
    main()