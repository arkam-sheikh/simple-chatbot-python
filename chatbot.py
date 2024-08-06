import tkinter as tk
from nltk.chat.util import Chat, reflections

# Define the pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hey there!", "Hi!",]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot created by you. You can call me ChatBot.",]
    ],
    [
        r"how are you ?",
        ["I am doing good. How about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright.", "It's OK, never mind.",]
    ],
    [
        r"I am fine",
        ["Great to hear that! How can I help you?",]
    ],
    [
        r"(.*) (location|city) ?",
        ["I am based in the cloud, but I can chat with you from anywhere!",]
    ],
    [
        r"what (.*) want ?",
        ["I just want to chat and make your day better!",]
    ],
    [
        r"(.*) created (.*)",
        ["I was created by a programmer using Python and NLTK.",]
    ],
    [
        r"(.*) (weather|temperature) in (.*)",
        ["I am not sure about the weather in %2, but you can check online for the latest updates.",]
    ],
    [
        r"(.*) help (.*)",
        ["I can help with answering simple questions and keeping you company.",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I enjoy talking about all kinds of sports! What's your favorite?",]
    ],
    [
        r"who (.*) (movie|actor|actress) ?",
        ["I love many movies and actors. What's your favorite?",]
    ],
    [
        r"quit",
        ["Bye! Take care.",]
    ],
    [
        r"what is your favorite color ?",
        ["I like blue. What's your favorite color?",]
    ],
    [
        r"do you like music ?",
        ["Yes, I love music! What about you?",]
    ],
    [
        r"can you help me with (.*) ?",
        ["I'll do my best to help you with %1.",]
    ],
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!",]
    ],
]

# Create Chat instance
chatbot = Chat(pairs, reflections)

# Define the function to handle sending messages
def send_message():
    user_input = user_entry.get()
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, "You: " + user_input + "\n")
    chat_log.config(state=tk.DISABLED)
    
    response = chatbot.respond(user_input)
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, "Bot: " + (response if response else "I didn't understand that.") + "\n")
    chat_log.config(state=tk.DISABLED)
    
    user_entry.delete(0, tk.END)
    chat_log.yview(tk.END)

# Create the main application window
app = tk.Tk()
app.title("ChatBot")

# Create chat log text area
chat_log = tk.Text(app, state=tk.DISABLED, width=50, height=20)
chat_log.grid(row=0, column=0, columnspan=2)

# Create user input entry field
user_entry = tk.Entry(app, width=40)
user_entry.grid(row=1, column=0)

# Create send button
send_button = tk.Button(app, text="Send", command=send_message)
send_button.grid(row=1, column=1)

# Start the application
app.mainloop()
