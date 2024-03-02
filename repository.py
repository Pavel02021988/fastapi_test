from sqlalchemy import select
from database import Task, new_session
from schemas import STask, STaskAdd


class TaskRepository:
    @classmethod
    async def add_task(cls, task: STaskAdd) -> int:
        async with new_session() as session:
            data = task.model_dump()
            new_task = Task(**data)

            session.add(new_task)
            await session.flush()
            await session.commit()

            return new_task.id

    @classmethod
    async def get_task(cls) -> list[STask]:
        async with new_session() as session:
            query = select(Task)
            result = await session.execute(query)
            task_models = result.scalars().all()
            tasks = [STask.model_validate(task_model) for task_model in task_models]

            return tasks
