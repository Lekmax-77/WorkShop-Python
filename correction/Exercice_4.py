
class Villager:
    def __init__(self, name, hp=100, attack=5, stamina=100):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.stamina = stamina
        self.is_alive = True

    def attack(self):
        if self.stamina >= 10:
            self.stamina -= 10
            print(f"{self.name} attacks!")

    def rest(self):
        if self.stamina <= 100:
            self.stamina += 10
            print(f"{self.name} rests!")

    def damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.is_alive = False
            print(f"{self.name} is dead!")

    def speak(self):
        print("Hello, my Name is " + self.name)


class Knight(Villager):
    def __init__(self, name, hp=150, attack=15, stamina=100):
        Villager.__init__(self, name, hp, attack, stamina)
        self.armor = 50

    def damage(self, damage):
        self.hp -= damage - self.armor
        if self.hp <= 0:
            self.is_alive = False
            print(f"{self.name} is dead!")