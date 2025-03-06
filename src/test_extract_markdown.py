import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        markdown_text = "![alt text](http://example.com/image.jpg)"
        result = extract_markdown_images(markdown_text)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][0], "alt text")
        self.assertEqual(result[0][1], "http://example.com/image.jpg")

    def test_extract_markdown_links(self):
        markdown_text = "[link text](http://example.com)"
        result = extract_markdown_links(markdown_text)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][0], "link text")
        self.assertEqual(result[0][1], "http://example.com")

    def test_extract_markdown_links_multiple(self):
        markdown_text = "[link text](http://example.com) and [another link](http://example.com/another)"
        result = extract_markdown_links(markdown_text)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0][0], "link text")
        self.assertEqual(result[0][1], "http://example.com")
        self.assertEqual(result[1][0], "another link")
        self.assertEqual(result[1][1], "http://example.com/another")

    def test_extract_markdown_links_no_links(self):
        markdown_text = "This is just plain text"
        result = extract_markdown_links(markdown_text)
        self.assertEqual(len(result), 0)
        self.assertEqual(result, [])

    def test_extract_markdown_links_empty(self):
        markdown_text = ""
        result = extract_markdown_links(markdown_text)
        self.assertEqual(len(result), 0)
        self.assertEqual(result, [])

    def test_extract_markdown_links_no_text(self):
        markdown_text = "[]()"
        result = extract_markdown_links(markdown_text)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][0], "")
        self.assertEqual(result[0][1], "")

    def test_extract_markdown_links_no_link(self):
        markdown_text = "[link text]"
        result = extract_markdown_links(markdown_text)
        self.assertEqual(len(result), 0)
        self.assertEqual(result, [])

    def test_extract_markdown_links_no_text_no_link(self):
        markdown_text = "[]"
        result = extract_markdown_links(markdown_text)
        self.assertEqual(len(result), 0)
        self.assertEqual(result, [])