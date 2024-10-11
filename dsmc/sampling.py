def sample_macroscopic_properties(particles):
    velocities = [p.velocity for p in particles]
    avg_velocity = sum(velocities) / len(velocities)
    temperature = compute_temperature(velocities)
    print(f"Average Temperature: {temperature}")

def compute_temperature(velocities):
    return sum(v.dot(v) for v in velocities) / (2 * len(velocities))
