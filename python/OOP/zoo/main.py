class Animal:
    def __init__(self):
        self.health = 80
        self.happiness = 50

    def display_info(self):
        print("Nombre: ", self.name, "\n" "Salud: ", self.health, "\n" "Felicidad: ", self.happiness, "\n")
        return self

    def feeding(self):
        self.happiness += 10
        return self


class Lion(Animal):

    def __init__(self, name, age, origin):
        super().__init__()
        self.name = name
        self.age = age
        self.origin = origin

    def display_info_lion(self):
        super().display_info()
        print("Origen: ", self.origin)
        return self

    def feeding_lion(self):
        super().feeding()
        self.health+=2
        return self


class Tiger(Animal):
    def __init__(self, name, age, weight):
        super().__init__()
        self.name = name
        self.age = age
        self.weight = weight

    def feeding_tiger(self):
        super().feeding()
        self.health+=5
        return self

class Bear(Animal):
    def __init__(self, name, age, type):
        super().__init__()
        self.name = name
        self.age = age
        self.type = type

    def feeding(self):
        self.happiness+=12
        self.health+=10
        return self

zoo = Animal()

animal1 = Lion("Maria", 12, "Kenia")
animal1.feeding().display_info()

tiger1 = Tiger("Bengala", 2, 150)
tiger1.feeding_tiger().display_info()

bear1 = Bear("Poo", 2, "Panda")
bear1.feeding().display_info()
