#ifndef DEF_CARNIVORE
#define DEF_CARNIVORE

#include "Poisson.h"

#include <string>


using namespace std;


class Carnivore : public Poisson
{
    public :

    Carnivore(); 
    Carnivore(string name);
    ~Carnivore();
    string virtual getName();
    string virtual getType();
    void virtual eat(string victim);

    protected:

    string m_name;

};


#endif