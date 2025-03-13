import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("tag", "value", [HTMLNode("tag-child","value-child"), HTMLNode("tag-child","value-child")],{"href": "https://www.google.com","target": "_blank",})
        node2 = HTMLNode("tag", "value", [HTMLNode("tag-child","value-child"), HTMLNode("tag-child","value-child")],{"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(node, node2)
    
    def test_empty_eq(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node, node2)
    
    def test_fail(self):
        node = HTMLNode("value")
        node2 = HTMLNode()
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode("tag", "value", [HTMLNode("tag-child","value-child"), HTMLNode("tag-child","value-child")],{"href": "https://www.google.com","target": "_blank",})
        print(node.props_to_html)
        self.assertEqual(" href=\"https://www.google.com\" target=\"_blank\"",node.props_to_html())

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )
    

if __name__ == "__main__":
    unittest.main()