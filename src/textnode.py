from htmlnode import LeafNode


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def eq(self, other):
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    def repr(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def textnode_to_htmlnode(text_node):
    match text_node.text_type:
        case "text":
            text_type_code = "text"
            leaf_node = LeafNode(None, text_type_code)
            return text_type_code, leaf_node
        case "bold":
            text_type_code = "bold"
            tag = "<b>"
            return LeafNode(tag, text_type_code)
        case "italic":
            text_type_code = "italic"
            tag = "<i>"
            return LeafNode(tag, text_type_code)
        case "code":
            text_type_code = "code"
            tag = "<code>"
            return LeafNode(tag, text_type_code)
        case "link":
            text_type_code = "link"
            tag = "<a>"
            prop = "<href>"
            return LeafNode(tag, text_type_code, prop)
        case "image":
            text_type_code = "image"
            tag = "<img>"
            props = {"src": text_node.url, "alst": text_type_code}
            return LeafNode(tag, "", props)
        case "":
            raise ValueError("no text_type provided")
