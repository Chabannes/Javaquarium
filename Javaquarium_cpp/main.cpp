#include <iostream>
#include "Aquarium.h"
#include "Herbivore.h"
#include "Carnivore.h"
#include "Poisson.h"
#include <stdio.h>

int main()

{
    freopen ("rapport aquarium.txt","w",stdout);
    Aquarium aquarium;

    aquarium.add_algue(10);
    aquarium.add_herbivore(5);
    aquarium.add_carnivore(2);

    aquarium.simuler(10);
    fclose (stdout);


}
