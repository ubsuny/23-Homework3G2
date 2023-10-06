import unittest
import math
import numpy as np
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

        # Create a particle with mass 1 and velocity 1
        particle = Particle(1, 1)

        # Calculate the expected momentum
        expected_momentum = 1

        # Calculate the actual momentum
        actual_momentum = particle.momentum()

        # Assert that the expected and actual momenta are equal
        self.assertEqual(expected_momentum, actual_momentum)

    def test_kinetic_energy(self):
        """Test the kinetic energy calculation."""

        # Create a particle with mass 1 and velocity 1
        particle = Particle(1, 1)

        # Calculate the expected kinetic energy
        expected_kinetic_energy = 0.5

        # Calculate the actual kinetic energy
        actual_kinetic_energy = particle.kinetic_energy()

        # Assert that the expected and actual kinetic energies are equal
        self.assertEqual(expected_kinetic_energy, actual_kinetic_energy)

