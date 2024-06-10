🎬 AI-Powered Text-to-Video Generator
Transform a simple text prompt into a captivating video with AI-generated story, images, and audio.

# 🚀 <b>Overview</b><br>
This project automates the creation of engaging videos from text prompts. It uses OpenAI's GPT-3.5 to generate a story, OpenAI's Image API to visualize key moments, and combines these with audio narration into a final video.

https://github.com/rhea164/text_to_video/assets/158840696/bbf1bbb5-2f30-4337-9a9a-595b65968091


# ✨ Features

• 📝 <b>Story Generation</b>: OpenAI's GPT-3.5 crafts a narrative from your prompt.<br>
• 🖼️ <b>Image Creation</b>: OpenAI's Image API generates visuals for story segments.<br>
• 🔊 <b>Audio Narration</b>: Text-to-speech conversion (macOS say command).<br>
• 🎥 <b>Video Compilation</b>: MoviePy combines images, captions, and audio.<br>
• 🌐 <b>Web Interface:</b> Streamlit provides an easy-to-use web app.<br>

# 🛠️ Tech Stack

• <b>Python</b>: Core programming language.<br>
• <b>OpenAI API</b>:<br>
  • gpt-3.5-turbo-instruct for story generation.<br>
  • Image.create for image generation.<br>
• <b>MoviePy</b>: Video editing library.<br>
• <b>FFmpeg</b>: Audio conversion (AIFF to MP3).<br>
• <b>Pillow (PIL)</b>: Image processing.<br>
• <b>NumPy</b>: Array operations for image handling.<br>
• <b>Streamlit:</b> Web app framework.

# 🔧 How It Works
1.<b>app.py:</b> Streamlit web interface.<br>
•User enters a prompt.<br>
•Calls text_generator.py and video_generator.py.<br>
•Displays generated text and video.<br>
1.<b>text_generator.py:</b> Takes a prompt, generates a story using GPT-3.5.<br>
2.<b>video_generator.py:</b><br>
• Splits story into max 10 segments.<br>
• For each segment:<br>
  • OpenAI Image API creates an image.<br>
  • say command narrates text (AIFF).<br>
  • FFmpeg converts AIFF to MP3.<br>
• MoviePy assembles images, captions, and audio.
# 🚦 Getting Started
1.<b>Clone this repository.</b><br>
2.<b>Install Python dependencies:</b><br>
 pip install -r requirements.txt<br>
3.<b>Install system dependencies:</b><br>
 <b>macOS:</b> brew install ffmpeg<br>
 <b>Ubuntu/Debian:</b> sudo apt-get install ffmpeg<br>
 <b>Windows:</b> Download from FFmpeg, add to PATH.<br>
4.<b>Add your OpenAI API key</b> <br>
5.<b>Run the Streamlit app:</b>
 streamlit run app.py<br>
6.<b>open displayed URL and enter the prompt</b><br>

Run: python text_generator.py<br>
python video_generator.py<br>

⚠️ Note for Non-macOS Users
The audio narration uses macOS's say command. For other platforms, consider gTTS or pyttsx3.

# 🔍 Key Files
• <b>app.py:</b> Streamlit web interface.<br>
• <b>text_generator.py:</b> Story generation.<br>
• <b>video_generator.py:</b> Image, audio, and video creation.<br>
• <b>.env:</b> Secure OpenAI API key storage.<br>

# 🎓 Learning Points
• <b>Full-stack AI:</b> OpenAI for text and images, system tools for audio.<br>
• <b>Web Dev with AI:</b> Integrating Streamlit for a user-friendly AI interface.<br>
• <b>Security:</b> Using python-dotenv for safe API key management.<br>
• <b>Media Manipulation:</b> Handling text, images, and audio with Python.<br>

# 🤝 Contributing
Contributions welcome! Fork and submit a PR.

