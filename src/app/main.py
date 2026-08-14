import asyncio
import json
from pathlib import Path

from app.db import AsyncSessionLocal, engine
from app.models import Base, LanguageItem, NPC, ScenarioLanguage, ScenarioNode


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("✅ Schema created (or already existed).")


async def seed_scenario(json_path: str = "data/scenarios/anmeldung_01.json"):
    path = Path(json_path)
    if not path.exists():
        print(f"❌ File not found: {json_path}")
        return

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    async with AsyncSessionLocal() as session:
        existing = await session.get(ScenarioNode, data["node"]["id"])
        if existing:
            print(f"⚠️ {data['node']['id']} already seeded. Skipping.")
            return

        session.add(NPC(**data["npc"]))
        session.add(ScenarioNode(**data["node"]))

        obj = data["node"]["learning_objectives"]
        categories = (
            ("vocab", obj["vocab"]),
            ("grammar", obj["grammar"]),
            ("expression", obj["expressions"]),
        )

        for category, terms in categories:
            for term in terms:
                existing_item = await session.get(LanguageItem, term)
                if not existing_item:
                    session.add(
                        LanguageItem(id=term, surface_form=term, category=category)
                    )
                session.add(
                    ScenarioLanguage(
                        scenario_id=data["node"]["id"],
                        language_item_id=term,
                        role="introduces",
                    )
                )

        await session.commit()
        print(f"✅ Seeded scenario {data['node']['id']} from {json_path}")


if __name__ == "__main__":
    import sys

    cmd = sys.argv[1] if len(sys.argv) > 1 else "init"
    if cmd == "init-db":
        asyncio.run(init_db())
    elif cmd == "seed":
        asyncio.run(seed_scenario())
    else:
        print("Usage: python -m app.main [init-db|seed]")