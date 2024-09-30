import uuid

from sqlalchemy import String, UUID, Integer, ARRAY
from sqlalchemy.orm import mapped_column, Mapped

from core.base_model import Base


class Cat(Base):
    __tablename__ = "cats"  # noqa

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    color: Mapped[str] = mapped_column(String)
    age: Mapped[int] = mapped_column(Integer)
    breed: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
