import os
import json
import shutil


def move(fileName, pathTo):
    for i in fileName:
        newPath = pathTo + "/"
        shutil.move(i, newPath)


def createDir(par):
    if not os.path.exists(par):
        os.makedirs(par)
        print(f"Directory {par} doesn't exists, so it has been created.")
    else:
        print(f"Directory {par} already exists.")


files = os.listdir()

files.remove("practice-5.py")
files.remove("extensions_by_type.json")

print(files)

donnotRemove = []

createDir("images")
createDir("docs")
createDir("audio")
createDir("video")
createDir("others")


with open("extensions_by_type.json") as f:
    data = json.load(f)

othExt = []

for ext in data.keys():
    if not (ext == "Text" or ext == "Raster image" or ext == "Video" or ext == "Audio"):
        othExt.append(ext)

print(othExt)

othExts = [i for i in othExt]

docExts = [doc.lower() for doc in data.get("Text")]
imgExts = [doc.lower() for doc in data.get("Raster image")]
vidExts = [doc.lower() for doc in data.get("Video")]
audExts = [doc.lower() for doc in data.get("Audio")]


otherExts = []
for i in othExt:
    lowercase_docs = []
    for doc in data[i]:
        lowercase_docs.append(doc.lower())
    otherExts.append(lowercase_docs)
otherExts = sum(otherExts, [])

images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]

print(images)

docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]

print(docs)

vids = [file for file in files if os.path.splitext(file)[1].lower() in vidExts]

print(vids)

auds = [file for file in files if os.path.splitext(file)[1].lower() in audExts]

print(auds)

others = []

for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (
        (ext not in vidExts)
        and (ext not in audExts)
        and (ext not in docExts)
        and (ext not in imgExts)
        and os.path.isfile(file)
    ):
        others.append(file)

print(others)

move(images, "images")
move(docs, "docs")
move(auds, "audio")
move(vids, "video")
move(others, "others")
