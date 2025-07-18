import re
from markdown_blocks import markdown_to_blocks,block_to_block_type,BlockType
from htmlnode import HTMLNode, ParentNode
from inline_markdown import split_nodes_delimiter, text_to_textnodes
from textnode import TextType, text_node_to_html_node, TextNode

def markdown_to_html_node(markdown):
    markdown_blocks = markdown_to_blocks(markdown)
    parent_children_list = []

    for block in markdown_blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                lines = block.split("\n")
                cleaned = " ".join(lines)
                children_list = text_to_child_nodes(cleaned)
                parent_children_list.append(ParentNode("p",children_list))
            case BlockType.HEADING:
                match = re.match(r"(#+)\s*(.*)", block)
                cleaned = block.lstrip("#")
                children_list = text_to_child_nodes(cleaned)
                parent_children_list.append(ParentNode(f"h{len(match.group(1))}",children_list))
            case BlockType.QUOTE:
                lines = []
                for line in block.replace('>', '').split("\n"):
                    lines.append(line.strip())
                cleaned_paragraph = " ".join(lines)
                children_list = text_to_child_nodes(cleaned_paragraph)
                parent_children_list.append(ParentNode("blockquote",children_list))
            case BlockType.CODE:
                node = [TextNode(block,TextType.TEXT)]
                children_list = split_nodes_delimiter(node,"`",TextType.CODE)
                html = text_node_to_html_node(children_list[0])
                
                parent_children_list.append(ParentNode("pre",[html]))
            case BlockType.ORDERED_LIST:
                children_list = []
                lines = block.split("\n")
                i = 1
                for line in lines:
                    cleaned = line.lstrip(f"{i}. ")
                    children_list.append(ParentNode("li",text_to_child_nodes(cleaned)))    
                    i += 1
                parent_children_list.append(ParentNode("ol",children_list))
            case BlockType.UNORDERED_LIST:
                children_list = []
                lines = block.split("\n")
                for line in lines:
                    cleaned = line.lstrip(f"- ")
                    children_list.append(ParentNode("li",text_to_child_nodes(cleaned)))    
                parent_children_list.append(ParentNode("ul",children_list))
            case _:
                raise Exception("Error: block type not included")
            
        parent_node = ParentNode("div",parent_children_list)
    return parent_node

def text_to_child_nodes(text):
    text_nodes_list = text_to_textnodes(text)
    child_nodes_list = []
    for text_node in text_nodes_list:
        child_nodes_list.append(text_node_to_html_node(text_node))
    return child_nodes_list