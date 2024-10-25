from moviepy.editor import *

def MP4toMP3(mp4, mp3):
    file_mp4 = AudioFileClip(mp4)
    file_mp4.write_audiofile(mp3)
    file_mp4.close()


def main():
    file_name: str = input("Enter an audiofile: ")
    input_file = "process_data\\data_vid\\{}".format(file_name)
    new_input_file = input_file[:-4]+".mp3"
    if(file_name[:-4]==".mp4"):
        MP4toMP3(input_file, new_input_file)
        print("complete")
    else:
        print("complete")

if __name__=="__main__":
    main()