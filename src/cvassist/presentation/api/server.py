"""Main API server module for CVAssist."""

from fastapi import FastAPI
from cvassist.presentation.api.routes import router


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(title="CVAssist API", version="1.0.0")
    
    # Include API routes
    app.include_router(router, prefix="/api/v1")
    
    return app


app = create_app()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)