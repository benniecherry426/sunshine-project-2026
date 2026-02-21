# 🚀 Setup Guide - Sunshine Project 2026

Complete step-by-step instructions to get your Accountant AI Chatbot running.

## Prerequisites

- **Python 3.8 or higher** - [Download here](https://www.python.org/downloads/)
- **OpenAI API Key** - [Get one here](https://platform.openai.com/api-keys)
- **Git** - [Download here](https://git-scm.com/) (optional)
- **Microphone & Speakers** - For voice features

## Step-by-Step Installation

### 1. Clone the Repository

**Option A: Using Git**
```bash
git clone https://github.com/benniecherry426/sunshine-project-2026.git
cd sunshine-project-2026
```

**Option B: Download ZIP**
1. Go to https://github.com/benniecherry426/sunshine-project-2026
2. Click "Code" → "Download ZIP"
3. Extract the ZIP file
4. Open terminal/command prompt in the extracted folder

### 2. Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- streamlit (web framework)
- openai (AI API)
- SpeechRecognition (voice input)
- pyttsx3 (text-to-speech)
- pandas (data handling)
- openpyxl (Excel files)
- matplotlib & seaborn (charts)
- And more...

### 4. Set Up OpenAI API Key

1. Go to [OpenAI Platform](https://platform.openai.com/account/api-keys)
2. Sign up or log in
3. Create a new API key
4. Copy the key (you won't see it again!)

5. Create `.env` file in project root:
   ```
   OPENAI_API_KEY=sk-your-key-here
   ```

**IMPORTANT:** Never share or commit your `.env` file!

### 5. Verify Installation

Test that everything is installed correctly:

```bash
python -c "import streamlit; import openai; import speech_recognition; print('✅ All dependencies installed!')"
```

You should see: `✅ All dependencies installed!`

### 6. Run the Application

```bash
streamlit run app.py
```

**Expected output:**
```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://your-ip:8501
```

The app will automatically open in your browser!

## 🎤 First Time Voice Setup

**Windows:**
1. Check microphone in Settings > Sound > Input devices
2. Set default microphone
3. Test microphone in system settings

**macOS:**
1. System Preferences > Security & Privacy > Microphone
2. Ensure browser has permission
3. Test microphone in System Preferences > Sound

**Linux:**
1. Check ALSA audio: `alsamixer`
2. Ensure PulseAudio is running
3. Test with: `arecord test.wav`

## 📝 First Time Use Checklist

- [ ] Python 3.8+ installed
- [ ] Virtual environment activated
- [ ] requirements.txt installed
- [ ] `.env` file created with API key
- [ ] Microphone tested and working
- [ ] `streamlit run app.py` command works
- [ ] App opens in browser at localhost:8501

## 🧪 Testing the Features

### Test 1: Voice Input
1. Go to "Voice Input" tab
2. Click "Start Listening"
3. Say: "I spent 10 dollars for coffee"
4. Verify transcription appears

### Test 2: Document Upload
1. Go to "Document Upload" tab
2. Upload any PDF or image file
3. Verify content is extracted

### Test 3: Spreadsheet Creation
1. Go to "Data Management" tab
2. Click "Create Spreadsheet" tab
3. Create a test spreadsheet
4. Verify file appears in spreadsheets folder

### Test 4: Visualization
1. Add some sample data
2. Go to "Visualization" tab
3. Create a chart
4. Verify chart displays

## 🔧 Troubleshooting

### Issue: "Python not found"
**Solution:**
- Ensure Python is installed: `python --version`
- On macOS/Linux, try: `python3 --version`
- Add Python to PATH if needed

### Issue: "ModuleNotFoundError"
**Solution:**
- Ensure virtual environment is activated (you see `(venv)` in terminal)
- Reinstall requirements: `pip install -r requirements.txt`

### Issue: "OpenAI API error"
**Solution:**
- Check `.env` file exists in project root
- Verify API key is correct (starts with `sk-`)
- Check API key has credits: https://platform.openai.com/account/billing/overview
- Ensure internet connection is active

### Issue: "Microphone not detected"
**Solution:**
- Restart the app: `Ctrl+C` then `streamlit run app.py`
- Check system microphone settings
- Try different microphone input source
- Increase timeout in config.py: `SPEECH_RECOGNITION_TIMEOUT = 15`

### Issue: "Streamlit not starting"
**Solution:**
- Clear Streamlit cache: `streamlit cache clear`
- Kill any existing processes: `pkill -f streamlit`
- Reinstall streamlit: `pip install --upgrade streamlit`

### Issue: "Port 8501 already in use"
**Solution:**
- Run on different port: `streamlit run app.py --server.port 8502`
- Or kill the process using port 8501

## 🌐 Running on Network

To access the app from another computer:

```bash
streamlit run app.py --server.address 0.0.0.0
```

Then use: `http://your-computer-ip:8501`

## 💾 File Structure After Setup

```
sunshine-project-2026/
├── .env                        # Your API key (AUTO-CREATED)
├── venv/                       # Virtual environment (AUTO-CREATED)
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── SETUP_GUIDE.md
├── .gitignore
├── modules/
│   ├── __init__.py            # (Create if missing)
│   ├── speech_handler.py
│   ├── document_processor.py
│   ├── data_manager.py
│   └── visualization.py
├── uploads/                    # AUTO-CREATED on first use
├── data/                       # AUTO-CREATED on first use
└── spreadsheets/              # AUTO-CREATED on first use
```

## 🆘 Getting Help

1. **Check the README.md** - Common questions answered
2. **Review config.py** - Customizable settings
3. **Check logs** - Streamlit shows errors in terminal
4. **GitHub Issues** - Report bugs or ask questions

## ✅ Next Steps

Once everything is working:

1. **Upload a real receipt** - Test document processing
2. **Try voice input** - Speak a transaction
3. **Create a spreadsheet** - Organize your data
4. **Generate charts** - Visualize your finances

## 🎓 Learning Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [OpenAI API Guide](https://platform.openai.com/docs/api-reference)
- [Python Guide](https://docs.python.org/3/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)

---

**You're all set! 🎉 Start using your Accountant AI Chatbot!**

For issues: Check troubleshooting section above or open a GitHub issue.