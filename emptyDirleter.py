import sys, time, os
import eyed3

def main():
    for path in sys.argv[1:]:
        removeEmptyDirs(path)

def removeEmptyDirs(path):
    deleted_paths = []
    for root, dirs, files in os.walk(path, topdown=False):
        print 'Checking: ' + root
        for path in dirs:
            if os.path.join(root, path) in deleted_paths:
                dirs.remove(path)
        if len(files) == 0 and len(dirs) == 0:
            print 'Deleting ' + root
            os.rmdir(root)
            deleted_paths.append(root)
    print '\n\n___' + str(len(deleted_paths)) + ' Empty Directories Were Deleted___'
    for item in reversed(deleted_paths):
        print item

if __name__ == '__main__':
    try:
        main()
        print 'DONE . . .'
    except Exception as e:
        print e
    time.sleep(100)

