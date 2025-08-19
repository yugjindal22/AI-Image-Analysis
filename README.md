# 🤖 AI Image Analysis Chat

A powerful Streamlit-based web application that combines image analysis with conversational AI using Google's Gemini 2.5 Flash model. Upload images and chat with AI about them in real-time!

## ✨ Features

- 📸 **Image Upload & Analysis** - Support for PNG, JPG, JPEG, GIF, BMP, WEBP formats
- 💬 **Conversational AI** - Chat with Google Gemini about your images
- 🧠 **Context Awareness** - AI remembers your conversation history
- 🔄 **Auto Image Clear** - Images automatically clear from context after analysis
- 🎨 **Clean UI** - Modern, responsive Streamlit interface
- ⚡ **Real-time Responses** - Streaming AI responses with thinking indicators

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **AI Model**: Google Gemini 2.5 Flash
- **Image Processing**: Pillow (PIL)
- **Package Management**: uv
- **Environment**: Python 3.11+

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher
- Google Gemini API key

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yugjindal22/AI-Image-Analysis.git
   cd AI-Image-Analysis
   ```

2. **Install dependencies using uv**

   ```bash
   uv sync
   ```

3. **Set up environment variables**
   Create a `.env` file in the project root:

   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

4. **Run the application**

   ```bash
   uv run streamlit run frontend.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:8501`

## 🎯 How to Use

1. **Upload an Image**

   - Use the sidebar to upload an image (drag & drop or browse)
   - Supported formats: PNG, JPG, JPEG, GIF, BMP, WEBP

2. **Start Chatting**

   - Type your question about the image in the chat input
   - Ask anything: "What do you see?", "Describe the colors", "What's happening here?"

3. **Continue the Conversation**

   - AI remembers your conversation history
   - Ask follow-up questions like "What did I ask before?"
   - Reference previous parts of the conversation

4. **Upload New Images**
   - Upload a new image anytime to change context
   - Previous image context is automatically cleared

## 💡 Example Questions

- "What objects do you see in this image?"
- "Describe the colors and mood of this picture"
- "Is there any text visible in the image?"
- "What emotions does this image convey?"
- "What did we discuss about the previous image?"
- "Can you elaborate on your last response?"

## 📁 Project Structure

```
AI-Image-Analysis/
├── frontend.py          # Streamlit web interface
├── main.py             # Core AI functions and Gemini integration
├── pyproject.toml      # Project dependencies and configuration
├── uv.lock            # Locked dependency versions
├── .env               # Environment variables (create this)
├── .gitignore         # Git ignore rules
├── README.md          # Project documentation
└── doraemon.png       # Sample image for testing
```

## 🔧 Configuration

### Environment Variables

| Variable         | Description                | Required |
| ---------------- | -------------------------- | -------- |
| `GEMINI_API_KEY` | Your Google Gemini API key | Yes      |

### Getting a Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key
4. Copy the key to your `.env` file

## 🎨 Features Overview

### Image Analysis

- **Multi-format Support**: Handles various image formats
- **Automatic Processing**: Images are processed and analyzed instantly
- **Context Management**: Images are cleared after analysis to prevent context bleeding

### Conversational AI

- **Memory**: AI remembers your entire conversation
- **Context Awareness**: Can reference previous messages and responses
- **Natural Language**: Ask questions in natural, conversational language

### User Interface

- **Responsive Design**: Works on desktop and mobile
- **Real-time Updates**: See messages appear as you type
- **Visual Feedback**: Loading indicators and status messages
- **Clean Layout**: Organized sidebar and main chat area

## 🔄 API Functions

### `generate_with_image(image_bytes, text_prompt, mime_type, chat_history)`

Analyzes an image with text prompt and conversation context.

### `generate_text_only(text_prompt, chat_history)`

Generates text responses with conversation context (no image).

## 🛡️ Error Handling

- **API Key Validation**: Checks for valid Gemini API key
- **Image Format Validation**: Ensures supported image formats
- **Error Messages**: Clear, user-friendly error messages
- **Graceful Degradation**: Continues working even if some features fail

## 🚧 Development

### Running in Development Mode

```bash
uv run streamlit run frontend.py --server.runOnSave true
```

### Adding Dependencies

```bash
uv add package_name
```

### Code Structure

- `frontend.py`: Streamlit UI and user interaction logic
- `main.py`: Core AI functions and Gemini API integration

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🐛 Issues & Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yugjindal22/AI-Image-Analysis/issues) page
2. Create a new issue if your problem isn't already reported
3. Provide detailed information about the problem

## 🙏 Acknowledgments

- **Google Gemini**: For providing the powerful AI model
- **Streamlit**: For the excellent web framework
- **uv**: For fast and reliable package management

## 📊 Stats

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red?style=flat-square&logo=streamlit)
![Gemini](https://img.shields.io/badge/Google-Gemini%202.5-green?style=flat-square&logo=google)

---

Made with ❤️ by [Yug Jindal](https://github.com/yugjindal22)
