
import re
import os
import sys
from pathlib import Path


def main():
    path = sys.argv[1]#r'C:\Users\Asus\Desktop\clean'
    if len(sys.argv) < 2:
        raise ValueError('empty path')
    if not (os.path.exists(path) and Path(path).is_dir()):
        raise ValueError('incorrect path')

    cleaner(path)
    print(':)')
#Translate
def normilize(word):
    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"#1234567890
    TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
                "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")#, "1", '2', '3', '4', '5', '6', '7', '8', '9', '0'
    TRANS = {}
    for c, t in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = t
        TRANS[ord(c.upper())] = t.upper()
    s = str(word.translate(TRANS)) 
    #s = re.sub(r'([-,])', '_', s)
    return re.sub(r'[^\d\w_.]+', '_', s)
#Clean
def cleaner(folder):
    all_files = os.listdir(folder)

    
    for file in all_files:
        #Photo
        if file.endswith('.jpg') or file.endswith('.png') or file.endswith('.jpeg') or file.endswith('.sgv'):
            images_path = folder + '_images'
            if not os.path.exists(images_path):
                os.makedirs(images_path)
            file_path = os.path.join(folder, file)
            new_file = os.path.join(images_path, normilize(file))
            os.replace(file_path, new_file)
            print(f'Image moved to "images": {file}')
        #Video
        if file.endswith('.mp4') or file.endswith('.avi') or file.endswith('.mov') or file.endswith('.mkv'):
            images_path = folder + '_videos'
            if not os.path.exists(images_path):
                os.makedirs(images_path)
            file_path = os.path.join(folder, file)
            new_file = os.path.join(images_path, normilize(file))
            os.replace(file_path, new_file)
            print(f'Video moved to "videos": {file}')
        #Document
        if file.endswith('.doc') or file.endswith('.docx') or file.endswith('.txt') or file.endswith('.pdf') or file.endswith('.xlsk') or file.endswith('.pptx'):
            images_path = folder + '_documents'
            if not os.path.exists(images_path):
                os.makedirs(images_path)
            file_path = os.path.join(folder, file)
            new_file = os.path.join(images_path, normilize(file))
            os.replace(file_path, new_file)
            print(f'Document moved to "images": {file}')
        #Music
        if file.endswith('.mp3') or file.endswith('.ogg') or file.endswith('.wav') or file.endswith('.amr'):
            images_path = folder + '_musics'
            if not os.path.exists(images_path):
                os.makedirs(images_path)
            file_path = os.path.join(folder, file)
            new_file = os.path.join(images_path, normilize(file))
            os.replace(file_path, new_file)
            print(f'Music moved to "musics": {file}')
        #Archive
        if file.endswith('.zip') or file.endswith('.gs') or file.endswith('.tar'):
            images_path = folder + '_archives'
            if not os.path.exists(images_path):
                os.makedirs(images_path)
            file_path = os.path.join(folder, file)
            new_file = os.path.join(images_path, normilize(file))
            os.replace(file_path, new_file)
            print(f'Archive moved to "archives": {file}')
        #:O
        else:
            images_path = folder + '_UFO^_^'
            if not os.path.exists(images_path):
                os.makedirs(images_path)
                file_path = os.path.join(folder, file)
                new_file = os.path.join(images_path, normilize(file))
                os.replace(file_path, new_file)
                print(f'UFO moved to "unidentaified objects": {file}')
        


if __name__ == "__main__":
    main()
#python motloch.py C:\Users\Asus\Desktop\clean | cd C:\Users\Asus\Desktop\p