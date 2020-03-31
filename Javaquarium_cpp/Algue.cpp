#include "Algue.h"


#include <iostream>
#include <string>
#include <vector>


Algue::Algue() 
{}

Algue::Algue(int num) : m_num(num)
{}

Algue::~Algue()
{}

int Algue::getVie() const
{
    return m_vie;
}

void Algue::isBit()
{
    m_vie = m_vie - 7;
}

string Algue::getType()
{
    return "Algue";
}

int Algue::getNum() const
{
    return m_num;
}