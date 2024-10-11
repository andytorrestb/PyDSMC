import numpy as np

class Particle:
    """Represents a particle in the DSMC simulation.

    Attributes:
        position (np.ndarray of shape (2,)): The position of the particle in the 2D domain.
        velocity (np.ndarray of shape (2,)): The velocity of the particle.
    """

    def __init__(self, position, velocity):
        """Initializes a particle with a given position and velocity.

        Args:
            position (list or np.ndarray of shape (2,)): The initial position of the particle.
            velocity (list or np.ndarray of shape (2,)): The initial velocity of the particle.
        """
        self.position = np.array(position)
        self.velocity = np.array(velocity)
