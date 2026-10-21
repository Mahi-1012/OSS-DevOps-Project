
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app import greet


class TestApp(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(
            greet("Student"),
            "Hello, Student! Your DevOps project is running."
        )


if __name__ == "__main__":
    unittest.main()
