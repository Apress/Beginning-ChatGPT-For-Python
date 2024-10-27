from pydub import AudioSegment
import os

# Path to the input audio file
input_audio_path = "audio-example.mp3"

# Load the audio file
audio = AudioSegment.from_mp3(input_audio_path)

# Define segment length (in milliseconds) - 10 minutes
segment_length_ms = 10 * 60 * 1000  # 10 minutes in milliseconds

# Split the audio into segments of ten minutes each
segments = [audio[i:i+segment_length_ms] for i in range(0, len(audio), segment_length_ms)]

# Output directory for saving segments
output_directory = "/path/to/output"

# Ensure output directory exists, create it if necessary
os.makedirs(output_directory, exist_ok=True)

# Process each segment (for example, you can save them to separate files)
for i, segment in enumerate(segments):
    segment.export(os.path.join(output_directory, f"segment_{i}.mp3"), format="mp3")
