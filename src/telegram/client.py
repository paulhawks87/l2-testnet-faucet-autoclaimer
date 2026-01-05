from telethon import TelegramClient
from ..config import Settings


def create_client(settings: Settings) -> TelegramClient:
    # Uses local session file: <TELEGRAM_SESSION_NAME>.session
    return TelegramClient(
        settings.telegram_session_name,
        settings.telegram_api_id,
        settings.telegram_api_hash,
    )
