# Magic Mirror

Magic Mirror is a Streamlit application that uses the Ollama API to analyze a live camera feed and describe the person in the picture. The app captures images from a webcam, sends them to Ollama for analysis, and displays the results in a user-friendly interface.

## Features

- Live camera feed preview
- Capture and analyze images using the Ollama API
- Display descriptive text about the captured image

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/magicmirror.git
    cd magicmirror
    ```

2. **Create a virtual environment and activate it:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Install Ollama:**
    
    Linux:
    ```sh
    curl -fsSL https://ollama.com/install.sh | sh
    ```

    Windows:
    Download and install Ollama from [https://ollama.com/download/OllamaSetup.exe](https://ollama.com/download/OllamaSetup.exe)
    <br>

5. **Pull LLAMA 3.2 Vision model:**  

    To install the llama3.2-vision model, run
    ```sh
    ollama pull llama3.2-vision
    ```
    on the respective command line (e. g. bash, powershell).

## Usage

1. Run the Streamlit application:

    ```sh
    streamlit run magicmirror.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Click on the 'Describe Me!' button and wait for the result.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

Christoph Döllinger

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Ollama API](https://ollama.com/)
