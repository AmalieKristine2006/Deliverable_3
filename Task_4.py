import Task_1
import Task_3


class Warrior(Character):
    #Den er riktitg
    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, weapon: Weapon = None, armor: int = 5) -> None:
        super().__init__(name=name, hp_max=hp_max, damage=damage, weapon=weapon)
        self.armor = armor

    # Skal ta mindre skade hvis spiller har skjold
    def take_damage(self, damage: int):
        super().take_damage(self, damage: int)
        damage = damage - self.armor
            

    