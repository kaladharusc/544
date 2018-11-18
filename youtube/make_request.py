import requests
import os
import collections
casey_dir = "/Users/kaladhar/Downloads/casey/"
alreadyFiles = os.listdir(casey_dir)

index = 0
def makeUtubeRequest(utubeReponse):
    while utubeReponse['nextPageToken']:
        url = "https://www.googleapis.com/youtube/v3/search?key=AIzaSyCHAzIGfl709SFlme_J1HXAkPyPKGF9hlQ&channelId=UCtinbF-Q-fVthA0qrFQTgXQ&part=snippet,id&order=date&maxResults=50&type=video"
        r = requests.get(url, {'pageToken': utubeReponse['nextPageToken']})
        utubeReponse = r.json()
        global index
        for video in utubeReponse['items']:
            index += 1
            #print(str(index) + " " + video['snippet']['videoId'])
            makeDIYCall(video['snippet']['title'], video['snippet']['publishedAt'], video['id']['videoId'])

def makeYouTube():
    url = "https://www.googleapis.com/youtube/v3/search?key=AIzaSyCHAzIGfl709SFlme_J1HXAkPyPKGF9hlQ&channelId=UCtinbF-Q-fVthA0qrFQTgXQ&part=snippet,id&order=date&maxResults=50"
    r = requests.get(url)
    utubeReponse = r.json()
    i = 0
    global index
    for video in utubeReponse['items']:
        index += 1
        #print(str(index) + " " + video['id']['videoId'])
        makeDIYCall(video['snippet']['title'], video['snippet']['publishedAt'], video['id']['videoId'])

    if utubeReponse['nextPageToken']:
        makeUtubeRequest(utubeReponse)

def makeDIYCall(name, time, id):
    print(name)
    fileName = time + "_" + name + ".txt"
    #print(fileName)
    if fileName in alreadyFiles:
        return
    r = requests.get("http://www.diycaptions.com/php/start.php?id=" + id)
    r = requests.post("http://www.diycaptions.com/php/build-srt.php", {"ajax_youtube_id" : id})
    fileName = fileName.replace("/", " ")
    fullFileName =  casey_dir + fileName
    file = open(fullFileName, "w")
    file.write(r.text)
    file.close()

def parse():
    files = os.listdir(casey_dir)
    contents = ""
    for file in files:
        f = open(casey_dir + file, "r")
        contents = contents + f.read()
    print(files)
    freqs = collections.Counter(contents.split())
    print(freqs)
    print(freqs['airport'])

if __name__ == '__main__':
    # r = requests.get("http://www.diycaptions.com/php/start.php?id=uqDKwle9Wr4")
    # r = requests.post("http://www.diycaptions.com/php/build-srt.php", {"ajax_youtube_id" : "uqDKwle9Wr4"})
    # print(r.content)
    # makeYouTube()
    parse()
    #print(os.path)