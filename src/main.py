import os, shutil

def copy_static(source_dir, destination_dir):
    if os.path.exists(destination_dir):
        shutil.rmtree(destination_dir)
    os.mkdir(destination_dir)
    copy_recursive(source_dir, destination_dir)

def copy_recursive(source, destination):
    files = os.listdir(source)
    for file in files:
        if os.path.isfile(os.path.join(source, file)):
            shutil.copy(os.path.join(source, file), destination)
        else:
            os.mkdir(os.path.join(destination, file))
            copy_recursive(os.path.join(source, file), os.path.join(destination, file))

            

def main():
    copy_static('static', 'public')

main()
