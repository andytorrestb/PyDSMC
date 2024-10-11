__author__ = "Andres Torres-Figueroa"
__status__ = "Dev"

import numpy as np
from src.dsmc.Grid import Grid
from src.dsmc.Particle import Particle

class DSMC:
    """Direct Simulation Monte Carlo (DSMC) class to manage particle motion and collisions.

    Attributes:
        num_particles (int): Number of particles in the simulation.
        domain_size (float): Size of the simulation domain.
        particle_mass (float): Mass of each particle.
        temperature (float): The temperature of the system (K).
        mean_velocity (float): The mean velocity calculated from temperature.
        dt (float): Time step for the simulation.
        particles (list of Particle): List of particle objects.
        grid (Grid): The grid used to sort particles for collisions.
    """

    def __init__(self, num_particles, domain_size, temperature, dt, num_cells):
        """Initializes the DSMC simulation with given parameters.

        Args:
            num_particles (int): Number of particles.
            domain_size (float): Size of the simulation domain.
            temperature (float): Temperature of the system in Kelvin.
            dt (float): Time step for simulation.
            num_cells (int): Number of grid cells along each axis.
        """
        self.num_particles = num_particles
        self.domain_size = domain_size
        self.particle_mass = 1.0  # Assume unit mass
        self.temperature = temperature
        self.mean_velocity = np.sqrt(2 * 1.38e-23 * self.temperature / self.particle_mass)
        self.dt = dt
        self.particles = self.initialize_particles()
        self.grid = Grid(domain_size, num_cells)

    def initialize_particles(self):
        """Initializes particle positions and velocities using Maxwell-Boltzmann distribution.

        Returns:
            list of Particle: List of Particle objects with random positions and velocities.
        """
        positions = np.random.rand(self.num_particles, 2) * self.domain_size
        velocities = np.random.normal(5, self.mean_velocity, (self.num_particles, 2))  # Shape (num_particles, 2)
        return [Particle(pos, vel) for pos, vel in zip(positions, velocities)]

    def apply_boundary_conditions(self):
        """Applies reflective boundary conditions to particles."""
        for particle in self.particles:
            for i in range(2):
                if particle.position[i] < 0:
                    particle.velocity[i] *= -1
                    particle.position[i] = 0
                elif particle.position[i] > self.domain_size:
                    particle.velocity[i] *= -1
                    particle.position[i] = self.domain_size

    def simulate_motion(self):
        """Updates particle positions based on their velocities."""
        for particle in self.particles:
            particle.position += particle.velocity * self.dt
        self.apply_boundary_conditions()

    def perform_collisions(self):
        """Performs particle collisions within the same cell."""
        for cell_row in self.grid.grid:
            for cell in cell_row:
                if len(cell) < 2:
                    continue
                num_collisions = len(cell) // 2
                for _ in range(num_collisions):
                    p1, p2 = np.random.choice(cell, size=2, replace=False)
                    self.collide(p1, p2)

    def collide(self, p1, p2):
        """Handles collisions between two particles.

        Args:
            p1 (int): Index of the first particle.
            p2 (int): Index of the second particle.
        """
        particle1 = self.particles[p1]
        particle2 = self.particles[p2]
        v_rel = particle1.velocity - particle2.velocity
        v_rel_mag = np.linalg.norm(v_rel)  # Scalar
        if v_rel_mag > 0:
            theta = np.random.uniform(0, 2 * np.pi)
            v_cm = (particle1.velocity + particle2.velocity) / 2  # Center of mass velocity
            v_rel_new = v_rel_mag * np.array([np.cos(theta), np.sin(theta)])  # Shape (2,)
            particle1.velocity = v_cm + v_rel_new / 2
            particle2.velocity = v_cm - v_rel_new / 2

    def run_simulation(self, num_steps):
        """Runs the DSMC simulation for a given number of time steps.

        Args:
            num_steps (int): Number of steps to simulate.
        """
        for step in range(num_steps):
            self.simulate_motion()
            self.grid.sort_particles(self.particles)
            self.perform_collisions()
