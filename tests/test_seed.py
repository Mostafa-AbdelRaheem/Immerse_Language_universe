import pytest
from sqlalchemy import func, select

from app.db import AsyncSessionLocal
from app.models import LanguageItem, NPC, ScenarioLanguage, ScenarioNode


@pytest.mark.asyncio
async def test_anmeldung_seed_data():
    async with AsyncSessionLocal() as session:
        node = await session.get(ScenarioNode, "anmeldung_01")
        npc = await session.get(NPC, "buergeramt_clerk_01")

        assert node is not None
        assert node.title == "Anmeldung (Wohnsitzanmeldung)"

        assert npc is not None
        assert npc.name == "Herr Krüger"

        item_count = await session.scalar(
            select(func.count()).select_from(LanguageItem)
        )
        assert item_count > 0

        link_count = await session.scalar(
            select(func.count())
            .select_from(ScenarioLanguage)
            .where(ScenarioLanguage.scenario_id == "anmeldung_01")
        )
        assert link_count > 0