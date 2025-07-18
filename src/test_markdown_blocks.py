import unittest
from markdown_blocks import *



class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    
    def test_markdown_to_blocks_multiple_newlines_and_usless_spaces(self):
        md = """
This is **bolded** paragraph                                                      



This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_block_type_code(self):
        block = "```code```"
        block_type = block_to_block_type(block)
        self.assertEqual(
            block_type,
            BlockType.CODE,
        )

    def test_markdown_to_block_type_code_fail(self):
        block = "`code`"
        block_type = block_to_block_type(block)
        self.assertNotEqual(
            block_type,
            BlockType.CODE,
        )

    def test_markdown_to_block_type_heading(self):
        block = "### heading"
        block_type = block_to_block_type(block)
        self.assertEqual(
            block_type,
            BlockType.HEADING,
        )

    def test_markdown_to_block_type_heading_fail(self):
        block = "####### heading"
        block_type = block_to_block_type(block)
        self.assertNotEqual(
            block_type,
            BlockType.HEADING,
        )

    def test_markdown_to_block_type_quote(self):
        block = """> quote\n> quote\n> quote"""
        block_type = block_to_block_type(block)
        self.assertEqual(
            block_type,
            BlockType.QUOTE,
        )

    def test_markdown_to_block_type_quote_fail(self):
        block = """> quote\n- quote\n> quote"""
        block_type = block_to_block_type(block)
        self.assertNotEqual(
            block_type,
            BlockType.QUOTE,
        )
    


    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "- list\n- items"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)



if __name__ == "__main__":
    unittest.main()
