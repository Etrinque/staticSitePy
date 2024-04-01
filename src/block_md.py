import re
import htmlnode as hn
import textnode as tn
import inline_md as imd

md_paragraph_type = "paragraph"
md_heading_type = "heading"
md_code_type = "code"
md_quote_type = "quote"
md_unordered_type = "unordered_list"
md_ordered_type = "ordered"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks


def markdown_to_htmlnode(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_htmlnode(block)
        children.append(html_node)
    return hn.ParentNode("div", children, None)


def text_to_children(text):
    text_nodes = imd.text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = tn.textnode_to_htmlnode(text_node)
        children.append(html_node)
    return children


def block_to_htmlnode(block):
    block_type = block_to_block_type(block)
    if block_type == md_paragraph_type:
        return paragraph_to_htmlnode(block)
    if block_type == md_heading_type:
        return heading_to_htmlnode(block)
    if block_type == md_code_type:
        return code_to_htmlnode(block)
    if block_type == md_ordered_type:
        return ordered_to_htmlnode(block)
    if block_type == md_unordered_type:
        return unordered_to_htmlnode(block)
    if block_type == md_quote_type:
        return quote_to_htmlnode(block)
    raise ValueError("Invalid block type")


def block_to_block_type(block):
    lines = block.split("\n")

    if (
        block.startswith("# ")
        or block.startswith("## ")
        or block.startswith("### ")
        or block.startswith("#### ")
        or block.startswith("##### ")
        or block.startswith("###### ")
    ):
        return md_heading_type
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return md_code_type
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return md_paragraph_type
        return md_quote_type
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return md_paragraph_type
        return md_unordered_type
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return md_unordered_type
        return md_unordered_type
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return md_paragraph_type
            i += 1
        return md_ordered_type
    return md_paragraph_type


def quote_to_htmlnode(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return hn.ParentNode("blockquote", children)


def unordered_to_htmlnode(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(hn.ParentNode("li", children))
    return hn.ParentNode("ul", html_items)


def ordered_to_htmlnode(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(hn.ParentNode("li", children))
    return hn.ParentNode("ol", html_items)


def paragraph_to_htmlnode(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return hn.ParentNode("p", children)


def code_to_htmlnode(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    children = text_to_children(text)
    code = hn.ParentNode("code", children)
    return hn.ParentNode("pre", [code])


def heading_to_htmlnode(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return hn.ParentNode(f"h{level}", children)
