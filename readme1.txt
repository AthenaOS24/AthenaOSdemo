# AI Virtual Psychologist - README

## Introduction
The AI Virtual Psychologist is a chatbot designed to provide basic psychological support and guidance. It consists of a frontend built with HTML, Bootstrap, and JavaScript, and a backend powered by FastAPI.

## Features
- Responsive chat UI with Bootstrap styling.
- Backend API using FastAPI.
- Predefined psychological support responses.
- Real-time communication between frontend and backend.

## Requirements
Ensure you have the following installed:
- Python 3.7+
- FastAPI
- Uvicorn
- A web browser (Chrome, Firefox, etc.)

## Installation & Setup

### 1. Clone the Repository
```sh
 git clone https://github.com/your-repo/ai-virtual-psychologist.git
 cd ai-virtual-psychologist
```

### 2. Set Up the Backend
#### Install Dependencies
```sh
pip install fastapi uvicorn
```

#### Run the Backend Server
```sh
uvicorn backend:app --reload
```
This starts the API at `http://127.0.0.1:8000/chat`.

### 3. Set Up the Frontend
Simply open the `index.html` file in a browser.

Alternatively, you can use a local server:
```sh
python -m http.server 8001
```
Then access it at `http://127.0.0.1:8001`.

## Usage
1. Enter a message in the chat input box.
2. Press "Send" or hit "Enter".
3. The bot will respond based on predefined psychological support prompts.

## Troubleshooting
- If the frontend is not receiving responses, ensure the backend is running at `http://127.0.0.1:8000/chat`.
- Check the browser console (F12 > Console) for any errors.
- Ensure CORS is enabled in the FastAPI backend.

## Future Improvements
- Add NLP processing for smarter responses.
- Store chat history for user analysis.
- Implement user authentication.

## License
MIT License - Free to use and modify.

## Contact
For issues or suggestions, create a GitHub issue or contact the developer.

