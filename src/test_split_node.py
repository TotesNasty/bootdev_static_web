import unittest
from split_nodes import split_nodes_image
from textnode import TextNode, TextType

class TestSplitNodes(unittest.TestCase):
    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https:..i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https:..i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_image_no_image(self):
        node = TextNode("This is text with no image", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([node], new_nodes)

    def test_split_image_multiple_images(self):
        node = TextNode(
            "This is text with an ![image](https:..i.imgur.com/zjjcJKZ.png) and another ![image](https:..i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https:..i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https:..i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )
