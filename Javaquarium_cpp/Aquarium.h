#ifndef DEF_AQUARIUM
#define DEF_AQUARIUM

#include "Poisson.h"
#include "Algue.h"
#include "Animal.h"


#include <vector>


using namespace std;


class Aquarium
{
    public:

    Aquarium();
    ~Aquarium();
    void virtual add_poisson(Poisson &poisson);
    int getNumberHerbivore() const;
    int getNumberCarnivore() const;
    int getNumberAlgue() const;
    void add_algue(int nb_algue);
    void add_herbivore(int nb_poissons);
    void born_herbivore();
    void born_carnivore();
    void add_carnivore(int nb_poissons);
    void next_tour();
    void print() const;
    void hunger();
    void poissonHunt(int thr_hunger);
    void poissonEat(Poisson &poisson);
    void afficherDeadPoissons();
    void alguesGrowBack();
    void poissonsGrowOld();
    void shuffleAnimalsOrder();
    int isAvailable(string poissonName) const;
    int findCouple(Poisson &poisson) const;
    void poissonReproduction();
    void algueReproduction();
    void simuler(int nb_tour);


    

    protected:

    vector <Poisson*> m_poissons;  // il faut utiliser un pointeur pour la creation de m_poissons car sinon le vecteur ne serait que de type Poisson
                                 // tandis qu'avec un pointeur le polymorphisme pourra se mettre en oeuvre 
    
    vector <Algue*> m_algues;
    vector <Poisson*> m_deadPoissons;
    vector <Poisson*> m_reproductiblePoissons;
    int m_nb_tour = 0;

    vector<string> m_existingHerbivore = {"Gobie","Sole", "Mulet","Limande","Vieille","Vive","Lieu","Tacot","Dorade","Crevette"};
    vector<string> m_existingCarnivore = {"Bar","Thon", "Pieuvre", "Maigre","Maquereau","Phoque","Turbo","Roussette","Raie","Morue"};



};


#endif