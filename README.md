🎬 Movie Recommendation System
This is a content-based movie recommendation system built using Streamlit, Python, and TMDb API. It suggests 5 similar movies based on the movie selected by the user, along with their poster images.

🚀 Features
Recommend top 5 similar movies using cosine similarity

Display movie posters using TMDb API

Fast and interactive web app powered by Streamlit

Clean and responsive UI

Handles API timeouts and errors gracefully

🛠️ Tech Stack
Frontend/UI: Streamlit

Backend: Python

Data Handling: Pandas

ML Model: Cosine similarity (precomputed and stored in similarity.pkl)

API: TMDb API

Data Source: movie_dict.pkl (movie metadata)

📦 Files Included
app.py – Main Streamlit application

movie_dict.pkl – Dictionary with movie details (title, movie_id)

similarity.pkl – Precomputed similarity matrix for fast recommendations

README.md – Project documentation (you are here!)

▶️ How to Run
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender
Install the dependencies:

bash
Copy
Edit
pip install -r requirements.txt
(You can create requirements.txt using pip freeze > requirements.txt)

Run the Streamlit app:

bash
Copy
Edit
streamlit run app.py
🖼️ Example Output
User selects a movie title

App displays:

5 most similar movies

Poster images using TMDb API

🌐 Live Demo (Optional)
You can deploy it to Streamlit Cloud and share the link here.

📌 Notes
Make sure you have an active internet connection (for fetching posters).

If TMDb API request fails or times out, a placeholder image is shown.

You can replace online posters with local ones for offline use (optional).

🤝 Contributing
Feel free to open issues or pull requests to improve the app!

📜 License
This project is licensed under the MIT License.
