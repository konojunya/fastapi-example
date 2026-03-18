from fastapi import APIRouter, HTTPException

from app.core.config import settings

import psycopg

router = APIRouter()

@router.get("/health", status_code=200)
async def health_check():
    return {"status": "ok"}

@router.get("/health/db", status_code=200)
async def health_check_db():
    try:
        with psycopg.connect(settings.database_url) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1")
                row = cur.fetchone()
        return {
            "status": "ok",
            "database": "connected",
            "result": row,
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            default={
                "status": "error",
                "database": "unreachable",
                "message": str(e),
            },
        )