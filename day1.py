from Elf import Elf
from Food import Food

def main():
    elves = []

    elf1 = Elf("Elf_1")
    elf1.addFood(Food("food1",1000))
    elf1.addFood(Food("food2",2000))
    elf1.addFood(Food("food3",3000))
    elves.append(elf1)

    elf2 = Elf("Elf_2")
    elf2.addFood(Food("food1",4000))
    elves.append(elf2)

    elf3 = Elf("Elf_3")
    elf3.addFood(Food("food1",5000))
    elf3.addFood(Food("food2",6000))
    elves.append(elf3)

    elf4 = Elf("Elf_4")
    elf4.addFood(Food("food1",7000))
    elf4.addFood(Food("food2",8000))
    elf4.addFood(Food("food3",9000))
    elves.append(elf4)

    elf5 = Elf("Elf_5")
    elf5.addFood(Food("food1",10000))
    elves.append(elf5)

    totalCalorieslist = []
    for elf in elves:
        totalCalorieslist.append(elf.getTotalCalories())

    print(f"Elf {totalCalorieslist.index(max(totalCalorieslist)) + 1} has the most calories, being {max(totalCalorieslist)}")

if __name__ == "__main__":
    main()