import streamlit as st
import pandas as pd
from surprise import Dataset, Reader, SVD
from collections import Counter

st.title("🎬 Movie Recommendation System")

# User ID input
user_id = st.number_input("Enter User ID:", min_value=1, step=1)

# Load MovieLens dataset
@st.cache_data
def load_data():
    ratings = pd.read_csv("ratings_small.csv")
    movies = pd.read_csv("movies.csv")
    return ratings, movies

ratings, movies = load_data()

# Generate recommendations when button is clicked
if st.button("Show Recommendations"):
    if user_id in ratings["userId"].values:
        # Get movies rated by the user
        user_movies = ratings[ratings["userId"] == user_id]["movieId"].tolist()

        # Extract genres of watched movies
        user_genres = movies[movies["movieId"].isin(user_movies)]["genres"].str.split("|").sum()

        # Identify user's top 3 favorite genres
        top_genres = Counter(user_genres).most_common(3)
        favorite_genres = [genre[0] for genre in top_genres]

        # Get unseen popular movies (rated at least 50 times)
        popular_movies = ratings["movieId"].value_counts()
        unrated_movies = popular_movies[popular_movies > 50].index.tolist()
        unrated_movies = [movie for movie in unrated_movies if movie not in user_movies]

        # Limit to top 1000 movies for faster processing
        unrated_movies = unrated_movies[:1000]

        # Train the model
        reader = Reader(rating_scale=(0.5, 5.0))
        data = Dataset.load_from_df(ratings[["userId", "movieId", "rating"]], reader)
        trainset = data.build_full_trainset()
        model = SVD()
        model.fit(trainset)

        # Make predictions
        predictions = [model.predict(user_id, movie) for movie in unrated_movies]
        predictions.sort(key=lambda x: x.est, reverse=True)

        # Filter recommendations based on user's favorite genres
        filtered_recommendations = []
        for pred in predictions:
            movie_id = pred.iid
            movie_genres = movies[movies["movieId"] == movie_id]["genres"].values
            if any(genre in movie_genres[0] for genre in favorite_genres):
                filtered_recommendations.append(pred)

        # Select top 10 recommendations
        top_recommendations = filtered_recommendations[:10]
        top_movie_ids = [pred.iid for pred in top_recommendations]
        recommended_movies = movies[movies["movieId"].isin(top_movie_ids)][["title", "genres"]]

        # Display results
        st.subheader(f"Recommended Movies for User {user_id}:")
        st.dataframe(recommended_movies)
    else:
        st.warning("⚠️ This User ID is not found in the dataset!")
