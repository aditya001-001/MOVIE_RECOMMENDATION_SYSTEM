# 🎬 Movie Recommendation System

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
- **Model**: Cosine Similarity (precomputed)  
- **API**: TMDb API for fetching movie posters  
- **Data**: Stored in `movie_dict.pkl` and `similarity.pkl`

---

## 📁 Project Structure
```
📦 movie-recommender/
├── app.py # Main Streamlit app
├── movie_dict.pkl # Movie metadata (title, ID)
├── similarity.pkl # Precomputed similarity matrix
├── README.md # Project documentation
└── requirements.txt # Python dependencies
```
---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender
```
### 2. Install the dependencies
```
pip install -r requirements.txt
```

### 3. Run the app
```
streamlit run app.py
```
## 🖼️ Example
Select a movie like "Inception", and the app will show 5 similar movies with their posters.

## ⚠️ Notes:

  - Requires an internet connection to fetch posters from TMDb.

  - In case of API timeout or failure, placeholder images are shown.

  - TMDb API key is used directly in the code for simplicity — consider hiding it using environment variables for production.

## 📜 License
This project is licensed under the MIT License. Feel free to use, modify, and share it.

## 🤝 Contributing
Pull requests are welcome. For major changes, open an issue first to discuss what you’d like to change.


