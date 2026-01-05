import asyncio
from .config import load_settings
from .logger import setup_logger
from .storage.state import StateStore
from .telegram.client import create_client
from .telegram.handlers import register_handlers
from .blockchain.rpc import get_web3
from .blockchain.faucet_api import FaucetApiClient
from .blockchain.faucet_contract import FaucetContractClaimer
from .scheduler.jobs import heartbeat, periodic_healthcheck


async def run():
    settings = load_settings()
    logger = setup_logger(settings.log_level)
    state = StateStore()

    logger.info("🚀 Starting L2 Testnet Faucet Auto-Claimer (Template)")
    logger.info(f"⚙️ Strategy: {settings.claim_strategy}")

    # Blockchain clients
    w3 = get_web3(settings.l2_rpc_url)
    faucet_api = FaucetApiClient(settings.faucet_api_url, settings.faucet_api_key)
    faucet_contract = None
    if settings.faucet_contract_address:
        faucet_contract = FaucetContractClaimer(w3, settings.faucet_contract_address)

    # Telegram client
    client = create_client(settings)

    async def claimer_callback(artifacts: dict, source: str, message_id: int):
        """
        Core claim logic (template).
        - Strategy 'api': call faucet API
        - Strategy 'contract': send contract tx
        """
        try:
            if settings.claim_strategy.lower() == "api":
                if not settings.faucet_api_url:
                    return {"ok": False, "reason": "FAUCET_API_URL not set"}

                # Example: use code if present
                result = faucet_api.claim(settings.wallet_address, claim_code=artifacts.get("code"))
                return {"ok": True, "mode": "api", "result": result}

            if settings.claim_strategy.lower() == "contract":
                if not faucet_contract:
                    return {"ok": False, "reason": "FAUCET_CONTRACT_ADDRESS not set"}

                tx_hash = faucet_contract.claim(
                    from_address=settings.wallet_address,
                    private_key=settings.wallet_private_key,
                    recipient=settings.wallet_address,
                )
                return {"ok": True, "mode": "contract", "tx_hash": tx_hash}

            return {"ok": False, "reason": f"Unknown CLAIM_STRATEGY: {settings.claim_strategy}"}
        except Exception as e:
            return {"ok": False, "error": str(e), "source": source, "message_id": message_id}

    register_handlers(client, logger, settings, claimer_callback, state)

    # Start background jobs
    bg1 = asyncio.create_task(heartbeat(logger))
    bg2 = asyncio.create_task(periodic_healthcheck(logger))

    # Run Telegram client
    async with client:
        logger.info("📡 Telegram client connected. Listening for messages...")
        await client.run_until_disconnected()

    bg1.cancel()
    bg2.cancel()


if __name__ == "__main__":
    asyncio.run(run())
