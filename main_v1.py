import os
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.compositing.concatenate import concatenate_videoclips

# specify directory path and video extensions
dir_path = os.getcwd()
# video_extensions = ('.mov', '.mts')
video_extensions = (".MOV", ".MTS")

# list of video clips
video_clips = []

# iterate over video files in directory
for file in os.listdir(dir_path):
    # check if file has a video extension
    if any(file.endswith(ext) for ext in video_extensions):
        # create VideoFileClip object
        video_clip = VideoFileClip(os.path.join(dir_path, file))
        # compress video clip using H.264 codec and save as mp4
        compressed_clip = video_clip.write_videofile(
            os.path.join(dir_path, os.path.splitext(file)[0] + ".mp4"),
            codec="libx264",
            temp_audiofile="temp-audio.m4a",
            remove_temp=True,
            audio_codec="aac",
        )
        # append compressed clip to list of video clips
        video_clips.append(compressed_clip)
        # close original video clip
        video_clip.close()

# concatenate video clips and save as mp4
final_clip = concatenate_videoclips(video_clips)
final_clip.write_videofile(
    os.path.join(dir_path, "combined.mp4"), codec="libx264", audio_codec="aac"
)

# close final clip
final_clip.close()
