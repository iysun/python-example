"""
RESTful API 后端（FastAPI + SQLite）
练习点：FastAPI、Pydantic 数据校验、SQLite、依赖注入、HTTP 状态码
运行：uvicorn main:app --reload
文档：访问 http://127.0.0.1:8000/docs 查看自动生成的 Swagger UI
"""
import sqlite3
from pathlib import Path

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware

from models.schemas import TaskCreate, TaskUpdate, TaskResponse
from routers import tasks

app = FastAPI(title="任务管理 API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])


@app.get("/")
def root():
    return {"message": "任务管理 API 运行中", "docs": "/docs"}
