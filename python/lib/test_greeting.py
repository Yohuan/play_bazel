import unittest

from python.lib import greeting


class TestGreeting(unittest.TestCase):
    def test_great(self):
        self.assertEqual(greeting.greet("yohuan"), "Hello yohuan")


if __name__ == "__main__":
    unittest.main()
