class Animal:

    alive = []

    def __init__(self, name: str, health: int = 100, hidden = False):
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self):
        return "{Name: %s, Health: %s, Hidden: %s}" % (self.name, self.health, self.hidden)

class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden

class Carnivore(Animal):
    @staticmethod
    def bite(other: Animal):
        if isinstance(other, Herbivore):
            if not other.hidden:
                other.health -= 50
                if other.health <= 0:
                    Animal.alive.remove(other)