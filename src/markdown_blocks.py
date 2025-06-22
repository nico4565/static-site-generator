# The .split() method can be used to split a string into blocks based on a delimiter (\n\n is a double newline).
# You should .strip() any leading or trailing whitespace from each block.
# Remove any "empty" blocks due to excessive newlines.
def markdown_to_blocks(markdown):
    processed_blocks = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        if not block:
            continue
        processed_blocks.append(block.strip())
    return processed_blocks