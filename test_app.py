import unittest
from app import hello, slow_function

class TestApp(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello(), "Hello, World!")

    def test_slow_function(self):
        self.assertEqual(slow_function(), "Processamento concluído")

if __name__ == "__main__":
    unittest.main()
