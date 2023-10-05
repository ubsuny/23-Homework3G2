# 1-D Elastic Collision

This code demonstrates how to calculate the final velocities of two objects involved in a one-dimensional elastic collision. It makes use of functional programming concepts such as lambda functions, lists, and the `map` function.

## Lambda Function

A lambda function `calculate_final_velocity` is defined to calculate the final velocity of one of the objects involved in the collision. The lambda function takes four arguments: `m1` (mass of the first object), `v1` (initial velocity of the first object), `m2` (mass of the second object), and `v2` (initial velocity of the second object). It uses the following formula for calculating the final velocity of the first object:

```python
((m1 - m2) / (m1 + m2)) * v1 + (2 * m2 / (m1 + m2)) * v2
```
This formula is based on the principles of conservation of momentum and kinetic energy in an elastic collision.

## elastic_collision Function

The `elastic_collision` function is the main function that calculates the final velocities of the two objects involved in the collision. It takes two lists as arguments:

- `masses`: A list containing the masses of both objects.
- `velocities`: A list containing the initial velocities of both objects.

Inside the function, the `map` function is used to apply the `calculate_final_velocity` lambda function to pairs of masses and velocities. The `reversed()` function is used to iterate in reverse order because the second object's parameters (mass and velocity) come first in the formula. The result is a list of final velocities for both objects.

## Example Usage

The code provides an example usage where:

- `masses` is set to [1, 1], indicating that both objects have the same mass.
- `velocities` is set to [1, -1], indicating that the first object is moving to the right with a velocity of 1 unit, and the second object is moving to the left with a velocity of -1 unit.

The `elastic_collision` function is called with these values, and the final velocities of both objects are calculated and printed to the console.

This code is a simple example of using functional programming concepts to solve a physics problem involving elastic collisions.

# 1-D Elastic Collision Animation

This code animates a one-dimensional elastic collision. It uses the Pygame library to create a simple visualization of two particles colliding elastically in a 1-D space.

## Pygame Initialization

The Pygame library is imported and initialized to create the animation window.

## Constants

- `WIDTH` and `HEIGHT` define the dimensions of the animation window.
- `BACKGROUND_COLOR` and `BODY_COLOR` define the background and particle colors, respectively.
- `BODY_RADIUS` specifies the radius of the particles.

## Pygame Window Setup

A Pygame window is created with the specified dimensions, and its title is set to "1-D Elastic Collision." A clock object is used to control the frame rate.

## Particle Class

A `Particle` class is defined to represent the particles involved in the collision. Each particle is initialized with mass, initial position (`x`), and initial velocity (`velocity`). The class has methods to update and draw the particle on the screen.

## Example Usage

Two particles (`particle1` and `particle2`) are created with different properties, including mass, initial position, and initial velocity.

## `calculate_final_velocities` Function

A function named `calculate_final_velocities` is defined to calculate the final velocities of two particles after an elastic collision. It takes two `Particle` objects as arguments and returns a tuple containing the final velocities for both particles. The function uses the 1-D elastic collision formulas to calculate the final velocities.

## Main Animation Loop

The main animation loop runs until the user closes the window. Inside the loop:

- Event handling allows the user to quit the program by closing the window.
- The screen is cleared with the background color.
- Particle positions are updated based on their velocities.
- A collision check is performed, and if the particles are close enough, their velocities are updated using the `calculate_final_velocities` function.
- The particles are drawn on the screen.
- The display is updated.
- The frame rate is controlled to 60 frames per second.

## Quitting the Program

Upon quitting the Pygame window, Pygame is quit, and the program exits.

This code demonstrates a basic simulation of an elastic collision in a 1-D space using Pygame and physics principles.


