import random
import numpy as np
import weakref


class Algae:

    max_life = 40
    instances = []

    def __init__(self, id, life, age=0):
        self.id = id
        self.life = life
        self.age = age
        self.__class__.instances.append(weakref.proxy(self))

    def __del__(self):
        Algae.instances.remove(self)

    @classmethod
    def reproduction_rate(cls):
        return int(300*np.exp(-len(cls.instances)/20))

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

    @life.setter
    def life(self, value):
        self._life = value
        if self._life >= 10:
            self._life = 10

        elif self._life >= type(self).max_life:
            del self

        elif self._life <= 0:
            del self

    def is_bit(self):
        self.life -= 3

    def grow_back(self):
        self.life += 1

    def reproduce(self, id_number):
        if self.life > 4:
            m = random.randrange(type(self).reproduction_rate(), type(self).reproduction_rate() + 1)
            baby_list = []
            for k in range(m):
                age = 0
                life = int(self.life/2)
                self.life = self.life/2
                new_id = "algae_" + str(id_number + k)
                baby_algae = Algae(new_id, age, life)
                baby_list.append(baby_algae)
            return baby_list
