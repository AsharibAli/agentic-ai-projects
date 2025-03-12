# E-commerce Agent Project Structure

```mermaid
graph TD
    A[E-commerce Agent] --> B[Frontend]
    A --> C[Backend]
    A --> D[Data Storage]
    A --> E[Configuration]

    %% Frontend Components
    B --> B1[Streamlit UI]
    B1 --> B1a[ui/layout.py]
    B1 --> B1b[ui/product_display.py]
    B1 --> B1c[run/web.py]

    %% Backend Components
    C --> C1[FastAPI Server]
    C1 --> C1a[run/server.py]
    C1 --> C1b[routes/product_routes.py]
    
    C --> C2[Services]
    C2 --> C2a[services/llm_service.py]
    C2 --> C2b[services/api_service.py]
    
    C --> C3[Models]
    C3 --> C3a[models/database.py]
    
    %% Data Storage
    D --> D1[database/company_db.json]
    
    %% Configuration
    E --> E1[config.py]
    E --> E2[.env]
    E --> E3[pyproject.toml]
```

## Component Descriptions

1. **Frontend (Streamlit)**
   - User interface for product management
   - Product display and categorization

2. **Backend (FastAPI)**
   - RESTful API endpoints
   - Business logic processing
   - Integration with LLM services

3. **Services**
   - LLM Service: AI-powered product classification
   - API Service: External API communication

4. **Data Models**
   - Database models for product information

5. **Data Storage**
   - JSON-based product database

6. **Configuration**
   - Environment variables
   - Project dependencies 