import utils
import math, json, os, glob, pathlib

def Resize(audioNum, audioPath, duration, trans):
    audio = "{path}\\{num}.mp3".format(path=audioPath, num=audioNum)
    audio_temp1 = "{path}\\{num}_temp.mp3".format(path=trans, num=audioNum)
    audio_temp = "{path}\\{num}.mp3".format(path=trans, num=audioNum)
    info = utils.GetInfo(audio)
    sound_size = float(info["format"]["duration"])
    size = math.floor(duration/sound_size)
    ExecProgram("ffmpeg", ["-y","-stream_loop", str(size), "-i" , audio, "-c","copy", "-f", "mp3" ,audio_temp1], "log.txt")
    ExecProgram("ffmpeg", ["-y", "-i" , audio_temp1,"-ss", "0", "-t",str(duration) ,"-q:a","0", "-map", "a" ,audio_temp], "log.txt")
    info = utils.GetInfo(audio_temp)
    duration = float(info["format"]["duration"])
    return audio_temp, audio_temp1, duration

#BuildDatabase("G:\\code\\python\\mv_pic\\mv_pic\\finished\\opai")
#utils.LoadDatabase("G:\\code\\python\\mv_pic\\mv_pic\\finished\\opai\\database.json")
#data = MediaInfo(info)
