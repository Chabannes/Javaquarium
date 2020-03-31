from Aquarium import *
from Predatory import *
from Fish import *


def main():

    my_aquarium = Aquarium(10, 20, 20)  # number of predatories, herbivores, algaes, randomly chosen in files

    for k in range(1, 30):
        print("\n\nROUND ", k)
        my_aquarium.show_aquarium()
        my_aquarium.make_predatory_eat()
        my_aquarium.make_herbivore_eat()
        my_aquarium.get_hungry()
        my_aquarium.make_give_birth()
        my_aquarium.make_insemination()
        my_aquarium.make_grow_old()
        my_aquarium.make_census()
        if k == 29:
            my_aquarium.plot_evolution()

if __name__ == '__main__':
    main()