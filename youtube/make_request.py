import requests
import os
import collections

import json


class Youtube:

    def __init__(self):
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        self.index = 0
        self.youtube_search_url = "https://www.googleapis.com/youtube/v3/search?key=AIzaSyCHAzIGfl709SFlme_J1HXAkPyPKGF9hlQ&"
        self.youtube_channel_url = "https://www.googleapis.com/youtube/v3/channels?key=AIzaSyCHAzIGfl709SFlme_J1HXAkPyPKGF9hlQ&"

        self.youtube_videos_url = "https://www.googleapis.com/youtube/v3/videos?key=AIzaSyCHAzIGfl709SFlme_J1HXAkPyPKGF9hlQ&"
        self.alreadyFiles = []

    def makeUtubeRequest(self, utubeReponse, channelId, dir_name):
        while utubeReponse['nextPageToken']:
            url = self.youtube_search_url + \
                "channelId="+channelId+"&part=snippet,id&order=date&maxResults=50&type=video"
            r = requests.get(url, {'pageToken': utubeReponse['nextPageToken']})
            utubeReponse = r.json()

            for video in utubeReponse['items']:
                self.index += 1
                # print(str(index) + " " + video['snippet']['videoId'])
                self.makeDIYCall(
                    video['snippet']['title'], video['snippet']['publishedAt'], video['id']['videoId'], dir_name)

    def parseInput(self):
        with open(self.dir_path+"/input.json", 'r') as f:
            input_json = json.loads(f.read())
            for channel in input_json['channels']:
                url = "{}forUsername={}&part=contentDetails".format(
                    self.youtube_channel_url, channel)
                r = requests.get(url)
                resp = r.json()
                self.makeYouTube(channel, resp["items"][0]["id"])
            for id in input_json["videos"]:
                url = "{}forUsername={}&part=snippet".format(
                    self.youtube_videos_url, channel)
                r = requests.get(url)
                resp = r.json()
                video = resp["items"][0]
                dir_name = self.dir_path+"/misc/"
                self.makeDIYCall(
                    video['snippet']['title'], video['snippet']['publishedAt'], video['id']['videoId'], dir_name)

    def makeYouTube(self, channel_name, channelId):
        dir_name = self.dir_path+"/data/"
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        self.alreadyFiles = os.listdir(dir_name)
        self.alreadyFiles = [x.decode('utf-8') for x in self.alreadyFiles]
        url = "{}channelId={}&part=snippet,id&order=date&maxResults=10".format(
            self.youtube_search_url, channelId)
        r = requests.get(url)
        utubeReponse = r.json()
        i = 0
        for video in utubeReponse['items']:
            self.index += 1
            # print(str(index) + " " + video['id']['videoId'])
            self.makeDIYCall(
                video['snippet']['title'], video['snippet']['publishedAt'], video['id']['videoId'], dir_name)

        if utubeReponse['nextPageToken']:
            self.makeUtubeRequest(utubeReponse, channelId, dir_name)

    def makeDIYCall(self, name, time, id, dir_name):
        print(name)
        fileName = name + ".txt"
        # print(fileName)
        if fileName in self.alreadyFiles:
            print("exists: ", fileName)
            return
        r = requests.get("https://www.diycaptions.com/php/start.php?id=" + id)
        r = requests.post(
            "https://www.diycaptions.com/php/build-srt.php", {"ajax_youtube_id": id})
        fileName = fileName.replace("/", " ")
        fullFileName = dir_name + fileName
        print(fullFileName, fileName)
        file = open(fullFileName, "w")
        file.write(r.text.encode('utf-8'))
        file.close()

    def parse(self, dir_name):
        files = os.listdir(dir_name)
        contents = ""
        for file in files:
            f = open(dir_name + file, "r")
            contents = contents + f.read()
        print(files)
        freqs = collections.Counter(contents.split())
        print(freqs)
        print(freqs['airport'])


if __name__ == '__main__':

    youtube = Youtube()
    youtube.parseInput()
