import unittest
import math
import numpy as np
import elastic_collision
class Particle:
    def __init__(self, mass, velocity):
        self.mass = mass
        self.velocity = velocity

    def momentum(self):
        """Calculate the momentum of the particle."""
        return self.mass * self.velocity

    def kinetic_energy(self):
        """Calculate the kinetic energy of the particle."""
        return 0.5 * self.mass * self.velocity ** 2
class ParticleTest(unittest.TestCase):

    def test_momentum(self):
        """Test the momentum calculation."""
        masses = [1, 1]
        velocities = [1, -1]
        # Calculate the expected momentum
        expected_momentum = 0

        # Calculate the actual momentum
        v = elastic_collision.elastic_collision(masses,velocities)
        v1=v[0]
        v2=v[1]
        m1=masses[0]
        m2=masses[1]
        actual_momentum=v1*m1+v2*m2

        # Assert that the expected and actual momenta are equal
        p_conserved=self.assertEqual(expected_momentum, actual_momentum)
        if p_conserved==None:
            print('momentum is conserved')
        else:
            print('error, momentum is not conserved')
        return p_conserved

    def test_kinetic_energy(self):
        """Test the kinetic energy calculation."""

        # Create a particle with mass 1 and velocity 1
        particle = Particle(1, 1)

        # Calculate the expected kinetic energy
        expected_kinetic_energy = 0.5

        # Calculate the actual kinetic energy
        actual_kinetic_energy = particle.kinetic_energy()

        # Assert that the expected and actual kinetic energies are equal
        #self.assertEqual(expected_kinetic_energy, actual_kinetic_energy)
        print(self.assertEqual(expected_kinetic_energy, actual_kinetic_energy))

if __name__ == '__main__':
    unittest.main()
