class Ninja:
    # implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        print(f"take {self.pet.name} for a walk")

    def feed(self):
        self.pet.eat()
        print(f"feed {self.pet.name} {self.pet_food}")

    def bathe(self):
        self.pet.noise()
        print(f"Give{self.pet.name} a bath")


class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = 100
        self.health = 100

    def sleep(self):
        self.energy = self.energy + 25

    def eat(self):
        self.energy = self.energy + 5
        self.health = self.health + 10

    def play(self):
        self.health = self.health + 5

    def noise(self):
        print("Bark")

    def print_info(self):
        print(self.energy, self.health)


Doggo = Pet("Doggo", "Lab", "Rolling")
Abby = Ninja("Abby", "Smith", "Bones", "Kibble", Doggo)

Doggo.print_info()
Abby.feed()
Abby.walk()
Abby.feed()
Abby.walk()
Abby.bathe()
Doggo.print_info()
