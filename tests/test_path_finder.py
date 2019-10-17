import unittest
from pathlib import Path

from handsdown.path_finder import PathFinder


class TestPathFinder(unittest.TestCase):
    def test_relative(self):
        path_finder = PathFinder(Path("/root/parent/source.py"))
        self.assertEqual(
            path_finder.relative(Path("/root/target.py")), Path("../target.py")
        )
        self.assertEqual(
            path_finder.relative(Path("/root/parent/target.py")), Path("target.py")
        )
        self.assertEqual(
            path_finder.relative(Path("/root2/other/target.py")),
            Path("../../root2/other/target.py"),
        )
        self.assertEqual(
            path_finder.relative(Path("/root/parent/source.py")), Path("source.py")
        )
        with self.assertRaises(ValueError):
            path_finder.relative(Path("second/source.py"))
