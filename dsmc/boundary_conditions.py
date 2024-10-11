def apply_boundary_conditions(particles):
    """Apply boundary conditions to reflect particles at the domain boundaries."""
    for particle in particles:
        # Reflect the particle if it exceeds the boundaries in x direction
        if particle.position[0] <= 0 or particle.position[0] >= 1.0:
            particle.velocity[0] *= -1  # Reflect x-velocity

        # Reflect the particle if it exceeds the boundaries in y direction
        if particle.position[1] <= 0 or particle.position[1] >= 1.0:
            particle.velocity[1] *= -1  # Reflect y-velocity

