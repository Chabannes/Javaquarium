from Aquarium import *


def main():

    my_aquarium = Aquarium(15, 25, 30)  # number of predatories, herbivores, algaes, randomly chosen in files
    max_rounds = 30

    for round in range(0, max_rounds + 1):
        my_aquarium.show_aquarium()
        my_aquarium.make_predatory_eat()
        my_aquarium.make_herbivore_eat()
        my_aquarium.get_hungry()
        my_aquarium.make_give_birth()
        my_aquarium.make_insemination()
        my_aquarium.make_grow_old()
        my_aquarium.make_census()
        if round == max_rounds:
            my_aquarium.plot_evolution()

if __name__ == '__main__':
    main()
