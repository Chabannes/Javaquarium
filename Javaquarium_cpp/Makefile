Exe: Aquarium.o Poisson.o Algue.o main.o Herbivore.o Carnivore.o Animal.o
	g++ -o Exe main.o Poisson.o Aquarium.o Algue.o Herbivore.o Carnivore.o Animal.o

Aquarium.o: Aquarium.cpp
	g++ -c Aquarium.cpp

Animal.o: Animal.cpp
	g++ -c Animal.cpp

Poisson.o: Poisson.cpp
	g++ -c Poisson.cpp

Herbivore.o: Herbivore.cpp
	g++ -c Herbivore.cpp

Carnivore.o: Carnivore.cpp
	g++ -c Carnivore.cpp

main.o: main.cpp
	g++ -c main.cpp

clean: 
	rm *.o Exe