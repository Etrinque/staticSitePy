class HtmlNode:
    def __init__(self, tag, value, children, props):
        self.tag = tag  # str
        self.value = value  # str
        self.children = children  # list
        self.props = props  # dict

    def to_html(self):
        raise NotImplementedError(
            "to_html method not implemented"
        )  # child will override

    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html

    def repr(self):
        return f"HtmlNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HtmlNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HtmlNode: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value},{self.props})"


class ParentNode(HtmlNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HtmlNode: No tag provided")
        if self.children is None:
            raise ValueError("Invalid HtmlNode: No child node present")
        child_html = ""
        for child in self.children:
            child_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}> {child_html} </{self.tag}>"

    def repr(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
