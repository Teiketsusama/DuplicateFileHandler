import os
import sys


# a root directory, a file extension, and a sort order as input
def find_duplicates(root_dir, file_ext, sort_order):
    file_groups = {}

    # os.walk function to iterate through all files and subdirectories of the root directory
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if not file_ext or filename.endswith(file_ext):
                file_path = os.path.join(dirpath, filename)
                file_size = os.path.getsize(file_path)
                # checks if the current file's size is already a key in the file_groups dictionary
                if file_size in file_groups:
                    # the file is appended to the list
                    file_groups[file_size].append(file_path)
                else:
                    # the file is added as the first item in the list associated with that size as the key
                    file_groups[file_size] = [file_path]

    # key=lambda x: x[0] is a lambda function used as a sorting key. It tells sorted() to sort the key-value pairs by
    # the first element of each pair, which is the size
    if sort_order == "2":
        sorted_groups = sorted(file_groups.items(), key=lambda x: x[0])
    elif sort_order == "1":
        sorted_groups = sorted(file_groups.items(), key=lambda x: x[0], reverse=True)
    else:
        print("Wrong option")
        return

    for group in sorted_groups:
        print(f"{group[0]} bytes")
        for file in group[1]:
            print(file)
        print()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Directory is not specified")
    else:
        root_dir = sys.argv[1]
        file_ext = input("Enter file format:")
        print("Size sorting options:")
        print("1. Descending")
        print("2. Ascending")
        sort_order = input("Enter a sorting option:")
        find_duplicates(root_dir, file_ext, sort_order)
