import unittest
import test_header
from src.dsmc.DSMC import DSMC

class TestDSMC(unittest.TestCase):
    def test_particle_initialization(self):
        num_particles = 100
        domain_size = 1.0
        temperature = 300
        dt = 0.005
        num_cells = 5

        dsmc_simulation = DSMC(num_particles, domain_size, temperature, dt, num_cells)
        self.assertEqual(len(dsmc_simulation.particles), num_particles)

    # Add more tests as necessary

if __name__ == '__main__':
    unittest.main()
