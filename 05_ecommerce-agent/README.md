# Ecommerce-Agent

AI-powered e-commerce platform for solopreneurs. This project demonstrates how to build a online store using Agents for product classification and shipping.

**Key Features:**

- AI product categorization
- Simple product database

**Learn:**

- AI integration in e-commerce
- AI for business automation
- Building scalable AI applications

## Architecture

The project consists of the following components:

1. Frontend: Streamlit Web Application
2. Backend: FastAPI Web Server with RESTful API
3. Services: LLM Service for product classification, Database Service for data management
4. External Components: Groq API for LLM model access
5. Data Storage: JSON file (company_db.json)

## Getting Started

### Prerequisites:
- Python 3.11 or higher
- UV package manager (https://astral.sh/uv)

### Setup:

1. Clone the repository:
   ```
   https://github.com/AsharibAli/agentic-ai-projects.git
   cd agentic-ai-projects/05_ecommerce-agent
   ```

2. Create a virtual environment and install dependencies using UV:
   ```
   # Create virtual environment (if not already created)
   uv venv
   ```

3. Set up environment variables:
   Copy the `.env.sample` file to `.env` and update with your actual API keys from [Groq Console](https://console.groq.com/):
   ```
   cp .env.sample .env
   # Edit .env and add your GROQ_API_KEY
   ```

### Running the application:

1. Start the backend server:
   ```
   uv run server
   ```

2. In a new terminal, start the frontend:
   ```
   uv run web
   ```

3. Access the web interface at http://localhost:8501

### UV Package Manager Commands

- Add new dependencies to pyproject.toml: `uv add package_name`
- Update all dependencies: `uv sync`
- Run Python scripts: `uv run python script.py`
- Execute project scripts: `uv run script_name`

### Project Structure

```
├── config.py               # Configuration settings
├── data/                   # Data directory
├── database/               # Database storage
├── models/                 # Database models
├── pyproject.toml          # Project dependencies and scripts
├── README.md               # Project documentation
├── routes/                 # FastAPI routes
├── run/                    # Run scripts for backend and frontend
├── services/               # Service modules including LLM
├── ui/                     # Streamlit UI components
├── utils/                  # Utility functions
```
