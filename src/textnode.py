from enum import Enum
from htmlnode import HTMLNode, LeafNode, ParentNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, TextType, url=None):
        self.url = url
        self.text = text
        self.TextType = TextType

    def __eq__(self, value):
        if isinstance(value, TextNode):
            return self.text == value.text and self.TextType == value.TextType and self.url == value.url
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.TextType.value}, {self.url})"
    

def text_node_to_html_node(text_node):
    match text_node.TextType:
        case TextType.TEXT:
            return LeafNode(value=text_node.text)
        case TextType.BOLD:
            return LeafNode(tag="b", value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag="code", value=text_node.text)
        case TextType.LINK:
            return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text})
        case _:
            raise ValueError(f"Invalid TextTypeL {text_node.TextType}")