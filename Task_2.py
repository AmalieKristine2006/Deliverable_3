import random

class Dice:
    def __init__(self, sides: int = 6) -> None:
       #The dice needs to have at least 2 sides
        if sides > 2:
            self.sides = sides

    def roll(self) -> int:
        # Rolls the dice and returns a number between 1 and the amount of sides
        return random.randint(1, self.sides)

    def __repr__(self) -> str:
        # Returns the number of sides on the dice
        return f"Dice(sides={self.sides})"
    
    def __call__(self) -> int:
        # Allows you to call and roll the dice
        return self.roll()

#test
a = Dice(sides=5)
print(a())

