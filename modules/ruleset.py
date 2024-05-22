"""
Name: Dominique Saile
Student ID: 105978
Email: sailedom@hs-albsig.de
Date: 22. May 2024
"""

class Ruleset:
    """
    This class represents the ruleset used for Conway's Game of Life.
    
    Attributes:
        rules (str): The ruleset in short notation (e.g., '23/3').
        cell_survives (list of int): List of neighbor counts for which a cell survives.
        cell_born (list of int): List of neighbor counts for which a cell is born.
    """
    
    def __init__(self, rules: str):
        """
        Initializes the Ruleset with a given rules string.
        
        Args:
            rules (str): The ruleset in short notation (e.g., '23/3').
            
        Raises:
            ValueError: If the rules string is not in the correct format.
        """
        self.rules = rules
        self.cell_survives, self.cell_born = self._parse_rules()

    def _parse_rules(self) -> tuple[list[int], list[int]]:
        """
        Parses the ruleset string into survival and birth rules.
        
        Returns:
            tuple: Two lists containing the survival and birth rules respectively.
        
        Raises:
            ValueError: If the rules string is not in the correct format.
        """
        try:
            survives, born = self.rules.split('/')
            cell_survives = [int(x) for x in survives]
            cell_born = [int(x) for x in born]
        except ValueError:
            raise ValueError("Invalid rules format. Expected format is '23/3' with digits and a slash.")
        
        return cell_survives, cell_born

    def calculate_next_state(self, current_state: int, num_alive_neighbors: int) -> int:
        """
        Calculates the next state of a cell based on the current state and the number of alive neighbors.
        
        Args:
            current_state (int): The current state of the cell (0 for dead, 1 for alive).
            num_alive_neighbors (int): The number of alive neighbors.
        
        Returns:
            int: The next state of the cell (0 for dead, 1 for alive).
        
        Raises:
            ValueError: If the current state is not 0 or 1, or if num_alive_neighbors is negative.
        """
        if current_state not in [0, 1]:
            raise ValueError("Current state must be 0 (dead) or 1 (alive).")
        if num_alive_neighbors < 0:
            raise ValueError("Number of alive neighbors cannot be negative.")
        
        if current_state == 1 and num_alive_neighbors in self.cell_survives:
            return 1
        elif current_state == 0 and num_alive_neighbors in self.cell_born:
            return 1
        else:
            return 0

