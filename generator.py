import os
from cuefilegenerator import write_cue_file

def get_audio_files(folder):
    audio_ext = [".mp3", ".m4a", ".ogg", ".opus", ".aac", ".flac", ".wav", ".wma", ".aiff", ".alac"]
    for file in os.listdir(folder):
        if file.endswith(tuple(audio_ext)):
            return file

def get_timestamps(tracklist):
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

def get_songs(tracklist):
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

####################################### main program #####################################
performer = input("Performer: ")
path = input("Enter DIRECTORY path where audio file and tracklist is (default './'): ")
if(path == ""):
    path = "./"
file = get_audio_files(path)
title = file.split(".")[0]

tracklist = input("Tracklist file (default 'tracklist.txt'): ")
# make "tracklist.txt" default tracklist
if(tracklist == ""):
    tracklist = path + "tracklist.txt"

# get timestamps and song names and artists
timestamps = get_timestamps(tracklist)
songs = get_songs(tracklist)

# write to a cuesheet
write_cue_file(performer, title, file, songs, timestamps, path)