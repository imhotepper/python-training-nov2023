import os
import unittest

from files import grep


class GrepTestCase(unittest.TestCase):
    filename = "test_file.txt"

    @classmethod
    def setUpClass(cls):
        lines = ["hello world", "hi world", "hello kitty"]
        with open(cls.filename, "w") as f:
            f.writelines([f"{l}\n" for l in lines])

    def test_no_match(self):
        result = grep("helo", self.filename)
        self.assertEqual(result, [], "lists are not equal")

    def test_match(self):
        result = grep("hello", self.filename)
        self.assertEqual(result, ["hello world\n", "hello kitty\n"])

    def test_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            grep("hello", "nonexistent_file.txt")

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.filename)


if __name__ == "__main__":
    unittest.main()
