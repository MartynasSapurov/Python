import unittest

from Homework_23 import simple_generator


class TestGenerator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("#"*70)

    @classmethod
    def tearDownClass(cls):
        print("")
        print("#" * 70)

    def test_first(self):
        self.assertEqual(list(simple_generator(1, 2, 20))[0], 1)
        self.assertEqual(list(simple_generator(12, 2, 20))[0], 12)
        self.assertEqual(list(simple_generator(101, 2, 20))[0], 101)

    def test_last(self):
        self.assertEqual(list(simple_generator(1, 2, 20))[19], 524288)
        self.assertEqual(list(simple_generator(5, 2, 20))[19], 2621440)
        self.assertEqual(list(simple_generator(7, 2, 20))[19], 3670016)

    def test_length(self):
        self.assertEqual(len(list(simple_generator(1, 2, 10))), 10)
        self.assertEqual(len(list(simple_generator(1, 2, 20))), 20)
        self.assertEqual(len(list(simple_generator(1, 2, 30))), 30)

    @unittest.expectedFailure
    def test_type(self):
        self.assertEqual(simple_generator("a", 2, 20), "Not supported data type")
        self.assertEqual(simple_generator(1, "a", 20), "Not supported data type")
        self.assertEqual(simple_generator(1, 2, "a"), "Not supported data type")

    def test_AssertionError(self):
        with self.assertRaises(TypeError):
            list(simple_generator("a", 2, 20))
            list(simple_generator(1, "a", 20))
            list(simple_generator(1, 2, "a"))


if __name__ == '__main__':
    unittest.main()
