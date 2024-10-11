import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class DSMCAnimation:
    """Class to create animations of the DSMC simulation.

    Attributes:
        dsmc (DSMC): DSMC object for managing simulation state.
        num_steps (int): Number of frames to animate.
        fig (matplotlib.figure.Figure): Matplotlib figure object.
        ax (matplotlib.axes.Axes): Matplotlib axes object.
        scat (matplotlib.collections.PathCollection): Scatter plot for particles.
    """

    def __init__(self, dsmc, num_steps):
        """Initializes the DSMCAnimation with DSMC simulation data.

        Args:
            dsmc (DSMC): DSMC object.
            num_steps (int): Number of animation frames.
        """
        self.dsmc = dsmc
        self.num_steps = num_steps
        self.fig, self.ax = plt.subplots()
        self.scat = self.ax.scatter(
            [particle.position[0] for particle in self.dsmc.particles],
            [particle.position[1] for particle in self.dsmc.particles], s=1)
        self.ax.set_xlim(0, self.dsmc.domain_size)
        self.ax.set_ylim(0, self.dsmc.domain_size)

    def update(self, frame):
        """Update function for animation at each frame.

        Args:
            frame (int): The current frame number.

        Returns:
            matplotlib.collections.PathCollection: The updated scatter plot.
        """
        self.dsmc.simulate_motion()
        self.dsmc.grid.sort_particles(self.dsmc.particles)
        self.dsmc.perform_collisions()
        self.scat.set_offsets([[p.position[0], p.position[1]] for p in self.dsmc.particles])  # Shape (num_particles, 2)
        return self.scat,

    def create_animation(self, filename):
        """Creates and saves the animation as a video file.

        Args:
            filename (str): The file path to save the animation.
        """
        anim = FuncAnimation(self.fig, self.update, frames=self.num_steps, interval=50, blit=True)
        anim.save(filename, writer='ffmpeg', fps=30)
        plt.show()
