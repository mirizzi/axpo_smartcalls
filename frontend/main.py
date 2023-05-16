import streamlit as st
from datetime import datetime

# Get user's IP address
ip_address = st.experimental_get_query_params().get("ip", ["Unknown"])[0]

# Get current date and time
current_date = datetime.now().strftime("%Y%m%d%H%M%S")

log_txt = open('log_'+ip_address+'.txt', 'a', encoding="utf-8")

log_txt.write('IP Adress: '+ip_address+'\n')
log_txt.write('Start Date: '+current_date+'\n')

# Set page title
st.set_page_config(page_title='Smart Calls',
                   page_icon='./axpo_2.png', layout='wide')

# Set page heading
st.title('Smart Calls')

# Add page subtitle and description
st.write('''
This application analyzes customer service calls to provide insights on customer sentiment and agent performance. 
''')

# Add file uploader component
uploaded_file = st.file_uploader('Choose a call file to analyze', type='mp3')

# If file is uploaded, display its name
if uploaded_file is not None:
    file_name = uploaded_file.name
    current_date = datetime.now().strftime("%Y%m%d%H%M%S")
    log_txt.write('Log Date: '+current_date+'\n')
    log_txt.write('Uploaded File: '+file_name+'\n')
else:
    file_name = '**No file uploaded**'

# # Call File Information
# st.write('## Call File Info')
# st.write('Here is the general info about the file:')
# st.write('File name: ' + file_name)

# # Input box for the prompt
# st.write('## Chat Prompt')
# user_input = st.text_area('Enter your prompt here', key='text_area')
# submitted = st.button('Submit')

# # Process the user input
# if submitted and user_input:
#     st.write('You entered:', user_input)
#     current_date = datetime.now().strftime("%Y%m%d%H%M%S")
#     log_txt.write('Log Date: '+current_date)
#     log_txt.write('Given Prompt: '+user_input)
# else:
#     st.write('**No prompt given**')

# Split the page into two columns
col1, col2 = st.columns(2)

with col1:
    st.write('## Original Call Transcription')
    st.write('Operador: ...')
    st.write('Cliente: ...')

with col2:
    st.write('## Translated Call Transcription')
    st.write('Operator: ...')
    st.write('Client: ...')

# Add call summary section
st.write('## Call Summary')
st.write('Here are some key insights from the call file:')

# Add customer sentiment section
st.write('## Customer Sentiment')
st.write('Here is an analysis of the customer sentiment during the call:')

# Add agent performance section
st.write('## Agent Performance')
st.write('Here is an analysis of the agent performance during the call:')

log_txt.close()
