import uuid
from datetime import datetime, timezone
from sqlalchemy import DateTime, ForeignKey, Integer, String, Text, UniqueConstraint
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(String, nullable=False)
    age: Mapped[int | None] = mapped_column(Integer, nullable=True)
    origin_country: Mapped[str | None] = mapped_column(String, nullable=True)
    profession: Mapped[str | None] = mapped_column(String, nullable=True)
    city: Mapped[str | None] = mapped_column(String, nullable=True)
    language_level: Mapped[str] = mapped_column(String, default="A1")
    entry_path: Mapped[str | None] = mapped_column(String, nullable=True)
    long_term_goal: Mapped[str | None] = mapped_column(String, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )


class WorldState(Base):
    __tablename__ = "world_states"

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id"), primary_key=True
    )
    current_location_node_id: Mapped[str | None] = mapped_column(
        ForeignKey("scenario_nodes.id"), nullable=True
    )
    visited_nodes: Mapped[list] = mapped_column(JSONB, default=list)
    flags: Mapped[dict] = mapped_column(JSONB, default=dict)
    clock: Mapped[dict] = mapped_column(JSONB, default=dict)


class NPCRelationship(Base):
    __tablename__ = "npc_relationships"
    __table_args__ = (UniqueConstraint("user_id", "npc_id", name="uq_user_npc"),)

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id"), nullable=False
    )
    npc_id: Mapped[str] = mapped_column(ForeignKey("npcs.id"), nullable=False)
    relationship_kind: Mapped[str] = mapped_column(String, nullable=False)
    trust: Mapped[int | None] = mapped_column(Integer, nullable=True)
    impression: Mapped[int | None] = mapped_column(Integer, nullable=True)
    interaction_count: Mapped[int] = mapped_column(Integer, default=0)
    memory_summary: Mapped[str | None] = mapped_column(Text, nullable=True)
    last_interaction_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )


class NotebookEntry(Base):
    __tablename__ = "notebook_entries"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id"), nullable=False
    )
    term_or_sentence: Mapped[str] = mapped_column(String, nullable=False)
    gloss: Mapped[str | None] = mapped_column(Text, nullable=True)
    source_scenario_id: Mapped[str | None] = mapped_column(
        ForeignKey("scenario_nodes.id"), nullable=True
    )
    encountered_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )
    struggle_count: Mapped[int] = mapped_column(Integer, default=0)
    status: Mapped[str] = mapped_column(String, default="new")
    origin: Mapped[str] = mapped_column(String, default="auto")
    personal_note: Mapped[str | None] = mapped_column(Text, nullable=True)


class NotebookLanguageItem(Base):
    __tablename__ = "notebook_language_items"

    notebook_entry_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("notebook_entries.id"), primary_key=True
    )
    language_item_id: Mapped[str] = mapped_column(
        ForeignKey("language_items.id"), primary_key=True
    )