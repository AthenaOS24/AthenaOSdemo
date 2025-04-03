from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Predefined chatbot responses for psychological support
responses = {
    "hello": "Hi there! I'm here to listen and help. 😊 How can I assist you today?",
    "how are you": "I'm just a bot, but I'm here to support you! How are you feeling?",
    "what is your name": "I am your Virtual Psychologist, here to assist you with your thoughts and feelings.",
    "bye": "Goodbye! Remember, you're not alone. Take care! 👋",
    "help": "I can help you talk through your thoughts. Try asking about stress, anxiety, or motivation.",
    "i feel sad": "I'm sorry you're feeling this way. Would you like to talk about what's making you sad?",
    "i am stressed": "Stress can be overwhelming. Have you tried deep breathing or taking a short break?",
    "i am anxious": "Anxiety can be tough. Sometimes, writing down your thoughts can help. Would you like to try that?",
    "i lack motivation": "It's okay to feel unmotivated sometimes. Setting small goals might help. What is one thing you can do today?",
    "i feel lonely": "Feeling lonely is tough. Try reaching out to a friend or engaging in a hobby you enjoy. You're not alone!",
    "i have trouble sleeping": "Sleep issues can be frustrating. Have you tried limiting screen time before bed and maintaining a routine?",
    "thank you": "You're very welcome! I'm always here to listen. 😊",
}

class UserInput(BaseModel):
    message: str

@app.post("/chat")
def chat(user_input: UserInput):
    message = user_input.message.lower().strip()
    return {"response": responses.get(message, "I hear you. Could you tell me more about how you're feeling?")}
