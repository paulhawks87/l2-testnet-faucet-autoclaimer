# L2 Testnet Faucet Auto-Claimer (Telegram + Web3 Template)

> ⚡ A professional-grade automation **template** for monitoring Telegram messages and triggering **testnet token claims** on Ethereum Layer 2 networks.  
> ✅ Modular structure • ✅ Clean configs • ✅ Logging • ✅ State persistence • ✅ Extensible claim strategies

---

## ✨ Overview

This repository is a **template project** that demonstrates how you can build a robust automation pipeline:

- 📡 Connect to Telegram (via **Telethon**)
- 👂 Listen to channels/bots for claim signals (links, codes, commands)
- 🧠 Decide whether and how to claim (rules, cooldowns, allowlists)
- 🔗 Interact with an L2 network:
  - (A) Call a faucet HTTP API (placeholder)
  - (B) Send a contract transaction to a faucet distributor (placeholder)
- 🗂️ Persist state (avoid duplicates, track cooldowns)
- ⏱️ Run scheduled jobs continuously

> ⚠️ This is **NOT** a CAPTCHA bypass tool.  
> Respect faucet terms, rate limits and legal boundaries.

---

## ✅ Requirements

- Python 3.10+
- A Telegram API App (`api_id` + `api_hash`)
- A wallet private key for testnet use (never mainnet funds)
- L2 RPC endpoint (testnet)
- (Optional) Faucet API URL / Contract Address

---

## 🛠️ Setup

## 1) Install dependencies

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

pip install -r requirements.txt
```
---

### 2) Configure environment

Copy `.env.example` → `.env` and fill your values:

```env
TELEGRAM_API_ID=123456
TELEGRAM_API_HASH=your_hash_here
TELEGRAM_SESSION_NAME=claimer_session

# Telegram sources (comma separated)
TELEGRAM_SOURCES=@SomeChannel,@SomeBot

# L2 chain + wallet
L2_RPC_URL=https://your-l2-testnet-rpc.example
WALLET_PRIVATE_KEY=0xyour_testnet_private_key
WALLET_ADDRESS=0xYourWalletAddress

# Claim strategy
CLAIM_STRATEGY=api   # api | contract

# API-based faucet claim
FAUCET_API_URL=https://your-faucet.example/claim
FAUCET_API_KEY=optional_key_here

# Contract-based faucet claim
FAUCET_CONTRACT_ADDRESS=0xYourContract
FAUCET_CONTRACT_CHAIN_ID=11155420
```
---

## 🔐 Security Notes

- Never commit `.env`
- Never commit your Telethon session files (`*.session`)
- Use a dedicated test wallet
- Consider rate limiting and safe backoff for automation

---

## 🧠 How it works (High-level)

1. Telegram client connects and subscribes to configured sources  
2. Handlers parse messages and extract claim artifacts (links/codes/keywords)  
3. A claim decision engine checks cooldowns & duplicates  
4. Claim is executed using one of two strategies  
5. Result is logged + persisted  

---

## 🧯 Disclaimer

This project is provided **as-is** for educational purposes.  
You are responsible for complying with Telegram ToS, faucet rules, and applicable laws.

---

## 📌 Roadmap Ideas (optional)

- ✅ Add SQLite persistence
- ✅ Add Prometheus metrics
- ✅ Docker container + systemd service
- ✅ Telegram bot interface for manual override
- ✅ Multi-wallet rotation (with compliance controls)

---

## 💬 Notes

If you want, you can adapt this template to:

- any L2 testnet
- any faucet mechanism (API / contract / bot-based)
- any detection patterns in Telegram
