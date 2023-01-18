import os
import sys
import hashlib


def get_size_paths(root_dir: str, file_ext: str, reverse: bool):
    file_groups = {}

    # os.walk function to iterate through all files and subdirectories of the root directory
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if not file_ext or filename.endswith(file_ext):
                file_size = os.path.getsize(file_path)
                # checks if the current file's size is already a key in the file_groups dictionary
                if file_size in file_groups:
                    # the file is appended to the list
                    file_groups[file_size].append(file_path)
                else:
                    # the file is added as the first item in the list associated with that size as the key
                    file_groups[file_size] = [file_path]
    return dict(sorted(file_groups.items(), key=lambda x: x[0], reverse=reverse))


def show_size_paths(file_groups: dict):
    for size, group in file_groups.items():
        print(f"{size} bytes")
        for file in group:
            print(file)
        print()


def get_size_hash_paths(file_groups: dict):
    hash_groups = {}
    for file_size, file_paths in file_groups.items():
        if len(file_paths) > 1:
            hash_groups[file_size] = {}
            for file in file_paths:
                with open(file, "rb") as f:
                    file_hash = hashlib.md5(f.read()).hexdigest()
                if file_hash in hash_groups[file_size]:
                    hash_groups[file_size][file_hash].append(file)
                else:
                    hash_groups[file_size][file_hash] = [file]
    return hash_groups


def show_size_hash_paths(hash_groups: dict):
    file_count = 1
    for file_size, hashes in hash_groups.items():
        print(f"\n{file_size} bytes")
        for hash, file_paths in hashes.items():
            if len(file_paths) > 1:
                print(f"Hash: {hash}")
                for file in file_paths:
                    print(f"{file_count}. {file}")
                    file_count += 1


def main():
    file_ext = input("Enter file format:\n")
    print("Size sorting options:", "1. Descending", "2. Ascending\n", sep="\n")
    while (sort_order := input("Enter a sorting option:\n")) not in "12":
        print("Wrong option\n")
    reverse = sort_order == "1"

    sorted_groups = get_size_paths(root_dir, file_ext, reverse)
    show_size_paths(sorted_groups)

    while (check_duplicates := input("\nCheck for duplicates?\n")) not in ("yes", "no"):
        print("Wrong option\n")
    check_duplicates = check_duplicates == "yes"

    if check_duplicates:
        hash_groups = get_size_hash_paths(sorted_groups)
        show_size_hash_paths(hash_groups)


if __name__ == "__main__":
    try:
        root_dir = sys.argv[1]
    except IndexError:
        print("Directory is not specified")
        sys.exit()
    else:
        main()
