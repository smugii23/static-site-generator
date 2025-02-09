def markdown_to_blocks(markdown):
    markdown = markdown.strip()
    split = markdown.split("\n\n")
    res = [line.strip() for line in split if line.strip() != ""]
    return res