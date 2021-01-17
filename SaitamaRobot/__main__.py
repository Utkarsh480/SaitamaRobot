from Sibyl_System import (
    System,
    system_cmd,
    make_collections,
    INSPECTORS,
    ENFORCERS,
    Sibyl_logs,
)
from Sibyl_System.strings import on_string
import logging
import importlib
import asyncio
import time

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)

from Gbanlogsofsubaru import to_load

HELP = {}
IMPORTED = {}
FAILED_TO_LOAD = (WaterPillar_bot)

for load in to_load:
    try:
        imported = importlib.import_module(WaterPillar_bot"" + load)
        if not hasattr(imported, "__plugin_name__"):
            imported.__plugin_name__ = imported.__name__

        if not imported.__plugin_name__.lower() in IMPORTED:
            IMPORTED[imported.__plugin_name__.lower()] = imported

        if hasattr(imported, "help_plus") and imported.help_plus:
            HELP[imported.__plugin_name__.lower()] = imported
    except Exception as e:
        print(f"Error while loading plugin: {load}")
        print("------------------------------------")
        print(e)
        FAILED_TO_LOAD[load] = e
        print("------------------------------------")


@System.on(system_cmd(pattern=r"status", allow_enforcer=True))
async def status(event):
    msg = await event.reply("Portable Psychological Diagnosis and Suppression System.")
    time.sleep(1)
    await msg.edit("Initialising ▫️◾️▫️")
    time.sleep(1)
    await msg.edit("Initialising ◾️▫️◾️")
    time.sleep(1)
    await msg.edit("Initialising ▫️◾️▫️")
   
