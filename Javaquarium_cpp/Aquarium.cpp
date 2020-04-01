#include "Aquarium.h"
#include "Carnivore.h"
#include "Herbivore.h"


#include <iostream>
#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <cstdlib>


Aquarium::Aquarium() 
{}


Aquarium::~Aquarium()
{}


void Aquarium::add_poisson(Poisson &poisson)
{
    m_poissons.push_back(&poisson);
}

int Aquarium::isAvailable(string poissonName) const
{
    int count = 1;

    for (int i = 0; i < m_poissons.size(); i++)
    {
        if (m_poissons[i]->getName() == poissonName)
        {
            count = 0;
        }
    }

    return count;

}

int Aquarium::getNumberHerbivore() const
{
    int count = 0;
    for (int i=0; i < m_poissons.size(); i++)
    {
        if (m_poissons[i]->getType() == "herbivore")
        {
            count++;
        }
    }
    return count;
}

int Aquarium::getNumberCarnivore() const
{
    int count = 0;
    for (int i=0; i < m_poissons.size(); i++)
    {
        if (m_poissons[i]->getType() == "carnivore")
        {
            count++;
        }
    }
    return count;
}

int Aquarium::getNumberAlgue() const
{
    return m_algues.size();
}




void Aquarium::add_algue(int nb_algue)
{
    for (int i = 0; i < nb_algue; i++)
    {
        m_algues.push_back(new Algue(m_algues.size()+1));        
    }
}


void Aquarium::add_herbivore(int nb_poissons)
{
    int added_poissons = 0;
    int count = 0;

    do{
        if (isAvailable(m_existingHerbivore[count]) == 1)
        {
            int age;
            string gender;
            int gender_ind;
            age = rand() % (4 + 1) + 1;
            gender_ind = rand() % (1 + 1) + 0;

            if (gender_ind >0)
            {
                gender = "masculin";
            }
            else
            {
                gender = "feminin";
            }

            m_poissons.push_back(new Herbivore(m_existingHerbivore[count])); 
            m_poissons.back()->setAge(age);
            m_poissons.back()->setGender(gender);
            added_poissons++;
        }
    count++;
    }while ((added_poissons < nb_poissons)|(count > m_poissons.size()));
}

void Aquarium::born_herbivore()
{
    int count = 0;
    int borned = 0;
    do{
        if (isAvailable(m_existingHerbivore[count]) == 1)
        {
            int age;
            string gender;
            int gender_ind;
            age = 0;
            gender_ind = rand() % (1 + 1) + 0;

            if (gender_ind >0)
            {
                gender = "masculin";
            }
            else
            {
                gender = "feminin";
            }

            m_poissons.push_back(new Herbivore(m_existingHerbivore[count])); 
            m_poissons.back()->setAge(age);
            m_poissons.back()->setGender(gender);
            cout << "Le petit herbivore " << m_poissons.back()->getName() << " est né " << endl;
            borned = 1;
            break;
        }
    count++;
    }while(count < m_existingHerbivore.size());

    if (borned == 0)
    {
        cout << "Naissance impossible: plus de place pour les herbivores "  << endl;
    }
}

void Aquarium::add_carnivore(int nb_poissons)
{
    int added_poissons = 0;
    int count = 0;

    do{
        if (isAvailable(m_existingCarnivore[count]) == 1)
        {
            int age;
            string gender;
            int gender_ind;
            age = rand() % (4 + 1) + 1;
            gender_ind = rand() % (1 + 1) + 0;

            if (gender_ind >0)
            {
                gender = "masculin";
            }
            else
            {
                gender = "feminin";
            }

            m_poissons.push_back(new Carnivore(m_existingCarnivore[count])); 
            m_poissons.back()->setAge(age);
            m_poissons.back()->setGender(gender);
            added_poissons++;
        }
    count++;
    }while ((added_poissons < nb_poissons)|(count > m_poissons.size()));
}

void Aquarium::born_carnivore()
{
    int count = 0;
    int borned = 0;
    do{
        if (isAvailable(m_existingCarnivore[count]) == 1)
        {
            int age;
            string gender;
            int gender_ind;
            age = 0;
            gender_ind = rand() % (1 + 1) + 0;

            if (gender_ind >0)
            {
                gender = "masculin";
            }
            else
            {
                gender = "feminin";
            }

            m_poissons.push_back(new Carnivore(m_existingCarnivore[count])); 
            m_poissons.back()->setAge(age);
            m_poissons.back()->setGender(gender);
            cout << "Le petit carnivore " << m_poissons.back()->getName() << " est né " << endl;
            borned = 1;
            break;
        }
    count++;
    }while(count < m_existingCarnivore.size());

    if (borned == 0)
    {
        cout << "Naissance impossible: plus de place pour les carnivores " << endl;
    }
}



void Aquarium::print() const
{
    cout << "\nL'aquarium contient : \n\n";

    for (vector<Poisson>::size_type i = 0; i != m_poissons.size(); i++) 
    {
        cout << "- " << m_poissons[i]->getName() << " - "<< m_poissons[i]->getType() << " - " << m_poissons[i]->getGender() << " - vie : " << m_poissons[i]->getVie() << "/10 ";
        cout << "- age : " << m_poissons[i]->getAge() << endl; 
    }
    cout << "- ";
    for (vector<Algue>::size_type i = 0; i != m_algues.size(); i++) 
    {
        cout << "Algue" << m_algues[i]->getNum() << " " << m_algues[i]->getVie() << "/10  ";
    }
    cout << "\n\n- Repartition des animaux : " << getNumberCarnivore() <<" carnivore(s), " << getNumberHerbivore() << " herbivore(s), " << getNumberAlgue() << " algue(s)" << endl;
}


void Aquarium::poissonEat(Poisson &poisson)
{
    string type;
    type = poisson.getType();

    if (type == "herbivore")
    {
        if (m_algues.size() > 0)
        {
            string victim = "none";
            for (int i = 0; i < m_algues.size(); i++)
            {
            m_algues[i]->isBit();
                if (m_algues[i]->getVie() <= 0)
                {
                    victim = to_string(m_algues[i]->getNum());
                    m_algues.erase(m_algues.begin()+i);
                }
            poisson.eat(victim);
            break; 
            }
        }

        else 
        {
            cout << "Le poisson " << poisson.getName() << " ne peut pas manger." << endl;
        }
    }

    if (type == "carnivore")
    {
        if (m_poissons.size() > 1)
        {
            for (int i=0; i < m_poissons.size(); i++)
            {
                if (m_poissons[i]->getType() != poisson.getType())  // le poisson ne peut pas se manger lui même
                {
                    m_poissons[i]->isBit();
                    string victim = "none";
                    if (m_poissons[i]->getVie() <= 0)
                    {
                        victim = m_poissons[i]->getName();
                        m_deadPoissons.push_back(m_poissons[i]);
                        m_poissons.erase(m_poissons.begin()+i);
                    }
                    poisson.eat(victim);
                    break;
                }
            }
        }

        else 
        {
            cout << "Le poisson " << poisson.getName() << " ne peut pas manger." << endl;
        }
     }
}

void Aquarium::hunger()
{
    for (int i = 0; i < m_poissons.size(); i++)
    {
        m_poissons[i]->updateVie(-1);
        if (m_poissons[i]->getVie() <= 0)
        {
            m_deadPoissons.push_back(m_poissons[i]);
            m_poissons.erase(m_poissons.begin()+i);
        }
    }

    cout << "La faim se fait ressentir ... et fait perdre un point de vie à tout les poissons." << endl;
}

void Aquarium::poissonHunt(int thr_hunger)
{
    for (int i=0; i < m_poissons.size(); i++)
    {
        if (m_poissons[i]->getVie() <=thr_hunger)
        {
            poissonEat(*m_poissons[i]);
        }
    }
}

void Aquarium::afficherDeadPoissons()
{

    for (int i = 0; i < m_poissons.size(); i++)
    {
        if (m_poissons[i]->getVie() <= 0)
        {
            m_deadPoissons.push_back(m_poissons[i]);
            m_poissons.erase(m_poissons.begin()+i);
        }
    }

    if (m_deadPoissons.size() == 0)
    {
        cout << "Aucun poisson n'est mort dans l'aquarium" << endl;
    }

    else
    {
        cout << "\n- Liste des poissons mort depuis le début :";
        for (int i = 0; i < m_deadPoissons.size(); i++)
        {
            cout << " " << m_deadPoissons[i]->getName();
        }
    }

    cout << endl;    
}

void Aquarium::alguesGrowBack()
{
    for (int i = 0; i < m_algues.size(); i++)
    {
        m_algues[i]->updateVie(1);   
    }
}

void Aquarium::poissonsGrowOld()
{
    int deads = 0;
    cout << "\n- Les poissons mort de vieillesse à ce tour : " ;
    for (int i = 0; i < m_poissons.size(); i++)
    {
        m_poissons[i]->growOld();
        if (m_poissons[i]->getAge() > 10)
        {
            deads++;
            cout << m_poissons[i]->getName() << " ";
            m_deadPoissons.push_back(m_poissons[i]);
            m_poissons.erase(m_poissons.begin()+i);
        }
    }  
    if (deads == 0)
    {
        cout << "Aucun.";
    }
    cout << endl;
}

int Aquarium::findCouple(Poisson &poisson) const
{
    string type = poisson.getType();
    string name = poisson.getName();
    string gender = poisson.getGender();
    int age = poisson.getAge();
    int value = -1;
    for (int i =0; i < m_reproductiblePoissons.size(); i++)
    {
        if((m_reproductiblePoissons[i]->getType() == type)&(m_reproductiblePoissons[i]->getName() != name)&(m_reproductiblePoissons[i]->getGender() != gender)&(age >2)&(m_reproductiblePoissons[i]->getAge()>2))
        {

            value = i;
            break;
        }
    }
    return value;
}

void Aquarium::poissonReproduction()
{
    if (m_nb_tour > 2)
        {
        m_reproductiblePoissons.clear();
        int ind = 0;
        for (int i =0; i < m_poissons.size(); i++)
        {
            if (m_poissons[i]->getVie()>7)
            {
            m_reproductiblePoissons.push_back(m_poissons[i]);
            }
        }
        int i = 0;
        if (m_reproductiblePoissons.size() > 0)
            {
            do
            {
                ind = findCouple(*m_reproductiblePoissons[i]);

                if (ind > -1)
                {

                    if (m_reproductiblePoissons[i]->getGender() == "feminin")
                    {
                        m_reproductiblePoissons.erase(m_reproductiblePoissons.begin()+i);
                    }
                    else
                    {
                        m_reproductiblePoissons.erase(m_reproductiblePoissons.begin()+ind);
                    }

                    if (m_reproductiblePoissons[i]->getType() == "herbivore")
                    {
                        born_herbivore();
                    }
                    if (m_reproductiblePoissons[i]->getType() == "carnivore")
                    {
                        born_carnivore();
                    }
                }
            i=i+1;
            }while(i+1 < m_reproductiblePoissons.size());
        }
    }
}


void Aquarium::algueReproduction()
{
    if (m_nb_tour > 1)
    {
        if (m_algues.size() > 50)
        {
            cout << "- Il n'y a déjà des algues partout, prolifération impossible." << endl;
        }

        else
        {
            for (int i = 0; i < m_algues.size();i++)
            {
                if (m_algues[i]->getVie() > 9)
                {
                    m_algues[i]->updateVie(-5);
                    m_algues.push_back(new Algue(m_algues.size()+1));
                    m_algues.back()->updateVie(-5);
                    m_algues.push_back(new Algue(m_algues.size()+1));
                    m_algues.back()->updateVie(-5);
                }
            }
        }
    }
}


void Aquarium::shuffleAnimalsOrder()
{
    auto rng1 = default_random_engine {};
    shuffle(begin(m_poissons), end(m_poissons), rng1);    

    auto rng2 = default_random_engine {};
    shuffle(begin(m_algues), end(m_algues), rng2);  

    auto rng3 = default_random_engine {};
    shuffle(begin(m_existingHerbivore), end(m_existingHerbivore), rng3);

    auto rng4 = default_random_engine {};
    shuffle(begin(m_existingCarnivore), end(m_existingCarnivore), rng4);   
}

void Aquarium::next_tour()
{
    cout << "\n\n---------------- TOUR NUMERO " << m_nb_tour + 1 << " ----------------\n\n";

    shuffleAnimalsOrder();
    hunger();
    poissonHunt(7);
    print();
    afficherDeadPoissons();
    alguesGrowBack();
    poissonsGrowOld();
    poissonReproduction();
    algueReproduction();
    m_nb_tour++;
}


void Aquarium::simuler(int nb_tour)
{
    for (int i = 0; i < nb_tour; i++)
    {
        next_tour();
        cout << endl;
    }
}
