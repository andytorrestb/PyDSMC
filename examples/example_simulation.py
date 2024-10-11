import sys, os
# Add the src folder to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import numpy as np

from dsmc.particle import Particle
from dsmc.simulation import run_simulation
from dsmc.constants import NUM_PARTICLES, DOMAIN_SIZE, TEMPERATURE, PARTICLE_MASS, BOLTZMANN_CONSTANT

def initialize_particles(num_particles):
    particles = []
    for _ in range(num_particles):
        position = np.random.rand(2) * DOMAIN_SIZE
        velocity = np.random.randn(2) * np.sqrt(BOLTZMANN_CONSTANT * TEMPERATURE / PARTICLE_MASS)
        particles.append(Particle(position, velocity))
    return particles

if __name__ == "__main__":
    particles = initialize_particles(NUM_PARTICLES)
    run_simulation(particles, 1000, 0.001)
