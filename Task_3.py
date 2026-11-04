class Weapon:
    def __init__(self, name: str, damage_dice: Dice) -> None:
        """Initialize the weapon with a name and damage value"""
        self.name = name
        self.damage_dice = damage_dice

    def roll_damage(self) -> int:
        """Roll the damage dice and return the damage value"""
        return self.damage_dice.roll()