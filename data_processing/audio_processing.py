import librosa
import numpy as np

def process_audio(audio_path: str, sr: int = 22050, duration: float = None) -> np.ndarray:
    """
    Process an audio file by loading it and extracting its features.

    Args:
        audio_path (str): Path to the audio file.
        sr (int): Target sampling rate. Defaults to 22050.
        duration (float): Duration of audio to load in seconds. Defaults to None (load full audio).

    Returns:
        np.ndarray: Mel spectrogram of the processed audio.

    Raises:
        FileNotFoundError: If the specified audio file does not exist.
        ValueError: If the audio cannot be loaded or processed.
    """
    try:
        # Load audio file
        y, _ = librosa.load(audio_path, sr=sr, duration=duration)

        # Extract mel spectrogram
        mel_spec = librosa.feature.melspectrogram(y=y, sr=sr)

        # Convert to log scale
        log_mel_spec = librosa.power_to_db(mel_spec, ref=np.max)

        return log_mel_spec
    except FileNotFoundError:
        raise FileNotFoundError(f"Audio file not found: {audio_path}")
    except Exception as e:
        raise ValueError(f"Error processing audio: {e}")

# Example usage
if __name__ == "__main__":
    try:
        sample_audio_path = "path/to/your/audio.wav"  # Replace with an actual audio path
        processed_audio = process_audio(sample_audio_path, duration=10)  # Process first 10 seconds
        print(f"Processed audio shape: {processed_audio.shape}")
        print(f"Value range: {processed_audio.min():.2f} to {processed_audio.max():.2f} dB")
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
