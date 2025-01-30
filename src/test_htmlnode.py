import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_html(self):
        node = HTMLNode(props={
    "href": "https://www.google.com",
    "target": "_blank",
})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')
    
    def test_props_html2(self):
        node = HTMLNode(props={"href": "test"})
        self.assertEqual(node.props_to_html(), ' href="test"')
    
    def test_props_html3(self):
        node = HTMLNode(props={"test": "test"})
        self.assertNotEqual(node.props_to_html(), ' href="test"')
    
