from Fish import *
import random
import weakref


class Herbivore(Fish):

    reproduction_rate = 0.7
    max_litter = 20
    instances = []

    def __init__(self, id, gender, age, life, specie):
        super().__init__(id, gender, age, life, diet='herbivore')
        self._specie = specie
        self.__class__.instances.append(weakref.proxy(self))

    def __del__(self):
        Herbivore.instances.remove(self)

    @property
    def diet(self):
        return self._diet

    @property
    def specie(self):
        return self._specie

    @specie.setter
    def specie(self, value):
        self._specie = value

    @diet.setter
    def diet(self, value):
        self._diet = value

    def eat(self):
        if self.life < 5:
            self.life += 2
            if self.life > 10:
                self.life = 10
            return True
        return False

    def is_bit(self):
        self.life -= 3
        if self.life <= 0:
            del self

    def give_birth(self, id_number):
        if self.pregnant:
            m = random.randrange(int(type(self).max_litter/2), type(self).max_litter+1)
            baby_list = []
            for k in range(m):
                gender = random.choice(["male", "female"])
                age = 0
                life = 5
                new_id = "herbivore_" + str(id_number + k)
                baby_herb = Herbivore(new_id, gender, age, life, self._specie)
                baby_list.append(baby_herb)
            return baby_list


