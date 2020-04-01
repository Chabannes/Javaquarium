import random
import matplotlib.pyplot as plt
import pandas as pd
from Predatory import *
from Herbivore import *
from Algae import *


class Aquarium:

    def __init__(self, nb_pred, nb_herb, nb_algae):
        self.pred_display = pd.DataFrame(columns=['id', 'specie', 'age', 'life', 'gender', 'pregnant'])
        self.herb_display = pd.DataFrame(columns=['id', 'specie', 'age', 'life', 'gender', 'pregnant'])
        self.algae_display = pd.DataFrame(columns=['id', 'age', 'life'])
        self.history_pred = [nb_pred]
        self.history_herb = [nb_herb]
        self.history_algae = [nb_algae]
        self.number_pred = len(Predatory.instances)
        self.number_herb = len(Herbivore.instances)
        self.number_algae = len(Algae.instances)
        self.round = 0

        pd_pred = pd.read_csv('predatory', header=None, names=['predatory'])
        pd_herb = pd.read_csv('herbivore', header=None, names=['herbivore'])

        for k in range(nb_pred):
            n = pd_pred.shape[0]
            x = random.randrange(n)
            specie = pd_pred.iloc[x]['predatory']
            new_id = "predatory_" + str(k + 1)
            gender = random.choice(['male', 'female'])
            age = random.randrange(1, Predatory.max_age)
            life = random.randrange(5, 11)
            Predatory(new_id, gender, age, life, specie)

        for k in range(nb_herb):
            n = pd_herb.shape[0]
            x = random.randrange(n)
            specie = pd_herb.iloc[x]['herbivore']
            new_id = "herbivore_" + str(k + 1)
            gender = random.choice(['male', 'female'])
            age = random.randrange(1, Herbivore.max_age)
            life = random.randrange(5, 11)
            Herbivore(new_id, gender, age, life, specie)

        for k in range(nb_algae):
            age = random.randrange(1, Algae.max_age)
            life = random.randrange(5, 11)
            new_id = "algae_" + str(k + 1)
            Algae(new_id, life, age)

    @property
    def algae(self):
        return Algae.instances

    @property
    def herb(self):
        return Herbivore.instances

    @property
    def pred(self):
        return Predatory.instances

    @property
    def number_pred(self):
        return len(Predatory.instances)

    @property
    def number_herb(self):
        return len(Herbivore.instances)

    @property
    def number_algae(self):
        return len(Algae.instances)

    @property
    def pred_display(self):
        return self._pred_display

    @property
    def herb_display(self):
        return self._herb_display

    @property
    def algae_display(self):
        return self._algae_display

    @property
    def round(self):
        return self._round

    @algae.setter
    def algae(self, value):
        self._algae = value

    @herb.setter
    def herb(self, value):
        self._herb = value

    @pred.setter
    def pred(self, value):
        self._pred = value

    @pred_display.setter
    def pred_display(self, value):
        self._pred_display = value

    @herb_display.setter
    def herb_display(self, value):
        self._herb_display = value

    @algae_display.setter
    def algae_display(self, value):
        self._algae_display = value

    @number_pred.setter
    def number_pred(self, value):
        self._number_pred = value

    @number_herb.setter
    def number_herb(self, value):
        self._number_herb = value

    @number_algae.setter
    def number_algae(self, value):
        self._number_algae = value

    @round.setter
    def round(self, value):
        self._round = value

    def make_predatory_eat(self):
        for pred in self.pred:
            if self.herb:
                if pred.eat():
                    n = random.randrange(len(self.herb))
                    self.herb[n].is_bit()

    def make_herbivore_eat(self):
        for herb in self.herb:
            if self.algae:
                if herb.eat():
                    n = random.randrange(len(self.algae))
                    self.algae[n].is_bit()

    def get_hungry(self):
        for pred in self.pred:
            pred.life -= 1

        for herb in self.herb:
            herb.life -= 1

    def make_give_birth(self):
        algae_candidates = [algae for algae in self.algae if (algae.age > Algae.sexual_maturity) & (algae.life > 3)]
        for algae in algae_candidates:
            algae.reproduce(self.number_algae)

        pregnant_pred = [pred for pred in self.pred if pred.pregnant == True]
        for pred in pregnant_pred:
            ind = self.number_pred
            pred.give_birth(ind)

        pregnant_herb = [herb for herb in self.herb if herb.pregnant == True]
        for herb in pregnant_herb:
            ind = self.number_herb
            herb.give_birth(ind)

    def make_insemination(self):
        male_pred_list = [pred for pred in self.pred if pred.gender == 'male']
        for male_pred in male_pred_list:
            dating_pool = [pred for pred in self.pred if (pred.specie == male_pred.specie)&(pred.gender == 'female')& \
                           (pred.age >= Predatory.sexual_maturity)&(pred.pregnant == False)&(pred.life > 2)]
            for female_pred in dating_pool:
                female_pred.inseminate()

        male_herb_list = [herb for herb in self.herb if herb.gender == 'male']
        for male_herb in male_herb_list:
            dating_pool = [herb for herb in self.herb if (herb.specie == male_herb.specie)&(herb.gender == 'female')& \
                           (herb.age >= Herbivore.sexual_maturity)&(herb.pregnant == False)&(herb.life > 2)]
            for female_herb in dating_pool:
                female_herb.inseminate()

    def make_grow_old(self):

        for algae in self.algae:
            algae.grow_back()

        for pred in self.pred:
            pred.age += 1

        for herb in self.herb:
            herb.age += 1

    def make_census(self):

        self.history_pred.append(self.number_pred)
        self.history_herb.append(self.number_herb)
        self.history_algae.append(self.number_algae)
        self.round += 1

    def show_aquarium(self):

        for k in range(len(self.pred)):
            pred = self.pred[k]
            self.pred_display.loc[k] = [pred.id, pred.specie, pred.age, pred.life, pred.gender, pred.pregnant]
        self.pred_display = self.pred_display.drop([ i for i in range(len(self.pred), len(self.pred_display.index))])

        for k in range(len(self.herb)):
            herb = self.herb[k]
            self.herb_display.loc[k] = [herb.id, herb.specie, herb.age, herb.life, herb.gender, herb.pregnant]
        self.herb_display = self.herb_display.drop([i for i in range(len(self.herb), len(self.herb_display.index))])

        for k in range(len(self.algae)):
            algae = self.algae[k]
            self.algae_display.loc[k] = [algae.id, algae.life, algae.age]
        self.algae_display = self.algae_display.drop([ i for i in range(len(self.algae), len(self.algae_display.index))])

        print("\nROUND %s\n" %self.round)

        if self.pred_display.empty:
            print("\nNo more predatories in the aquarium.")
        else:
            print("\nThe predatories in the aquarium are :\n", self.pred_display)

        if self.herb_display.empty:
            print("No more herbivores in the aquarium.")
        else:
            print("\nThe herbivores in the aquarium are :\n", self.herb_display)

        if self.algae_display.empty:
            print("\nNo more algaes in the aquarium.")
        else:
            print("\nThe algaes in the aquarium are :\n", self.algae_display)

    def plot_evolution(self):

        time = list(range(0, self.round + 1))
        plt.figure()
        plt.title('Aquarium Evolution until round %s' %(self.round))
        plt.plot(time, self.history_pred, label='predatories', c='r', linewidth=3)
        plt.plot(time, self.history_herb, label='herbivores', c='b', linewidth=3)
        plt.plot(time, self.history_algae, label='algaes', c='g', linewidth=3)
        plt.grid()
        plt.xlabel('Number of rounds')
        plt.ylabel('Fauna and Flora quantities')
        plt.legend()
        plt.show()