import numpy as np

# Define a lambda function that calculates the final velocity for one body.
calculate_final_velocity = lambda m1, v1, m2, v2: (
    ((m1 - m2) / (m1 + m2)) * v1 + (2 * m2 / (m1 + m2)) * v2
)

def elastic_collision(masses, velocities):
    """
    Calculate final velocities of two objects involved in an elastic collision.

    Args:
        masses (list): A list of masses for both objects.
        velocities (list): A list of initial velocities for both objects.

    Returns:
        list: A list containing the final velocities for both objects.
    """
    # Use map to apply the calculate_final_velocity lambda function to pairs of masses and velocities.
    # The lambda function takes one mass and velocity for each object and calculates the final velocity for that object.
    # The reversed() function is used to iterate in reverse order, as the second object's parameters come first in the formula.
    final_velocities = list(map(calculate_final_velocity, masses, velocities, reversed(masses), reversed(velocities)))
    return final_velocities

# Example usage:
masses = [1, 1]
velocities = [1, -1]

# Call the function to calculate final velocities.
final_velocities = elastic_collision(masses, velocities)

print(f"Final velocities: {final_velocities}")
