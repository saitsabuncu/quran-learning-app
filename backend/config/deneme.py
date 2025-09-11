from gtts import gTTS

ayet = "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"
tts = gTTS(text=ayet, lang='ar')
tts.save("fatiha_ayet1.mp3")

print("Ses dosyası oluşturuldu!")
