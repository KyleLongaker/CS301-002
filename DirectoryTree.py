## Group Members: Katelyn Juhl, Kyle Longaker

class DirectoryNode:
    def __init__(self, data):
        self.data = data
        self.children = {}
        self.parent = None
#########################################################
class DirectoryTree:
    def __init__(self, root='/'):
        self.root = DirectoryNode(root)

    def find_node(self, path):
        parts = path.strip('/').split('/')
        current = self.root
        for part in parts:
            if part not in current.children:
                return None
            current = current.children[part]
        return current

    def insert_file(self, path):
        parts = path.strip('/').split('/')
        current = self.root
        for part in parts[:-1]:
            if part not in current.children:
                current.children[part] = DirectoryNode(part)
                current.children[part].parent = current
            current = current.children[part]
        file_name = parts[-1]
        if file_name not in current.children:
            current.children[file_name] = DirectoryNode(file_name)
            current.children[file_name].parent = current
        else:
            raise FileExistsError(f'File {file_name} already exists at {path}')

    def delete_file(self, path):
        node_to_delete = self.find_node(path)
        if node_to_delete is None:
            raise IndexError('File Not Found')
        parent = node_to_delete.parent
        if parent:
            del parent.children[node_to_delete.data]

    def move_file(self, source_path, destination_path):
        source_node = self.find_node(source_path)
        if source_node is None:
            raise IndexError('Source does not exist')

        destination_node = self.find_node(destination_path)
        if destination_node is None:
            raise IndexError('Destination does not exist')

        if source_node.parent:
            del source_node.parent.children[source_node.data]

        destination_node.children[source_node.data] = source_node
        source_node.parent = destination_node

    def print_tree(self, node=None, indent=""):
        if node is None:
            node = self.root
        print(indent + node.data)
        for child in node.children.values():
            self.print_tree(child, indent + "\t")

# Example instantiation and usage of DirectoryTree class
directory_tree = DirectoryTree()
directory_tree.insert_file('/usr/log/log1.log')
directory_tree.insert_file('/var/log/log2.log')
directory_tree.print_tree()

# Now let's fix the file system operations
import os
import shutil

def delete_directory(directory_name):
    try:
        shutil.rmtree(directory_name)
        print(f"Directory {directory_name} has been deleted.")
    except OSError as e:
        print(f"Error: {e.filename} - {e.strerror}.")

def move_renamed_files(source_directory):
    renamed_dir = os.path.join(source_directory, "renamed")
    os.makedirs(renamed_dir, exist_ok=True)

    for root, dirs, files in os.walk(source_directory):
        for file_name in files:
            if file_name.endswith("_renamed.fa"):
                shutil.move(os.path.join(root, file_name), renamed_dir)

# Placeholder for the filelist function which needs to be defined
def filelist(directory):
    # This should return a list of file paths based on your criteria
    return [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.fa')]

# Example usage of file system operations
mydir = input("Enter directory name: ")
delete_directory(mydir)
# move_renamed_files would be called with the specific directory
# move_renamed_files(mydir)

        






























