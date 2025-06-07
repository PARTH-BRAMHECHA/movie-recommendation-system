<<<<<<< HEAD
from flask import Flask, render_template, request, jsonify
import pickle
import requests
import os
from dotenv import load_dotenv
import os
from download_utils import download_files

# Download .pkl files at runtime
download_files()

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Load movie data and similarity matrix
movies = pickle.load(open("movies_list.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))
movie_titles = movies['title'].values

TMDB_API_KEY = os.getenv("TMDB_API_KEY")

def fetch_movie_id_by_title(title):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={title}"
    response = requests.get(url)
    data = response.json()
    if data['results']:
        return data['results'][0]['id']
    return None

def fetch_poster(movie_id):
    if not movie_id:
        return "https://via.placeholder.com/300x450?text=No+Poster"
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
    response = requests.get(url)
    data = response.json()
    poster_path = data.get('poster_path', '')
    if poster_path:
        return f"https://image.tmdb.org/t/p/w500/{poster_path}"
    return "https://via.placeholder.com/300x450?text=No+Poster"

def recommend(movie):
    try:
        index = movies[movies['title'] == movie].index[0]
    except IndexError:
        return [], []
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_titles = []
    recommended_posters = []
    for i in distances[1:6]:
        title = movies.iloc[i[0]].title
        movie_id = fetch_movie_id_by_title(title)
        recommended_titles.append(title)
        recommended_posters.append(fetch_poster(movie_id))
    return recommended_titles, recommended_posters

@app.route('/', methods=['GET', 'POST'])
def index():
    selected_movie = None
    recommendations = []
    posters = []

    if request.method == 'POST':
        selected_movie = request.form.get('movie')
        if selected_movie:
            recommendations, posters = recommend(selected_movie)

    preload_posters = [
        fetch_poster(1632),
        fetch_poster(299536),
        fetch_poster(17455),
        fetch_poster(2830),
        fetch_poster(429422)
    ]

    return render_template(
        'index.html',
        movie_titles=movie_titles,
        selected_movie=selected_movie,
        recommendations=zip(recommendations, posters),
        preload_posters=preload_posters
    )

@app.route('/api/recommend', methods=['POST'])
def api_recommend():
    data = request.get_json()
    movie = data.get('movie')
    if not movie:
        return jsonify({'error': 'No movie provided'}), 400
    recommendations, posters = recommend(movie)
    return jsonify({'recommendations': recommendations, 'posters': posters})

if __name__ == "__main__":
    app.run(debug=True)
=======
from flask import Flask, render_template, request, jsonify
import pickle
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Load movie data and similarity matrix
movies = pickle.load(open("movies_list.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))
movie_titles = movies['title'].values

TMDB_API_KEY = os.getenv("TMDB_API_KEY")

def fetch_movie_id_by_title(title):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={title}"
    response = requests.get(url)
    data = response.json()
    if data['results']:
        return data['results'][0]['id']
    return None

def fetch_poster(movie_id):
    if not movie_id:
        return "https://via.placeholder.com/300x450?text=No+Poster"
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
    response = requests.get(url)
    data = response.json()
    poster_path = data.get('poster_path', '')
    if poster_path:
        return f"https://image.tmdb.org/t/p/w500/{poster_path}"
    return "https://via.placeholder.com/300x450?text=No+Poster"

def recommend(movie):
    try:
        index = movies[movies['title'] == movie].index[0]
    except IndexError:
        return [], []
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_titles = []
    recommended_posters = []
    for i in distances[1:6]:
        title = movies.iloc[i[0]].title
        movie_id = fetch_movie_id_by_title(title)
        recommended_titles.append(title)
        recommended_posters.append(fetch_poster(movie_id))
    return recommended_titles, recommended_posters

@app.route('/', methods=['GET', 'POST'])
def index():
    selected_movie = None
    recommendations = []
    posters = []

    if request.method == 'POST':
        selected_movie = request.form.get('movie')
        if selected_movie:
            recommendations, posters = recommend(selected_movie)

    preload_posters = [
        fetch_poster(1632),
        fetch_poster(299536),
        fetch_poster(17455),
        fetch_poster(2830),
        fetch_poster(429422)
    ]

    return render_template(
        'index.html',
        movie_titles=movie_titles,
        selected_movie=selected_movie,
        recommendations=zip(recommendations, posters),
        preload_posters=preload_posters
    )

@app.route('/api/recommend', methods=['POST'])
def api_recommend():
    data = request.get_json()
    movie = data.get('movie')
    if not movie:
        return jsonify({'error': 'No movie provided'}), 400
    recommendations, posters = recommend(movie)
    return jsonify({'recommendations': recommendations, 'posters': posters})

if __name__ == "__main__":
    app.run(debug=True)
