🎬 Movie Recommendation System

This is a content-based movie recommendation system built using **Python**, **Streamlit**, and the **TMDb API**. It recommends 5 similar movies based on a selected movie and displays their posters in a clean web interface.

---

## 🔍 Features

- Recommend top 5 similar movies
- Display movie posters using TMDb API
- Interactive UI using Streamlit
- Handles API errors and timeouts
- Fast and lightweight (uses precomputed similarity)

---

## 🛠️ Tech Stack

- **Frontend/UI**: Streamlit
- **Backend**: Python
- **Similarity Model**: Cosine Similarity (using scikit-learn or precomputed)
- **API**: TMDb for posters
- **Data**: TMDb dataset converted to `movie_dict.pkl`

---

## 📁 Project Structure

📦 movie-recommender/
├── app.py # Main Streamlit app
├── movie_dict.pkl # Movie metadata (title, ID)
├── similarity.pkl # Precomputed similarity matrix
├── README.md # Project documentation
└── requirements.txt # Python dependencies (optional)

yaml
Copy
Edit

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender
2. Install the dependencies
bash
Copy
Edit
pip install -r requirements.txt
If you don’t have requirements.txt, create it:

bash
Copy
Edit
pip freeze > requirements.txt
3. Run the app
bash
Copy
Edit
streamlit run app.py
🖼️ Example
Select a movie like "Avatar" and get 5 similar movies along with their posters.

🌐 Live Demo
(Optional — include link if hosted on Streamlit Cloud)
🔗 View Live App

⚠️ Notes
Requires an internet connection to fetch posters from TMDb.

If the poster fails to load, a placeholder image is displayed.

TMDb API key is used directly — consider securing it for production use.

📜 License
This project is licensed under the MIT License. Feel free to use and modify it.

🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first.
