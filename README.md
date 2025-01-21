# Magic Mirror

Magic Mirror is a Streamlit application that uses the Ollama API to analyze a live camera feed and describe the person in the picture. The app captures images from a webcam, sends them to Ollama for analysis, and displays the results in a user-friendly interface.

## Features

- Live camera feed preview
- Capture and analyze images using the Ollama API
- Display descriptive text about the captured image

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/magicmirror.git
    cd magicmirror
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit application:

    ```sh
    streamlit run magicmirror.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Use the interface to start the camera, capture an image, and analyze it.

## File Structure

- `magicmirror.py`: The main application script.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

Christoph Döllinger

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Ollama API](https://ollama.com/)
