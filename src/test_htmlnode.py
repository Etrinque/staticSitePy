import unittest

from htmlnode import HtmlNode
from htmlnode import LeafNode
from htmlnode import ParentNode


class TestHtmlNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HtmlNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_parent_node_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            None,
        )

        node2 = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
            ],
            None,
        )

        # FAIL HERE
        node3 = ParentNode(
            "p",
            None,
            None,
        )

        node.to_html()
        node2.to_html()
        node3.to_html()


if __name__ == "__main__":
    unittest.main()
