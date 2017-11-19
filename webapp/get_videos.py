import os

video_path = os.path.dirname(os.path.abspath(__file__)) + "/videos/"

def getVideos():
    list = os.listdir(video_path)
    # print(list)
    return list
