import os

def write_cue_file(performer, title, file, tracks, tracks_timestamp, savePath):
    f = open(savePath + title + ".cue", "w")
    # check if all of data is present
    if(performer == ""):
        print("Performer not specified!")
        return 1
    elif(title == ""):
        print("Title not specified!")
        return 1
    elif(file == ""):
        print("File path not specified!")
        return 1
    elif(len(tracks) != len(tracks_timestamp)):
        print("Tracks and timestamps count does not match")
        return 1
    else:
        # try to guess codec, this might not work always
        # TODO: make this somehow automated, maybe some packages?
        extension = file.split(".")[1]
        codec = ""
        if(extension == "mp3"):
            codec = "MP3"
        elif(extension == "m4a"):
            codec = "AAC"
        elif(extension == "ogg" or extension == "opus"):
            codec = "AIFF"
        elif(extension == "flac"):
            codec = "FLAC"
        elif(extension == "alac"):
            codec = "ALAC"
        # write info about cuesheet
        f.write("PERFORMER \"" + performer + "\"\n")
        f.write("TITLE \"" + title + "\"\n")
        f.write("FILE \"" + file + "\" " + str(codec) + "\n")

        # write individual tracks
        for i in range(len(tracks)):
            # TRACK 0x AUDIO
            f.write("\tTRACK %02d AUDIO\n" % (i+1,))
            # PERFORMER "DJ_name"
            f.write("\t\tPERFORMER \"" + tracks[i].split(" - ")[0] + "\"\n")
            # TITLE "title"
            f.write("\t\tTITLE \"" + tracks[i].split(" - ")[1] + "\"\n")
            # INDEX 01 timestamp
            f.write("\t\tINDEX 01 " + tracks_timestamp[i] + ":00\n")
        f.close()
        return 0