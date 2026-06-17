"""
任务资源的 CRUD 路由
"""
from typing import List, Optional

from fastapi import APIRouter, HTTPException, Query

from models.schemas import TaskCreate, TaskUpdate, TaskResponse

router = APIRouter()


@router.get("/", response_model=List[TaskResponse])
def list_tasks(
    completed: Optional[bool] = Query(None, description="过滤已完成/未完成"),
    priority: Optional[str] = Query(None, description="按优先级过滤"),
):
    """获取所有任务（支持过滤）。"""
    # TODO: 查询数据库，根据参数过滤，返回列表
    raise NotImplementedError


@router.post("/", response_model=TaskResponse, status_code=201)
def create_task(task: TaskCreate):
    """创建新任务。"""
    # TODO: 插入数据库，返回带 id 和 created_at 的完整对象
    raise NotImplementedError


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    """按 ID 获取单个任务。"""
    # TODO: 查询数据库，不存在则 raise HTTPException(status_code=404)
    raise NotImplementedError


@router.patch("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, update: TaskUpdate):
    """部分更新任务（只更新传入的字段）。"""
    # TODO: 找到任务，只更新 update 中非 None 的字段，保存并返回
    raise NotImplementedError


@router.delete("/{task_id}", status_code=204)
def delete_task(task_id: int):
    """删除任务。"""
    # TODO: 删除记录，不存在则 404
    raise NotImplementedError
