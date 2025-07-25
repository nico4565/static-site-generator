import re
from markdown_blocks import markdown_to_blocks


def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    print("start extract title...")
    for block in blocks:
        if re.match(r"# .*",block):
            title = block.lstrip("#")
            return title.strip()
        raise Exception("No title present")