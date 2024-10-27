#use whisper AI and get lectures or videos to break down into text. 
from moviepy.editor import *
import whisper
from conversion import MP4toMP3


def transcribe(file):
    model = whisper.load_model("medium.en")
    try:
        result = model.transcribe(file)
        output_path  = "process_data\\output_vid"
        with open(output_path+"\\output.txt", "w") as f:
            f.write(result["text"]+"\n")
        #print(result["text"])
    except Exception as e:
        print("Error", e)

def main():
    file_name: str = input("Enter an audiofile: ")
    input_file = "process_data\\data_vid\\{}".format(file_name)
    new_input_file = input_file[:-4]+".mp3"
    if(file_name[-4:]==".mp4"):
        MP4toMP3(input_file, new_input_file)
        transcribe(new_input_file)
        print("complete")
    else:
        transcribe(input_file)
        print("complete_nc")

if __name__=="__main__":
    main()
