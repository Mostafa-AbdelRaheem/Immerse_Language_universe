from sqlalchemy import ForeignKey, Integer, String, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class ScenarioNode(Base):
    __tablename__ = "scenario_nodes"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    category: Mapped[str] = mapped_column(String, nullable=False)
    location: Mapped[str] = mapped_column(String, nullable=False)

    applicable_profiles: Mapped[list] = mapped_column(JSONB, default=list)
    prerequisites: Mapped[list] = mapped_column(JSONB, default=list)
    next_nodes: Mapped[list] = mapped_column(JSONB, default=list)
    difficulty_by_level: Mapped[dict] = mapped_column(JSONB, default=dict)
    npc_refs: Mapped[list] = mapped_column(JSONB, default=list)
    learning_objectives: Mapped[dict] = mapped_column(JSONB, default=dict)
    possible_outcomes: Mapped[list] = mapped_column(JSONB, default=list)
    failure_states: Mapped[list] = mapped_column(JSONB, default=dict)
    world_state_deltas: Mapped[dict] = mapped_column(JSONB, default=dict)
    relationship_deltas: Mapped[dict] = mapped_column(JSONB, default=dict)
    required_documents: Mapped[list] = mapped_column(JSONB, default=list)
    reentry_dialogue_rules: Mapped[dict] = mapped_column(JSONB, default=dict)
    recurring_dialogue_rules: Mapped[dict] = mapped_column(JSONB, default=dict)
    notebook_candidates: Mapped[list] = mapped_column(JSONB, default=list)


class NPC(Base):
    __tablename__ = "npcs"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    age: Mapped[int | None] = mapped_column(Integer, nullable=True)
    occupation: Mapped[str] = mapped_column(String, nullable=False)
    personality: Mapped[str] = mapped_column(Text, nullable=False)
    speaking_style: Mapped[str] = mapped_column(Text, nullable=False)
    formality: Mapped[str] = mapped_column(String, nullable=False)
    patience: Mapped[str] = mapped_column(String, nullable=False)
    knowledge_scope: Mapped[list] = mapped_column(JSONB, default=list)
    goals_this_scene: Mapped[list] = mapped_column(JSONB, default=list)
    relationship_kind: Mapped[str] = mapped_column(String, nullable=False)


class LanguageItem(Base):
    __tablename__ = "language_items"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    surface_form: Mapped[str] = mapped_column(String, nullable=False)
    category: Mapped[str] = mapped_column(String, nullable=False)


class ScenarioLanguage(Base):
    __tablename__ = "scenario_language"

    scenario_id: Mapped[str] = mapped_column(
        ForeignKey("scenario_nodes.id"), primary_key=True
    )
    language_item_id: Mapped[str] = mapped_column(
        ForeignKey("language_items.id"), primary_key=True
    )
    role: Mapped[str] = mapped_column(String, nullable=False)