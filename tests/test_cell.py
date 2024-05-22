import unittest
from modules.ruleset import Ruleset
from modules.cell import Cell

class TestCell(unittest.TestCase):
    def setUp(self):
        # Initial ruleset for testing
        self.ruleset = Ruleset("23/3")
        # Initialize cells for testing
        self.cell_alive = Cell(1, self.ruleset)
        self.cell_dead = Cell(0, self.ruleset)

    def test_initial_state(self):
        # Test initial state of cells
        self.assertEqual(self.cell_alive.state, 1)
        self.assertEqual(self.cell_dead.state, 0)

    def test_from_string(self):
        # Test creation from string
        self.assertEqual(Cell.from_string('1', self.ruleset).state, 1)
        self.assertEqual(Cell.from_string('0', self.ruleset).state, 0)
        with self.assertRaises(ValueError):
            Cell.from_string('2', self.ruleset)
        with self.assertRaises(ValueError):
            Cell.from_string('a', self.ruleset)

    def test_add_neighbor(self):
        # Test adding neighbors
        neighbor = Cell(1, self.ruleset)
        self.cell_alive.add_neighbor(neighbor)
        self.assertEqual(len(self.cell_alive.neighbors), 1)
        self.assertEqual(self.cell_alive.neighbors[0], neighbor)

    def test_calculate_state_of_next_iteration(self):
        # Test calculation of next state
        neighbor1 = Cell(1, self.ruleset)
        neighbor2 = Cell(1, self.ruleset)
        neighbor3 = Cell(1, self.ruleset)
        self.cell_dead.add_neighbor(neighbor1)
        self.cell_dead.add_neighbor(neighbor2)
        self.cell_dead.add_neighbor(neighbor3)
        self.cell_dead.calculate_state_of_next_iteration()
        self.assertEqual(self.cell_dead._state_next_iteration, 1)

    def test_update_state(self):
        # Test update state
        neighbor1 = Cell(1, self.ruleset)
        neighbor2 = Cell(1, self.ruleset)
        self.cell_alive.add_neighbor(neighbor1)
        self.cell_alive.add_neighbor(neighbor2)
        self.cell_alive.calculate_state_of_next_iteration()
        self.cell_alive.update_state()
        self.assertEqual(self.cell_alive.state, 1)

    def test_warnings(self):
        # Test warnings for too many neighbors
        for _ in range(8):
            self.cell_alive.add_neighbor(Cell(0, self.ruleset))
        with self.assertWarns(Warning):
            self.cell_alive.add_neighbor(Cell(0, self.ruleset))

        # Test warnings for update state without calculation
        cell = Cell(1, self.ruleset)
        with self.assertWarns(Warning):
            cell.update_state()

if __name__ == '__main__':
    unittest.main()
