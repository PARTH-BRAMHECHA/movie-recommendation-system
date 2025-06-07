# 🎬 Movie Recommendation System

A web-based movie recommender built with Flask, Bootstrap, and The Movie Database (TMDB) API.  
Select a movie and instantly get visually appealing recommendations with posters and titles!

---

## ✨ Features

- Modern, responsive Bootstrap UI  
- Movie selection with instant recommendations  
- Movie posters fetched dynamically from TMDB  
- Carousel of popular movies  
- Easy deployment to Heroku or any cloud platform

---

## 🚀 Screenshots

### Home & Recommendations

![Recommendations Screenshot](https://pplx-res.cloudinary.com/image/private/user_uploads/5939154/877c462b-e20b-497a-9511-a8f0d1880789/Screenshot-2025-06-06-225920.jpg)

### Carousel & Selection

![Carousel Screenshot](https://pplx-res.cloudinary.com/image/private/user_uploads/5939154/3b24ea05-214b-44df-88e9-b470be934036/Screenshot-2025-06-06-225932.jpg)

---

## 🛠️ Setup & Installation

1. **Clone the repo:**

    ```bash
    git clone https://github.com/yourusername/movie-recommender.git
    cd movie-recommender
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Add your data files:**

    - Place `movies_list.pkl` and `similarity.pkl` in the project root.

4. **Set your TMDB API key:**

    - Edit `app.py` and replace the placeholder with your TMDB API key.

5. **Run the app:**

    ```bash
    python app.py
    ```

    The app will be available at [http://localhost:5000](http://localhost:5000)

---


## 📂 Project Structure
```
movie-recommender/
│
├── app.py
├── movies_list.pkl
├── similarity.pkl
├── requirements.txt
├── .env  #Place TMDB API KEY
└── templates/
   └── index.html
```

---

## 🙏 Credits

- [Flask](https://flask.palletsprojects.com/)
- [Bootstrap](https://getbootstrap.com/)
- [The Movie Database (TMDB) API](https://www.themoviedb.org/documentation/api)

---

## 📧 Contact

For questions or suggestions, open an issue or contact [your.email@example.com](mailto:your.email@example.com).
