"""
Name: Dominique Saile
Student ID: 105978
Email: sailedom@hs-albsig.de
Date: 22. May 2024
"""

import numpy as np
from modules.cell import Cell
from modules.ruleset import Ruleset

class Universe:
    """
    This class represents the universe for Conway's Game of Life.
    
    Attributes:
        height (int): The height of the visible universe.
        width (int): The width of the visible universe.
        ruleset (Ruleset): The ruleset used to determine cell states.
        p_cell_alive (float): The probability of a cell being alive at the start.
        char_alive (str): Character representing a living cell in the console.
        char_dead (str): Character representing a dead cell in the console.
        _cells (list of list of Cell): 2D list representing the universe with Cell objects.
    """
    
    def __init__(self, height: int, width: int, ruleset: Ruleset, p_cell_alive: float, 
                 char_alive: str = '*', char_dead: str = '.'):
        """
        Initializes the Universe with given dimensions, ruleset, and initial cell state probability.
        
        Args:
            height (int): The height of the visible universe.
            width (int): The width of the visible universe.
            ruleset (Ruleset): The ruleset used to determine cell states.
            p_cell_alive (float): The probability of a cell being alive at the start.
            char_alive (str): Character representing a living cell in the console.
            char_dead (str): Character representing a dead cell in the console.
        
        Raises:
            ValueError: If height or width are not positive or if p_cell_alive is not between 0 and 1.
        """
        self._validate_parameters(height, width, p_cell_alive)
        
        self.height = height
        self.width = width
        self.ruleset = ruleset
        self.p_cell_alive = p_cell_alive
        self.char_alive = char_alive
        self.char_dead = char_dead
        self._cells = self._create_universe()

    def _validate_parameters(self, height: int, width: int, p_cell_alive: float):
        """
        Validates the input parameters for the Universe constructor.
        
        Args:
            height (int): The height of the visible universe.
            width (int): The width of the visible universe.
            p_cell_alive (float): The probability of a cell being alive at the start.
        
        Raises:
            ValueError: If height or width are not positive or if p_cell_alive is not between 0 and 1.
        """
        if height <= 0 or width <= 0:
            raise ValueError("Height and width must be positive integers.")
        if not (0 <= p_cell_alive <= 1):
            raise ValueError("Probability of cell being alive must be between 0 and 1.")

    def _create_empty_universe(self) -> list:
        """
        Creates an empty universe with all cells dead.
        
        Returns:
            list: 2D list representing the universe with dead cells.
        """
        return [[Cell(0, self.ruleset) for _ in range(self.width + 2)] for _ in range(self.height + 2)]

    def _initialize_visible_universe(self, universe: list) -> list:
        """
        Initializes the visible part of the universe with random alive or dead cells.
        
        Args:
            universe (list): The 2D list representing the universe.
        
        Returns:
            list: The initialized universe with random alive and dead cells.
        """
        for i in range(1, self.height + 1):
            for j in range(1, self.width + 1):
                state = np.random.choice([0, 1], p=[1 - self.p_cell_alive, self.p_cell_alive])
                universe[i][j] = Cell(state, self.ruleset)
        return universe

    def _add_neighbors_to_cells(self, universe: list) -> list:
        """
        Adds neighbors to each cell in the visible universe.
        
        Args:
            universe (list): The 2D list representing the universe.
        
        Returns:
            list: The universe with neighbors added to each cell.
        """
        for i in range(1, self.height + 1):
            for j in range(1, self.width + 1):
                neighbors = [
                    universe[i-1][j-1], universe[i-1][j], universe[i-1][j+1],
                    universe[i][j-1], universe[i][j+1],
                    universe[i+1][j-1], universe[i+1][j], universe[i+1][j+1]
                ]
                universe[i][j].neighbors = neighbors
        return universe

    def _create_universe(self) -> list:
        """
        Creates the universe by initializing the visible part and adding neighbors.
        
        Returns:
            list: The fully initialized universe.
        """
        universe = self._create_empty_universe()
        universe = self._initialize_visible_universe(universe)
        universe = self._add_neighbors_to_cells(universe)
        return universe

    def print_universe(self):
        """
        Prints the current state of the universe to the console.
        """
        for i in range(1, self.height + 1):
            line = ''.join(self.char_alive if cell.state == 1 else self.char_dead for cell in self._cells[i][1:self.width + 1])
            print(line)

    def run_one_iteration(self):
        """
        Runs one iteration of the Game of Life, updating all cell states.
        """
        for i in range(1, self.height + 1):
            for j in range(1, self.width + 1):
                self._cells[i][j].calculate_state_of_next_iteration()
        
        for i in range(1, self.height + 1):
            for j in range(1, self.width + 1):
                self._cells[i][j].update_state()
        
        self.print_universe()
