class Weapons:
    def __init__(self, name: str, Dice: int):
        """Initialize the weapon with a name and damage value"""
        self.name = name
        self.damage_dice = Dice

    def roll_damage(self) -> int:
        """Roll the damage dice and return the damage value"""
        self.damage_dice.roll(self.damage_dice)    