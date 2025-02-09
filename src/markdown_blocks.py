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

    if len(split) < 2:
        return block_type_paragraph

    if len(first_word) <= 6 and set(first_word) == {"#"} and split[1]:
        return block_type_heading

    if markdown.startswith("```") and markdown.endswith("```") and len(markdown[3:-3].strip()) > 0:
        return block_type_code

    if all(line.startswith(">") for line in lines):
        return block_type_quote

    if all(line.startswith(("* ", "- ")) for line in lines):
        return block_type_olist
    
    if all(line.startswith(f"{index + 1}. ") for index, line in enumerate(lines)):
        return block_type_ulist
    
    return block_type_paragraph
        
    