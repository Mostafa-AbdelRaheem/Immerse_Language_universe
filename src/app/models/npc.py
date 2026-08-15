from sqlalchemy import Integer, String, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class NPC(Base):
    """
    Content table — one row per NPC definition, shared across all users.
    (Per-user relationship state to an NPC lives in NPCRelationship later,
    not here — that's the content/instance split from architecture.md §2.)
    """
    __tablename__ = "npcs"

    # primary_key=True: this is the unique row identifier. We're using the
    # NPC's natural string id (e.g. "buergeramt_clerk_01") from the node
    # specs directly, rather than generating a separate UUID — this content
    # is hand-authored with meaningful IDs already, so a surrogate key would
    # just be redundant.
    id: Mapped[str] = mapped_column(String, primary_key=True)

    name: Mapped[str] = mapped_column(String, nullable=False)

    # int | None because some NPCs might not specify an age in future
    # content — nullable=True is the DB-side statement of the same thing.
    age: Mapped[int | None] = mapped_column(Integer, nullable=True)

    occupation: Mapped[str] = mapped_column(String, nullable=False)

    # Text vs String: no hard limit either way in Postgres, but Text signals
    # "this can be a paragraph" (personality, speaking_style) vs String
    # signaling "this is a short label" (name, formality) — a readability
    # convention, not a functional difference in Postgres specifically.
    personality: Mapped[str] = mapped_column(Text, nullable=False)
    speaking_style: Mapped[str] = mapped_column(Text, nullable=False)

    formality: Mapped[str] = mapped_column(String, nullable=False)
    patience: Mapped[str] = mapped_column(String, nullable=False)

    # JSONB: Postgres's binary JSON column type. We use it here because
    # knowledge_scope and goals_this_scene are variable-length lists that
    # we never need to query/filter by individual element — they're read
    # as a whole and handed to the Narrative Agent's prompt. If we later
    # needed "find all NPCs with X in knowledge_scope" as a real query,
    # a proper join table would be worth it; not needed yet.
    knowledge_scope: Mapped[list] = mapped_column(JSONB, default=list)
    goals_this_scene: Mapped[list] = mapped_column(JSONB, default=list)

    # "personal" | "procedural" — plain string, not a Postgres ENUM type.
    # Only two values exist and nothing validates against a fixed set yet;
    # an ENUM would need a migration to extend if a third kind ever shows
    # up. Revisit if that becomes a real constraint we want enforced.
    relationship_kind: Mapped[str] = mapped_column(String, nullable=False)