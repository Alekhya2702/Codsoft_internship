import random

# Define a dictionary of rules and responses
ml_guide_rules = {
    "What is machine learning?": " Machine learning is a subfield of artificial intelligence (AI) that focuses on the development of algorithms and statistical models that enable computers to learn and make predictions or decisions without being explicitly programmed.",
    
    "Supervised Learning": "Supervised learning is a type of machine learning where the algorithm is trained on a labeled dataset, meaning it learns from input-output pairs.",
    
    "Unsupervised Learning": " Unsupervised learning is a type of machine learning where the algorithm learns patterns and structures in data without labeled outputs.",
    
    "Reinforcement Learning": " Reinforcement learning is a type of machine learning where an agent learns to make sequential decisions to maximize cumulative rewards in an environment.",
    
    "Overfitting in Machine Learning": " Overfitting occurs when a model learns the training data too well, capturing noise and making it perform poorly on unseen data.",
    
    "Bias-Variance Trade-off": "The bias-variance trade-off is the balance between a model's underfitting (high bias) and overfitting (high variance) when choosing its complexity.",
    
    "Cross-Validation": " Cross-validation is a technique to evaluate the performance of a machine learning model by splitting the dataset into multiple subsets for training and testing.",
    
    "What is a Feature in Machine Learning?": "A feature, also known as a predictor or attribute, is an individual input variable used by a machine learning model.",
    
    "What are Hyperparameters?": "Hyperparameters are parameters of a machine learning model that are set before training and control aspects of the learning process, like model complexity.",
    
    "What is a Confusion Matrix?": "A confusion matrix is a table used to evaluate the performance of a classification model, showing the number of true positives, true negatives, false positives, and false negatives.",
    
    "What is Precision in Classification?": " Precision is a measure of the accuracy of positive predictions made by a classification model. It is calculated as the ratio of true positives to the total positive predictions.",
    
    "What is Recall in Classification?": " Recall, also known as sensitivity or true positive rate, measures the ability of a classification model to identify all relevant instances. It is calculated as the ratio of true positives to the total actual positives.",
    
    "What is a Decision Tree in Machine Learning?": "A decision tree is a supervised learning algorithm that can be used for both classification and regression tasks. It makes decisions by splitting data into branches based on feature values.",

    "What is K-Means Clustering?":" K-Means clustering is an unsupervised learning algorithm used to partition data into K clusters based on similarity."
}

# Define a function to generate responses based on user input
def get_response(user_input):
    user_input = user_input.strip()
    for rule, response in ml_guide_rules.items():
        if user_input.lower() == rule.lower():
            return response
    return "I'm sorry, I don't have information on that specific topic. Please ask about a different aspect of AI."

# Main loop to interact with the chatbot
print("AI Guide Chatbot: Hello! How can I assist you with information about AI?")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("AI Guide Chatbot: Goodbye! If you have more questions in the future, feel free to return.")
        break
    response = get_response(user_input)
    print("AI Guide Chatbot:", response)