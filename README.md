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
-   **Serverless Deployment**: AWS SAM template for easy deployment to AWS Lambda.

---

## 🛠️ Tech Stack

-   **Backend**: Python, FastAPI, PyTorch, Transformers, Uvicorn
-   **Frontend**: React, Vite, TypeScript, TailwindCSS
-   **Testing**: PyTest
-   **Deployment**: Docker, AWS SAM, AWS Lambda
-   **CI/CD**: GitHub Actions

---

## 📂 Project Structure

```
SafeLens/
├── backend/
│   ├── app/              # FastAPI application
│   ├── aws/              # AWS Lambda and SAM deployment
│   │   ├── lambda_function.py
│   │   └── Dockerfile
│   ├── tests/
│   ├── Dockerfile        # Docker configuration for local dev
│   ├── requirements.txt
│   ├── samconfig.toml    # SAM configuration
│   └── template.yaml     # SAM template
│
├── frontend/
│   ├── src/
│   │   ├── App.tsx
│   │   └── components/
│   ├── package.json
│   └── tailwind.config.js
│
├── .github/
│   └── workflows/
│       └── ci.yml
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

---
## 🚀 Deploying to AWS with SAM

You can deploy the backend as a serverless application on AWS using the AWS Serverless Application Model (SAM).

### Prerequisites for AWS Deployment

-   AWS CLI, configured with your credentials.
-   AWS SAM CLI.
-   Docker.

### Deployment Steps

1.  Navigate to the `backend` directory.
2.  Build the SAM application. This command builds the Docker image for the Lambda function.

    ```bash
    sam build
    ```

3.  Deploy the application to your AWS account. You will be guided through a series of prompts.

    ```bash
    sam deploy --guided
    ```

Once deployed, SAM will output the API Gateway endpoint URL. You can use this URL to interact with your live serverless backend. You can then update the `fetch` URL in the frontend `App.tsx` to point to your new AWS endpoint.
