import sys, time, os
import eyed3
import pymedia.audio.acodec as acodec
import pymedia.muxer as muxer

global artist, album, audio_files

def main():
    global audio_files
    args = []
    audio_files = []
    for path in sys.argv[1:]:
        getFiles(path)
    print audio_files
    setFileMeta()

def getFiles(path):
    global audio_files
    for root, dirs, files in os.walk(path, topdown=True):
        for file in files:
            if file.split('.')[-1] in ['mp3']:
                filename = os.path.join(root, file)
                audio_files.append(filename)

def setFileMeta():
    global audio_files, artist, album
    for file in audio_files:
        try:
            print file
            audiofile = eyed3.load(file)
            audiofile.tag.album = album
            audiofile.tag.artist = artist
            print 'Length: '+str(audiofile.tag.length)
            audiofile.tag.save()
        except:
            print 'Failed to update data for ' + file

if __name__ == '__main__':
    global artist, album
    album = unicode(raw_input('Album: '))
    artist = unicode(raw_input('Artist: '))
    try:
        main()
        print 'DONE . . .'
    except Exception as e:
        print e
    time.sleep(100)

