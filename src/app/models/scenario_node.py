from sqlalchemy import String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class ScenarioNode(Base):
    """
    Content table — one row per scenario/situation, shared across all users.
    See architecture.md §2: this is "content," versioned like a CMS —
    contrast with WorldState/NPCRelationship (instance data, one row per
    user), which we'll build later.
    """
    __tablename__ = "scenario_nodes"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    category: Mapped[str] = mapped_column(String, nullable=False)
    location: Mapped[str] = mapped_column(String, nullable=False)

    # NOTE: these three fields are references to other tables' rows in
    # concept, but stored as plain JSONB lists of strings — Postgres does
    # NOT enforce that these IDs actually exist anywhere. That's the
    # contrast we'll set up against real ForeignKey next.
    applicable_profiles: Mapped[list] = mapped_column(JSONB, default=list)
    prerequisites: Mapped[list] = mapped_column(JSONB, default=list)
    next_nodes: Mapped[list] = mapped_column(JSONB, default=list)
    npc_refs: Mapped[list] = mapped_column(JSONB, default=list)

    difficulty_by_level: Mapped[dict] = mapped_column(JSONB, default=dict)
    learning_objectives: Mapped[dict] = mapped_column(JSONB, default=dict)
    possible_outcomes: Mapped[list] = mapped_column(JSONB, default=list)
    failure_states: Mapped[list] = mapped_column(JSONB, default=list)
    world_state_deltas: Mapped[dict] = mapped_column(JSONB, default=dict)
    relationship_deltas: Mapped[dict] = mapped_column(JSONB, default=dict)
    required_documents: Mapped[list] = mapped_column(JSONB, default=list)
    reentry_dialogue_rules: Mapped[dict] = mapped_column(JSONB, default=dict)
    recurring_dialogue_rules: Mapped[dict] = mapped_column(JSONB, default=dict)
    notebook_candidates: Mapped[list] = mapped_column(JSONB, default=list)