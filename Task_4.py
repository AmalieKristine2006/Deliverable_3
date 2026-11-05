
class Warrior(Character):
    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, weapon: Weapons = None, armor: int = 5) -> None:
        super().__init__(name=name, hp_max=hp_max, damage=damage, weapon=weapon)
        self.armor = armor




    Character.take_damage()