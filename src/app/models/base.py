# from datetime import datetime, timezone
# from sqlalchemy import DateTime
# from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


# class Base(DeclarativeBase):
#     pass


# class TimestampMixin:
#     created_at: Mapped[datetime] = mapped_column(
#         DateTime(timezone=True),
#         default=lambda: datetime.now(timezone.utc),
#         nullable=False,
#     )
#     updated_at: Mapped[datetime] = mapped_column(
#         DateTime(timezone=True),
#         default=lambda: datetime.now(timezone.utc),
#         onupdate=lambda: datetime.now(timezone.utc),
#         nullable=False,
#     )
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Every model class inherits from this. SQLAlchemy uses it to collect
    all table definitions in one registry (Base.metadata), which is what
    lets us later do Base.metadata.create_all() to build every table at once.
    """
    pass