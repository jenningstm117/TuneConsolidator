import sys, time, os
import eyed3

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
                filename = os.path.join(root, filetest1)
                audio_files.append(filename)

def setFileMeta():
    global audio_files, artist, album
    for file in audio_files:
        try:
            print file
            audiofile = eyed3.load(file)
            if album != '':
                audiofile.tag.album = album
            if artist != '':
                audiofile.tag.artist = artist
            audiofile.tag.save()
        except:
            print 'Failed to update data for ' + file

            test2 change

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

test1 change