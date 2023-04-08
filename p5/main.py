import os
import json
import shutil


class FileOrganizer:
    def __init__(self):
        with open("extensions_by_type.json") as f:
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
                    if ext not in ["Text", "Raster image", "Video", "Audio"]
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
            new_path = destination_path + "/"
            shutil.move(file, new_path)

    def organize(self):
        files = os.listdir()
        files.remove("main.py")
        files.remove("problem-5-oop.py")
        files.remove("practice-5.py")
        files.remove("practice-5-v2.py")
        files.remove("practice-5-oop.py")
        files.remove("extensions_by_type.json")
        self.create_directory("images")
        self.create_directory("docs")
        self.create_directory("audios")
        self.create_directory("videos")
        self.create_directory("others")

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


organizer = FileOrganizer()
organizer.organize()
