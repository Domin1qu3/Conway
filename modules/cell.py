"""
Name: Dominique Saile
Student ID: 105978
Email: sailedom@hs-albsig.de
Date: 22. May 2024
"""

class Cell:
    """
    This class represents a single cell in Conway's Game of Life.
    
    Attributes:
        _current_state (int): The current state of the cell (0 for dead, 1 for alive).
        _state_next_iteration (int or None): The state of the cell in the next iteration.
        neighbors (list): List of neighboring Cell objects.
        ruleset (Ruleset): The ruleset to determine the cell's next state.
    """
    
    def __init__(self, initial_state: int, ruleset):
        """
        Initializes the Cell with an initial state and a ruleset.
        
        Args:
            initial_state (int): The initial state of the cell (0 for dead, 1 for alive).
            ruleset (Ruleset): The ruleset to determine the cell's next state.
        
        Raises:
            ValueError: If initial_state is not 0 or 1.
        """
        if initial_state not in [0, 1]:
            raise ValueError("Initial state must be 0 (dead) or 1 (alive).")
        
        self._current_state = initial_state
        self._state_next_iteration = None
        self.neighbors = []
        self.ruleset = ruleset

    @classmethod
    def from_string(cls, state_str: str, ruleset):
        """
        Creates a Cell object from a string representing the initial state.
        
        Args:
            state_str (str): The initial state as a string ('0' or '1').
            ruleset (Ruleset): The ruleset to determine the cell's next state.
        
        Returns:
            Cell: A new Cell object with the given initial state.
        
        Raises:
            ValueError: If state_str is not '0' or '1'.
        """
        if state_str not in ['0', '1']:
            raise ValueError("State string must be '0' or '1'.")
        
        initial_state = int(state_str)
        return cls(initial_state, ruleset)

    @property
    def state(self) -> int:
        """
        The current state of the cell (read-only).
        
        Returns:
            int: The current state of the cell.
        """
        return self._current_state

    @state.setter
    def state(self, value):
        raise AttributeError("Cannot change state directly. Use update_state().")

    def add_neighbor(self, neighbor):
        """
        Adds a neighboring cell to the cell's neighbors list.
        
        Args:
            neighbor (Cell): A neighboring Cell object.
        
        Raises:
            Warning: If the cell already has 8 neighbors.
        """
        if len(self.neighbors) >= 8:
            import warnings
            warnings.warn("Cell already has 8 neighbors.")
        self.neighbors.append(neighbor)

    def calculate_state_of_next_iteration(self):
        """
        Calculates and sets the state of the cell for the next iteration.
        """
        num_alive_neighbors = sum(neighbor.state for neighbor in self.neighbors)
        self._state_next_iteration = self.ruleset.calculate_next_state(self._current_state, num_alive_neighbors)

    def update_state(self):
        """
        Updates the current state to the next iteration's state.
        
        Raises:
            Warning: If _state_next_iteration is None.
        """
        if self._state_next_iteration is None:
            import warnings
            warnings.warn("State for next iteration is not calculated. Calling calculate_state_of_next_iteration().")
            self.calculate_state_of_next_iteration()
        
        self._current_state = self._state_next_iteration
        self._state_next_iteration = None

    def __str__(self):
        """
        Returns the string representation of the cell's current state.
        
        Returns:
            str: The current state of the cell as a string.
        """
        return str(self._current_state)
