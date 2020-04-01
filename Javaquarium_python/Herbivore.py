from Fish import *
import random


class Herbivore(Fish):

    reproduction_rate = 0.8
    max_litter = 2
    sexual_maturity = 4
    max_age = 20
    hunger_threshold = 3
    instances = []

    def __init__(self, id, gender, age, life, specie):
        super().__init__(id, gender, age, life, diet='herbivore')
        self._specie = specie
        self.__class__.instances.append(self)

    @property
    def diet(self):
        return self._diet

    @property
    def specie(self):
        return self._specie

    @property
    def age(self):
        return self._age

    @property
    def life(self):
        return self._life

    @specie.setter
    def specie(self, value):
        self._specie = value

    @diet.setter
    def diet(self, value):
        self._diet = value

    @life.setter
    def life(self, value):
        self._life = value
        if self._life >= 10:
            self._life = 10

        elif self._life <= 0:
            Herbivore.instances.remove(self)

    @age.setter
    def age(self, value):
        self._age = value
        if self._age >= type(self).max_age:
            Herbivore.instances.remove(self)

    def eat(self):
        if self.life < Herbivore.hunger_threshold:
            self.life += 3
            if self.life > 10:
                self.life = 10
            return True
        return False

    def is_bit(self):
        self.life -= 3

    def inseminate(self):
        n = random.randrange(0, 11) * 0.1
        if n <= Herbivore.reproduction_rate:
            self.pregnant = True

    def give_birth(self, id_number):
        if self.pregnant:
            m = random.randrange(int(type(self).max_litter/2), type(self).max_litter+1)
            for k in range(m):
                gender = random.choice(["male", "female"])
                age = 0
                life = 5
                new_id = "herbivore_" + str(id_number + k)
                Herbivore(new_id, gender, age, life, self._specie)
                self.pregnant = False
