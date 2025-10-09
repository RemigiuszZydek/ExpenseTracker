# ExpenseTracker

Simple FastAPI app to track my personal expenses using SQLite database.

## Technologies
- Python 3.13
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic

## Installation

1. Clone the repository:
   ```bash
   git clone <repo_url>
   cd ExpenseTracker
  ```
2. Create a virtual environment:
  ```bash
  python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

3. Install dependencies:
  ```bash
  pip install -r requirements.txt
```

4. Run the FastAPI server:
   ```bash
     uvicorn backend.main:app --reload
   ```
