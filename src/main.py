
from copystatic import copy_static
from generate_page import generate_page

dir_path_static = "./static"
dir_path_public = "./public"


def main():
    copy_static(dir_path_static, dir_path_public)
    generate_page('content/index.md', 'template.html', 'public/index.html')

main()