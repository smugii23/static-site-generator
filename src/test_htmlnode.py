import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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

class ParentNodeTest(unittest.TestCase):
    def test_parent_node(self):
        node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],)
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )
    
