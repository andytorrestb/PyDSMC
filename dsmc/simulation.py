from dsmc.particle import Particle
from dsmc.collisions import handle_collisions
from dsmc.boundary_conditions import apply_boundary_conditions
from dsmc.sampling import sample_macroscopic_properties

def run_simulation(particles, num_steps, delta_t):
    for step in range(num_steps):
        for particle in particles:
            particle.move(delta_t)
        handle_collisions(particles)
        apply_boundary_conditions(particles)
        if step % 10 == 0:
            sample_macroscopic_properties(particles)
