# Vertical AI Agents Starter Template

[![CI](https://github.com/langchain-ai/react-agent/actions/workflows/unit-tests.yml/badge.svg)](https://github.com/langchain-ai/react-agent/actions/workflows/unit-tests.yml)
[![Integration Tests](https://github.com/langchain-ai/react-agent/actions/workflows/integration-tests.yml/badge.svg)](https://github.com/langchain-ai/react-agent/actions/workflows/integration-tests.yml)

## Directory Structure
- All prototyping notebooks are in the prototypes directory.
- All final agents will live in in the src directory.

## Getting Started

### Prerequisites

1. **Install `uv` Package Manager:**
   ```bash
   pip install uv

### Local Setup

To get startedfollow these steps:

1. **Clone the repository:**

   ```sh
   git clone https://github.com/...
   cd ...
   ```

2. **Create a `.env` file:**

Copy the `.env.example` file to `.env` and update the environment variables as needed:

```sh
cp .env.example .env
```

3. **Run LangGraph Server:**

a. Install uv package manager ```python pip install uv```

b. Create Virtual Environment and activate it 
```python 
uv venv
source .venv/bin/activate
```

c. Install packages in pyproject.toml
```python 
uv run
```

d. Run LangGraph Server
- Ensure you have docker engine running (i.e: Open Docker Desktop)
```python 
uv pip install langgraph-cli
uv run langgraph up
```

If you get any error in `d` step stop all containers, run `docker system prune` and try again.


---------------------------------------------------------------------------------------------

## How To Use With Docker & Compose file

### Step 01 : Clone This Repo

```bash
https://github.com/panaversity/langgraph-agents-template.git
```

### Step 02 : Create Docker Image 

 - Install Docker Desktop

 - Open Docker Desktop

 - Run Below Command to create Docker Image & also Container up

 ```bash
 docker compose up 
 ```

 Or if we want to run in detach mode ( Background )

 ```bash
 docker compose up -d 
 ```

### Step 03 : Open Langgraph Studio

 - Click Below Link to view your graph

 <a href="https://smith.langchain.com/studio/thread?baseUrl=http%3A%2F%2F127.0.0.1%3A8123">Langgraph Studio URL</a>


### Step 04 : How We REflect your change in container

 - Simply Down Your Container

 ```bash
 docker compose down
 ```

 - Then again up your container

 ```bash
 docker compose up -d
 ```

 - It's reflect your local changes in Container & Graph
 
### Step 05 : Change model from OPENAI to GOOGLE GEMINI (OPTIONAL)

 - in `configration.py` file change the below 26 number line:
 

 ```code
  default="openai/gpt-4o",
 ```

 To

 ```code
 default="google_genai/gemini-1.5-flash",
 ```
