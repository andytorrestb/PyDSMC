import numpy as np

class Particle:
    def __init__(self, position, velocity):
        self.position = np.array(position)
        self.velocity = np.array(velocity)

    def move(self, delta_t):
        self.position += self.velocity * delta_t
