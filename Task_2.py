import random

class Dice:
    def __init__(self, sides: int = 6) -> None:
       #Terningen må ha minst 2 side
        if sides < 2:
            self.sides = sides

   
   def roll(self) -> int:
        # Triller terningen og returnerer et tall mellom 1 og antall sider
        return random.randint(1, self.sides)

    def __repr__(self) -> str:
        # Returnerer hvor mange sider terningen har
        return f"Dice(sides={self.sides})"
    
    def __call__(self) -> int:
        pass




"""Create a Dice class that can create any n-sided Dice (n>=2), where the default
number of sides is 6.

Add a roll() method to roll the dice, using random.randint(1, self.sides) .
Add a __repr__ method that returns string representations like Dice(sides=6) .
Implement a __call__ method that allow you to roll the dice created by d20 =
Dice(sides=20) by calling d20.roll() .
See the Python documentation of __call__ or this example"""