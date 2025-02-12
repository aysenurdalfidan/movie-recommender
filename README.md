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

## Running the Streamlit App
Launch the application with:

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

## Case Study: Challenges & Solutions
### **Handling Large Datasets Efficiently**
- **Challenge:** The MovieLens 25M dataset is massive, making it computationally expensive to process all ratings.
- **Solution:** Filtered out movies with **less than 10 ratings** and kept only movies rated by **at least 50 users** to ensure reliable recommendations.

### **Optimizing Model Performance**
- **Challenge:** The initial model suffered from high computational costs and slow training times.
- **Solution:** Implemented **SVD with hyperparameter tuning** and optimized filtering (keeping only the top 1000 unseen movies for each user).

### **Balancing Personalization & Popularity**
- **Challenge:** A purely collaborative filtering approach sometimes recommended obscure movies.
- **Solution:** Integrated **genre-based filtering**, ensuring that recommendations align with a user's preferred genres while still considering overall movie popularity.

---

## Results & Impact
**Achieved RMSE:** ~0.777 (lower error means better recommendations).  
**Successfully personalized recommendations** by analyzing user preferences dynamically.  
**Improved efficiency** by reducing dataset size and focusing on high-quality movies.  
**Deployed an interactive Streamlit app** that allows real-time movie suggestions.  

---

## Learnings & Takeaways
- **Data preprocessing is crucial** for scalable and effective recommendation systems.
- **Combining collaborative filtering with content-based approaches** (genre filtering) enhances recommendation quality.
- **Reducing the dataset smartly** (e.g., filtering by rating count) can significantly **boost performance** without sacrificing accuracy.
- **Building an interactive UI (Streamlit)** makes machine learning models more accessible and user-friendly.
