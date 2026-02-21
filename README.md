# ☀️ Sunshine Project 2026 - Accountant AI Chatbot

An intelligent AI-powered chatbot for financial document processing, data analysis, and visualization using OpenAI API and Streamlit.

## 🌟 Features

- **🎤 Voice Input**: Speak naturally to input financial data (e.g., "I spent 60 dollars for phone bill")
- **📄 Document Processing**: Upload and extract data from PDFs, images, invoices, and receipts
- **💬 Natural Language Understanding**: AI-powered interpretation of financial transactions
- **📊 Spreadsheet Management**: Create custom spreadsheets with categorized data
- **📈 Visualization**: Generate charts, graphs, and dashboards from your financial data
- **🤖 AI Analysis**: Powered by OpenAI's GPT-4 for intelligent financial insights

## 🛠️ Technology Stack

- **Streamlit** - Web application framework
- **OpenAI API** - AI processing and analysis
- **Python 3.8+** - Programming language
- **Pandas** - Data manipulation
- **Openpyxl** - Excel spreadsheet handling
- **Matplotlib & Seaborn** - Data visualization
- **SpeechRecognition** - Voice input processing
- **pyttsx3** - Text-to-speech output

## 📋 Prerequisites

- Python 3.8 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))
- Microphone (for voice input)
- Speakers (for audio feedback)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/benniecherry426/sunshine-project-2026.git
   cd sunshine-project-2026
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your OpenAI API key**
   - Create a `.env` file in the project root:
   ```bash
   OPENAI_API_KEY=your_api_key_here
   ```

## 💻 Running the Application

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

## 📖 Usage

### 1. **Voice Input**
   - Click "Start Listening" button
   - Speak naturally about your financial transaction
   - The bot will transcribe and ask for categorization
   - Data is saved to your spreadsheet

   Example: "I spent 60 dollars for phone bill"

### 2. **Document Upload**
   - Upload receipts, invoices, or financial documents (PDF, JPG, PNG, DOCX)
   - The bot extracts text and financial information
   - Provide a description of the document
   - AI analyzes and categorizes the data

### 3. **Data Management**
   - Create custom spreadsheets with your categories
   - Add transactions manually or from processed documents
   - View all your financial data in organized tables
   - Export data as Excel files

### 4. **Visualization**
   - Generate pie charts for expense distribution
   - Create bar charts for category analysis
   - View spending trends with line charts
   - Access comprehensive financial dashboards

## 📁 Project Structure

```
sunshine-project-2026/
├── app.py                      # Main Streamlit application
├── config.py                   # Configuration settings
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore file
├── .env                        # API keys (create this file)
├── README.md                   # This file
├── modules/
│   ├── speech_handler.py      # Voice input/output handling
│   ├── document_processor.py  # Document and image processing
│   ├── data_manager.py        # Spreadsheet management
│   └── visualization.py       # Charts and dashboards
├── uploads/                    # Uploaded documents (auto-created)
├── data/                       # Data files (auto-created)
└── spreadsheets/              # Generated spreadsheets (auto-created)
```

## 🔧 Configuration

Edit `config.py` to customize:
- OpenAI model version
- Speech recognition language
- Upload folder location
- Maximum file size
- Application title and description

## 📚 Module Details

### **speech_handler.py**
- Captures audio input from microphone
- Converts speech to text using Google Speech Recognition
- Converts text to speech for audio feedback

### **document_processor.py**
- Extracts text from PDFs, images, Word documents
- Uses OpenAI Vision API for image analysis
- Analyzes extracted content with AI

### **data_manager.py**
- Creates Excel spreadsheets with custom categories
- Adds transactions to existing spreadsheets
- Manages financial data in structured format

### **visualization.py**
- Generates pie, bar, and line charts
- Creates comprehensive financial dashboards
- Visualizes spending patterns and trends

## 🤖 AI Capabilities

The bot uses OpenAI's GPT-4 to:
- Understand natural language financial descriptions
- Extract data from documents and images
- Categorize transactions intelligently
- Analyze spending patterns
- Provide financial insights

## 🔐 Security

- API keys stored in `.env` file (never commit this!)
- Local data storage in `uploads/` and `data/` folders
- No external data sharing by default

## 🐛 Troubleshooting

**Microphone not working:**
- Check if microphone is properly connected
- Ensure browser has microphone permissions
- Try adjusting `SPEECH_RECOGNITION_TIMEOUT` in config.py

**OpenAI API errors:**
- Verify API key is correct in `.env` file
- Check API key has sufficient credits
- Ensure internet connection is active

**File upload issues:**
- Check file size is under 10MB (adjustable in config.py)
- Supported formats: PDF, DOCX, PNG, JPG, JPEG, TXT, XLSX, CSV

## 📊 Example Workflow

1. Click "Voice Input" → Speak "I spent $50 on lunch"
2. Bot asks for category (select "Meals")
3. Data saved to spreadsheet
4. Go to "Visualization" → Create pie chart
5. See expenses distributed by category

## 🤝 Contributing

Contributions are welcome! Please feel free to:
- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation

## 📝 License

This project is open source and available under the MIT License.

## 📧 Contact & Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check existing documentation in this README

## 🎯 Roadmap

Future enhancements:
- Bank account integration
- Real-time expense tracking
- Multi-user support
- Mobile app version
- Advanced AI predictions
- Email report generation
- Database backend

---

Made with ☀️ by benniecherry426 - Sunshine Project 2026