
from copystatic import copy_static
from generate_page import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"


def main():
    copy_static(dir_path_static, dir_path_public)
    generate_pages_recursive('content', 'template.html', 'public')

main()