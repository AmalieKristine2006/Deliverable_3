from Task_1 import Character
from Task_3 import Weapon


class Warrior(Character):
    
    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, weapon: Weapon = None, armor: int = 5) -> None:
        super().__init__(name=name, hp_max=hp_max, damage=damage, weapon=weapon)
        self.armor = armor

    # The character takes less damage when it has armor
    def take_damage(self, damage: int):
        super().take_damage(damage=damage)
        damage = damage - self.armor
            
class Mage(Character):
    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, weapon: Weapon = None, mana: int = 30, mana_max: int = 30) -> None:
        super().__init__(name=name, hp_max=hp_max, damage=damage, weapon=weapon)
        self.mana = mana

    def attack(self, target: 'Character'):
    # If it has more than 10 mana it spends 10 to attack with double damage
        if self.mana >= 10:
              self.mana -= 10
              target.take_damage(self.damage*2)
        # If it doesnt have 10 mana it attacks normally and collect 5 more mana
        else: 
             super().attack(target=target)
             self.mana = self.mana + 5

        

    