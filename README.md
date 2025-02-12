# AI-Powered Movie Recommendation System  

An AI-based **Movie Recommendation System** built using **Streamlit, Surprise (SVD), and the MovieLens 25M dataset**.  
This system provides **personalized movie recommendations** based on user preferences and collaborative filtering.  

## Features
**Collaborative Filtering (SVD)** for personalized recommendations  
**Genre-based filtering** to enhance recommendation accuracy  
**Fast and scalable model** using Surprise library  
**Interactive UI** with Streamlit for real-time recommendations  

---

## Dataset
This project is based on the **MovieLens 25M dataset**, which consists of:  
- **25 million ratings** from **162,000 users** on **62,000 movies**  
- User-movie interaction data to train the recommendation engine  

**Due to GitHub’s file size limit, we provide a smaller dataset:**  
- **Sample dataset (1M rows):** `ratings_small.csv`  
- **Full dataset (25M rows):** Available on [MovieLens Website](https://grouplens.org/datasets/movielens/25m/)  
- **Alternative Kaggle Source:** [MovieLens 25M Dataset](https://www.kaggle.com/datasets/garymk/movielens-25m-dataset)  

To use the full dataset, download it from the link above and replace `ratings_small.csv` with the full dataset.  

---

## 🚀 Running the Streamlit App
After installing dependencies, launch the application with:

```bash
streamlit run app.py
```

Then open your browser to access the interactive recommendation system.

---

## How It Works
1. **User enters their ID**  
2. **The system analyzes the user's favorite genres**  
3. **Unseen movies are filtered and ranked based on predicted ratings**  
4. **Top 10 personalized recommendations are displayed**  

This system utilizes **Singular Value Decomposition (SVD)** from the **Surprise** library for collaborative filtering.  

---

## Machine Learning Approach
This recommendation system is built using **Collaborative Filtering**, which predicts user preferences based on past interactions.  
- **Matrix Factorization (SVD)** is used to reduce dimensionality and improve recommendation accuracy.  
- **Genre filtering** is applied to further refine recommendations.  

### Model Training & Evaluation
- **SVD Model** trained on 80% of the dataset, tested on 20%.
- **Performance Metric:** RMSE (Root Mean Squared Error).
- **Movies with less than 10 ratings are removed** to enhance recommendation reliability.
- **Filtering step:** Only movies with at least 50 ratings are included for predictions.
- **Top 1000 movies are selected** for efficient recommendation.

---

## Technologies Used
- **Python** (Data Processing & Model Training)  
- **Surprise (SVD Algorithm)** (Collaborative Filtering)  
- **Streamlit** (Web UI for recommendations)  
- **Pandas, NumPy** (Data Manipulation)  
- **Scikit-learn (Cosine Similarity for Movie Similarity Calculation)**
