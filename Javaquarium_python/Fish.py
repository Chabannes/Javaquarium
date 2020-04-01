

class Fish:

    def __init__(self, id, gender, age, life, diet):
        self.id = id
        self.gender = gender
        self.age = age
        self.life = life
        self.pregnant = False
        self.diet = diet

    @property
    def id(self):
        return self._id

    @property
    def gender(self):
        return self._gender

    @property
    def age(self):
        return self._age

    @property
    def pregnant(self):
        return self._pregnant

    @property
    def diet(self):
        return self._diet

    @id.setter
    def id(self, value):
        self._id = value

    @gender.setter
    def gender(self, value):
        self._gender = value

    @age.setter
    def age(self, value):
        self._age = value

    @pregnant.setter
    def pregnant(self, value):
        self._pregnant = value

    @diet.setter
    def diet(self, value):
        self._diet = value
