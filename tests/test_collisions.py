import unittest
import numpy as np
import test_header
from dsmc.particle import Particle
from dsmc.collisions import handle_collisions

class TestCollisions(unittest.TestCase):

    def test_collision_velocities_exchange(self):
        """Test that after a collision, the velocities of two particles are exchanged."""
        # Initialize two particles with known velocities
        p1 = Particle([0.5, 0.5], [1.0, 0.0])  # Particle 1 with velocity [1.0, 0.0]
        p2 = Particle([0.5, 0.5], [-1.0, 0.0]) # Particle 2 with velocity [-1.0, 0.0]
        
        # Create a list of particles and call handle_collisions
        particles = [p1, p2]
        handle_collisions(particles)
        
        # After collision, velocities should be exchanged
        self.assertTrue(np.array_equal(p1.velocity, [-1.0, 0.0]), "Particle 1 velocity did not exchange correctly")
        self.assertTrue(np.array_equal(p2.velocity, [1.0, 0.0]), "Particle 2 velocity did not exchange correctly")

    def test_multiple_collisions(self):
        """Test multiple particle collisions to check random pair selection."""
        # Initialize particles with different velocities
        p1 = Particle([0.1, 0.1], [1.0, 0.0])
        p2 = Particle([0.2, 0.2], [0.0, 1.0])
        p3 = Particle([0.3, 0.3], [-1.0, 0.0])
        p4 = Particle([0.4, 0.4], [0.0, -1.0])
        
        particles = [p1, p2, p3, p4]
        
        # Call handle_collisions multiple times to simulate multiple collision events
        for _ in range(10):
            handle_collisions(particles)
        
        # Ensure the particles' velocities are valid (we don't know exact outcomes due to randomness)
        for p in particles:
            self.assertEqual(len(p.velocity), 2, "Particle velocity must be a 2D vector")
            self.assertGreater(np.linalg.norm(p.velocity), 0, "Particle velocity should not be zero after collisions")

    def test_no_collision_changes_positions(self):
        """Test that collisions only change velocities, not particle positions."""
        p1 = Particle([0.5, 0.5], [1.0, 0.0])
        p2 = Particle([0.5, 0.5], [-1.0, 0.0])
        
        initial_positions = [p.position.copy() for p in [p1, p2]]
        
        # Apply collisions
        particles = [p1, p2]
        handle_collisions(particles)
        
        # Ensure positions remain unchanged
        for i, p in enumerate(particles):
            self.assertTrue(np.array_equal(p.position, initial_positions[i]), "Particle positions should not change after collisions")

# Run the unit tests
if __name__ == '__main__':
    unittest.main()
