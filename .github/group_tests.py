import unittest
from group import groups_of_3

class TestGroupsOf3(unittest.TestCase):
    def test_exact_groups(self):
        self.assertEqual(groups_of_3([1, 2, 3, 4, 5, 6, 7, 8, 9]), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_incomplete_group(self):
        self.assertEqual(groups_of_3([1, 2, 3, 4, 5, 6, 7, 8]), [[1, 2, 3], [4, 5, 6], [7, 8]])

    def test_empty_list(self):
        self.assertEqual(groups_of_3([]), [])

    def test_single_group(self):
        self.assertEqual(groups_of_3([1, 2]), [[1, 2]])

if __name__ == '__main__':
    unittest.main()
