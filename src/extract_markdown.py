import re

def extract_markdown_images(markdown_text):
    image_urls = re.findall(r'!\[.*?\]\((.*?)\)', markdown_text)
    alt_texts = re.findall(r'!\[(.*?)\]', markdown_text)
    result = list(zip(alt_texts, image_urls))
    return result

def extract_markdown_links(markdown_text):
    link_urls = re.findall(r'\[(.*?)\]\((.*?)\)', markdown_text)
    return link_urls


