from flask import Flask, request, render_template
from flask_navigation import Navigation
from pytube import Playlist
from pytube import YouTube
from pathlib import Path
import os
import re
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', title='Home')
@app.route("/download", methods=["GET","POST"])
def downloadVideo():
	
	if request.method == 'POST' and 'video_url' in request.form:
		url = request.form["video_url"]
		yt=YouTube(url)
		YouTube(url).streams.filter(only_audio=True)
		stream=yt.streams.get_by_itag(251)
		stream.download()
		#p=Playlist(url)
		#for video in p.videos:
			#video.streams.last.download()
			

	return render_template('download.html', title='Second page')
	
@app.route('/navpage')
def navpage():
    return render_template('navpage.html', title='Third page')
  
  
@app.route('/about')
def about():
    return render_template('about.html', title='First page')
  
if __name__ == "__main__":
    app.run()
    	
