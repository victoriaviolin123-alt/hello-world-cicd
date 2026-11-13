
import unittest
from pathlib import Path

class TestWebsite(unittest.TestCase):

    def test_homepage_contains_hello_world(self):
        html = Path("index.html").read_text()
        self.assertIn("Hello, world!", html)

    def test_homepage_has_html_structure(self):
        html = Path("index.html").read_text()
        self.assertIn("<html>", html)
        self.assertIn("</html>", html)

if __name__ == "__main__":
    unittest.main()
