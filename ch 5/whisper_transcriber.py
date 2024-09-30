import os
import openai
from dotenv import load_dotenv

def transcribe_mp3_files(openai_api_key, mp3_folder_path):
    # Set OpenAI API key
    openai.api_key = openai_api_key

    # Model used for transcription
    model = "whisper-1"

    # Desired format for the transcription response
    response_format = "text"

    # Iterate over each MP3 file in the folder
    for filename in sorted(os.listdir(mp3_folder_path)):
        if filename.endswith(".mp3"):
            file_path = os.path.join(mp3_folder_path, filename)
            try:
                # Read the content of the MP3 file
                with open(file_path, "rb") as f:
                    file_content = f.read()

                # Transcribe the MP3 file
                response = openai.audio.transcriptions.create(
                    file=(filename, file_content),
                    model=model,
                    response_format=response_format
                )
                # Print the entire response object
                print(response)
            except Exception as e:
                print(f"Transcription error for file {filename}: {e}")

def main():
    # Load environment variables from .env file
    load_dotenv()

    # API key for OpenAI
    openai_api_key = os.getenv("OPENAI_API_KEY")

    # Folder containing the MP3 files to be transcribed
    mp3_folder_path = "/PATH/TO/FOLDER"  # Replace with your MP3 folder path

    # Transcribe MP3 files
    transcribe_mp3_files(openai_api_key, mp3_folder_path)

if __name__ == "__main__":
    main()
