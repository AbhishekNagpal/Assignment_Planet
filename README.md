# Assignment_Planet

Problem statement
Create a simulation program for life on a new planet, which eventually should reach an equilibrium. 
Following are the guidelines.

Make as many assumptions as you want and document them all.
The simulation should represent life on a planet.
The planet should be completely empty during start.
In equilibrium, the life should be at peace and sustainable.
Define maximum of 10 laws for simulation.
Following two laws are given.
 - Stronger eliminates the weak in second interaction.
 - A living organism eventually dies.
Write the program in any language you prefer.

Please note that there is no right or wrong answer. I want you to be honest, and please don’t discuss with 
anybody else. It’s not only a test of your programming skills but also a test of your thinking, attitude and
 general understanding of things around us. Use your imagination and creativity, and create a lasting impression
 
ASSUMPTIONS
1. There Exists some Initial Population in the planet to proceed life(Panspermia Theory). In this we taken 50.
2. Living organisms can move around the planet and interact with each other.
3. Living organisms can reproduce and create offspring.
4. Living organisms have a certain lifespan and die of old age.
5. Living organisms have a certain level of strength that determines their ability to survive.


Laws for the simulation:
1. Stronger eliminates the weak in second interaction.
2. A living organism eventually dies.
3. Living organisms can only reproduce if they have enough resources and are above a certain age(Age considered is 10).
4. Living organisms move randomly around the planet.
5. Living organisms consume resources when they move and interact.


Approach to Problem.
Initialize the planet with a fixed land area
Initialize a small population of simple, single-celled organisms
Set the simulation time steps

for each time step:
    for each living organism:
        Consume resources
        Attempt to reproduce
        Interact with other organisms
        Potentially die from natural causes or interactions
    Update the population and resource levels
    Check for ecosystem balance and equilibrium

if equilibrium is reached:
    Print the final state of the simulation
else:
    Continue the simulation for the remaining time steps
