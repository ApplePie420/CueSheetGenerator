import os
import traceback
from cuefilegenerator import write_cue_file

version = 1.2

def default_error_msg(stackTrace):
    print("Some error occured. Check logfile and/or post an issue.")
    log = open("log.txt", "w")
    log.write(str(stackTrace))
    log.close()
    exit()
    return 1

def get_audio_files(folder):
    audio_ext = [".mp3", ".m4a", ".ogg", ".opus", ".aac", ".flac", ".wav", ".wma", ".alac"]
    for file in os.listdir(folder):
        if file.endswith(tuple(audio_ext)):
            return file

def get_timestamps(tracklist):
    try:
        # open file
        f = open(tracklist, "r")
        # read lines and split by \n
        content = f.read()
        content = content.split("\n")

        # array to return
        tStamps = []

        # get all timestamps
        for song in content:
            timestamps = song.split(" ")[0]

            #get individually hours, minutes and seconds
            hours =  timestamps.split(":")[0]
            minutes = timestamps.split(":")[1]
            seconds = timestamps.split(":")[2]

            # parse hours into minutes
            if(int(hours) > 0):
                minutes = int(minutes) + int(hours)*60

            # create cuefile timestamp in format MM:SS where MM is minutes, SS seconds
            timestamp = str(minutes) + ":" + str(seconds)
            tStamps.append(timestamp)
        return tStamps
    except:
        track = traceback.format_exc()
        default_error_msg(track)

def get_songs(tracklist):
    try:
        # open file
        f = open(tracklist, "r")
        # read lines and split by \n
        content = f.read()
        content = content.split("\n")

        # array to return
        songs = []

        for song in content:
            track = song[9:]
            songs.append(track)

        return songs
    except:
        track = traceback.format_exc()
        default_error_msg(track)

####################################### main program #####################################
print(".cue sheet generator by N3ttX (github.com/ApplePie420) v" + str(version))
performer = input("Performer: ")
# handle empty performer name
if(performer == ""):
    print("Mixes are done by someone. Please, don't be a dick and write their name here.")
    exit()

path = input("Enter DIRECTORY path where audio file and tracklist is (default './'): ")
# default path to ./
if(path == ""):
    path = "./"

file = get_audio_files(path)
# handle no audio files
if(file == None):
    print("There are no audio files detected in the folder you've specified.")
    exit()
title = file.split(".")[0]

tracklist = input("Tracklist file (default 'tracklist.txt'): ")
# make "tracklist.txt" default tracklist
if(tracklist == ""):
    tracklist = path + "tracklist.txt"

# get timestamps and song names and artists
timestamps = get_timestamps(tracklist)
songs = get_songs(tracklist)

# write to a cuesheet
success = write_cue_file(performer, title, file, songs, timestamps, path)
if(success == 0):
    print("Your cue file is generated. Enjoy! :)")