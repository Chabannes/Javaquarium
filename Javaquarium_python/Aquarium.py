import random
import matplotlib.pyplot as plt
import pandas as pd
from Predatory import *
from Herbivore import *
from Algae import *


class Aquarium:

    def __init__(self, nb_pred, nb_herb, nb_algae):
        self._pred_display = pd.DataFrame(columns=['id', 'specie', 'age', 'life', 'gender', 'pregnant', 'object'])
        self._herb_display = pd.DataFrame(columns=['id', 'specie', 'age', 'life', 'gender', 'pregnant', 'object'])
        self._algae_display = pd.DataFrame(columns=['id', 'age', 'life', 'object'])
        self._history_pred = [nb_pred]
        self._history_herb = [nb_herb]
        self._history_algae = [nb_algae]
        self._number_pred = nb_pred
        self._number_herb = nb_herb
        self._number_algae = nb_algae
        self._round = 0

        pd_pred = pd.read_csv('predatory', header=None, names=['predatory'])
        pd_herb = pd.read_csv('herbivore', header=None, names=['herbivore'])

        for k in range(self._number_pred):
            n = pd_pred.shape[0]
            x = random.randrange(n)
            specie = pd_pred.iloc[x]['predatory']
            id = "predatory_" + str(k + 1)
            gender = random.choice(['male', 'female'])
            age = random.randrange(1, 11)
            life = random.randrange(6, 11)
            pred = Predatory(id, gender, age, life, specie)
            self._pred_display.loc[k] = [pred.id, pred.specie, pred.age, pred.life, pred.gender, pred.pregnant, pred]

        for k in range(self._number_herb):
            n = pd_herb.shape[0]
            x = random.randrange(n)
            specie = pd_herb.iloc[x]['herbivore']
            id = "herbivore_" + str(k + 1)
            gender = random.choice(['male', 'female'])
            age = random.randrange(1, 11)
            life = random.randrange(6, 11)
            herb = Herbivore(id, gender, age, life, specie)
            self._herb_display.loc[k] = [herb.id, herb.specie, herb.age, herb.life, herb.gender, herb.pregnant, herb]

        for k in range(self._number_algae):
            age = random.randrange(1, 31)
            life = random.randrange(6, 11)
            algae = Algae("algae_" + str(k + 1), life, age)
            self._algae_display.loc[k] = [algae.id, algae.life, age, algae]

    @property
    def number_pred(self):
        return len(self._pred_display.index)

    @property
    def number_herb(self):
        return len(self._herb_display.index)

    @property
    def number_algae(self):
        return len(self._algae_display.index)

    @property
    def round(self):
        return self._round

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
        for index, row in self._pred_display.iterrows():    # while k < len(self._pred_display.index):
            if not self._herb_display.empty:
                if row['object'].eat():
                    n = random.randrange(len(self._herb_display.index))
                    self._herb_display.iloc[n]['object'].is_bit()
                    if self._herb_display.iloc[n]['object'].life <= 0:
                        self._herb_display = self._herb_display[self._herb_display['object'] != self._herb_display.iloc[n]['object']]
                    else:
                        self._herb_display.loc[self._herb_display.id == self._herb_display.iloc[n].id, 'life'] = self._herb_display.iloc[n].life
            else:
                break

    def make_herbivore_eat(self):
        for index, row in self._herb_display.iterrows():
            if not self._algae_display.empty:
                if row['object'].eat():
                    n = random.randrange(len(self._algae_display.index))
                    self._algae_display.iloc[n]['object'].is_bit()
                    if self._algae_display.iloc[n]['object'].life <= 0:
                        self._algae_display = self._algae_display[self._algae_display['object'] != self._algae_display.iloc[n]['object']]
                    else:
                        self._algae_display.loc[self._algae_display.id == self._algae_display.iloc[n].id, 'life'] = self._algae_display.iloc[n].life
            else:
                break

    def get_hungry(self):
        for index, row in self._pred_display.iterrows():
            row['object'].life -= 1
            if row['object'].life <= 0:  # object deleted in Fish
                self._pred_display = self._pred_display[self._pred_display['object'] != row['object']]
            else:
                self._pred_display.loc[self._pred_display['object'] == row['object'], 'life'] = row['object'].life

        for index, row in self._herb_display.iterrows():
            row['object'].life -= 1
            if row['object'].life <= 0:  # object deleted in Fish
                self._herb_display = self._herb_display[self._herb_display['object'] != row['object']]
            else:
                self._herb_display.loc[self._herb_display['object'] == row['object'], 'life'] = row['object'].life

    def make_give_birth(self):
        algae_candidates = self._algae_display.loc[self._algae_display['life'] > 2]
        for index, row in algae_candidates.iterrows():
            new_algae_list = row['object'].reproduce(len(Algae.instances))
            if new_algae_list:
                ind = len(self._algae_display.index)
                for k in range(len(new_algae_list)): #if new_algae:
                    self._algae_display.loc[ind + k] = [new_algae_list[k].id, new_algae_list[k].life, new_algae_list[k].age, new_algae_list[k]]

        pregnant_pred = self._pred_display.loc[self._pred_display['pregnant'] == True]
        for index, row in pregnant_pred.iterrows():
            new_pred_list = row['object'].give_birth(len(Predatory.instances))
            ind = len(self._pred_display.index)
            for k in range(len(new_pred_list)):
                self._pred_display.loc[ind + k] = [new_pred_list[k].id, new_pred_list[k].specie, new_pred_list[k].age, new_pred_list[k].life, \
                                           new_pred_list[k].gender, new_pred_list[k].pregnant, new_pred_list[k]]
            ###
            row['object'].pregant = False
            self._pred_display.loc[self._pred_display.object == row['object'], 'pregnant'] = row['object'].pregnant
            ###

        pregnant_herb = self._herb_display.loc[self._herb_display['pregnant'] == True]
        for index, row in pregnant_herb.iterrows():
            new_herb_list = row['object'].give_birth(len(Herbivore.instances))
            ind = len(self._herb_display.index)
            for k in range(len(new_herb_list)):
                self._herb_display.loc[ind + k] = [new_herb_list[k].id, new_herb_list[k].specie, new_herb_list[k].age, new_herb_list[k].life, \
                                           new_herb_list[k].gender, new_herb_list[k].pregnant, new_herb_list[k]]
            ###
            row['object'].pregant = False
            self._herb_display.loc[self._herb_display.object == row['object'], 'pregnant'] = row['object'].pregnant
            ###

    def make_insemination(self):
        male_predatories = self._pred_display.loc[self._pred_display['gender'] == 'male']
        male_herbivores = self._herb_display.loc[self._herb_display['gender'] == 'male']

        for index_male, row_male in male_predatories.iterrows():
            dating_pool = self._pred_display.loc[(self._pred_display['specie'] == row_male['object'].specie) & \
                                            (self._pred_display['gender'] != row_male['object'].gender) & (self._pred_display['age'] > 6)]

            for index_female, row_female in dating_pool.iterrows():
                if not row_female['object'].pregnant:
                    n = random.randrange(0, 11) * 0.1
                    if n <= Predatory.reproduction_rate:
                        ###
                        row_female['object'].pregnant = True
                        self._pred_display.loc[self._pred_display.object == row_female['object'], 'pregnant'] = row_female['object'].pregnant
                        ###

        for index_male, row_male in male_herbivores.iterrows():
            dating_pool = self._herb_display.loc[(self._herb_display['specie'] == row_male['object'].specie) & \
                                            (self._herb_display['gender'] != row_male['object'].gender) & (self._herb_display['age'] > 6)]

            for index_female, row_female in dating_pool.iterrows():
                if not row_female['object'].pregnant:
                    n = random.randrange(0, 11) * 0.1
                    if n <= Herbivore.reproduction_rate:
                        ###
                        row_female['object'].pregnant = True
                        self._herb_display.loc[self._herb_display.object == row_female['object'], 'pregnant'] = row_female['object'].pregnant
                        ###

    def make_grow_old(self):          # LES 20 ANS DOIVENT ETRE INTEGRES A CHAQUE CLASS !!!!!!!!!!!!!!!!!!!!!!!!!!

        for index, row in self._algae_display.iterrows():
            row['object'].age += 1
            if row['object'].age > 40:
                self._algae_display = self._algae_display[self._algae_display['object'] != row['object']]
            else:
                self._algae_display.loc[self._algae_display.object == row.object, 'age'] = row['object'].age

        k = 0
        while k < len(self._pred_display.index):
            self._pred_display.iloc[k]['object'].age += 1
            if self._pred_display.iloc[k]['object'].age > 20:
                self._pred_display = self._pred_display[self._pred_display['object'] != self._pred_display.iloc[k]['object']]
            else:
                # UPDATE
                self._pred_display.loc[self._pred_display.object == self._pred_display.iloc[k].object, 'age'] = self._pred_display.iloc[k]['object'].age
            k += 1
        k = 0
        while k < len(self._herb_display.index):
            self._herb_display.iloc[k]['object'].age += 1
            if self._herb_display.iloc[k]['object'].age > 20:
                del self._herb_display.iloc[k]['object']  # die of old age
                self._herb_display = self._herb_display[self._herb_display['object'] != self._herb_display.iloc[k]['object']]
            else:
                # UPDATE
                self._herb_display.loc[self._herb_display.object == self._herb_display.iloc[k].object, 'age'] = self._herb_display.iloc[k]['object'].age
            k += 1

        for index, row in self._algae_display.iterrows():
            row['object'].grow_back()
            self._algae_display.loc[self._algae_display.object == row.object, 'life'] = row['object'].life  # UPDATE

    def make_census(self):

        self._history_pred.append(self.number_pred)
        self._history_herb.append(self.number_herb)
        self._history_algae.append(self.number_algae)
        self._round += 1

    def show_aquarium(self):

        show_pred =  self._pred_display[['id', 'age', 'life', 'gender', 'pregnant']]
        show_herb =  self._herb_display[['id', 'age', 'life', 'gender', 'pregnant']]
        show_algae =  self._algae_display[['id', 'life']]

        print("\nThe predatories in the aquarium are :\n", show_pred)
        print("\nThe herbivores in the aquarium are :\n", show_herb)
        print("\nThe algaes in the aquarium are :\n", show_algae)

    def plot_evolution(self):
        time = list(range(0, self._round + 1))
        plt.figure()
        plt.title('Aquarium Evolution until round %s' %(self._round))
        plt.plot(time, self._history_pred, label='predatories', c='r', linewidth=3)
        plt.plot(time, self._history_herb, label='herbivores', c='b', linewidth=3)
        plt.plot(time, self._history_algae, label='algaes', c='g', linewidth=3)
        plt.xlabel('Number of rounds')
        plt.ylabel('Fauna and Flora quantities')
        plt.legend()
        plt.show()