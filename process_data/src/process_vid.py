#use whisper AI and get lectures or videos to break down into text. 
import whisper

model = whisper.load_model("turbo")
result = model.transcribe("audio.mp3")
print(result["text"])
