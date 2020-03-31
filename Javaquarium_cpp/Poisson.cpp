#include "Poisson.h"


#include <iostream>
#include <string>
#include <vector>


Poisson::Poisson() 
{}

Poisson::~Poisson()
{}

string Poisson::getGender() const
{
    return m_gender;
}

string Poisson::getType() 
{
    return "Poisson";
}

int Poisson::getVie() const
{
    return m_vie;
}

void Poisson::setGender(string gender)
{
    if ((gender=="masculin")|(gender=="feminin"))
    {
        m_gender = gender;
    }
    else
    {
        cout << "Veuillez afficher un sexe valide pour le poisson" << endl;
        exit(0);
    }
}

void Poisson::isBit()
{
    m_vie = m_vie - 3;
    if (m_vie <= 0);
}

void Poisson::growOld()
{
    m_age = m_age + 1;
}

void Poisson::setAge(int age)
{
    m_age = age;
}

int Poisson::getAge() const
{
    return (m_age);
}
