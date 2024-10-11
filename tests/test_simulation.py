import unittest
import numpy as np
import test_header
from dsmc.particle import Particle
from dsmc.simulation import run_simulation
from dsmc.constants import NUM_PARTICLES, DOMAIN_SIZE, DELTA_T
from dsmc.boundary_conditions import apply_boundary_conditions
from dsmc.collisions import handle_collisions


class TestSimulation(unittest.TestCase):

    def test_simulation_initialization(self):
        """Test that particles are initialized and handled correctly in the simulation."""
        particles = self._initialize_test_particles(5)

        # Check that the correct number of particles are initialized
        self.assertEqual(len(particles), 5, "Incorrect number of particles initialized")

        # Check that the particles have non-zero velocities
        for particle in particles:
            self.assertGreater(np.linalg.norm(particle.velocity), 0, "Particle velocity should be non-zero")

    def test_particle_movement_in_simulation(self):
        """Test that particles move correctly over a few time steps."""
        particles = self._initialize_test_particles(2)

        initial_positions = [p.position.copy() for p in particles]

        # Run the simulation for 1 time step
        run_simulation(particles, 1, DELTA_T)

        # Check that each particle moved from its initial position
        for i, particle in enumerate(particles):
            self.assertFalse(np.array_equal(particle.position, initial_positions[i]), "Particle did not move correctly")

    def test_particle_boundary_conditions(self):
        """Test that boundary conditions are applied correctly (particles should reflect off boundaries)."""
        # Initialize a particle near the boundary with a velocity that will make it cross the boundary
        particles = [Particle([0.999, 0.999], [1.0, 1.0])]  # Particle should cross the upper boundary

        # Apply boundary conditions manually to ensure the reflection
        apply_boundary_conditions(particles)

        # Run the simulation to trigger boundary condition reflection
        run_simulation(particles, 1, DELTA_T)

        # Check if the velocity has been inverted (indicating a boundary collision)
        self.assertLess(particles[0].velocity[0], 0, "Particle did not reflect off the boundary correctly in x-direction")
        self.assertLess(particles[0].velocity[1], 0, "Particle did not reflect off the boundary correctly in y-direction")


    def test_particle_collisions(self):
        """Test that particle collisions change velocities appropriately."""
        # Initialize two particles that are close enough to collide
        p1 = Particle([0.5, 0.5], [1.0, 0.0])
        p2 = Particle([0.5, 0.5], [-1.0, 0.0])
        particles = [p1, p2]

        # Apply collision handling
        handle_collisions(particles)

        # Check that the velocities have changed
        self.assertTrue(np.any(p1.velocity != [1.0, 0.0]), "Particle 1 velocity did not change after collision")
        self.assertTrue(np.any(p2.velocity != [-1.0, 0.0]), "Particle 2 velocity did not change after collision")

    @staticmethod
    def _initialize_test_particles(num_particles):
        """Helper function to initialize a list of particles for testing."""
        particles = []
        for _ in range(num_particles):
            position = np.random.rand(2) * DOMAIN_SIZE
            velocity = np.random.randn(2)  # Random velocity
            particles.append(Particle(position, velocity))
        return particles


# Run the unit tests
if __name__ == '__main__':
    unittest.main()
