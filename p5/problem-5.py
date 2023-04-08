import os
import json
import shutil


def move(fileName, pathTo):
    for i in fileName:
        newPath = pathTo+"/"
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


# imgExts = ["." + exts for exts in rawImgExts]
# print(imgExts)

# with open("imgExts.txt", "a") as f:
#     f.write("\n".join(imgExts))

with open("extensions_by_type.json") as f:
    data = json.load(f)


# with open("imgExts.txt") as f:
#     lines = f.readlines()

# for line in lines:
#     imgExts.append(line.replace("\n", ""))

# print(imgExts)

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
# otherExts = [doc.lower() for doc in data.get(i for i in othExt)]
# otherExts = sum([[doc.lower() for doc in data[i]] for i in othExt], [])

otherExts = []
for i in othExt:
    lowercase_docs = []
    for doc in data[i]:
        lowercase_docs.append(doc.lower())
    otherExts.append(lowercase_docs)
otherExts = sum(otherExts, [])


############

images = [file for file in files if os.path.splitext(file)[
    1].lower() in imgExts]

print(images)

docs = [file for file in files if os.path.splitext(file)[
    1].lower() in docExts]

print(docs)

vids = [file for file in files if os.path.splitext(file)[
    1].lower() in vidExts]

print(vids)

auds = [file for file in files if os.path.splitext(file)[
    1].lower() in audExts]

print(auds)

#############


# print(os.path.splitext(files[2]))


# print(data)
# print(type(data))
# print(data.keys())


# print(docExts)

# if ".doc" in docExts:
#     print("YES")

# print(otherExts)
# print(len(otherExts))

others = []

for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in vidExts) and (ext not in audExts) and (ext not in docExts) and (ext not in imgExts) and os.path.isfile(file):
        others.append(file)

print(others)

# others = [file for file in files if os.path.splitext(file)[1].lower() not in vidExts and os.path.splitext(file)[1].lower() not in audExts and os.path.splitext(file)[1].lower() not in docExts and os.path.splitext(file)[1].lower() not in imgExts and os.path.isfile(file)]

# print(otherExts)

# print(len(otherExts))


# for i in images:
#     newPath = "images/"
#     shutil.move(i, newPath)

# for i in docs:
#     newPath = "docs/"
#     shutil.move(i, newPath)

# for i in vids:
#     newPath = "video/"
#     shutil.move(i, newPath)

# for i in auds:
#     newPath = "audio/"
#     shutil.move(i, newPath)

# for i in others:
#     newPath = "others/"
#     shutil.move(i, newPath)

move(images, "images")
move(docs, "docs")
move(auds, "audio")
move(vids, "video")
move(others, "others")
