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
  v1_final = ((m1 - m2) / (m1 + m2))*v1+(2*m2/(m1+m2))*v2

  # Calculate the final velocity of the second body.
  v2_final = ((2*m1) / (m1 + m2))*v1+((m2-m1)/(m1+m2))*v2

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

  # Calculate the x- and y-components of the initial velocities.
  vx1, vy1 = velocities[0] * np.cos(angles[0]), velocities[0] * np.sin(angles[0])
  vx2, vy2 = velocities[1] * np.cos(angles[1]), velocities[1] * np.sin(angles[1])

  # Calculate the final x- and y-components of the velocities.
  vx1_final, vx2_final = conserve_momentum(masses[0], vx1, masses[1], vx2)
  vy1_final, vy2_final = conserve_momentum(masses[0], vy1, masses[1], vy2)

  # Calculate the final velocities.
  velocities_final = [
      np.sqrt(vx1_final**2 + vy1_final**2),
      np.sqrt(vx2_final**2 + vy2_final**2)
  ]

  # Calculate the final angles.
  angles_final = [
      np.arctan2(vy1_final, vx1_final),
      np.arctan2(vy2_final, vx2_final)
  ]

  # Convert the angles back to degrees.
  angles_final = np.degrees(angles_final)

  return velocities_final, angles_final

# Unit Test:

masses = [1, 1]
velocities = [1,0]
angles = [0, 0]

velocities_final, angles_final = elastic_collision(masses, velocities, angles)

print(f"Final velocities: {velocities_final}")
print(f"Final angles: {angles_final}")
