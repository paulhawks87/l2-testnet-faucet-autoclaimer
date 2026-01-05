from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os


class Settings(BaseModel):
    # Telegram
    telegram_api_id: int = Field(..., alias="TELEGRAM_API_ID")
    telegram_api_hash: str = Field(..., alias="TELEGRAM_API_HASH")
    telegram_session_name: str = Field("claimer_session", alias="TELEGRAM_SESSION_NAME")
    telegram_sources: str = Field("", alias="TELEGRAM_SOURCES")

    # Blockchain
    l2_rpc_url: str = Field(..., alias="L2_RPC_URL")
    wallet_private_key: str = Field(..., alias="WALLET_PRIVATE_KEY")
    wallet_address: str = Field(..., alias="WALLET_ADDRESS")

    # Claim strategy
    claim_strategy: str = Field("api", alias="CLAIM_STRATEGY")

    # Faucet API
    faucet_api_url: str = Field("", alias="FAUCET_API_URL")
    faucet_api_key: str = Field("", alias="FAUCET_API_KEY")

    # Faucet contract
    faucet_contract_address: str = Field("", alias="FAUCET_CONTRACT_ADDRESS")
    faucet_contract_chain_id: int = Field(0, alias="FAUCET_CONTRACT_CHAIN_ID")

    # Operational
    claim_cooldown_seconds: int = Field(3600, alias="CLAIM_COOLDOWN_SECONDS")
    log_level: str = Field("INFO", alias="LOG_LEVEL")

    def sources_list(self) -> list[str]:
        raw = (self.telegram_sources or "").strip()
        if not raw:
            return []
        return [s.strip() for s in raw.split(",") if s.strip()]


def load_settings() -> Settings:
    load_dotenv()
    data = {k: os.getenv(k) for k in os.environ.keys()}
    # Pydantic will map aliases
    return Settings.model_validate(data)
