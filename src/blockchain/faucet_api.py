import requests


class FaucetApiClient:
    """
    Generic faucet API client (placeholder).
    Replace the payload/headers/endpoint logic with your faucet specification.
    """

    def __init__(self, base_url: str, api_key: str = ""):
        self.base_url = base_url
        self.api_key = api_key

    def claim(self, wallet_address: str, claim_code: str | None = None) -> dict:
        headers = {}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"

        payload = {
            "address": wallet_address,
            "code": claim_code,  # optional
        }

        # Placeholder request format; adapt to your faucet's requirements
        resp = requests.post(self.base_url, json=payload, headers=headers, timeout=30)
        return {
            "status_code": resp.status_code,
            "text": resp.text[:5000],
        }
