from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from typing import Optional

class Base(DeclarativeBase):
    pass

class TaskTable(Base):

    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    label: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    status: Mapped[bool] = mapped_column(Boolean)

    def make_dict(self):
        return {
            "label": self.label,
            "description": self.description,
            "status": self.status
        }
