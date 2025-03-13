import os
import shutil

from copystatic import copy_files_recursive
from gencontent import generate_page


dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating page...")
    for root, dirs, files in os.walk(dir_path_content):
        for file in files:
            if file.endswith(".md"):
                # Construct the full path to the markdown file
                md_file_path = os.path.join(root, file)
                
                # Construct output HTML path relative to the public directory
                relative_path = os.path.relpath(root, dir_path_content)
                output_html_dir = os.path.join(dir_path_public, relative_path)
                os.makedirs(output_html_dir, exist_ok=True)
                
                # Generate the HTML filename
                output_html_path = os.path.join(output_html_dir, "index.html")
                
                # Generate the page
                generate_page(md_file_path, template_path, output_html_path)

main()