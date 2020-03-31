#include "Herbivore.h"


#include <iostream>
#include <string>
#include <vector>



Herbivore::Herbivore()
{}

Herbivore::Herbivore(string name) : m_name(name)
{}

Herbivore::~Herbivore()
{}

string Herbivore::getType()
{
   return "herbivore";
}

string Herbivore::getName() 
{
   return m_name;
}

void Herbivore::eat(string victim)
{
   if (victim == "none")
   {
      cout << "Le poisson " << m_name << " a mangé." << endl;
   }

   else 
   {
      cout << "Le poisson " << m_name << " a mangé en entier l'algue" << victim << endl;
   }
   m_vie = m_vie + 2;
   if (m_vie > 10)
   {
      m_vie = 10;
   }
}
