"""API routes for CVAssist."""

from fastapi import APIRouter, Depends, HTTPException
from typing import Dict, Any

from cvassist.application.services.api_service import ApiService
from cvassist.application.use_cases.test_connection import TestConnectionUseCase
from cvassist.infrastructure.container import create_application

router = APIRouter()


def get_test_connection_use_case() -> TestConnectionUseCase:
    """Dependency to get the test connection use case."""
    cli_commands = create_application()
    return cli_commands.test_connection_use_case


@router.get("/")
async def root() -> Dict[str, str]:
    """Root endpoint to confirm API is running."""
    return {"message": "CVAssist API is running!"}


@router.get("/test-connection")
async def test_connection(test_use_case: TestConnectionUseCase = Depends(get_test_connection_use_case)) -> Dict[str, Any]:
    """Endpoint to test connection to OpenRouter API."""
    try:
        result = test_use_case.execute()

        if result["success"]:
            return {
                "success": True,
                "message": "API is working correctly",
                "content": result.get("content", "")
            }
        else:
            raise HTTPException(
                status_code=result.get("status_code", 500),
                detail={
                    "success": False,
                    "message": "Connection failed",
                    "error_message": result.get("error_message", "Unknown error")
                }
            )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={
                "success": False,
                "message": "Internal server error",
                "error": str(e)
            }
        )