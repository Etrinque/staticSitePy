import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("this is a TEST","str","text")
        node2 = TextNode("this is a TEST","str","text")
        self.assertEqual(node.repr(), node2.repr())

    def test_uneq(self):
        node = TextNode("this is a TEST","str","text")
        node2 = TextNode("this is a TEST failure","str","")
        self.assertNotEqual(node.repr(), node2.repr())

if __name__ == "__main__":
    unittest.main()