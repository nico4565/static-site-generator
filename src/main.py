import sys
from textnode import *
from htmlnode import *
from inline_markdown import *
from directoryutils import clean_and_clone
from generate_page import generate_page_recurs
import os

def main():
    text_node = TextNode("This is some anchor text",TextType.LINK,"https://www.boot.dev")
    # text_node_2 = TextNode("This is some anchor text",TextType.LINK,"https://www.boot.dev")
    # html_node = HTMLNode("tag", "value",[HTMLNode("tag-child","value-child"),HTMLNode("tag-child","value-child")], {"href": "https://www.google.com",
    # "target": "_blank",})
    # print(html_node.props_to_html())
    # print(text_node.__eq__(text_node_2))
    #(text_node)
    # print(html_node)
    #nodes = text_to_textNode("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
    #print(nodes)
    basepath = sys.argv[1] if len(sys.argv) else "/"
    print(basepath)
    clean_and_clone("public", "static")
    generate_page_recurs("content", "template.html" , "docs", basepath)


main()