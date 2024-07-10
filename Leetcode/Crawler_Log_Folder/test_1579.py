from unittest import TestCase

from Leetcode.Crawler_Log_Folder.L1579 import Solution


class TestSolution(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_min_operations(self):
        # Example Crawler_Log_Folder cases
        self.assertEqual(self.solution.min_operations(["d1/", "d2/", "../", "d21/", "./"]), 2)
        self.assertEqual(self.solution.min_operations(["d1/", "d2/", "./", "d3/", "../", "d31/"]), 3)
        self.assertEqual(self.solution.min_operations(["d1/", "../", "../", "../"]), 0)
        self.assertEqual(self.solution.min_operations(["./", "../", "./"]), 0)
        self.assertEqual(self.solution.min_operations(["d1/", "d2/", "../", "../", "../"]), 0)
        self.assertEqual(self.solution.min_operations([]), 0)
        self.assertEqual(self.solution.min_operations(["d1/"]), 1)

if __name__ == "__main__":
    import unittest
    unittest.main()
