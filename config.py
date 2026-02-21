import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenAI Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = "gpt-4-turbo"

# Application Configuration
APP_TITLE = "Sunshine Project 2026 - Accountant AI Chatbot"
APP_DESCRIPTION = "An intelligent AI chatbot for financial document processing and analysis"

# Upload Configuration
UPLOAD_FOLDER = "uploads"
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
ALLOWED_EXTENSIONS = {'pdf', 'txt', 'docx', 'xlsx', 'csv', 'png', 'jpg', 'jpeg'}

# Speech Configuration
SPEECH_RECOGNITION_TIMEOUT = 10
SPEECH_LANGUAGE = "en-US"

# Data Configuration
DATA_FOLDER = "data"
SPREADSHEET_FOLDER = "spreadsheets"

# Create necessary directories
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(DATA_FOLDER, exist_ok=True)
os.makedirs(SPREADSHEET_FOLDER, exist_ok=True)