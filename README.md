# Immerse_Language_universe"
leben-in-deutschland/
├── docker-compose.yml
└── backend/
    ├── .env
    ├── requirements.txt
    ├── data/                       # Declarative seed data (JSON/YAML)
    │   └── scenarios/
    │       └── anmeldung_01.json   # Content lives here, NOT hardcoded in Python
    │
    ├── app/
    │   ├── __init__.py
    │   ├── main.py                 # App entrypoint & CLI commands (seed/init-db)
    │   ├── config.py               # Pydantic Settings
    │   ├── db.py                   # Async Engine & Session factory
    │   ├── models/                 # Folder instead of monolithic models.py
    │   │   ├── __init__.py         # Re-exports models for easy imports
    │   │   ├── base.py             # DeclarativeBase & Timestamp mixins
    │   │   ├── user.py             # User & World State models
    │   │   ├── scenario.py         # Nodes, Language Items, NPCs
    │   │   └── game.py             # Active turn/session state
    │   │
    │   ├── services/               # Core business logic / Orchestrator
    │   └── api/                    # FastAPI routes (added in Step 2)
    │
    └── tests/                      # Pytest tests (replaces manually run scripts)