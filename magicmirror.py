# Magic Mirror: A Streamlit app that uses Ollama to analyze a live camera feed and describe the person in the picture.
# The app uses the Ollama API to generate a description of the person in the picture.
# Author: Christoph Döllinger
# Date: 2025-01-21

from ollama import generate
import streamlit as st
import cv2
from functools import wraps
from threading import Thread
from streamlit.runtime.scriptrunner import add_script_run_ctx, get_script_run_ctx

# Function wrapper to run in a thread
def run_in_thread(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        thread = Thread(target=func, args=args, kwargs=kwargs)
        ctx = get_script_run_ctx()
        add_script_run_ctx(thread, ctx)
        thread.start()
    return wrapper

# Function to show live camera feed
@run_in_thread
def show_camera():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while st.session_state.camera_active:
        ret, frame = cap.read()
        if not ret:
            st.write("Failed to capture image")
            break
        st.session_state.lastFrame = frame

    cap.release()

# Function to send picture to Ollama
@run_in_thread
def send_to_ollama(image):
    st.session_state.loading = True

    # Convert image to bytes
    _, buffer = cv2.imencode('.jpg', image)
    image_bytes = buffer.tobytes()
    
    # Extract recognized text from Ollama output
    response = generate('llama3.2-vision', 
                        'Describe like a good friend talking to me how I am looking on the photo! Be nice and honest. Just write 1 to 3 sentences like in a text message. Use emoticons and markdown. Start with "Hey there..."', 
                        images=[image_bytes], 
                        stream=False)
    
    st.session_state.response = response.response
    st.session_state.loading = False

@st.fragment(run_every=0.1)
def draw_preview(preview):
    if st.session_state.lastFrame is not None:
        frame = st.session_state.lastFrame
        preview = st.image(frame, channels="BGR")

    # Capture and analyze the picture
    if st.button("Describe Me!"):
        frame = st.session_state.lastFrame
        if frame is not None:
            send_to_ollama(frame)
    
    # Show result or loading message
    if st.session_state.loading:
        st.info("Analyzing the picture, please wait...")
    elif 'response' in st.session_state:
        st.write(st.session_state.response)

# Initialize session states
def init_states():
    if 'camera_active' not in st.session_state:
        st.session_state.camera_active = True
    if 'lastFrame' not in st.session_state:
        st.session_state.lastFrame = None
    if 'camera_started' not in st.session_state:
        st.session_state.camera_started = False
    if 'response' not in st.session_state:
        st.session_state.response = ""
    if 'loading' not in st.session_state:
        st.session_state.loading = False

def main():
    init_states()
    st.title("Magic Mirror")

    # Start the camera preview in a separate thread
    if st.session_state.camera_started is False:
        st.session_state.camera_started = True
        show_camera()
    
    # Show preview image
    preview = st.empty()
    draw_preview(preview)

if __name__ == '__main__':
    main()
