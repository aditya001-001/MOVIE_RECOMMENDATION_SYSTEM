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


📜 License
This project is licensed under the MIT License. Feel free to use and modify it.

🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first.
