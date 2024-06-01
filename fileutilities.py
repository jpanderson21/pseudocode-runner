import os

class FileUtilities:
    @classmethod
    def read_file(cls, filepath):
        with open(filepath, "r") as f:
            file_contents = f.read()
        return file_contents

    @classmethod
    def write_file(cls, filepath, contents):
        with open(filepath, "w") as f:
            f.write(contents)

    @classmethod
    def delete_file(cls, filepath):
        os.remove(filepath)

    @classmethod
    def execute_script(cls, filepath):
        with open(filepath, "r") as f:
            exec(f.read())
