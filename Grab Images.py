import struct
import imghdr
from os import listdir, makedirs
from os.path import isfile, join, expanduser, exists
from shutil import copyfile


def get_image_size(fname):
    '''Determine the image type of fhandle and return its size.'''
    with open(fname, 'rb') as fhandle:
        head = fhandle.read(24)
        if len(head) != 24:
            return
        if imghdr.what(fname) == 'png':
            check = struct.unpack('>i', head[4:8])[0]
            if check != 0x0d0a1a0a:
                return
            width, height = struct.unpack('>ii', head[16:24])
        elif imghdr.what(fname) == 'gif':
            width, height = struct.unpack('<HH', head[6:10])
        elif imghdr.what(fname) == 'jpeg':
            try:
                fhandle.seek(0) # Read 0xff next
                size = 2
                ftype = 0
                while not 0xc0 <= ftype <= 0xcf:
                    fhandle.seek(size, 1)
                    byte = fhandle.read(1)
                    while ord(byte) == 0xff:
                        byte = fhandle.read(1)
                    ftype = ord(byte)
                    size = struct.unpack('>H', fhandle.read(2))[0] - 2
                # We are at a SOFn block
                fhandle.seek(1, 1)  # Skip `precision' byte.
                height, width = struct.unpack('>HH', fhandle.read(4))
            except Exception: #IGNORE:W0703
                return
        else:
            return
        return width, height

def makeDir(userPath):
    if not exists(userPath):
        try:
            makedirs(userPath)
        except OSError as exc: # prevent race condition
            if exc.errno != errno.EEXIST:
                raise

def grabFiles(myDir):
    return [f for f in listdir(myDir) if isfile(join(myDir, f))]

def main():
    userPath = expanduser('~')
    
    tempPath = userPath + "\Desktop\\images\\"
    oldPath  = userPath + "\Desktop\\pictures\\"
    fullPath = userPath + "\Desktop\\Wallpapers\\"
    print(tempPath)
    print(oldPath)
    print(fullPath)

    oldImages = grabFiles(oldPath)
    sizes = []
    for file in oldImages:

        size = get_image_size(oldPath + file)
        if size not in sizes:
            makeDir(str(fullPath) + str(size))
            sizes.append(size)
            print("create " + str(fullPath) + str(size))
        print("copy " + str(file) + " to " + str(fullPath) + str(size))
        copyfile(oldPath+file, fullPath+str(size) + "\\" + file)

if __name__ == '__main__':
    main()
