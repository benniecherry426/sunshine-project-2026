import streamlit as st
import json
from modules.speech_handler import SpeechHandler
from modules.document_processor import DocumentProcessor
from modules.data_manager import DataManager
from modules.visualization import Visualization
from config import APP_TITLE, APP_DESCRIPTION

# Page configuration
st.set_page_config(
    page_title=APP_TITLE,
    page_icon="☀️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'speech_handler' not in st.session_state:
    st.session_state.speech_handler = SpeechHandler()
if 'doc_processor' not in st.session_state:
    st.session_state.doc_processor = DocumentProcessor()
if 'data_manager' not in st.session_state:
    st.session_state.data_manager = DataManager()
if 'visualization' not in st.session_state:
    st.session_state.visualization = Visualization()

# Header
st.title("☀️ Sunshine Project 2026")
st.subheader("Accountant AI Chatbot")
st.write(APP_DESCRIPTION)

# Sidebar navigation
with st.sidebar:
    st.title("Navigation")
    page = st.radio("Select a module:", [
        "🏠 Home",
        "🎤 Voice Input",
        "📄 Document Upload",
        "📊 Data Management",
        "📈 Visualization",
        "ℹ️ About"
    ])

# Pages
if page == "🏠 Home":
    st.info("Welcome to Sunshine Project 2026! Select a module from the sidebar to get started.")
    
    st.markdown("""
    ## Features:
    - 🎤 **Voice Input**: Speak naturally to input financial data
    - 📄 **Document Processing**: Upload receipts, invoices, and financial documents
    - 📊 **Data Management**: Create spreadsheets and organize financial data
    - 📈 **Visualization**: Create charts and dashboards from your data
    - 🤖 **AI Analysis**: Intelligent processing using OpenAI API
    """)

elif page == "🎤 Voice Input":
    st.subheader("Voice Input Module")
    st.write("Speak to input financial data naturally. For example: 'I spent 60 dollars for phone bill'")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🎤 Start Listening", key="voice_button"):
            st.session_state.speech_handler.speak("I'm listening. Please tell me about your expense.")
            voice_text = st.session_state.speech_handler.process_voice_input()
            
            if voice_text:
                st.success(f"Transcribed: {voice_text}")
                st.session_state.last_voice_input = voice_text
                
                # Ask for description
                description = st.text_area("Describe this transaction:", value=voice_text)
                category = st.selectbox("Select category:", ["Utilities", "Travel", "Office Supplies", "Meals", "Other"])
                
                if st.button("Save Transaction"):
                    st.success(f"✅ Saved: {description} ({category})")
                    st.session_state.speech_handler.speak("Transaction saved successfully!")

elif page == "📄 Document Upload":
    st.subheader("Document Upload Module")
    st.write("Upload financial documents, receipts, or invoices")
    
    uploaded_file = st.file_uploader("Choose a file", type=['pdf', 'txt', 'docx', 'xlsx', 'csv', 'png', 'jpg', 'jpeg'])
    
    if uploaded_file is not None:
        st.info(f"📁 Processing: {uploaded_file.name}")
        
        # Process the file
        content = st.session_state.doc_processor.process_uploaded_file(uploaded_file)
        
        if content:
            st.success("✅ File processed successfully!")
            st.text_area("Extracted Content:", value=content, height=200)
            
            # Ask for description
            description = st.text_area("Provide a description of this document:")
            
            if st.button("Analyze with AI"):
                st.session_state.speech_handler.speak("Analyzing your document")
                analysis = st.session_state.doc_processor.analyze_with_ai(
                    content,
                    f"Extract financial information and categorize it. Description: {description}"
                )
                
                if analysis:
                    st.subheader("AI Analysis Results:")
                    st.write(analysis)

elif page == "📊 Data Management":
    st.subheader("Data Management Module")
    
    tab1, tab2, tab3 = st.tabs(["Create Spreadsheet", "Add Data", "View Data"])
    
    with tab1:
        st.write("Create a new spreadsheet with custom categories")
        
        spreadsheet_name = st.text_input("Spreadsheet Name:", "Financial_Data")
        
        # Get category names from user
        st.write("**Define Categories:** (Enter category names separated by commas)")
        categories_input = st.text_input("Categories:", "Income,Utilities,Travel,Food,Office Supplies,Entertainment,Other")
        categories = [cat.strip() for cat in categories_input.split(",")]
        
        if st.button("✅ Create Spreadsheet"):
            st.session_state.data_manager.create_spreadsheet(spreadsheet_name, categories)
            st.session_state.speech_handler.speak(f"Spreadsheet {spreadsheet_name} has been created successfully!")
    
    with tab2:
        st.write("Add data to existing spreadsheet")
        
        spreadsheets = st.session_state.data_manager.list_spreadsheets()
        
        if spreadsheets:
            selected_sheet = st.selectbox("Select Spreadsheet:", spreadsheets)
            
            col1, col2, col3 = st.columns(3)
            with col1:
                date = st.date_input("Date:")
            with col2:
                description = st.text_input("Description:")
            with col3:
                amount = st.number_input("Amount:", min_value=0.0, step=0.01)
            
            category = st.selectbox("Category:", ["Income", "Utilities", "Travel", "Food", "Office Supplies", "Entertainment", "Other"])
            
            if st.button("➕ Add Data"):
                st.success("✅ Data added successfully!")
        else:
            st.warning("No spreadsheets found. Create one first!")
    
    with tab3:
        st.write("View data from spreadsheets")
        
        spreadsheets = st.session_state.data_manager.list_spreadsheets()
        
        if spreadsheets:
            selected_sheet = st.selectbox("Select Spreadsheet:", spreadsheets, key="view_sheet")
            
            if st.button("📊 Load Data"):
                file_path = f"spreadsheets/{selected_sheet}"
                data = st.session_state.data_manager.get_spreadsheet_data(file_path)
                
                if data is not None:
                    st.dataframe(data, use_container_width=True)
        else:
            st.warning("No spreadsheets found.")

elif page == "📈 Visualization":
    st.subheader("Visualization Module")
    
    spreadsheets = st.session_state.data_manager.list_spreadsheets()
    
    if spreadsheets:
        selected_sheet = st.selectbox("Select Spreadsheet:", spreadsheets)
        file_path = f"spreadsheets/{selected_sheet}"
        data = st.session_state.data_manager.get_spreadsheet_data(file_path)
        
        if data is not None:
            chart_type = st.selectbox("Select Chart Type:", ["Pie Chart", "Bar Chart", "Line Chart", "Dashboard"])
            
            if chart_type == "Pie Chart":
                st.session_state.visualization.create_pie_chart(data, "Category", "Amount", "Expense Distribution")
            
            elif chart_type == "Bar Chart":
                st.session_state.visualization.create_bar_chart(data, "Category", "Amount", "Expenses by Category")
            
            elif chart_type == "Line Chart":
                if "Date" in data.columns:
                    st.session_state.visualization.create_line_chart(data, "Date", "Amount", "Spending Trend")
                else:
                    st.warning("Date column required for line chart")
            
            elif chart_type == "Dashboard":
                st.session_state.visualization.create_dashboard(data)
    else:
        st.warning("No spreadsheets found. Create one first!")

elif page == "ℹ️ About":
    st.subheader("About Sunshine Project 2026")
    st.markdown("""
    **Sunshine Project 2026** is an intelligent AI-powered accountant chatbot designed to help you manage your finances efficiently.
    
    ### Features:
    - 🎤 **Natural Language Processing**: Speak naturally to input financial data
    - 📄 **Document Recognition**: Extract data from receipts, invoices, and financial documents
    - 🤖 **AI Analysis**: Powered by OpenAI's GPT-4
    - 📊 **Data Organization**: Automatic spreadsheet creation and management
    - 📈 **Visualization**: Beautiful charts and dashboards
    
    ### Technology Stack:
    - **Streamlit** - Web application framework
    - **OpenAI API** - AI analysis and understanding
    - **Python** - Backend programming
    - **Pandas & Openpyxl** - Data management
    - **Matplotlib & Seaborn** - Visualization
    
    ### Getting Started:
    1. Set up your OpenAI API key in `.env` file
    2. Run: `streamlit run app.py`
    3. Start with voice input or document upload
    4. Organize your data into spreadsheets
    5. Generate insights with visualizations
    
    Made with ☀️ for better financial management!
    """)\n