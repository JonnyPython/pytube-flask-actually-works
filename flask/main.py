from flask import Flask, request, render_template
from pytube import Playlist
from pathlib import Path
import os
import re
app = Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html')
@app.route("/download", methods=["GET","POST"])
def downloadVideo():
	if request.method == 'POST' and 'video_url' in request.form:
		url = request.form["video_url"]
		p = Playlist(url)
		for video in p.videos:
			video.streams.last().download()
	return render_template('download.html')
if __name__ == "__main__":
    app.run()
    
