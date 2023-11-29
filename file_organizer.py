from pathlib import Path
from threading import Thread
import shutil


class FileOrganizer:
    def __init__(self, path):
        self.dir_to_sort = Path(path)
        if not self.dir_to_sort.is_dir():
            raise ValueError(f'The directory {self.dir_to_sort} does not exist.')

    def get_extensions_from_dir(self):
        """
        Returns a set of unique file extensions in the directory.
        """
        extensions = set()
        for file_path in self.dir_to_sort.glob('**/*'):
            if file_path.is_file():
                extensions.add(file_path.suffix.lstrip('.').lower()) or 'no_extension'
        return extensions

    def move_file_to_extension_dir(self, file_path):
        """
        Moves a file to a directory named after its extension.
        """
        if not file_path.is_file():
            return

        extension = file_path.suffix.lstrip('.').lower() or 'no_extension'
        extension_dir = self.dir_to_sort / extension
        extension_dir.mkdir(exist_ok=True)

        try:
            file_path.rename(extension_dir / file_path.name)
        except Exception as e:
            print(f'Error moving file {file_path.name}: {e}')

    def sort_files(self):
        """
        Sorts files in the directory by their extensions using threads.
        """
        files = [f for f in self.dir_to_sort.glob('**/*') if f.is_file()]
        threads = []
        for file_path in files:
            print(file_path)
            thread = Thread(target=self.move_file_to_extension_dir, args=(file_path,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    def delete_non_extension_folders(self):
        """
        Deletes subdirectories that are not named after file extensions present in the directory.
        """
        valid_extensions = self.get_extensions_from_dir()
        subdirectories = [d for d in self.dir_to_sort.iterdir() if d.is_dir()]

        for subdir in subdirectories:
            if subdir.name not in valid_extensions and subdir.name != 'no_extension':
                try:
                    shutil.rmtree(subdir)
                    print(f"Deleted non-extension directory: {subdir}")
                except Exception as e:
                    print(f"Error deleting non-extension directory {subdir}: {e}")






