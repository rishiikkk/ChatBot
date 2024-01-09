import nltk
import random
from nltk.chat.util import Chat, reflections

# Define the chatbot responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot.",]
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you!", "I'm just a computer program, so I don't have feelings, but thanks for asking!"]
    ],
    [
        r"(.*) (good|great|fine)",
        ["That's awesome!", "I'm glad to hear that."]
    ],
    [
        r"(.*) (help|support)",
        ["I can help you with various topics. What do you need help with?"]
    ],
    [
        r"quit",
        ["Goodbye!", "See you later!"]
    ],
    [
        r"(.*) (joke)",
        ["hahaha"]
    ]
]
# Create a Chat instance
chat = Chat(pairs, reflections)
def main():
    print("Hello! I'm your chatbot. Type 'quit' to exit the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
        response = chat.respond(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()