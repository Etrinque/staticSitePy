import os
from block_md import markdown_to_htmlnode


def gen_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_htmlnode(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace(f"{{Title}}", title)
    template = template.replace(f"{{Content}}", html)

    dest_dir = os.path.dirname(dest_path)
    if dest_dir != "":
        os.makedirs(dest_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("No title found")
