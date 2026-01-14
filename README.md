# SRS Ambiguity Detection Chatbot 🤖

A smart NLP-based chatbot that helps analyze Software Requirement Specification (SRS) documents, detects ambiguities, and helps you refine them into clear, professional requirements.

**🔴 Live Demo:** [https://srs-ambiguity-chatbot.vercel.app/](https://srs-ambiguity-chatbot.vercel.app/)

## ✨ Key Features

*   **Ambiguity Detection**: Automatically identifies vague terms like "fast", "user-friendly", "secure", etc.
*   **Interactive Clarification**: Asks you specific follow-up questions to define vague terms (e.g., "How many seconds is 'fast'?").
*   **Requirement Classification**: Classifies requirements as **Functional (FR)** or **Non-Functional (NFR)**.
*   **Smart Suggestions**: Provides measurable, standard improvements for detected ambiguities.
*   **PDF Report Generation**: Generates a professional PDF report with "Before & After" comparisons of your requirements.
*   **In-Memory Processing**: optimized for serverless deployment (Vercel).

## 🚀 How to Run Locally

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/YOUR_USERNAME/srs-ambiguity-chatbot.git
    cd srs-ambiguity-chatbot
    ```

2.  **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**
    ```bash
    python app.py
    ```

5.  **Open in Browser:**
    Go to `http://127.0.0.1:5000`

##  Deployment

This project is configured for deployment on **Vercel** as a serverless Flask application.

### Configuration Files
*   `vercel.json`: Specifies the runtime and build configuration.
*   `requirements.txt`: Lists necessary Python packages.
*   `.gitignore`: Excludes unnecessary files.

To deploy your own version, simply push code to GitHub and import the project into Vercel.

## 🛠️ Tech Stack

*   **Backend**: Python, Flask
*   **Frontend**: HTML5, CSS3, Vanilla JavaScript
*   **PDF Generation**: FPDF2
*   **NLP**: Custom regex-based pattern matching and rule-based classification

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
