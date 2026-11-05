import random

class Dice:
    def __init__(self, sides: int = 6) -> None:
       #Terningen må ha minst 2 side
        if sides > 2:
            self.sides = sides

    def roll(self) -> int:
        # Triller terningen og returnerer et tall mellom 1 og antall sider
        return random.randint(1, self.sides)

    def __repr__(self) -> str:
        # Returnerer hvor mange sider terningen har
        return f"Dice(sides={self.sides})"
    
    def __call__(self) -> int:
        # Triller terningen?
        return self.roll()

#test
a = Dice(sides=5)
print(a())

