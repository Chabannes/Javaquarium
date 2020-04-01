import random
import numpy as np


class Algae:

    max_age = 20
    sexual_maturity = 4
    instances = []

    def __init__(self, id, life, age):
        self.id = id
        self.life = life
        self.age = age
        self.__class__.instances.append(self)

    @classmethod
    def garbage_deads(cls):
        cls.instances = [algae for algae in cls.instances if algae.life > 0]

    @classmethod
    def reproduction_rate(cls):
        return int(300*np.exp(-len(cls.instances)/30))

    @property
    def id(self):
        return self._id

    @property
    def age(self):
        return self._age

    @property
    def life(self):
        return self._life

    @id.setter
    def id(self, value):
        self._id = value

    @age.setter
    def age(self, value):
        self._age = value
        if self._age >= type(self).max_age:
            Algae.instances.remove(self)

    @life.setter
    def life(self, value):
        self._life = value
        if self._life >= 10:
            self._life = 10

        elif self._life <= 0:
            Algae.instances.remove(self)

    def is_bit(self):
        self.life -= 10

    def grow_back(self):
        self.life += 1
        self.age += 1

    def reproduce(self, id_number):
        if self.life > 4:
            m = random.randrange(type(self).reproduction_rate(), type(self).reproduction_rate() + 1)
            for k in range(m):
                age = 0
                life = int(self.life/2 + 1)
                self.life = life
                new_id = "algae_" + str(id_number + k)
                Algae(new_id, life, age)