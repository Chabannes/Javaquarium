#ifndef DEF_HERBIVORE
#define DEF_HERBIVORE

#include "Poisson.h"

#include <string>


using namespace std;


class Herbivore : public Poisson
{
    public :

    Herbivore(); 
    Herbivore(string name);
    ~Herbivore();
    string virtual getName();
    string virtual getType();
    void virtual eat(string victim);


    protected:

    string m_name;

};


#endif