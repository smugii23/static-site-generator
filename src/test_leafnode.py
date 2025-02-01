import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leafnode_no_tag(self):
        node = LeafNode(None, "Plain text")
        self.assertEqual(node.to_html(), "Plain text")
    
    def test_leafnode_with_tag(self):
        node = LeafNode("p", "This is a paragraph.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph.</p>")
    
    def test_leafnode_with_props(self):
        node = LeafNode("a", "Click here", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click here</a>')
    
    def test_leafnode_no_value(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)
    
if __name__ == "__main__":
    unittest.main()
