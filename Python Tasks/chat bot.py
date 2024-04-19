import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')  # Download tokenizer for sentence splitting


pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, nice to meet you!", "Hi %1! How can I help you today?"]
    ],
    [
        r"what is your name?",
        ["My name is Chatbot. What's yours?"]
    ],
    [
        r"how are you doing?",
        ["I'm doing well, thanks for asking! How about you?"]
    ],
    [
        r"(.*) weather (.*)",
        ["Sorry, I can't provide weather information yet. But I can tell you a fun fact: Did you know that lightning can heat the air around it to 50,000 degrees Fahrenheit?"]
    ],
    [
        r"goodbye",
        ["Goodbye! Have a nice day."]
    ],
    [
        r"(.*)",
        ["Sorry, I don't understand. Can you rephrase that?"]
    ]
]


def chatbot():
    print("Hi! I'm a simple chatbot. How can I help you?")

    reflections = {
        "what is your name?": "My name is Chatbot",
        "how are you?": "I'm doing well, thanks for asking!"
    }

    chatbot = Chat(pairs, reflections)
    chatbot.converse()


if __name__ == "__main__":
    chatbot()



# Explanation:

# Import Libraries:

# nltk: Provides Natural Language Toolkit for text processing.
# Chat and reflections from nltk.chat.util: Classes for building chatbots.
# Download Resources:

# nltk.download('punkt'): Downloads the Punkt tokenizer for splitting sentences.
# Define Chat Patterns and Responses:

# pairs: A list of tuples containing two elements:
# The first element is a regular expression that defines the pattern the user might say.
# The second element is a list of possible responses the chatbot can give.
# Define Reflections (Optional):

# reflections: A dictionary that maps user questions to predefined chatbot responses.
# chatbot() Function:

# Prints a greeting message.
# Creates a Chat object with the defined pairs and reflections.
# Calls the converse() method to start the conversation.
# Run the Chatbot:

# The if __name__ == "__main__": block ensures the chatbot() function only runs when this script is executed directly.
# Limitations:

# This is a basic example and doesn't understand complex sentences.
# You can extend the pairs list to handle more conversation topics.
# Consider using nltk.classify for advanced pattern matching and classification.
# Further Enhancements:

# Explore libraries like spaCy for more advanced NLP capabilities.
# Train the chatbot on a larger dataset to improve its responses.
# Integrate with external APIs to provide information (e.g., weather).
