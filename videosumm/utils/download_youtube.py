from pytube import YouTube
from pytube.cli import on_progress

class youtube():
    def __init__(self,url):
        self.url = url

    def download(self):
        print(f"[-] DOWNLOADING YOUTUBE VIDEO")
        # try for 5 times
        times = 5
        for i in range(times):
            # making object of youtube class,
            # on_progress_callback will show downloading on CLI
            yt = YouTube(self.url,on_progress_callback=on_progress)
            # download 720p or 480p video
            video = yt.streams.filter(progressive = True,file_extension = 'mp4').order_by('resolution').desc().first()
            #saving in the same directory
            video.download(filename='input_video')
            return '' , 'input_video.mp4'
            
        


            