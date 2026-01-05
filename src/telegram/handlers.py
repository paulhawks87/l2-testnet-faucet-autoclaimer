import re
from telethon import events
from ..storage.state import StateStore


CLAIM_URL_REGEX = re.compile(r"(https?://\S+)", re.IGNORECASE)
CLAIM_CODE_REGEX = re.compile(r"\bCODE[:\s]+([A-Z0-9_-]{6,})\b", re.IGNORECASE)


def extract_claim_artifacts(text: str) -> dict:
    """
    Generic extraction:
    - URLs
    - a claim code pattern like "CODE: ABC123XYZ"
    Adapt patterns to your Telegram sources.
    """
    urls = CLAIM_URL_REGEX.findall(text or "")
    m = CLAIM_CODE_REGEX.search(text or "")
    code = m.group(1) if m else None

    return {"urls": urls, "code": code}


def build_message_key(source: str, message_id: int) -> str:
    return f"{source}:{message_id}"


def register_handlers(client, logger, settings, claimer_callback, state: StateStore):
    @client.on(events.NewMessage)
    async def on_new_message(event):
        try:
            chat = await event.get_chat()
            source = getattr(chat, "username", None) or getattr(chat, "title", "unknown")
            text = event.raw_text or ""

            # Filter only configured sources (simple match)
            allowed = settings.sources_list()
            if allowed:
                normalized = f"@{source}" if not str(source).startswith("@") else str(source)
                if normalized not in allowed and str(source) not in allowed:
                    return

            artifacts = extract_claim_artifacts(text)
            key = build_message_key(str(source), event.message.id)

            logger.info(f"📩 Message from {source} | id={event.message.id}")
            if artifacts["urls"] or artifacts["code"]:
                logger.info(f"🔎 Detected artifacts: {artifacts}")

                if not state.can_claim(key, settings.claim_cooldown_seconds):
                    logger.info(f"⏳ Cooldown active for {key}, skipping.")
                    return

                # Trigger claim logic (sync wrapper or async safe)
                result = await claimer_callback(artifacts, source=str(source), message_id=event.message.id)

                state.mark_claimed(key, meta={"result": result, "artifacts": artifacts})
                logger.info(f"✅ State saved for {key}")
        except Exception as e:
            logger.exception(f"Handler error: {e}")
