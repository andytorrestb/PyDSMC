import unittest
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import test_header
from src.dsmc.DSMC import DSMC
from src.dsmc.Animation import DSMCAnimation

__author__ = "Andres Torres-Figueroa"
__status__ = "Dev"


class TestSimulationWithVideo(unittest.TestCase):
    """Test case to simulate particle flow and save a video of the flow."""

    def test_flow_simulation_with_video(self):
        """Runs a DSMC simulation and saves a video of the flow as an MP4 file."""
        # Parameters
        num_particles = 10000
        domain_size = 1.0
        temperature = 300
        dt = 0.001
        num_cells = 20
        num_time_steps = 500
        video_filename = 'test_flow_simulation.mp4'

        # Initialize DSMC simulation
        dsmc_simulation = DSMC(num_particles, domain_size, temperature, dt, num_cells)

        # Create a figure for the animation
        fig, ax = plt.subplots()
        scat = ax.scatter([p.position[0] for p in dsmc_simulation.particles],
                          [p.position[1] for p in dsmc_simulation.particles], s=1)
        ax.set_xlim(0, domain_size)
        ax.set_ylim(0, domain_size)

        # Update function for the animation
        def update(frame):
            dsmc_simulation.simulate_motion()
            dsmc_simulation.grid.sort_particles(dsmc_simulation.particles)
            dsmc_simulation.perform_collisions()
            scat.set_offsets([[p.position[0], p.position[1]] for p in dsmc_simulation.particles])
            return scat,

        # Create and save the animation as an MP4 video
        ani = FuncAnimation(fig, update, frames=num_time_steps, interval=50, blit=True)
        ani.save(video_filename, writer='ffmpeg', fps=30)

        # Check if the video file was successfully created
        self.assertTrue(os.path.exists(video_filename), f"Video file '{video_filename}' not created.")
        print(f"Video saved as {video_filename}")

        # Clean up (optional)
        # if os.path.exists(video_filename):
        #     # os.remove(video_filename)


if __name__ == '__main__':
    unittest.main()
