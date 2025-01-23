import os.path

class FileManager:

    def __init__(self,file_path):
        self.file_path=file_path


    def read_product_name(self):
        #read the search keyword from the file

        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File not found at : {self.file_path}")

        with open(self.file_path,'r') as file:
            keyword=file.read().strip()
        return keyword




