import os
from moviepy.editor import VideoFileClip, concatenate_videoclips

# get current directory path
dir_path = os.getcwd()
print("Current directory: " + dir_path)

# list of video file extensions
# video_extensions = [".mts", ".mov"]
video_extensions = [".MTS", ".MOV"]

# compress video with H.264 codec
codec = "libx264"

# list to store video clips
video_clips = []

# iterate over video files in directory
for file in os.listdir(dir_path):
    # check if file has a video extension
    if any(file.endswith(ext) for ext in video_extensions):
        # create VideoFileClip object
        video_clip = VideoFileClip(os.path.join(dir_path, file))
        # append video clip to list of video clips
        video_clips.append(video_clip)

# concatenate video clips and write to new file
final_clip = concatenate_videoclips(video_clips)

# prompt user for output file name and extension
output_name = input("Enter the name for the output video file (without extension): ")
output_ext = input("Enter the file extension for the output video file (e.g. mp4): ")

# save the concatenated video to a file in the same directory as the original video files
output_path = os.path.join(dir_path, output_name + "." + output_ext)
final_clip.write_videofile(output_path, codec=codec)
