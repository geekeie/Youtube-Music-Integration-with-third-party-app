from flask import current_app, render_template, request
import requests

def search_youtube_music(query):
    api_key = current_app.config['YOUTUBE_API_KEY']
    search_url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&type=video&key={api_key}"
    response = requests.get(search_url)
    return response.json()

@current_app.route('/', methods=['GET', 'POST'])
def index():
    music_results = None
    if request.method == 'POST':
        query = request.form['query']
        music_results = search_youtube_music(query)
    return render_template('index.html', results=music_results)
