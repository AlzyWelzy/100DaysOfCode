import os
import shutil
import pathlib
import json


class Organize:
    def __init__(self):
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

        self.create_dir = [
            "images",
            "docs",
            "audios",
            "videos",
            "others",
        ]

        self.data_path = pathlib.Path("extensions_by_type.json")
        with self.data_path.open() as f:
            self.data = json.load(f)

        self.docExts = [ext.lower() for ext in self.data.get("Text")]
        self.imgExts = [ext.lower() for ext in self.data.get("Raster image")]
        self.vidExts = [ext.lower() for ext in self.data.get("Video")]
        self.audExts = [ext.lower() for ext in self.data.get("Audio")]

        self.otherExts = sum(
            [
                [
                    e.lower()
                    for e in self.data[ext]
                    if ext
                    not in [
                        "Text",
                        "Raster image",
                        "Video",
                        "Audio",
                    ]
                ]
                for ext in self.data.keys()
            ],
            [],
        )

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

    def organize(self):
        files = os.listdir()

        for file in self.not_to_move:
            files.remove(file)

        for directory in self.create_dir:
            self.create_directory(directory)

        images = [
            file for file in files if os.path.splitext(file)[1].lower() in self.imgExts
        ]

        docs = [
            file for file in files if os.path.splitext(file)[1].lower() in self.docExts
        ]

        vids = [
            file for file in files if os.path.splitext(file)[1].lower() in self.vidExts
        ]

        auds = [
            file for file in files if os.path.splitext(file)[1].lower() in self.audExts
        ]

        others = [
            file
            for file in files
            if os.path.splitext(file)[1].lower()
            not in (self.vidExts + self.audExts + self.docExts + self.imgExts)
            and os.path.isfile(file)
        ]

        self.move_files(images, "images")
        self.move_files(docs, "docs")
        self.move_files(vids, "videos")
        self.move_files(auds, "audios")
        self.move_files(others, "others")


def main():
    organize = Organize()
    organize.organize()


if __name__ == "__main__":
    main()
