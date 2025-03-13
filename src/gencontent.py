import os
from block_breakdown import markdown_to_html_node


def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")
    if not os.path.exists(from_path):
        raise FileNotFoundError(f"The file {from_path} does not exist.")
    
    # Check file permissions
    if not os.access(from_path, os.R_OK):
        raise PermissionError(f"The file {from_path} is not readable.")
   
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()
    print("Extracting title...")
    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)


def extract_title(md):
    print("still extracting title")  # Debugging line
    lines = md.splitlines()
    for line in lines:
        print("Processing line:", repr(line))  # Debugging line
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")
