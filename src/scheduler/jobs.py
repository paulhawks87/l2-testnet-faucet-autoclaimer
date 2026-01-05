import asyncio
import time


async def heartbeat(logger, interval_seconds: int = 60):
    while True:
        logger.info("💓 Heartbeat: service running")
        await asyncio.sleep(interval_seconds)


async def periodic_healthcheck(logger, interval_seconds: int = 300):
    while True:
        # Placeholder: you can ping RPC, check balances, etc.
        logger.info("🩺 Healthcheck: OK (placeholder)")
        await asyncio.sleep(interval_seconds)
