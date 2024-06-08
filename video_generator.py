import openai
import re
import os
import subprocess
import urllib.request
import numpy as np
from moviepy.editor import *
from PIL import Image

def generate_video(text):
    # Create Necessary Folders
    os.makedirs("images", exist_ok=True)

    def generate_image(prompt):
        try:
            response = openai.Image.create(prompt=prompt, n=1, size="1024x1024")
            image_url = response['data'][0]['url']
            return image_url
        except Exception as e:
            print(f"Error generating image: {e}")
            return "https://via.placeholder.com/1024x1024.png?text=Story+Image"

    # Split the story into segments (by sentences, then combine if too many)
    sentences = re.split(r'(?<=[.!?])\s+', text)
    max_segments = 10

    if len(sentences) <= max_segments:
        segments = sentences
    else:
        # Combine sentences into larger segments
        avg_sentences_per_segment = len(sentences) // max_segments
        segments = []
        current_segment = ""
        for sentence in sentences:
            current_segment += sentence + " "
            if len(current_segment.split()) >= avg_sentences_per_segment:
                segments.append(current_segment.strip())
                current_segment = ""
        if current_segment:
            segments.append(current_segment.strip())

    # Ensure only 10 segments are used
    segments = segments[:10]

    segment_images = []
    print(f"Generating {len(segments)} AI Images for the story segments...")
    for i, segment in enumerate(segments, 1):
        image_prompt = segment[:1000] if len(segment) > 1000 else segment
        image_url = generate_image(image_prompt)
        image_path = f"images/segment_image_{i}.jpg"
        urllib.request.urlretrieve(image_url, image_path)
        segment_images.append(image_path)
        print(f"Image {i} saved: {image_path}")

    # Convert text to speech using macOS 'say' command
    print("Converting story to speech...")
    with open("story_text.txt", "w", encoding="utf-8") as file:
        file.write(text)

    subprocess.run(["say", "-v", "Samantha", "-f", "story_text.txt", "-o", "story_audio.aiff"])
    print("Story audio saved as story_audio.aiff")

    # Convert .aiff to .mp3 for compatibility
    subprocess.run(["ffmpeg", "-i", "story_audio.aiff", "-acodec", "libmp3lame", "-q:a", "2", "story_audio.mp3"])
    print("Converted story_audio.aiff to story_audio.mp3")

    # Create video
    print("Creating video...")
    audio = AudioFileClip("story_audio.mp3")

    # Calculate video size for 16:9 aspect ratio
    video_width, video_height = 1280, 720

    # Create clips for each segment
    segment_durations = [len(seg.split()) / 3 for seg in segments]  # Rough estimate: 3 words per second
    total_duration = sum(segment_durations)
    scale = audio.duration / total_duration

    segment_clips = []
    for i, (image_path, duration, segment_text) in enumerate(zip(segment_images, segment_durations, segments)):
        image = Image.open(image_path)
        image = image.resize((int(image.width * video_height / image.height), video_height), Image.Resampling.LANCZOS)
        image_clip = ImageClip(np.array(image)).set_duration(duration * scale).set_position("center")

        text_clip = TextClip(segment_text, fontsize=24, color='white', font='Arial',
                            size=(video_width * 0.8, None), method='caption')
        text_clip = text_clip.set_position(('center', 'bottom')).set_duration(duration * scale)

        clip = CompositeVideoClip([image_clip, text_clip], size=(video_width, video_height))
        segment_clips.append(clip)

    # Concatenate all clips
    final_clip = concatenate_videoclips(segment_clips).set_audio(audio)

    # Write final video
    print("Rendering final video...")
    final_clip.write_videofile("final_story_video.mp4", fps=24, codec='libx264')
    print("The Final Video Has Been Created Successfully!")

    # Clean up temporary files
    for file in ["story_text.txt", "story_audio.aiff", "story_audio.mp3"] + segment_images:
        if os.path.exists(file):
            os.remove(file)
    print("Temporary files cleaned up.")