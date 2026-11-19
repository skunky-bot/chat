# Skunky Chat

Responsive, accessible **rule-based development preview** of the Skunky conversational interface.

Open `index.html` locally or host as static content. Supported intents describe search, scan, collect, API and privacy. The preview is **not a generative AI agent**, does not call external models, and does not transmit or persist messages.

Future production integration must use authenticated Skunky API sessions, server-side model/tool access, permission-scoped actions, multilingual support and consent-aware logging. No browser API keys or admin secrets.

See `skunky-bot/www/docs/architecture/ADR-0001-skunky-platform.md`. Test with `python -m pytest -q tests/test_chat.py`.
