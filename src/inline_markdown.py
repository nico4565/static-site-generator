from textnode import TextNode, TextType
import re

def text_to_textnodes(text):
    new_nodes = [TextNode(text,TextType.TEXT)]
    new_nodes = split_nodes_delimiter(new_nodes,"**",TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes,"_",TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes,"`",TextType.CODE)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)
    return new_nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        matches = extract_markdown_images(old_node.text)
        if not matches:
            if old_node.text != "":
                new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = []
        for match in matches:
            if not sections:
                sections = old_node.text.split(f"![{match[0]}]({match[1]})",1)
            else:
                new_sect = sections.pop(len(sections)-1)
                new_split = new_sect.split(f"![{match[0]}]({match[1]})",1)
                if len(new_split) != 2:
                    raise ValueError("invalid markdown, image section not closed")
                sections = sections + new_split

        for i in range(len(sections)):
            if sections[i] == "":
                if(len(matches)>= i+1):
                    split_nodes.append(TextNode(matches[i][0], TextType.IMAGE,matches[i][1]))
                continue
            split_nodes.append(TextNode(sections[i], TextType.TEXT))
            if(len(matches)>= i+1):
                split_nodes.append(TextNode(matches[i][0], TextType.IMAGE,matches[i][1]))

        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        matches = extract_markdown_links(old_node.text)
        if not matches:
            if old_node.text != "":
                new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = []
        for match in matches:
            if not sections:
                sections = old_node.text.split(f"[{match[0]}]({match[1]})",1)
                if len(sections) != 2:
                    raise ValueError("invalid markdown, image section not closed")
            else:
                new_sect = sections.pop(len(sections)-1)
                new_split = new_sect.split(f"[{match[0]}]({match[1]})",1)
                if len(new_split) != 2:
                    raise ValueError("invalid markdown, image section not closed")
                sections = sections + new_split

        for i in range(len(sections)):
            if sections[i] == "":
                if(len(matches)>= i+1):
                    split_nodes.append(TextNode(matches[i][0], TextType.LINK,matches[i][1]))
                continue
            split_nodes.append(TextNode(sections[i], TextType.TEXT))
            if(len(matches)>= i+1):
                split_nodes.append(TextNode(matches[i][0], TextType.LINK,matches[i][1]))

        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    return matches
