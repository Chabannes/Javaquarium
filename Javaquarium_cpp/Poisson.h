#ifndef DEF_POISSON
#define DEF_POISSON

#include <string>
#include "Animal.h"



using namespace std;


class Poisson : public Animal
{
    public :

    Poisson(); 
    virtual ~Poisson();
    string virtual getName() = 0;
    string virtual getType();
    void virtual eat(string victim) = 0;
    void virtual isBit();
    void setAge(int age);
    void setGender(string gender);
    string getGender() const;
    int getVie() const;
    int getAge() const;
    void growOld();

    protected:

    string m_gender;
    int m_age;


};


#endif