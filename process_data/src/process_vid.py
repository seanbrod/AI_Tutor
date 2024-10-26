#use whisper AI and get lectures or videos to break down into text. 
from moviepy.editor import *
import whisper

def transcribe(file, name):
    model = whisper.load_model("medium.en")
    try:
        result = model.transcribe(file)
        output_path  = "process_data\\output_vid"
        with open(output_path + "\\" + name[:-3] + "txt", "w") as f:
            f.write(result["text"]+"\n")
        #print(result["text"])
    except Exception as e:
        print("Error", e)

def main():
    file_name: str = input("Enter an audiofile: ")
    input_file = "process_data\\data_vid\\{}".format(file_name)
    transcribe(input_file, file_name)
    print("complete")

if __name__=="__main__":
    main()
