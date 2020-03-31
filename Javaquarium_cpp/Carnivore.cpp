#include "Carnivore.h"


#include <iostream>
#include <string>
#include <vector>



Carnivore::Carnivore()
{}

Carnivore::Carnivore(string name) : m_name(name)
{}

Carnivore::~Carnivore()
{}

string Carnivore::getType()
{
   return "carnivore";
}

string Carnivore::getName()
{
   return m_name;
}

void Carnivore::eat(string victim)
{
   if (victim == "none")
   {
      cout <<"Le poisson " << m_name << " a mangé." << endl;
   }

   else
   {
      cout <<"Le poisson " << m_name << " a mangé en entier le poisson " << victim << endl;
   }
   m_vie = m_vie + 5;
   if (m_vie > 10)
   {
      m_vie = 10;
   }
}
