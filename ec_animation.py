#This code animates 1-D elastic collision (RUN in VS code does not work on Jupyter/online platforms).
# Import the Pygame library and system module
import pygame
import sys

# Initialize the Pygame library
pygame.init()

# Constants for the screen dimensions and colors
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (255, 255, 255)
BODY_COLOR = (0, 0, 255)
BODY_RADIUS = 20

# Create the Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("1-D Elastic Collision")
clock = pygame.time.Clock()

# Define a class to represent particles
class Particle:
    def __init__(self, mass, x, velocity):
        """Initialize a particle with given mass, initial position, and initial velocity.

        Args:
            mass (float): The mass of the particle.
            x (float): The initial x-coordinate of the particle.
            velocity (float): The initial velocity of the particle.
        """
        self.mass = mass
        self.x = x
        self.velocity = velocity

    def update(self):
        """Update the particle's position based on its velocity."""
        self.x += self.velocity

    def draw(self):
        """Draw the particle on the screen using Pygame."""
        pygame.draw.circle(screen, BODY_COLOR, (int(self.x), HEIGHT // 2), BODY_RADIUS)

# Example usage:

# Define the properties of the first particle
mass1 = 1
x1 = WIDTH * 0.25
velocity1 = 1  # Initial velocity

# Create the first particle
particle1 = Particle(mass1, x1, velocity1)

# Define the properties of the second particle
mass2 = 10000
x2 = WIDTH * 0.75
velocity2 = 0  # Initial velocity

# Create the second particle
particle2 = Particle(mass2, x2, velocity2)

# Function to calculate the final velocities after a collision using map and lambda
def calculate_final_velocities(particle1, particle2):
    """Calculate final velocities after an elastic collision between two particles using mathematical formulas.

    Args:
        particle1 (Particle): The first particle involved in the collision.
        particle2 (Particle): The second particle involved in the collision.

    Returns:
        tuple: A tuple containing the final velocities of both particles after the collision.
    """
    delta_m = particle1.mass - particle2.mass
    total_m = particle1.mass + particle2.mass
    
    # Calculate final velocities using the 1-D elastic collision formulas
    v1_final = particle1.velocity - (2 * particle2.mass / total_m) * (particle1.velocity - particle2.velocity)
    v2_final = particle2.velocity - (2 * particle1.mass / total_m) * (particle2.velocity - particle1.velocity)
    
    return v1_final, v2_final

# Main animation loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen with the background color
    screen.fill(BACKGROUND_COLOR)

    # Update particle positions
    particle1.update()
    particle2.update()

    # Check for collision (when the particles are close enough)
    if abs(particle1.x - particle2.x) <= 2 * BODY_RADIUS:
        # Calculate new velocities after collision using calculate_final_velocities function with map and lambda
        particle1.velocity, particle2.velocity = map(lambda v: round(v, 2), calculate_final_velocities(particle1, particle2))

    # Draw particles on the screen
    particle1.draw()
    particle2.draw()

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)

# Quit Pygame and exit the program
pygame.quit()
sys.exit()

