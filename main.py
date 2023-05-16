import streamlit as st
from backend.mp3_to_text import SpeechWorker

sw = SpeechWorker()

# Set page title
st.set_page_config(page_title='Smart Calls',
                   page_icon='./png/axpo_2.png', layout='wide')

col1, col2 = st.columns(2)
col1.title('Smart Calls')
col2.image('png/axpo_2.png')

# Add page subtitle and description
st.write('''
This application analyzes customer service calls to provide insights on customer sentiment and agent performance. 
''')

# Add file uploader component
uploaded_file = st.file_uploader('Choose a call file to analyze', type='mp3')

st.write('## Original Call Transcription')
if uploaded_file is not None:
    file_name = uploaded_file.name
    for chunk in sw.recognize_once(uploaded_file):
        st.info(chunk)
else:
    file_name = '**No file uploaded**'
