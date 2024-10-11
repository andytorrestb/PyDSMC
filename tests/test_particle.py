import unittest
import numpy as np
import test_header
from dsmc.particle import Particle

class TestParticle(unittest.TestCase):

    def test_particle_initialization(self):
        """Test that a particle is initialized with correct position and velocity."""
        position = [0.5, 0.5]
        velocity = [1.0, 1.0]
        particle = Particle(position, velocity)

        # Check if the position and velocity are initialized correctly
        self.assertTrue(np.array_equal(particle.position, position), "Particle position not initialized correctly")
        self.assertTrue(np.array_equal(particle.velocity, velocity), "Particle velocity not initialized correctly")

    def test_particle_movement(self):
        """Test that particle moves according to its velocity and time step."""
        # Initialize particle at position (0.0, 0.0) with velocity (1.0, 1.0)
        particle = Particle([0.0, 0.0], [1.0, 1.0])
        
        # Move the particle with a time step of 1.0
        delta_t = 1.0
        particle.move(delta_t)

        # After moving, the position should be updated to (1.0, 1.0)
        expected_position = [1.0, 1.0]
        self.assertTrue(np.array_equal(particle.position, expected_position), "Particle did not move correctly")

    def test_particle_zero_velocity(self):
        """Test that a particle with zero velocity doesn't move."""
        # Initialize particle at position (0.0, 0.0) with zero velocity
        particle = Particle([0.0, 0.0], [0.0, 0.0])

        # Move the particle with a time step of 1.0
        delta_t = 1.0
        particle.move(delta_t)

        # Since the velocity is zero, the position should remain unchanged
        expected_position = [0.0, 0.0]
        self.assertTrue(np.array_equal(particle.position, expected_position), "Particle with zero velocity moved unexpectedly")

    def test_particle_negative_velocity(self):
        """Test that a particle with negative velocity moves in the correct direction."""
        # Initialize particle at position (1.0, 1.0) with velocity (-1.0, -1.0)
        particle = Particle([1.0, 1.0], [-1.0, -1.0])

        # Move the particle with a time step of 1.0
        delta_t = 1.0
        particle.move(delta_t)

        # After moving, the position should be updated to (0.0, 0.0)
        expected_position = [0.0, 0.0]
        self.assertTrue(np.array_equal(particle.position, expected_position), "Particle with negative velocity did not move correctly")

# Run the unit tests
if __name__ == '__main__':
    unittest.main()
