import Food

class Elf:
    def __init__(self, name):
        self.name = name
        self.foodbag = []

    def addFood(self, item):
        self.foodbag.append(item)

    def getTotalCalories(self):
        total = 0
        for item in self.foodbag:
            total += item.calories
        return total
