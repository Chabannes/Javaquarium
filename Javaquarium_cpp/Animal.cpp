#include "Animal.h"


#include <iostream>
#include <string>
#include <vector>


Animal::Animal() 
{}

Animal::~Animal() 
{}

int Animal::getVie() const
{
    return m_vie;
}

string Animal::getType()
{
    return "Animal";
}

void Animal::updateVie(int dVie)
{
    m_vie = m_vie + dVie;
    if (m_vie >10)
    {
        m_vie = 10;
    }
}
