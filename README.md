# CVAssist

A CV assistance tool that integrates with OpenRouter API to provide AI-powered assistance for CV creation and management.

## How to Run

1. Install dependencies:
```bash
poetry install
```

2. Set up environment variables:
```bash
cp .env.example .env
# Add your OpenRouter API key to .env
```

3. Run the CLI application:
```bash
poetry run python src/cvassist/main.py
```

4. Or run the FastAPI service:
```bash
poetry run uvicorn cvassist.presentation.api.server:app --reload
```