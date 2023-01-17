import os

class Storage:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def list_files(self):
        return os.listdir(self.folder_path)

    def read_file(self, filename):
         if os.path.isfile(os.path.join(self.folder_path, filename)):
            with open(os.path.join(self.folder_path, filename), 'r') as file:
                return file.read()

    def write_file(self, filename, content):
            with open(os.path.join(self.folder_path, filename), 'w') as file:
                file.write(content)

    def get_file_name(self, filename):
        return os.path.basename(filename)

    def change_file_extension(self, file, newextension):
        file_name, file_ext = os.path.splitext(file)
        # new file name and extension
        new_file_name = file_name + '_new'
        new_file_ext = newextension
        # join the new file name and extension
        return  os.path.join(self.folder_path,new_file_name+new_file_ext)