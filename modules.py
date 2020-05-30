
def CreateFolder(foldername):
    from os import mkdir, makedirs, path, chdir, getcwd
    try:
        mkdir('{}'.format(foldername))
    except FileExistsError:
        pass
    a = path.join(getcwd(), foldername)
    chdir(a)

def WriteFile(title, songbody, url):
    title = title.strip().replace("'","_").replace(' ','_').replace('\\','_').replace('/','_')
    with open('{}.txt'.format(title), 'w') as wfile:
        print(title, file=wfile)
        print('\n', file=wfile)
        print("-"*50, file=wfile)
        print('\n', file=wfile)
        for row in songbody:
            print(row, file=wfile)
        print("-"*50, file=wfile)
        print('Resource:\n', url, file=wfile)


def GetSongText(url):
    """add text and get lyrics """
    print(url)
    from bs4 import BeautifulSoup
    from urllib.request import urlopen
    htmldata = urlopen(url)
    bs_obj = BeautifulSoup(htmldata, "lxml")
    # title
    try:
        old_title = bs_obj.h2.string
        title = old_title.strip()
        print(title)
    except AttributeError:
        pass
    print('-'*50)
    # song lyrics
    text_body = bs_obj.findAll('div', {'id': 'song-body'})
    songbody = []
    for row in text_body:
        print(row.get_text())
        songbody.append(row.get_text())
    # write to a file
    # FIXME: buradaya eger bos ise gec ifadesi gelmeli
    if len(songbody) <= 0 :
        pass
    else:
        WriteFile(title, songbody, url)


def GetLinks(url):
    from urllib.request import urlopen, Request
    from urllib.parse import urljoin
    from bs4 import BeautifulSoup
    dataset = urlopen(url)
    # bs_obj
    bs_obj = BeautifulSoup(dataset, "lxml")
    pathList = []
    # href add
    for i in bs_obj.findAll('a', href=True, text=True):
        pathList.append(i['href'])
    song_links = []
    for link in pathList:
        if link.startswith('https') == True and link.startswith('/') == False:
            pass
        else:
            songlink = urljoin('https://lyricstranslate.com', link)
            print(songlink)
            song_links.append(songlink)
    print(song_links)
    with open('songlinks.txt', 'w') as wfile:
        for link in song_links:
            print(link, file=wfile)
