# SafeLens

**AI-powered content safety, harmful content filtering, and compliance monitoring.**

This repository contains the source code for SafeLens, a platform for real-time content moderation using AI. It includes a Python backend powered by FastAPI and a pre-trained NLP model, along with a modern React frontend.

---

## 🚀 Features

-   **FastAPI Backend**: A high-performance Python backend serving the NLP model.
-   **Transformer-Based NLP**: Uses a `distilbert` model from Hugging Face for text classification (toxicity/sentiment).
-   **React Frontend**: A sleek, responsive dashboard built with Vite, React, and TailwindCSS.
-   **Docker Support**: Containerize the backend for easy deployment.
-   **CI/CD Pipeline**: A GitHub Actions workflow to automatically run tests.

---

## 🛠️ Tech Stack

-   **Backend**: Python, FastAPI, PyTorch, Transformers, Uvicorn
-   **Frontend**: React, Vite, TypeScript, TailwindCSS
-   **Testing**: PyTest
-   **CI/CD**: GitHub Actions
-   **Containerization**: Docker

---

## 📂 Project Structure

```
SafeLens/
├── backend/
│   ├── app/
│   │   ├── main.py         # FastAPI application
│   │   ├── models.py       # Pydantic models
│   │   └── services.py     # NLP moderation logic
│   ├── tests/
│   │   └── test_api.py     # API tests
│   ├── Dockerfile          # Docker configuration
│   └── requirements.txt    # Python dependencies
│
├── frontend/
│   ├── src/
│   │   ├── App.tsx         # Main React component
│   │   └── components/     # Reusable UI components
│   ├── package.json        # Node.js dependencies
│   └── tailwind.config.js  # TailwindCSS configuration
│
├── .github/
│   └── workflows/
│       └── ci.yml          # CI/CD workflow
│
└── README.md
```

---

## 🏁 Getting Started

### Prerequisites

-   Python 3.9+ and Pip
-   Node.js 16+ and npm
-   (Optional) Docker

### 1. Backend Setup

Navigate to the `backend` directory:

```bash
cd backend
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Run the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`. You can access the interactive API documentation at `http://127.0.0.1:8000/docs`.

### 2. Frontend Setup

In a new terminal, navigate to the `frontend` directory:

```bash
cd frontend
```

Install the required Node.js packages:

```bash
npm install
```

Run the React development server:

```bash
npm run dev
```

The frontend application will be available at `http://localhost:5173`.

### 3. Using the Application

1.  Open the frontend URL (`http://localhost:5173`) in your browser.
2.  Enter any text into the text area.
3.  Click "Analyze Content".
4.  The application will send the text to the backend API and display the moderation result.

---

## 🐳 Running with Docker

You can also run the backend inside a Docker container.

1.  Make sure Docker is running.
2.  Build the Docker image from the `backend` directory:

    ```bash
    cd backend
    docker build -t safelens-backend .
    ```

3.  Run the container:

    ```bash
    docker run -p 8000:8000 safelens-backend
    ```

The API will be accessible on `http://localhost:8000` just like before.
