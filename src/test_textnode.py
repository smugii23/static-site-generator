import unittest

from textnode import TextNode, TextType  


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("Test node", TextType.ITALIC)
        node2 = TextNode("Test node", TextType.CODE)
        self.assertNotEqual(node, node2)

    def test_eq3(self):
        node = TextNode("Test node!", TextType.TEXT)
        node2 = TextNode("Test node?", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq4(self):
        node = TextNode("Test node", TextType.TEXT, url="test.test")
        node2 = TextNode("Test node", TextType.TEXT, url=None)
        self.assertNotEqual(node, node2)
        
if __name__ == "__main__":
    unittest.main()