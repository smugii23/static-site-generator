from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node
from htmlnode import HTMLNode, ParentNode, LeafNode

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"

def markdown_to_blocks(markdown):
    markdown = markdown.strip()
    split = markdown.split("\n\n")
    res = [line.strip() for line in split if line.strip() != ""]
    return res

def block_to_block_type(markdown):
    split = markdown.split(' ', 1)
    lines = markdown.split('\n')
    first_word = split[0]

    if len(first_word) <= 6 and set(first_word) == {"#"} and len(split) > 1:
        return block_type_heading

    if lines[0].startswith("```") and lines[-1].endswith("```") and len(lines) > 1:
        return block_type_code

    if all(line.startswith(">") for line in lines):
        return block_type_quote

    if all(line.startswith(("* ", "- ")) for line in lines):
        return block_type_ulist
    
    if all(line.startswith(f"{index + 1}. ") for index, line in enumerate(lines)):
        return block_type_olist
    
    return block_type_paragraph

def block_type_to_tag(block_type, block_content):
    split = block_content.split(' ', 1)
    if block_type == block_type_paragraph:
        return "p"

    if block_type == block_type_heading:
        return f"h{len(split[0])}"

    if block_type == block_type_code:
        return "code"

    if block_type == block_type_quote:
        return "blockquote"
    
    if block_type == block_type_ulist:
        return "ul"
    
    if block_type == block_type_olist:
        return "ol"

def code_block_to_html_node(block_content):
    lines = block_content.split("\n")
    code_node = LeafNode(tag="code", value='\n'.join(lines[1:-1]))
    pre_node = ParentNode(tag="pre", children=[code_node])
    return pre_node

def extract_text_from_block(block_type, block_content):
    lines = block_content.split('\n')
    split = block_content.split(' ', 1)
    if block_type == block_type_heading:
        return split[1]
    if block_type == block_type_quote:
        cleaned_lines = [line.lstrip(">").strip() for line in lines]
        return ' '.join(cleaned_lines)
    if block_type == block_type_ulist:
        cleaned_lines = [line.removeprefix("* ").removeprefix("- ") for line in lines]
        return cleaned_lines
    if block_type == block_type_olist:
        cleaned_lines = [line.removeprefix(f"{index + 1}. ") for index, line in enumerate(lines)]
        return cleaned_lines
    if block_type == block_type_paragraph:
        return ' '.join(lines)


def list_to_html(block_type, lines):
    list_nodes = []
    if block_type == block_type_ulist:
        for line in lines:
            list_nodes.append(ParentNode(tag="li", children=text_to_children(line)))
        ul_node = ParentNode(tag="ul", children=list_nodes)
        return ul_node
    if block_type == block_type_olist:
        for line in lines:
            list_nodes.append(ParentNode(tag="li", children=text_to_children(line)))
        ol_node = ParentNode(tag="ol", children=list_nodes)
        return ol_node

def text_to_children(text):
    html_nodes = []
    nodes = text_to_textnodes(text)
    for node in nodes:
        html_nodes.append(text_node_to_html_node(node))
    return html_nodes

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        tag = block_type_to_tag(block_type, block)
        cleaned_lines = extract_text_from_block(block_type, block)
        if tag == "code":
            node = code_block_to_html_node(block)
            children.append(node)
        elif tag == "ul" or tag == "ol":
            node = list_to_html(block_type, cleaned_lines)
            children.append(node)
        else:
            node = ParentNode(tag=tag, children=text_to_children(cleaned_lines))
            children.append(node)
    return ParentNode(tag="div", children=children)