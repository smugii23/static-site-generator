from markdown_blocks import markdown_to_html_node
from htmlnode import HTMLNode
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

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for entry in os.listdir(dir_path_content):
        if os.path.isfile(os.path.join(dir_path_content, entry)):
            generate_page(os.path.join(dir_path_content, entry), template_path, os.path.join(dest_dir_path, os.path.splitext(entry)[0] + ".html"))
        else:
            os.makedirs(os.path.join(dest_dir_path, entry), exist_ok=True)
            generate_pages_recursive(os.path.join(dir_path_content, entry), template_path, os.path.join(dest_dir_path, entry))

def extract_title(markdown):
    if markdown.startswith("# "):
        return markdown.removeprefix("#").strip()
    else:
        raise Exception("no header")

