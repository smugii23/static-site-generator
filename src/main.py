import os, shutil

def copy_static(source_dir, destination_dir):
    if os.path.exists(destination_dir):
        shutil.rmtree(destination_dir)
        os.mkdir(destination_dir)
            

def main():
    print(TextNode("This is a text node", TextType.BOLD_TEXT, "https://www.boot.dev "))

main()
