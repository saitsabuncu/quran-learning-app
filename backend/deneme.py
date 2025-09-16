import whisper


model=whisper.load_model("base") # base / small / medium / large

result = model.transcribe(r"C:\Projeler\quran-learning-app\backend\media\audio\fatiha_ayet1.mp3", language="ar")


