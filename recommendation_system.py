data = {
    'Movies': {
        'The Lord of the rings': ['Fantasy', 'Adventure'],
        'Titanic': ['Comedy', 'Romance'],
        'The Avengers': ['Action', 'Adventure', 'Fantasy'],
        'Shutter island': ['Thriller', 'Mystery','Suspense'],
        'Home Alone': ['Comedy', 'Drama']
    },
    'Books': {
        'Jack Reacher': ['Mystery', 'Thriller'],
        'The fault in our stars': ['Fiction', 'Drama'],
        'Harry Potter': ['Science Fiction', 'Adventure'],
        'The lord of rings': ['Fantasy', 'Adventure'],
        'It started with a friend request': ['Fiction', 'Drama','Romance']
    },
    'Series': {
        'Stranger things': ['Horror', 'Drama','Fiction'],
        'Peaky blinders': ['Crime', 'Drama'],
        'Sherlock holmes': ['Crime', 'Mystery'],
        'Dark': ['Thriller', 'Mystery','Supernatural'],
        'Emily in paris': ['Comedy', 'Drama']
    }
}

# Function to recommend items based on user preferences
def recommend_items(category, user_preferences):
    recommended_items = []

    for item, attributes in data[category].items():
        if all(attribute in attributes for attribute in user_preferences):
            recommended_items.append(item)

    return recommended_items

# Function to take user preferences as input
def get_user_preferences():
    print("Enter your preferences (comma-separated) for the selected category:")
    user_input = input().strip().split(',')
    return [preference.strip() for preference in user_input]

# Function to recommend items for a given category based on user preferences
def recommend_category(category):
    print(f"Recommendations for {category}:")
    user_preferences = get_user_preferences()
    recommended_items = recommend_items(category, user_preferences)

    if recommended_items:
        print(f"Recommended {category} for preferences: {', '.join(user_preferences)}")
        for item in recommended_items:
            print(f"{category}: {item}")
    else:
        print(f"No {category} found for the given preferences.")

# Ask the user to select a category (Movies, Books, or Series)
while True:
    print("Select a category: Movies, Books, Series (or 'exit' to quit)")
    selected_category = input().strip().capitalize()

    if selected_category == 'Exit':
        break

    if selected_category in data:
        recommend_category(selected_category)
    else:
        print("Invalid category. Please select Movies, Books, or Series.")