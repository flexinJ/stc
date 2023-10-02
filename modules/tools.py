import pytube
import moviepy.editor

class Video:

    def __init__(self, url):
        self.url = url
        self.yt = pytube.YouTube(url)
        self.videos_path = "db\\videos"
        self.audios_path = "db\\audios" 

    def title(self):
        return self.yt.title
    
    def author(self):
        return self.yt.author
    
    def date(self):
        return self.yt.publish_date

    def views(self):
        return self.yt.views

    def thumbnail(self):
        return self .yt.thumbnail_url

    def stream(self):
        return self.yt.streams.get_highest_resolution()
    
    def download(self):
        return self.stream().download(self.videos_path)

    def transforming(self):
        dir = "db\\videos\\"+self.title()+".mp4"
        print(dir)
        clip = moviepy.editor.VideoFileClip(str(dir))
