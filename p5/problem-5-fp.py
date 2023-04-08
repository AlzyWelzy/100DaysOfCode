import os
import json
import shutil
from functools import partial
from typing import List, Tuple


def create_directory(directory: str) -> None:
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory {directory} doesn't exist, so it has been created.")
    else:
        print(f"Directory {directory} already exists.")


def move_files(file_names: List[str], destination_path: str) -> None:
    for file in file_names:
        new_path = destination_path + "/"
        shutil.move(file, new_path)


def get_files_by_extension(extensions: List[str]) -> List[str]:
    return [file for file in os.listdir() if os.path.splitext(file)[1].lower() in extensions]


def organize(extensions_by_type: dict) -> None:
    files = os.listdir()
    files.remove("extensions_by_type.json")
    create_directory("images")
    create_directory("docs")
    create_directory("audios")
    create_directory("videos")
    create_directory("others")

    move_files(get_files_by_extension(
        extensions_by_type["Raster image"]), "images")
    move_files(get_files_by_extension(extensions_by_type["Text"]), "docs")
    move_files(get_files_by_extension(extensions_by_type["Video"]), "videos")
    move_files(get_files_by_extension(extensions_by_type["Audio"]), "audios")

    others = [file for file in files if os.path.splitext(file)[1].lower(
    ) not in sum(extensions_by_type.values(), []) and os.path.isfile(file)]
    move_files(others, "others")


def main():
    with open("extensions_by_type.json") as f:
        extensions_by_type = json.load(f)
    organize(extensions_by_type)


if __name__ == "__main__":
    main()
