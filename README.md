# L2 Testnet Faucet Auto-Claimer (Telegram + Web3 Template)

> ⚡ A professional-grade **automation template** for monitoring Telegram messages and triggering **testnet token claims** on Ethereum Layer 2 networks.
>
> ✅ Designed to look like a real production tool  
> ✅ Modular architecture (Telegram / Blockchain / Storage / Scheduler)  
> ✅ Easy to extend with your own faucet endpoints, smart contracts, and rules  

---

## ✨ What is this?

This repository is a **template project** that demonstrates how you can build a robust automation pipeline:

- 📡 Connect to Telegram (via Telethon)
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

## 🧩 Key Features

- 🤖 Telegram integration using **Telethon**
- 🔐 Secure config via `.env`
- 🧾 Structured logging (console + file)
- 🗃️ Local persistence using JSON storage (extendable to SQLite/Redis)
- 🔄 Scheduler loop for periodic polling and health checks
- 🧰 Extensible claim strategies:
  - API-based faucet claim (HTTP)
  - On-chain claim via Web3 transaction

---

## 🗂️ Project Structure

```text
src/
  main.py
  config.py
  logger.py

  telegram/
    client.py
    handlers.py

  blockchain/
    rpc.py
    faucet_api.py
    faucet_contract.py
    tx_builder.py

  storage/
    state.py

  scheduler/
    jobs.py
