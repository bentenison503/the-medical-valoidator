import os
import librosa


def get_audio_paths(folder_path):
    """Finds all .mp3 files and returns their full paths."""
    all_items = os.listdir(folder_path)
    mp3_only = list(filter(lambda file: file.endswith('.mp3'), all_items))
    full_paths = list(map(lambda file: os.path.join(folder_path, file), mp3_only))
    return full_paths


def analyze_beats(file_path):
    """Loads an audio file and returns the timestamps of the beats."""
    print(f"\n🎧 Loading audio file: {file_path}")

    # 1. Load the audio into mathematical arrays
    y, sr = librosa.load(file_path)

    # 2. Ask librosa to calculate the tempo and find the beat frames
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

    # 3. Convert abstract frames into readable seconds (timestamps)
    beat_timestamps = librosa.frames_to_time(beat_frames, sr=sr)

    # 4. Print the results using array slicing
    print(f"Estimated Tempo: {tempo[0]:.2f} BPM")
    print(f"Total beats found: {len(beat_timestamps)}")
    print(f"First 5 beat drops (in seconds): {beat_timestamps[:5]}")

    return beat_timestamps


# --- Main Execution ---
my_folder = '.'
audio_files = get_audio_paths(my_folder)

# Use a loop to process every file we found
for audio_file in audio_files:
    analyze_beats(audio_file)