#ifndef DEF_ALGUE
#define DEF_ALGUE

#include <string>
#include "Animal.h"


using namespace std;


class Algue : public Animal
{
    public :

    Algue(); 
    Algue(int num); 
    ~Algue();
    int getVie() const;
    void virtual isBit();
    string virtual getType();
    int getNum() const;

    protected:
    int m_num;

};


#endif