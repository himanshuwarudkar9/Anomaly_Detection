import streamlit as st
import joblib

# Load the trained model
model = joblib.load('anomaly_test.pkl')

# Add custom CSS for background image
# Set background image using HTML
st.markdown(
        """
        <style>
        .reportview-container {
            background: url('https://ff12.fastforwardlabs.com/figures/iso.png') no-repeat center center fixed;
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
# Create the Streamlit app
st.title('Web Application Log Anomaly Detection')

# Text input for user to enter log details
st.header('Enter Log Details:')
ip_address = st.text_input('IP Address:')
http_request_line = st.text_input('HTTP Request Line:')
user_agent = st.text_input('User Agent:')
protocol = st.text_input('Protocol:')
http_status_code = st.text_input('HTTP Status Code:')
response_size = st.number_input('Size of Response in Bytes:')
date = st.date_input('Date:')
hour = st.number_input('Hour:')
minute = st.number_input('Minute:')
seconds = st.number_input('Seconds:')
num_requests = st.number_input('Number of Requests:')

# Make a prediction
if st.button('Detect Anomaly'):
    input_data = [ip_address, http_request_line, user_agent, protocol,
                  http_status_code, response_size, date, hour, minute, seconds,
                  num_requests]
    prediction = model.predict([input_data])
    if prediction[0] == 1:
        st.error('Anomaly Detected!')
    else:
        st.success('No Anomaly Detected.')

# Display footer
st.text('This is a demo app for anomaly detection.')

