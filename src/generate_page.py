from markdown_blocks import markdown_to_html_node
from htmlnode import HTMLNode
from extract_title import extract_title
import os

def generate_page(from_path, template_path, dest_path):
    print(f"Generating path from {from_path} to {dest_path} using {template_path}")
    with open(from_path, 'r') as file:
        from_text = file.read()
    with open(template_path, 'r') as file:
        template_text = file.read()
    from_node = markdown_to_html_node(from_text)
    from_html = from_node.to_html()
    title = extract_title(from_text)
    template_text = template_text.replace("{{ Title }}", title).replace("{{ Content }}", from_html)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, 'w') as file:
        file.write(template_text)