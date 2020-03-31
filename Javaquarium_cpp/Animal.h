#ifndef DEF_ANIMAL
#define DEF_ANIMAL

#include <string>


using namespace std;


class Animal
{
    public :

    Animal(); 
    virtual ~Animal();
    int getVie() const;
    string virtual getType();
    void updateVie(int dVie);
    void virtual isBit() = 0;

    protected:

    int m_vie = 10;


};

#endif