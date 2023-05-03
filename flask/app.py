from flask import Flask, request, render_template, url_for, redirect
#from flask_navigation import Navigation
from pytube import Playlist
import urllib
from urllib.parse import urlparse
from urllib.parse import quote
from six.moves import urllib
from pytube import YouTube
import psycopg2
from pathlib import Path
import os
import re
app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='flask_db',
                            user=os.environ['DB_USERNAME'],
                            password=os.environ['DB_PASSWORD'])
    return conn





@app.route("/")
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM sites;')
    sites = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', title='Home',sites=sites)
@app.route("/download", methods=["GET","POST"])
def downloadVideo():
	
	if request.method == 'POST' and 'video_url' in request.form:
		url = request.form["video_url"]
		"""
		yt=YouTube(url)
		YouTube(url).streams.filter(file_extension='mp4')
		stream=yt.streams.get_by_itag(18)
		stream.download()
		"""
		p=Playlist(url)
		for video in p.videos:
			video.streams.last().download()
		
		
		url=str(url)
		print(url)
		conn = get_db_connection()
		cur = conn.cursor()
		cur.execute('INSERT INTO sites (url)'
            'VALUES (%s)',
            (url,))
		conn.commit()
		cur.close()
		conn.close()
		#return redirect(url_for('index'))
		
		
		
		
		#p=Playlist(url)
		#for video in p.videos:
			#video.streams.last.download()
			

	return render_template('download.html', title='Confirmation page')
	

@app.route('/navpage')
def navpage():
    return render_template('navpage.html', title='Motivation page')
  
  
@app.route('/about')
def about():
    return render_template('about.html', title='About page')
  
if __name__ == "__main__":
    app.run()
    	
