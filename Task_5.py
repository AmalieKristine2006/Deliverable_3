from Task_1 import Character


class Battle:
    def __init__(self, hero: Character, enemy: Character) -> None:
        """Initialize the battle with a hero and a enemy character"""
        self.hero = hero
        self.enemy = enemy

    def play_round(self) -> None:
        """Play a round of the battle where both characters attack each other"""
        self.hero.attack(self.enemy) 
        if self.enemy.is_alive:
            self.enemy.attack(self.hero)

    def simulate_battle(self) -> None:
        """Simulate the battle until one character is defeated"""
        while self.hero.is_alive and self.enemy.is_alive:
            self.play_round()