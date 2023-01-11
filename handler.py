import os
import sys


def find_duplicates(root_dir, file_ext, sort_order):
    file_groups = {}

    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if not file_ext or filename.endswith(file_ext):
                file_path = os.path.join(dirpath, filename)
                file_size = os.path.getsize(file_path)
                if file_size in file_groups:
                    file_groups[file_size].append(file_path)
                else:
                    file_groups[file_size] = [file_path]

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
