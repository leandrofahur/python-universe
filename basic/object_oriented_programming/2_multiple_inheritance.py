class Hero:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"{self.name} is attacking with {self.power}")

class Warrior(Hero):
    def __init__(self, name, power, weapon):
        # super() is used to call the constructor of the parent class.
        super().__init__(name, power)
        self.weapon = weapon

    def attack(self):
        print(f"{self.name} is attacking with the weapon {self.weapon}")

class Mage(Hero):
    def __init__(self, name, power, spell):
        # If the parent class has a constructor, you must call it in the child class.
        super().__init__(name, power)
        self.spell = spell

    def attack(self):
        print(f"{self.name} is attacking with the spell {self.spell}")

hero = Hero("John Doe", "Sword")
warrior = Warrior("Warrior Doe", "Sword", "Sword")
mage = Mage("Mage Doe", "Fire", "Fireball")

print(hero.attack())
print(warrior.attack())
print(mage.attack())


