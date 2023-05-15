import streamlit as st

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
else:
    file_name = '**No file uploaded**'

# Call File Information
st.write('## Call File Info')
st.write('Here is the general info about the file:')
st.write('File name: ' + file_name)

# Add call summary section
st.write('## Call Summary')
st.write('Here are some key insights from the call file:')

# Add customer sentiment section
st.write('## Customer Sentiment')
st.write('Here is an analysis of the customer sentiment during the call:')

# Add agent performance section
st.write('## Agent Performance')
st.write('Here is an analysis of the agent performance during the call:')
