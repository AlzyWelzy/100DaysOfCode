from moviepy.editor import VideoFileClip, concatenate_videoclips

# directory path
dir_path = '/path/to/directory'

# list of video file extensions
video_extensions = ['.mts', '.mov']

# compress video with H.264 codec
codec = 'libx264'

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
final_clip.write_videofile(os.path.join(dir_path, 'combined_video.mp4'), codec=codec)
