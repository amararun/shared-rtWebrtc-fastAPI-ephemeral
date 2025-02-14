# AI Models Proxy Server

This FastAPI application serves as a secure proxy server for various AI model endpoints including OpenAI, Gemini, and OpenRouter. Instead of exposing API keys in frontend applications, this proxy server handles all API calls securely, storing sensitive credentials server-side.

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url> .
   pip install -r requirements.txt
   ```

2. **Environment Variables**
   - Create a `.env` file based on `.env.example`
   - Update the following API keys based on which services you plan to use:
   ```
   OPENAI_API_KEY=your_openai_api_key
   GEMINI_API_KEY=your_gemini_api_key
   OPENROUTER_API_KEY=your_openrouter_api_key
   ```

3. **Configure CORS Settings**
   The application needs to know which origins are allowed to make requests. You have several options:

   a. For testing purposes, you can allow all origins:
   ```python
   allow_origins=["*"]
   ```

   b. For production, specify exact origins:
   ```python
   allow_origins=[
       "https://your-domain.com",
       "http://localhost:8123",  # for local development
       "http://localhost:5199"   # for local development
   ]
   ```

   c. If you're using the current configuration, make sure to add your domain to the existing list of allowed origins in `app.py`

## API Endpoints

### 3.1 Session Endpoint
- **Route**: `/session`
- **Method**: GET
- **Purpose**: Creates a realtime session for OpenAI
- **Parameters**: 
  - `model`: The AI model to use
  - `voice`: The voice configuration
- **Returns**: Session configuration and tokens

### 3.2 OpenAI Chat Completion
- **Route**: `/open-chat-completion`
- **Method**: POST
- **Purpose**: Proxy for OpenAI's chat completion API
- **Input**: Standard OpenAI chat completion payload (messages array, model, temperature, etc.)
- **Returns**: OpenAI's chat completion response

### 3.3 OpenRouter Completion
- **Route**: `/open-router-completion`
- **Method**: POST
- **Purpose**: Proxy for OpenRouter's AI models
- **Input**: OpenRouter compatible chat completion payload
- **Returns**: Model response from OpenRouter

### 3.4 Gemini Chat Completion
- **Route**: `/gemini-chat-completion`
- **Method**: POST
- **Purpose**: Proxy for Google's Gemini AI model
- **Input**: Gemini-compatible content generation payload
- **Returns**: Gemini's generated response

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