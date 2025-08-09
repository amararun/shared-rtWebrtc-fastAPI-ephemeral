# AI Models Proxy Server

## Live App
A full version of app using this backed is deployed and available at [app.tigzig.com](https://app.tigzig.com)  
DATS-4 : Database AI Suite - Version 4 as well as Voice AI Apps on the site

This FastAPI application serves as a secure proxy server for various AI model endpoints including OpenAI, Gemini, and OpenRouter. Instead of exposing API keys in frontend applications, this proxy server handles all API calls securely, storing sensitive credentials server-side.

## Features

- **Secure API Key Management**: Keeps all your API keys on the server, so you don't have to expose them in your frontend code.
- **OpenAI Fallback**: Automatically switches to OpenRouter if a request to OpenAI fails or times out, ensuring high availability.
- **Resilient Requests**: Implements a retry mechanism with exponential backoff for OpenAI requests, making the connection more reliable.
- **Structured Logging**: Keeps detailed logs of requests and responses for easy debugging and monitoring.

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url> .
   pip install -r requirements.txt
   ```

2. **Environment Variables**
   - Create a `.env` file by copying the `.env.example` file.
   - The `.env.example` file contains dummy keys. Replace them with your actual API keys for the services you intend to use.
   ```
   OPENAI_API_KEY=your_openai_api_key
   GEMINI_API_KEY=your_gemini_api_key
   OPENROUTER_API_KEY=your_openrouter_api_key
   OPENAI_FALLBACK=google/gemini-pro # Optional: Specify a fallback model on OpenRouter
   ```

3. **Configure CORS Settings**
   You need to configure which domains are allowed to make requests to the server. Open `app.py` and modify the `allow_origins` list.

   - **For development**, you can use a permissive setting, but this is not recommended for production:
     ```python
     allow_origins = ["*"]
     ```
   - **For production**, you should list the specific domains that will access your proxy:
     ```python
     allow_origins = [
        "https://your-frontend-app.com",
        "https://your-ai-tool.com",
        "http://localhost:1234", # Example for local development
        "http://localhost:5678"  # Example for another local service
        ]
     ```

## API Endpoints

### Session Endpoint
- **Route**: `/session`
- **Method**: GET
- **Purpose**: Initiates a real-time streaming session with OpenAI's audio API. This is useful for applications that require low-latency voice communication.
- **Parameters**: 
  - `model`: The AI model to use (e.g., `gpt-4o`).
  - `voice`: The voice to use for the session (e.g., `alloy`).
- **Returns**: Session configuration details, including a session ID and tokens.

### OpenAI Chat Completion
- **Route**: `/open-chat-completion`
- **Method**: POST
- **Purpose**: A proxy for OpenAI's chat completion API. If the request to OpenAI fails or times out, it automatically falls back to a specified OpenRouter model.
- **Input**: Standard OpenAI chat completion payload.
- **Returns**: A standard chat completion response from either OpenAI or OpenRouter.

### OpenRouter Completion
- **Route**: `/open-router-completion`
- **Method**: POST
- **Purpose**: A direct proxy for OpenRouter's chat completion API, allowing you to use any model available on their platform.
- **Input**: OpenRouter compatible chat completion payload.
- **Returns**: A chat completion response from OpenRouter.

### Gemini Chat Completion
- **Route**: `/gemini-chat-completion`
- **Method**: POST
- **Purpose**: A proxy for Google's Gemini API.
- **Input**: A Gemini-compatible content generation payload.
- **Returns**: A response from the Gemini API.

## Running the Application

Start the server using uvicorn:
```bash
uvicorn app:app --reload
```

The server will start on `http://localhost:8000` by default.

## Security Considerations

- Never commit your `.env` file to version control
- Always use specific origins in production instead of wildcard (*) CORS settings
- Implement rate limiting and additional security measures for production use 



-------
Built by Amar Harolikar // More tools at [app.tigzig.com](https://app.tigzig.com)  // [LinkedIn Profile](https://www.linkedin.com/in/amarharolikar)
