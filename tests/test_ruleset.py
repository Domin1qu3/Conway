import unittest
from modules.ruleset import Ruleset

class TestRuleset(unittest.TestCase):
    def setUp(self):
        self.ruleset = Ruleset("23/3")

    def test_parse_rules(self):
        self.assertEqual(self.ruleset.cell_survives, [2, 3])
        self.assertEqual(self.ruleset.cell_born, [3])

    def test_calculate_next_state(self):
        # Test for alive cell with sufficient neighbors to survive
        self.assertEqual(self.ruleset.calculate_next_state(1, 2), 1)
        # Test for alive cell with insufficient neighbors to survive
        self.assertEqual(self.ruleset.calculate_next_state(1, 1), 0)
        # Test for dead cell with sufficient neighbors to become alive
        self.assertEqual(self.ruleset.calculate_next_state(0, 3), 1)
        # Test for dead cell with insufficient neighbors to become alive
        self.assertEqual(self.ruleset.calculate_next_state(0, 2), 0)

    def test_invalid_rules(self):
        with self.assertRaises(ValueError):
            Ruleset("invalid/rules")

    def test_invalid_current_state(self):
        with self.assertRaises(ValueError):
            self.ruleset.calculate_next_state(2, 3)

    def test_negative_alive_neighbors(self):
        with self.assertRaises(ValueError):
            self.ruleset.calculate_next_state(1, -1)

if __name__ == '__main__':
    unittest.main()
