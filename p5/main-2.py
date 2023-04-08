import os
import shutil
import pathlib
import json


class FileOrganizer:
    def __init__(self, source_path="."):
        self.source_path = pathlib.Path(source_path)
        self.not_to_move = [
            "main.py",
            "main-2.py",
            "main-3.py",
            "problem-5.py",
            "problem-5-fp.py",
            "problem-5-oop.py",
            "practice-5.py",
            "practice-5-v2.py",
            "practice-5-oop.py",
            "extensions_by_type.json",
        ]
        self.extensions_by_type = self.load_extensions_by_type()
        self.extensions = self.get_extensions()

    def load_extensions_by_type(self):
        with open("extensions_by_type.json") as f:
            return json.load(f)

    def get_extensions(self):
        extensions = {
            "Text": self.extensions_by_type.get("Text", []),
            "Raster image": self.extensions_by_type.get("Raster image", []),
            "Video": self.extensions_by_type.get("Video", []),
            "Audio": self.extensions_by_type.get("Audio", []),
            "Other": [],
        }
        for ext in self.extensions_by_type.keys():
            if ext not in extensions:
                extensions["Other"].extend(self.extensions_by_type[ext])
        return extensions

    def create_directory(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Directory {directory} doesn't exist, so it has been created.")
        else:
            print(f"Directory {directory} already exists.")

    def move_files(self, file_names, destination_path):
        for file in file_names:
            try:
                new_path = destination_path + "/"
                shutil.move(file, new_path)
            except Exception as e:
                print(f"Error: {e}")
            else:
                print(f"Moved {file} to {new_path}")
            finally:
                print("Done.")

    def organize_files(self):
        files = list(self.source_path.glob("*"))
        files = [file for file in files if file.name not in self.not_to_move]
        files_by_extension = {ext: [] for ext in self.extensions.keys()}
        for file in files:
            ext = file.suffix.lower()[1:]
            if ext in self.extensions["Text"]:
                files_by_extension["Text"].append(file)
            elif ext in self.extensions["Raster image"]:
                files_by_extension["Raster image"].append(file)
            elif ext in self.extensions["Video"]:
                files_by_extension["Video"].append(file)
            elif ext in self.extensions["Audio"]:
                files_by_extension["Audio"].append(file)
            else:
                files_by_extension["Other"].append(file)
        for directory in self.extensions.keys():
            if not directory:
                continue
            self.create_directory(directory)
            destination_path = self.source_path / directory
            self.move_files(files_by_extension[directory], str(destination_path))


def main():
    organizer = FileOrganizer()
    organizer.organize_files()


if __name__ == "__main__":
    main()
