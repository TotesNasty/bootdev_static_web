import unittest
from textnode import TextNode, TextType
from node_delimiter import split_nodes_delimiter

class TestNodeDelimiter(unittest.TestCase):
    def test_no_delimiter(self):
        node = TextNode("This is just plain text", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text, "This is just plain text")
        self.assertEqual(result[0].text_type, TextType.TEXT)

    def test_delimiter_simple(self):
        node = TextNode("This is **bold** text", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "This is ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "bold")
        self.assertEqual(result[1].text_type, TextType.BOLD)
        self.assertEqual(result[2].text, " text")
        self.assertEqual(result[2].text_type, TextType.TEXT)

    def test_delimiter_complex(self):
        node = TextNode("This is **bold** and *italic* text", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        result = split_nodes_delimiter(result, "*", TextType.ITALIC)        

    def test_nontext_node(self):
        nodes = [
            TextNode("This is **bold** text", TextType.TEXT),
            TextNode("This is allready bold text", TextType.BOLD)
        ]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(len(result), 4)