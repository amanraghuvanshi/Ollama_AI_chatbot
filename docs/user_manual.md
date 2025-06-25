# User Manual

## Overview

Welcome to the **DeepSeek AI Chatbot** user manual! This locally hosted chatbot uses the `deepseek-r1:1.5b` model to provide intelligent responses to your queries. The application features an intuitive frontend and robust backend for seamless interaction.

---

## System Requirements

### Hardware

* A system with at least:

  * **8 GB RAM** (16 GB recommended for optimal performance)
  * **4 CPU cores**
  * **10 GB free disk space**

### Software

* **Python 3.8+**
* **Pip** (Python package installer)
* **Ollama CLI** (installed and configured)
* **Streamlit** or **Gradio** (for frontend interaction)
* Supported operating systems:

  * Windows 10+
  * macOS 10.15+
  * Linux (Ubuntu 20.04 or later)

---

## Installation and Setup

### Step 1: Clone the Repository

1. Open your terminal or command prompt.
2. Clone the project repository:

   ```bash
   git clone <repository-url>
   cd project-root
   ```

### Step 2: Set Up Python Environment

1. Create a virtual environment:

   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:

   * **Windows**:

     ```bash
     venv\Scripts\activate
     ```
   * **Mac/Linux**:

     ```bash
     source venv/bin/activate
     ```
3. Install required dependencies:

   ```bash
   pip install -r backend/requirements.txt
   pip install -r frontend/requirements.txt
   ```

### Step 3: Install and Configure Ollama

1. Install the Ollama CLI:

   * Follow [Ollama's installation guide](https://ollama.com/docs/installation).
2. Pull the `deepseek-r1:1.5b` model:

   ```bash
   ollama pull deepseek-r1:1.5b
   ```

### Step 4: Set Environment Variables

1. Create a `.env` file in the `project-root` directory:

   ```plaintext
   OLLAMA_PATH=/path/to/ollama
   ```
2. Modify `OLLAMA_PATH` based on your system.

---

## Running the Application

### Backend

1. Start the backend server:

   ```bash
   python backend/app.py
   ```
2. The backend runs on:

   ```
   http://localhost:8000
   ```

### Frontend

Choose one of the following interfaces:

#### Option 1: Streamlit

1. Run the Streamlit application:

   ```bash
   streamlit run frontend/streamlit_app.py
   ```
2. Open the URL displayed in the terminal (e.g., `http://localhost:8501`).

#### Option 2: Gradio

1. Run the Gradio application:

   ```bash
   python frontend/gradio_app.py
   ```
2. Open the URL displayed in the terminal (e.g., `http://localhost:7860`).

---

## Using the Application

### Querying the Chatbot

1. Enter your query in the input box.
2. Press **Submit** (Streamlit) or **Send** (Gradio).
3. The AI model processes your query and displays the response.

### Example Queries

* **General Knowledge:**

  * *"What is artificial intelligence?"*
* **Technical Support:**

  * *"Explain the difference between supervised and unsupervised learning."*
* **Creative Assistance:**

  * *"Write a poem about technology."*

---

## Troubleshooting

### Common Issues

1. **Model Not Found:**

   * Ensure the `deepseek-r1:1.5b` model is pulled using the Ollama CLI.
   * Verify `OLLAMA_PATH` in the `.env` file is correct.

2. **Backend Not Responding:**

   * Ensure the backend server is running (`python backend/app.py`).
   * Check if another service is using port 8000.

3. **Frontend Not Loading:**

   * Ensure all frontend dependencies are installed.
   * Restart the application.

### Viewing Logs

* Logs are stored in the `logs/` directory:

  * `app.log` for general logs
  * `errors.log` for error-specific logs

---

## Future Enhancements

* Integration with external APIs for extended capabilities.
* Advanced frontend customization options.
* Multi-language support.

---

## Support

For questions or issues, please contact:

* **Email:** [support@example.com](mailto:support@example.com)
* **GitHub Issues:** [Project Repository](https://github.com/your-repository-link)

Thank you for using the DeepSeek AI Chatbot!
