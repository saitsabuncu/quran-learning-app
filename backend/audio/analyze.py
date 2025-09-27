import whisper
from difflib import SequenceMatcher

model = whisper.load_model("base")

def analyze_audio_submission(audio_path, expected_text):
    result = model.transcribe(audio_path, language="ar")
    predicted_text = result['text'].strip()
    # Benzerlik oranı
    similarity = SequenceMatcher(None, expected_text, predicted_text).ratio()
    
    # Detaylı farklar
    matcher = SequenceMatcher(None, expected_text, predicted_text)
    differences = []
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "replace":
            differences.append({"type": "mismatch", "expected": expected_text[i1:i2], "predicted": predicted_text[j1:j2]})
        elif tag == "delete":
            differences.append({"type": "missing", "expected": expected_text[i1:i2]})
        elif tag == "insert":
            differences.append({"type": "extra", "predicted": predicted_text[j1:j2]})
            # "equal" olanları atlıyoruz
            
    return {
        "expected": expected_text,
        "predicted": predicted_text,
        "similarity": round(similarity * 100, 2),
        "differences": differences
    }
if __name__ == "__main__":
    result = analyze_audio_submission(
        r"C:\Projeler\quran-learning-app\backend\media\audio\fatiha_ayet1.mp3",
        "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"
    )
    print(result)