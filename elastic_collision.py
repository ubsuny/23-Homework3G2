#I am just curious, is this code only for calculating final velovities? If I understand it correctly. I dont see any momentum or KE. Or is this incomplete?
Thank you
import numpy as np

def conserve_momentum(m1, v1, m2, v2):
    """Calculates the final velocities of two bodies in an elastic collision, given their masses and initial velocities.

    Args:
        m1: Mass of the first body.
        v1: Initial velocity of the first body.
        m2: Mass of the second body.
        v2: Initial velocity of the second body.

    Returns:
        A tuple of two floats, representing the final velocities of the first and second bodies, respectively.
    """

    # Calculate the final velocity of the first body.
    v1_final = ((m1 - m2) / (m1 + m2)) * v1 + (2 * m2 / (m1 + m2)) * v2

    # Calculate the final velocity of the second body.
    v2_final = (2 * m1 / (m1 + m2)) * v1 + ((m2 - m1) / (m1 + m2)) * v2

    return v1_final, v2_final

def elastic_collision(masses, velocities, angles):
    """Calculates the final velocities of two bodies in an elastic collision, given their masses, initial velocities, and angles.

    Args:
        masses: A list or array of the masses of the two bodies.
        velocities: A list or array of the initial velocities of the two bodies.
        angles: A list or array of the angles of the initial velocities of the two bodies, in degrees.

    Returns:
        A tuple of two lists or arrays, representing the final velocities of the two bodies, respectively.
    """

    # Convert the angles to radians.
    angles = np.radians(angles)

    # Calculate the x- and y-components of the initial velocities using map.
    initial_vx = list(map(lambda v, angle: v * np.cos(angle), velocities, angles))
    initial_vy = list(map(lambda v, angle: v * np.sin(angle), velocities, angles))

    # Calculate the final x- and y-components of the velocities using conserve_momentum.
    final_vx = conserve_momentum(masses[0], initial_vx[0], masses[1], initial_vx[1])
    final_vy = conserve_momentum(masses[0], initial_vy[0], masses[1], initial_vy[1])

    # Calculate the final velocities using list comprehension.
    velocities_final = [np.sqrt(vx ** 2 + vy ** 2) for vx, vy in zip(final_vx, final_vy)]

    # Calculate the final angles using list comprehension.
    angles_final = [np.arctan2(vy, vx) for vx, vy in zip(final_vx, final_vy)]

    # Convert the angles back to degrees.
    angles_final = np.degrees(angles_final)

    return velocities_final, angles_final

# Example usage:
masses = [1, 1]
velocities = [0, -1]
angles = [0, 0]

velocities_final, angles_final = elastic_collision(masses, velocities, angles)

print(f"Final velocities: {velocities_final}")
print(f"Final angles: {angles_final}")
