import unittest

from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        markdown = "# Hello"
        self.assertEqual(extract_title(markdown), "Hello")

    def test_extract_title2(self):
        markdown = "## Hello!"
        with self.assertRaises(Exception):
            extract_title(markdown)

    def test_extract_title3(self):
        self.assertEqual(extract_title("#    Hello    "), "Hello")
    
    def test_extract_title4(self):
        with self.assertRaises(Exception):
            extract_title("Hello without hash")
    
    def test_extract_title5(self):
        with self.assertRaises(Exception):
            extract_title("")

if __name__ == "__main__":
    unittest.main()