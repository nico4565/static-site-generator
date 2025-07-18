from enum import Enum
import re

class BlockType(Enum):
        PARAGRAPH = "paragraph"
        HEADING = "heading"
        CODE = "code"
        QUOTE = "quote"
        UNORDERED_LIST = "unordered_list"
        ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    
    lines = block.split("\n")
    if re.match(r"#{1,6} .*",block):
          return BlockType.HEADING 
    if re.match(r"`{3}[\s\S]*`{3}",block):
          return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def markdown_to_blocks(markdown):
    processed_blocks = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        if not block:
            continue
        processed_blocks.append(block.strip())
    return processed_blocks