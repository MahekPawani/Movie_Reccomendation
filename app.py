from data_processing import load_datasets
from content_based import ContentBasedRecommender
from collaborative import CollaborativeRecommender
from hybrid import HybridRecommender

def main():
    ratings, movies, credits, keywords, links = load_datasets()

    # Build content model
    content_model = ContentBasedRecommender(movies)
    content_model.build_model()

    # Build collaborative model
    collab_model = CollaborativeRecommender(ratings)
    collab_model.build_model()

    # Build hybrid system
    hybrid = HybridRecommender(content_model, collab_model, movies, links)

    # Example
    user_id = 1
    movie_title = "Toy Story"

    recommendations = hybrid.recommend(user_id, movie_title, top_n=5)

    print("\nRecommended Movies:")
    for movie in recommendations:
        print(movie)

if __name__ == "__main__":
    main()


from assistant import MovieAssistant

# After building hybrid model
assistant = MovieAssistant(hybrid, movies)

print("Movie Assistant Ready! Type 'exit' to quit.")

while True:
    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        break

    response = assistant.handle_request(user_id=1, user_input=user_input)
    print("\nAssistant:", response)
