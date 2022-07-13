import os
import glob
import subprocess
import pathlib
import shutil, json, math, audio
from utils import *
#!/usr/bin/env python



def TransPic(path, folder ,remove = False, start=1, end =10):
    cwd = os.getcwd()
    result = False
    if path != '':
         list_of_files = filter( os.path.isfile,
                                glob.glob("{path}\\{dir}".format(path=path,dir=folder) + "/*.png") )
         num = start
         #while num < end:
         
         pre_dir       = "{cwddir}\\preview".format(cwddir=path)
         pathlib.Path(pre_dir).mkdir(parents=True, exist_ok=True)
         for file in list_of_files:
             
             img            = "{cwddir}\\pic\\{name}\\image.png".format(cwddir=path,name=num)
             yml            = "{cwddir}\\temp\\asset.yml".format(cwddir=path,name=num)
             path_num       = "{cwddir}\\pic\\{name}\\".format(cwddir=path,name=num)
             pre_pic       = "{cwddir}\\preview\\{name}.png".format(cwddir=path,name=num)
             default_file = "{cwddir}\\temp\\asset.yml".format(cwddir=cwd)
             pathlib.Path(path_num).mkdir(parents=True, exist_ok=True)
             shutil.copy(yml, path_num)
             #ffmpeg -i 632_quest_main_stand_r18_412.png -vf "scale=w=2048:h=2048:force_original_aspect_ratio=1,pad=2048:2048:(ow-iw)/2:(oh-ih)/2:color=black@0" output.png
             ExecProgram("ffmpeg", ["-y","-i" , file , "-vf" ,"scale=w=1024:h=1200:force_original_aspect_ratio=1,pad=1024:1200:(ow-iw)/2:(oh-ih)/2:color=black@0", img], "log.txt")
             
             shutil.copy(img, pre_pic)
             num = num+1

def MakePic(path, remove = False, start=1, end =10):
    cwd = os.getcwd()
    result = False
    if path != '':
         list_of_dir = os.listdir(path)
         num = start
         pre_dir       = "{cwddir}\\preview".format(cwddir=cwd)
         ref_dir       = "{cwddir}\\preview_ref".format(cwddir=cwd)
         mod_dir       = "{cwddir}\\preview_mod".format(cwddir=cwd)
         pathlib.Path(pre_dir).mkdir(parents=True, exist_ok=True)
         pathlib.Path(ref_dir).mkdir(parents=True, exist_ok=True)
         pathlib.Path(mod_dir).mkdir(parents=True, exist_ok=True)
         while num < end:
             for dir in list_of_dir:
                 
                 img            = "{cwddir}\\pic\\{name}\\image.png".format(cwddir=cwd,name=dir)
                 yml            = "{cwddir}\\pic\\{name}\\asset.yml".format(cwddir=cwd,name=dir)
                 pre_pic       = "{cwddir}\\preview\\{name}.png".format(cwddir=cwd,name=num)
                 ref_pic       = "{cwddir}\\preview_ref\\{name}.png".format(cwddir=cwd,name=dir)
                 #mod_pic       = "{cwddir}\\preview_mod\\{name}".format(cwddir=cwd,name=stories[num-1])
                 path_num       = "{cwddir}\\new\\{name}\\_child\sprite".format(cwddir=cwd,name=num)
                 default_path   = "{cwddir}\\new\\{name}".format(cwddir=cwd,name=num)
                 default_file = "{cwddir}\\temp\\asset.yml".format(cwddir=cwd)
                 pathlib.Path(path_num).mkdir(parents=True, exist_ok=True)
                 shutil.copy(img, path_num)
                 shutil.copy(img, pre_pic)
                 shutil.copy(img, ref_pic)
                 #shutil.copy(img, mod_pic)
                 shutil.copy(yml, path_num)
                 shutil.copy(default_file, default_path)

                 num = num+1

                 if num > end:
                     break



def MakeVideo(path, id = 1, asset= None, mod = "Shuangxiu"):
    cwd = os.getcwd()
    result = False
    if path != '':
         list_of_files = filter( os.path.isfile,
                                glob.glob(path + "/*.mp4") )
         list_of_dir = os.listdir(path)
         num = id
         for file in list_of_files:
             #img = "{name}\\image.png".format(name=dir)
             #yml = "{name}\\asset.yml".format(name=dir)
             if asset != None:
                 default_file = asset
             else:
                 default_file = "{path}\\asset.yml".format(path=path)
             default_path = "UI\\{mod}\\Shuangxiu{name}".format(mod=mod, name=num)
             path_num =     "UI\\{mod}\\Shuangxiu{name}".format(mod=mod, name=num)
             vid_name =     "UI\\{mod}\\Shuangxiu{name}\\video.mp4".format(mod=mod, name=num)
             pathlib.Path(path_num).mkdir(parents=True, exist_ok=True)
             #ExecProgram("ffmpeg", ["-i" , file , "-af" ,"volume=-30dB" ,"-filter_complex", "fade=d=0.5, reverse, fade=d=1, reverse","-vcodec" ,"libx264",vid_name], "log.txt")
             ExecProgram("ffmpeg", ["-y","-i" , file , "-af" ,"volume=-5dB", "-vcodec" ,"copy",vid_name], "log.txt")
             #shutil.copy(img, path_num)
             #shutil.copy(yml, path_num)
             shutil.copy(default_file, default_path)
             num = num+1
             #if 
             #shutil.copy(src, dst)
             #break
         return num
def MakeVideoByPath(path = "", id = 1, mod ="Shuangxiu"):
    cwd = os.getcwd()
    result = False
    if path != '':
         list_of_dir = os.listdir(path)
         xmlFile = "{path}\\asset.yml".format(path=path)
         for folder in list_of_dir:
             toPath = "{path}\\{folder}".format(path=path, folder=folder)
             if os.path.isdir(toPath):
                id = MakeVideo(toPath, id, xmlFile, mod)
    return id
def TranscodeVideo(path, remove = False, id = 1):
    cwd = os.getcwd()
    result = False
    if path != '':
         list_of_files = filter( os.path.isfile,
                                glob.glob(path + "/*.mpg") )
         list_of_dir = os.listdir(path)
         num = id
         for file in list_of_files:
             #img = "{name}\\image.png".format(name=dir)
             #yml = "{name}\\asset.yml".format(name=dir)
             default_file = "{path}\\asset.yml".format(path=path)
             default_path = "UI\\Shuangxiu\\Shuangxiu{name}".format(name=num)
             path_num = "UI\\Shuangxiu\\Shuangxiu{name}".format(name=num)
             vid_name = "UI\\Shuangxiu\\Shuangxiu{name}\\video.mp4".format(name=num)
             pathlib.Path(path_num).mkdir(parents=True, exist_ok=True)
             #ExecProgram("ffmpeg", ["-i" , file , "-af" ,"volume=-30dB" ,"-filter_complex", "fade=d=0.5, reverse, fade=d=1, reverse","-vcodec" ,"libx264",vid_name], "log.txt")
             TranscodeVideoToMP4(file, vid_name)
             #ExecProgram("ffmpeg", ["-y", "-i" , file ,"-c:a","mp3", "-c:v","copy", "-f", "mp4" ,vid_name], "log.txt")
             
             #shutil.copy(img, path_num)
             #shutil.copy(yml, path_num)
             shutil.copy(default_file, default_path)
             num = num+1
             #if 
             #shutil.copy(src, dst)
             #break
         return num

def TranscodeVideoOnly(path = "", ext=".mpg", save="trans"):
    cwd = os.getcwd()
    result = False
    if path != '':
         list_of_files = filter( os.path.isfile,
                                glob.glob(path + "/*{ext}".format(ext=ext)) )
         list_of_dir = os.listdir(path)
         num = 1
         for file in list_of_files:
             trans = save
             pathlib.Path(trans).mkdir(parents=True, exist_ok=True)
             #ExecProgram("ffmpeg", ["-y", "-i" , file , "-c:v" ,"h264_nvenc","-c:a","ac3", "-threads" ,"8","-f", "mp4" ,"{path}\\{num}.mp4".format(path=trans, num=num)], "log.txt")
             output = "{path}\\{num}.mp4".format(path=trans, num=num)
             TranscodeVideoToMP4(file, output)
             num = num+1
         return num

def TranscodeVideoLoop(path = "", times = "3", ext=".mpg", id = 1):
    cwd = os.getcwd()
    result = False
    if path != '':
         list_of_files = filter( os.path.isfile,
                                glob.glob(path + "/*{ext}".format(ext=ext)) )
         list_of_dir = os.listdir(path)
         num = id
         for file in list_of_files:
             trans = "trans"
             pathlib.Path(trans).mkdir(parents=True, exist_ok=True)
             output = "{path}\\{num}.mp4".format(path=trans, num=num)
             TranscodeLoopVideo(file, output, times)
             num = num+1
         return num


def TranscodeVideoMerge(path = "", ext=".mpg"):
    cwd = os.getcwd()
    result = False
    if path != '':
         list_of_files = filter( os.path.isfile,
                                glob.glob(path + "/*{ext}".format(ext=ext)) )
         list_of_dir = os.listdir(path)
         videos = []
         for file in list_of_dir:
             base = os.path.basename(file)
             audio_name = os.path.splitext(base)[0]
             audioNum = int(audio_name)
             videos.append(audioNum)
         videos.sort()
         trans = "trans"
         pathlib.Path(trans).mkdir(parents=True, exist_ok=True)
         filename = "{path}\\merge.txt".format(path=trans)
         video = "{path}\\merge.mp4".format(path=trans)
         f = open(filename, "w")
         
         for num in videos:
             input = "'{path}\\{num}{ext}'".format(path=path, num=num, ext=ext)
             f.write("file {input}\n".format(input=input))
         f.close()
         TranscodeMergeVideos(filename, video)
             #break
             #ffmpeg -i video.mp4 -i audio.wav -c:v copy -c:a aac output.mp4
             
         return num
#def AudioResize(audioNum, audioPath, duration, trans):
#    audio = "{path}\\{num}.mp3".format(path=audioPath, num=audioNum)
#    audio_temp1 = "{path}\\{num}_temp.mp3".format(path=trans, num=audioNum)
#    audio_temp = "{path}\\{num}.mp3".format(path=trans, num=audioNum)
#    info = GetInfo(audio)
#    sound_size = float(info["format"]["duration"])
#    size = math.floor(duration/sound_size)
#    ExecProgram("ffmpeg", ["-y","-stream_loop", str(size), "-i" , audio, "-c","copy", "-f", "mp3" ,audio_temp1], "log.txt")
#    ExecProgram("ffmpeg", ["-y", "-i" , audio_temp1,"-ss", "0", "-t",str(duration) ,"-q:a","0", "-map", "a" ,audio_temp], "log.txt")
#    info = GetInfo(audio_temp)
#    duration = float(info["format"]["duration"])
#    return audio_temp, audio_temp1, duration


def TranscodeVideoLoopMergeAudio(path = "", audioPath = "", times = "3", ext=".mpg"):
    cwd = os.getcwd()
    result = False
    if path != '':
         list_of_files = filter( os.path.isfile,
                                glob.glob(path + "/*{ext}".format(ext=ext)) )
         list_of_audio = filter( os.path.isfile,
                                glob.glob(audioPath + "/*.mp3".format(ext=ext)) )
         audios = []
         videos = []
         for file in list_of_audio:
             base = os.path.basename(file)
             audio_name = os.path.splitext(base)[0]
             audioNum = int(audio_name)
             audios.append(audioNum)
         list_of_dir = os.listdir(path)
         for file in list_of_dir:
             base = os.path.basename(file)
             audio_name = os.path.splitext(base)[0]
             audioNum = int(audio_name)
             videos.append(audioNum)
         audios.sort()
         videos.sort()
         num = id
         audioId = 0
         audioNum=audios[audioId]
         audioId = audioId+1
         trans = "trans"
         pathlib.Path(trans).mkdir(parents=True, exist_ok=True)
         for num in videos:
             if num > audioNum:
                if audioId > len(audios):
                    break
                audioNum=audios[audioId]
                audioId = audioId+1

             output = "{cwd}\\{path}\\{num}.mp4".format(cwd=cwd, path=trans, num=num)
             input = "{path}\\{num}{ext}".format(path=path, num=num, ext=ext)
             input_temp = "{path}\\{num}_loop.mp4".format(path=trans, num=num, ext=ext)
             print("input:"+input)
             print("output:"+output)
             ExecProgram("ffmpeg", ["-y","-stream_loop", times, "-i" , input, "-c","copy", "-f", "mp4" ,input_temp], "log.txt")
             info = GetInfo(input_temp)
             duration = float(info["format"]["duration"])
             
             audio_temp, audio_temp1, duration = audio.Resize(audioNum, audioPath, duration, trans)
             
             TranscodeMergeAudioVideo(input_temp, audio_temp, output)
             info = GetInfo(audio_temp)
             os.remove(input_temp)
             os.remove(audio_temp1)
             os.remove(audio_temp)
             #break
             
         return num

def TranscodeAudio(path = "", ext=".mpg", start = 0, end = 1):
    cwd = os.getcwd()
    result = False
    if path != '':
         list_of_files = filter( os.path.isfile,
                                glob.glob(path + "/*{ext}".format(ext=ext)) )
         list_of_dir = os.listdir(path)
         for file in list_of_files:
             trans = "trans"
             base = os.path.basename(file)
             name = os.path.splitext(base)[0]
             pathlib.Path(trans).mkdir(parents=True, exist_ok=True)
             output = "{path}\\{num}.mp3".format(path=trans, num=name)
             TranscodeCutAudio(file, output, start, end)
             #num = num+1
         return 

def TranscodeAudioVideo(path = "", ext=".mpg"):
    cwd = os.getcwd()
    result = False
    if path != '':
         list_of_files = filter( os.path.isfile,
                                glob.glob(path + "/*{ext}".format(ext=ext)) )
         list_of_dir = os.listdir(path)
         for file in list_of_files:
             trans = "trans"
             base = os.path.basename(file)
             name = os.path.splitext(base)[0]
             output = "{cwd}\\{path}\\{num}.mp4".format(cwd=cwd, path=trans, num=name)
             pathlib.Path(trans).mkdir(parents=True, exist_ok=True)
             #ffmpeg -i sample.avi -ss 00:03:05 -t 00:00:45.0 -q:a 0 -map a sample.mp3
             #ExecProgram("ffmpeg", ["-y", "-i" , file,"-ss", str(start), "-t",str(end) ,"-q:a","0", "-map", "a" ,"{path}\\{num}.mp3".format(path=trans, num=name)], "log.txt")
             
             TranscodeAudioToMP3(file, output)
             #num = num+1
         return 

