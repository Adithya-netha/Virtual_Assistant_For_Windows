import os
import subprocess
import tempfile
from playsound import playsound  # pip install playsound==1.2.2
import threading


def speak(text: str, voice: str = "Matthew") -> None:
    try:
        # Create a temporary file for the audio output
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmpfile:
            output_file = tmpfile.name

        # Construct the command with the specified voice and text
        command = f'edge-tts --voice "{voice}" --text "{text}" --write-media "{output_file}"'

        # Execute the command
        subprocess.run(command, shell=True, check=True)

        # Define a function to play the sound and clean up the file
        def play_and_cleanup(file_path):
            playsound(file_path)
            os.remove(file_path)

        # Start playback in a separate thread
        threading.Thread(target=play_and_cleanup, args=(output_file,)).start()

    except subprocess.CalledProcessError as e:
        print(f"Subprocess error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
speak("heelo sir iam jarvis")