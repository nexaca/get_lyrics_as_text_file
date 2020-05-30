from modules import GetSongText,CreateFolder,GetLinks
from os import path, mkdir,makedirs

fname = input('Foldername:\n')
fname = fname.lower().replace(' ','_')

url = input('ARTIST URL:\n')

GetLinks(url)

with open('songlinks.txt', 'r') as rfile:
    links = rfile.readlines()
    CreateFolder(fname)
    for url in links:
        if url.find('lyricstranslate') != -1:
            GetSongText(url)
