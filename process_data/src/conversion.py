from moviepy.editor import *

def MP4toMP3(mp4, mp3):
    video = VideoFileClip(mp4)
    video.audio.write_audiofile(mp3)


def main():
    file_name: str = input("Enter an audiofile: ")
    input_file = "process_data/data_vid/{}".format(file_name)
    output_file = input_file[:-4]+".mp3"
    if(file_name[-4:]==".mov"):
        MP4toMP3(input_file, output_file)
        print("complete")
    else:
        print("complete_null")

if __name__=="__main__":
    main()
