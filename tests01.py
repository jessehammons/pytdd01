import unittest


class Testing(unittest.TestCase):
    def test_string(self):
        a = "some"
        b = "some"
        self.assertEqual(a, b)

    def test_int(self):
        a = 3
        b = 3
        self.assertEqual(a, b)

    def test_boolean(self):
        a = True
        b = True

        self.assertEqual(a, b)  # a comment
        # another comment


if __name__ == "__main__":
    unittest.main()
