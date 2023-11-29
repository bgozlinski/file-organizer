from file_organizer import FileOrganizer


if __name__ == '__main__':
    try:
        dir_to_sort = 'Bałagan'

        sorter = FileOrganizer(dir_to_sort)
        extensions = sorter.get_extensions_from_dir()
        print(extensions)
        sorter.sort_files()
        sorter.delete_non_extension_folders()

    except ValueError as e:
        print(e)
