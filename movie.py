from base import Base
from datetime import date
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, String, Date

class Movie(Base):
    __tablename__ = "movies"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    release_year: Mapped[date] = mapped_column(Date, nullable=False)
    duration_in_min: Mapped[int] = mapped_column(Integer, nullable=False)