import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_none(self):
        # Test when props is None
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")
        
    def test_props_to_html_empty(self):
        # Test when props is empty
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), "")
        
    def test_props_to_html_with_props(self):
        # Test with actual props
        node = HTMLNode(props={"href": "https://example.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com" target="_blank"')
#####Testing LeafNode
    def test_leaf_to_html_p(self):
         node = LeafNode("p", "Hello, world!")
         self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(value="Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
    
    def test_leaf_to_html_b(self):
        node = LeafNode("b", "Hello, world!")
        self.assertEqual(node.to_html(), "<b>Hello, world!</b>")

    def test_leaf_to_html_s(self):
        node = LeafNode("s", "Hello, world!")
        self.assertEqual(node.to_html(), "<s>Hello, world!</s>")
#####Testing ParentNode
    def test_parent_to_html(self):
        node = ParentNode("div", [LeafNode("p", "Hello, world!")])
        self.assertEqual(node.to_html(), "<div><p>Hello, world!</p></div>")

    def test_parent_to_html_no_tag(self):
        node = ParentNode(children=[LeafNode("p", "Hello, world!")])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_no_children(self):
        node = ParentNode("div")
        with self.assertRaises(ValueError):
            node.to_html()

    def test_parent_to_html_children(self):
        child_node = LeafNode("p", "Hello, world!")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><p>Hello, world!</p></div>")

    def test_to_html_grandchildren(self):
        grandchild_node = LeafNode("p", "Hello, world!")
        child_node = ParentNode("div", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><div><p>Hello, world!</p></div></div>")
