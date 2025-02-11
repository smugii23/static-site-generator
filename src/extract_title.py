def extract_title(markdown):
    if markdown.startswith("# "):
        return markdown.removeprefix("#").strip()
    else:
        raise Exception("no header")

