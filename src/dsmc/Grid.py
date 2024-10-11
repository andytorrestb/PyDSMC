class Grid:
    """Represents the simulation grid for sorting particles.

    Attributes:
        domain_size (float): The size of the domain (in each direction).
        num_cells (int): The number of cells along each axis of the grid.
        cell_size (float): The size of each cell in the grid.
        grid (list of list of list of int): A 2D grid where each cell stores a list of particle indices.
    """

    def __init__(self, domain_size, num_cells):
        """Initializes the grid with a given domain size and number of cells.

        Args:
            domain_size (float): The size of the domain (assumed square).
            num_cells (int): The number of cells along each axis of the grid.
        """
        self.domain_size = domain_size
        self.num_cells = num_cells
        self.cell_size = domain_size / num_cells
        self.grid = self.create_grid()

    def create_grid(self):
        """Creates a 2D grid where each cell is an empty list.

        Returns:
            list of list of list of int: A 2D list representing the grid with empty cells.
        """
        return [[[] for _ in range(self.num_cells)] for _ in range(self.num_cells)]

    def clear_grid(self):
        """Clears the grid by reinitializing it."""
        self.grid = self.create_grid()

    def sort_particles(self, particles):
        """Sorts particles into the grid cells based on their positions.

        Args:
            particles (list of Particle): List of particles in the simulation.
        """
        self.clear_grid()
        for idx, particle in enumerate(particles):
            cell_x = int(particle.position[0] // self.cell_size)
            cell_y = int(particle.position[1] // self.cell_size)
            cell_x = min(cell_x, self.num_cells - 1)
            cell_y = min(cell_y, self.num_cells - 1)
            self.grid[cell_x][cell_y].append(idx)
