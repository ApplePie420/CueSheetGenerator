# Cue sheet generator
You like your songs organised, and when listening to sets, you want to just look at foobar2000 (you don't use anything else, be honest ;) and know, what song is playing. For that, there is certain type of file called _cuesheet_. This file contains info about track artist, title and its timestamp in the mix. I love these files, it's really convinient on PC and mobile. But manually creating these files, or using some online generators is major pain in the butt. And since you already have (presumably) tracklist with timestamps, why not create a tool that generates this file for you?

# Usage
## Installation
You don't need any special packages. Only two imports that I use are _os_ package for manipulating with files, and my custom [cue file generator](cuefilegenerator.py). So just clone the repo:
```bash
git clone https://github.com/ApplePie420/CueSheetGenerator.git
```

and then run

```bash
python generator.py
```

and just follow instructions.

## Using the script
First of all, insert __name of performer__, i.e. the person that mixed the set.

Then, it'll ask you for path where __your audio file and tracklist.txt is__. Enter full path, for example
```
D:\music\sets\myFavouriteProducer\myFavouriteMix\
```
or on linux
```
/home/yourName/music/myFavouriteProducer/myFavouriteMix/
```
You __do not need__ to insert the path between quotation marks, even if it contains spaces. It works somehow. If it doesn't, then try it with them :D

__Script automatically looks for audio files__ with these extensions:
- mp3
- m4a
- ogg/opus
- aac
- flac
- wav
- wma
- alac
Although for now, it only works with __mp3, m4a, ogg/opus, flac and alac__.

Next, you need to specify your __tracklist__ file. By default, it will look for file named `tracklist.txt`. If your tracklist is named differently, for example `list.txt`, type that in. __!Be sure that tracklist is formatted as needed (example below)!__.

And if everything went well, a _.cue_ file should append in your directory.

# Tracklist format
Obviously, this script is not magical and it cannot read your tracklist properly unless it is formatted properly. So your tracklist should look like this:
```
00:00:00 Artist - Title
00:05:30 Artist - Title
00:12:58 Artist - Title
...
01:03:34 Artist - Title
```

You __HAVE__ to have a space between timestamp and song name, and a ` - ` (aka space dash space) between artist and title. 
Time is formatted in HH:MM:SS, where HH is hours, MM are minutes and SS seconds. Script automatically transforms hours into minutes, and adds CD frame (defaults to 00). And yes, there __HAS__ to be leading zeroes. 1. It makes it look pretty and 2. I've hardcoded timestamp length.. :D (I will change it later)

I may add different tracklist formats support later, but honestly why. This is very readable, compact and have all necessary information. And __YES, you can have `[label]` at the end__. If you have problem with this tracklist format, either get used to it, fork this script and modify it, or create other script to convert your format to mine. 

# Todo list
[x] - ~~Automatically detect codec for cue `FILE` parameter~~
[ ] - Ignore missing leading zeroes
[ ] - Add `REM GENRE` and `DATE`

If you have Issues, you know where to post them. Please, feel free to fork, upgrade and request merge. I made this in under an hour so it won't be perfect.