from textnode import *
from htmlnode import *

def main():
    text_node = TextNode("This is some anchor text",TextType.LINK,"https://www.boot.dev")
    text_node_2 = TextNode("This is some anchor text",TextType.LINK,"https://www.boot.dev")
    html_node = HTMLNode("tag", "value",[HTMLNode("tag-child","value-child"),HTMLNode("tag-child","value-child")], {"href": "https://www.google.com",
    "target": "_blank",})
    print(html_node.props_to_html())
    print(text_node.__eq__(text_node_2))
    print(text_node)
    print(html_node)


main()