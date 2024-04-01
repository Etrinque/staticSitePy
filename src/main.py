import os
import shutil
import logging

from copystatic import copy_files_to_static
from gencontent import gen_page

dir_public = "./public"
dir_static = "./static"
dir_content = "./content"
dir_template = "./template.html"


def main():
    print("Deleting public dir...")
    if os.path.exists(dir_public):
        shutil.rmtree(dir_public)

    print("Copying static site to new Public Directory...")
    copy_files_to_static(dir_static, dir_public)

    print("Generating Page...")
    gen_page(
        os.path.join(dir_content, "index.md"),
        dir_template,
        os.path.join(dir_public, "index.hmtl"),
    )

main()
