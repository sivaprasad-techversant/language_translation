# # import required modules
# from pydub import AudioSegment
# AudioSegment.converter = "C:/Users/SIVA/Downloads/ffmpeg-snapshot/ffmpeg"
#
# # assign files
# input_file = "common_voice_en_31832759.mp3"
# output_file = "common_voice_en_31832759.wav"
#
# # convert mp3 file to wav file
# sound = AudioSegment.from_mp3(input_file)
# sound.export(output_file, format="wav")
from pydub import AudioSegment
import os

# assign files
input_file = "C:/Users/SIVA/Techversant Training/speech_recognition/speech_recognition/input/"
output_file = "C:/Users/SIVA/Techversant Training/speech_recognition/speech_recognition/output/"

files = os.listdir(input_file)
for i in files:
# convert mp3 file to wav file
  a = input_file+i
  sound = AudioSegment.from_mp3(a)
  sound.export(output_file+i, format="wav")