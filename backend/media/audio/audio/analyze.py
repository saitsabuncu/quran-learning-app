import whisper
from difflib import SequenceMatcher

model = whisper.load_model("base")

def analyze_audio_submission(audio_path, expected_text):
    result = model.transcribe(audio_path, language="ar")
    predicted_text = result['text'].strip()
    similarity = SequenceMatcher(None, expected_text, predicted_text).ratio()
    
    return {
        "expected": expected_text,
        "predicted": predicted_text,
        "similarity": round(similarity * 100, 2)
    }
result = analyze_audio_submission(
    r"C:\Projeler\quran-learning-app\backend\media\audio\fatiha_ayet1.mp3",
    "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"
)
print(result)