import unittest
from modules.ruleset import Ruleset
from modules.cell import Cell
from modules.universe import Universe

class TestUniverse(unittest.TestCase):
    def setUp(self):
        self.ruleset = Ruleset("23/3")
        self.universe = Universe(3, 3, self.ruleset, 0.5, '*', '.')

    def test_initialization(self):
        # Test if the universe initializes correctly
        self.assertEqual(self.universe.height, 3)
        self.assertEqual(self.universe.width, 3)
        self.assertEqual(self.universe.p_cell_alive, 0.5)
        self.assertEqual(self.universe.char_alive, '*')
        self.assertEqual(self.universe.char_dead, '.')
        self.assertEqual(len(self.universe._cells), 5)  # including boundary
        self.assertEqual(len(self.universe._cells[0]), 5)  # including boundary

    def test_create_empty_universe(self):
        # Test creation of an empty universe
        empty_universe = self.universe._create_empty_universe()
        for row in empty_universe:
            for cell in row:
                self.assertEqual(cell.state, 0)

    def test_initialize_visible_universe(self):
        # Test initialization of the visible universe
        universe = self.universe._create_empty_universe()
        initialized_universe = self.universe._initialize_visible_universe(universe)
        visible_cells = [initialized_universe[i][j].state for i in range(1, 4) for j in range(1, 4)]
        self.assertTrue(any(cell == 1 for cell in visible_cells))  # Check that some cells are alive
        self.assertTrue(any(cell == 0 for cell in visible_cells))  # Check that some cells are dead

    def test_add_neighbors_to_cells(self):
        # Test adding neighbors to each cell
        universe = self.universe._create_empty_universe()
        initialized_universe = self.universe._initialize_visible_universe(universe)
        universe_with_neighbors = self.universe._add_neighbors_to_cells(initialized_universe)
        for i in range(1, 4):
            for j in range(1, 4):
                self.assertEqual(len(universe_with_neighbors[i][j].neighbors), 8)

    def test_create_universe(self):
        # Test complete creation of the universe
        universe = self.universe._create_universe()
        self.assertEqual(len(universe), 5)  # including boundary
        self.assertEqual(len(universe[0]), 5)  # including boundary
        for i in range(1, 4):
            for j in range(1, 4):
                self.assertIsInstance(universe[i][j], Cell)
                self.assertEqual(len(universe[i][j].neighbors), 8)

    def test_print_universe(self):
        # Test printing of the universe
        universe = self.universe._create_universe()
        self.universe.print_universe()  # Ensure no errors are raised during printing

    def test_run_one_iteration(self):
        # Test running one iteration of the universe
        universe = self.universe._create_universe()
        self.universe.run_one_iteration()  # Ensure no errors are raised during one iteration

    def test_invalid_parameters(self):
        # Test invalid parameters in the constructor
        with self.assertRaises(ValueError):
            Universe(0, 3, self.ruleset, 0.5)
        with self.assertRaises(ValueError):
            Universe(3, 0, self.ruleset, 0.5)
        with self.assertRaises(ValueError):
            Universe(3, 3, self.ruleset, -0.1)
        with self.assertRaises(ValueError):
            Universe(3, 3, self.ruleset, 1.1)

if __name__ == '__main__':
    unittest.main()
