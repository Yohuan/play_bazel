import unittest

from python.lib import greeting


class TestGreeting(unittest.TestCase):
    def test_get_great(self):
        self.assertEqual(greeting.get_greet("yohuan"), "Hello yohuan")


if __name__ == "__main__":
    unittest.main()
