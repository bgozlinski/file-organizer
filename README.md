# File Organizer

File Organizer is a Python tool designed to help organize files in a directory by sorting them into folders based on their file extensions. It also provides functionality to delete subdirectories that do not correspond to any file extension found in the directory.

## Features

- **Sort Files by Extension**: Organizes files into subdirectories named after their extensions.
- **Multithreaded Sorting**: Uses multithreading to improve the efficiency of sorting large numbers of files.
- **Delete Non-Extension Folders**: Removes any subdirectory that doesn't match the set of file extensions present in the directory.

## Requirements

- Python 3.x
- `pathlib` (included in the standard library)
- `threading` (included in the standard library)
- `shutil` (included in the standard library)

## Installation

No additional installation is required as the script uses standard Python libraries. Simply clone this repository or 
download the `file_organizer.py` script.

## Usage

To use the File Organizer, create an instance of the `FileOrganizer` class with the path of the directory you want to 
organize. Then, call the `sort_files` method to sort the files, and optionally call `delete_non_extension_folders` 
if you want to remove non-extension directories.

## Caution

Use the delete_non_extension_folders method with caution, as it will permanently delete directories and their contents 
from the filesystem. Always back up your data before using this functionality.

## License

For more information on the MIT license, you can visit [MIT License](https://opensource.org/licenses/MIT).
This project is licensed under the terms of the MIT license. See the LICENSE file for details.