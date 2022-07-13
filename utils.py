import argparse
import subprocess
import sys, json, os, glob, pathlib, math
from pathlib import Path
from typing import NamedTuple
def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())
def json2obj(data): return json.loads(data, object_hook=_json_object_hook)
class Stream:
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)
    def update(self, data):
        self.__dict__.update(data)
    def GetDict(self):
        return self.__dict__
class MediaInfo:
    video = None
    audio = None
    filename = ""
    duration = 0
    dir = ""
    def __init__(self, data = None):
        if data == None:
            return
        if 'format' in data:
            self.__dict__.update(data["format"])
        else:
            self.__dict__.update(data)
        if "dir" not in data:
            self.dir = str(self.GetDir())
        if "audio" in data:
            self.audio = Stream() 
            self.audio.update(data["audio"])
        if "video" in data:            
            self.video = Stream() 
            self.video.update(data["video"])
        if "streams" in data:
            for stream in data["streams"]:
                if stream["codec_type"] == "audio":
                    self.audio = Stream() 
                    self.audio.update(stream)
                if stream["codec_type"] == "video":
                    self.video = Stream() 
                    self.video.update(stream)
    def GetDict(self):
        if self.video != None:
            self.video = self.video.GetDict()
            
        if self.audio != None:
            self.audio = self.audio.GetDict()
        return self.__dict__
    def GetDir(self):
        return pathlib.Path(self.filename).parent
    def OnlyVideo(self):
        return self.video != None and self.audio == None
    def OnlyAudio(self):
        return self.video == None and self.audio != None

def GetVideoFileFromDir(dir, files):
    list_of_files = filter( os.path.isfile,
                                    glob.glob("{path}\\".format(path=dir) + "/*.mp4") )
    for file in list_of_files:
        files.append(file)
    return files
def GetAudioFileFromDir(dir, files):
    list_of_files = filter( os.path.isfile,
                                    glob.glob("{path}\\".format(path=dir) + "/*.ogg") )
    for file in list_of_files:
        files.append(file)
    return files
def GetFiles(path, files):
    list_of_dir = filter( os.path.isdir,
                                glob.glob("{path}\\*".format(path=path)) )
    for dir in list_of_dir:
        files = GetVideoFileFromDir(dir, files)
        files = GetAudioFileFromDir(dir, files)
        files = GetFiles(dir, files)
    return files

def BuildDatabase(path):
    files = GetFiles(path, [])
    data = {'only_video':{},'only_audio':{},'all':{}}
    json_data = []
    for file in files:
        info = GetInfo(file)
        media = MediaInfo(info)
        media.duration = float(media.duration)
        time = math.ceil(media.duration)
        name = str(time)
        media_data = media.GetDict()
        if name not in data["all"]:
            data["all"][name] = []
            data["only_video"][name] = []
            data["only_audio"][name] = []
        if media.OnlyVideo() == False and media.OnlyAudio() == False:
            data["all"][name].append(media_data)
        elif media.OnlyVideo():
            data["only_video"][name].append(media_data)
        elif media.OnlyAudio():
            data["only_audio"][name].append(media_data)
    name = "{path}\\database.json".format(path=path)
    Save(name, data)
def find_cost_low_audio(audios, video, count = 1):
    #audio_duration = float(audio.duration)
    video_duration = float(video.duration)
    loop_size = video_duration*count
    audio = None
    
    #if video_duration < audio_duration:
    try:
        if video_duration > 20:
            #aus = sorted(audios, reverse=lambda d: d.duration)
            au = next(item for item in audios if video_duration > item.duration and math.floor(video_duration-item.duration)<6 and item.count < 2)
        else:
            au = next(item for item in audios if loop_size > item.duration and (math.floor(loop_size-item.duration))<1 and item.count < 3)
        if au != None:
            print("video_duration: {info}".format(info=video_duration))
            #print("audio_duration: {info}".format(info=audio_duration))
            print("video looped duration: {info}".format(info=loop_size))
            audio_duration = float(au.duration)
            print("new audio_duration: {info}, used: {cnt}".format(info=audio_duration, cnt=au.count))
            au.count = au.count +1
            audio = au
    except:
        return find_cost_low_audio(audios, video, count + 1)
    return audio_duration, count, audio, video_duration

def MergeVideoByAudioDuration(audios, viedos):
    id = 0
    looped = 1
    for video in viedos:
        #audio = audios[id]
        #id = id+1
        #if id % len(audios) == 0:
        #    id = 0
        #    looped = looped+1

        audio_duration, loop, audio, video_duration = find_cost_low_audio(audios, video, 1)
        #continue
        loop_dir = video.dir.replace("opai", "opai_loop")
        merge_dir = video.dir.replace("opai", "opai_merge")
        pathlib.Path(loop_dir).mkdir(parents=True, exist_ok=True)
        pathlib.Path(merge_dir).mkdir(parents=True, exist_ok=True)
    
        vid_loop = video.filename.replace("opai", "opai_loop")
        vid_merge = video.filename.replace("opai", "opai_merge")
        if video_duration < audio_duration:
            TranscodeLoopVideo(video.filename, vid_loop, str(loop))
        else:
            vid_loop = video.filename
        TranscodeMergeAudioVideo(vid_loop, audio.filename, vid_merge)
    count = 0
    for au in audios:
        if au.count == 0:
            print("never used: {name}, {dur}".format(name=au.filename, dur=au.duration))
            count = count+1

    print("never used: {count}, audios:{num}, vidios:{vids}".format(count=count, num=len(audios),vids=len(viedos)))
def LoadDatabase(file):
    viedo_short = []
    viedo_long = []
    viedo_very_long = []
    db = Load(file)
    fast = []
    slow = []

    only_video = db["only_video"]
    only_audio = db["only_audio"]
    all = db["all"]
    
    for key in only_audio:
        for info in only_audio[key]:
            media = MediaInfo(info)
            #media.count = 0
            #fast.append(media)
            #continue
            if "mid" in media.dir:
                media.count = 0
                fast.append(media)
            if "fast" in media.dir:
                media.count = 0
                fast.append(media)
    for key in only_video:
        for info in only_video[key]:
            media = MediaInfo(info)
            time = int(key)
            #if time < 7:
            viedo_short.append(media)
            #elif time < 12:
            #viedo_long.append(media)
            #else:
            #    viedo_very_long.append(media)
    print("short: {num}".format(num=len(viedo_short)))
    audio = sorted(fast, key=lambda d: d.duration)
    video = sorted(viedo_short, key=lambda d: d.duration)
    #MergeVideoByAudioDuration(audio, video)
    return audio, video
    #print("long: {num}".format(num=len(viedo_long)))
    #print("very long: {num}".format(num=len(viedo_very_long)))
    
    
    #MergeVideoByAudioDuration(slow, viedo_long)
    #MergeVideoByAudioDuration(fast, viedo_very_long)
def Save(file, data):
    if data != None:
        with open(file, 'w') as outfile:
            json.dump(data, outfile)
def Load(file):
    with open(file, 'r') as outfile:
        data = json.load(outfile)
    return data
def ExecProgram(program, args, log = None):
    if log != None:
        logFile = open(log, 'w')
    cmd = [program]
    cmd.extend(args)
    process = subprocess.run(
        cmd, stdout=logFile)

    if process.returncode == 0:
        return logFile
    else:
        print(process.stderr)
    return logFile 

class FFProbeResult(NamedTuple):
    return_code: int
    json: str
    error: str


def ffprobe(file_path) -> FFProbeResult:
    command_array = ["ffprobe",
                     "-v", "quiet",
                     "-print_format", "json",
                     "-show_format",
                     "-show_streams",
                     file_path]
    result = subprocess.run(command_array, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8", universal_newlines=True)
    return FFProbeResult(return_code=result.returncode,
                         json=result.stdout,
                         error=result.stderr)
def GetInfo(filename):
    ffprobe_result = ffprobe(file_path=filename)
    if ffprobe_result.return_code == 0:
        # Print the raw json string
        print(ffprobe_result.json)

        # or print a summary of each stream
        d = json.loads(ffprobe_result.json)
        return d

def TranscodeLoopVideo(file, output, times):
    return ExecProgram("ffmpeg", ["-y","-stream_loop", times, "-i" , file, "-c","copy", "-f", "mp4" ,output], "log.txt")

def TranscodeMergeVideos(filename, video):
    return ExecProgram("ffmpeg", ["-y","-f", "concat", "-safe", "0" ,"-i", filename,"-c:a","mp3", "-c:v","copy", "-f", "mp4" ,video], "log.txt")

def TranscodeMergeAudioVideo(input_temp, audio_temp, output):
    #ffmpeg -i video.mp4 -i audio.wav -c:v copy -c:a aac output.mp4
    return ExecProgram("ffmpeg", ["-y","-i", input_temp, "-i" , audio_temp, "-c","copy", "-f", "mp4" ,output], "log.txt")

def TranscodeCutAudio(file, output, start, end):
    #ffmpeg -i sample.avi -ss 00:03:05 -t 00:00:45.0 -q:a 0 -map a sample.mp3
    return ExecProgram("ffmpeg", ["-y", "-i" , file,"-ss", str(start), "-t",str(end) ,"-q:a","0", "-map", "a" , output], "log.txt")

def TranscodeAudioToMP3(file, output):
    return ExecProgram("ffmpeg", ["-y" ,"-i", file,"-c:a","mp3", "-c:v","copy", "-f", "mp4" ,output], "log.txt")

def TranscodeVideoToMP4(file, output):
    return ExecProgram("ffmpeg", ["-y", "-i" , file , "-f", "mp4" , output], "log.txt")