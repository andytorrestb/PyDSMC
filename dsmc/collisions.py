import random

def handle_collisions(particles):
    for i in range(len(particles) // 2):
        p1, p2 = random.sample(particles, 2)
        collide(p1, p2)

def collide(p1, p2):
    p1.velocity, p2.velocity = p2.velocity, p1.velocity
