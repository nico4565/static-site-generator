import unittest
from extract_title import extract_title


class TestHTMLNode(unittest.TestCase):
    def test_extraction(self):
        md = """
# Hello

This is another paragraph 
"""

        title = extract_title(md)
        self.assertEqual(
            title,
            "Hello",
        )

    def test_extraction_failure(self):
        md = """
This is another paragraph with no title
"""
        with self.assertRaises(Exception):
            extract_title(md)

if __name__ == "__main__":
    unittest.main()
