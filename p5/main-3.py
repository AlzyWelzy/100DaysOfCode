import os
import shutil
import pathlib
import json


class Organizer:
    def __init__(self, source_path="."):
        self.source_path = source_path
        self.destinations = {
            "images": [],
            "docs": [],
            "audios": [],
            "videos": [],
            "others": [],
        }

    def organize(self):
        self.get_file_extensions()

        # create the directories if they don't exist
        for destination in self.destinations:
            if not os.path.exists(destination):
                os.makedirs(destination)

        # move the files to their respective directories
        for filename, ext in self.get_files_by_extension():
            if ext in self.destinations:
                new_path = os.path.join(
                    self.source_path, self.destinations[ext], filename
                )
                shutil.move(os.path.join(self.source_path, filename), new_path)
                print(f"Moved {filename} to {new_path}")
            else:
                print(f"No destination found for file {filename}")

    def get_file_extensions(self):
        with open("extensions_by_type.json") as f:
            extensions_by_type = json.load(f)

        self.extensions = {}
        for file_type, extensions in extensions_by_type.items():
            for extension in extensions:
                self.extensions[extension.lower()] = file_type.lower()

    def get_files_by_extension(self):
        for filename in os.listdir(self.source_path):
            if filename not in self.destinations.values():
                ext = os.path.splitext(filename)[1][1:].lower()
                yield filename, self.extensions.get(ext, "others")


if __name__ == "__main__":
    organizer = Organizer()
    organizer.organize()
