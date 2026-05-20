# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T17:52:18.007091+00:00`
- Price records: `672`
- Market context records: `1343`
- Flow alert records: `5779`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8783`

## Conditions

- `news_risk_high`: News Risk is elevated.
- `macro_risk_high`: Macro Risk is elevated.
- `risk_on_high`: Risk-On score is elevated.
- `market_context_high`: Market Context is supportive.
- `polymarket_volume_spike`: Polymarket 24h volume z-score is elevated.
- `flow_alert_high`: Flow Alert score is elevated.
- `news_and_polymarket`: News Risk and Polymarket volume spike happen together.
- `risk_on_and_context`: Risk-On and Market Context are both supportive.
- `macro_and_flow`: Macro Risk and Flow Alert are elevated together.

## Top Patterns

- `market_context_high->crypto_major_24h` score `14.3422` n `128` status `ready` deltaP `35.1562` edge `1.074` maxDD `-8.0553`
- `market_context_high->metal_24h` score `12.9479` n `128` status `ready` deltaP `11.8056` edge `1.167` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.4548` n `128` status `ready` deltaP `28.3854` edge `0.8003` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.5109` n `128` status `ready` deltaP `25.5208` edge `0.3144` maxDD `-5.3574`
- `market_context_high->commodity_24h` score `2.6332` n `128` status `ready` deltaP `-9.375` edge `0.4301` maxDD `-6.8535`
- `market_context_high->equity_24h` score `2.2792` n `128` status `ready` deltaP `18.4028` edge `0.4022` maxDD `-14.2815`
- `market_context_high->equity_4h` score `2.2364` n `157` status `ready` deltaP `11.7388` edge `0.1786` maxDD `-3.6396`
- `market_context_high->fx_24h` score `1.3548` n `128` status `ready` deltaP `14.8438` edge `0.0604` maxDD `-0.3831`
- `market_context_high->unknown_24h` score `0.7719` n `128` status `ready` deltaP `-4.8611` edge `0.3697` maxDD `-10.1706`
- `market_context_high->equity_1h` score `0.1049` n `157` status `ready` deltaP `3.0683` edge `0.031` maxDD `-1.7505`
- `market_context_high->index_1h` score `0.0212` n `157` status `ready` deltaP `5.0145` edge `0.0147` maxDD `-1.6329`
- `market_context_high->metal_4h` score `0.0185` n `157` status `ready` deltaP `13.2205` edge `0.0565` maxDD `-6.4478`
- `market_context_high->index_4h` score `-0.0032` n `157` status `ready` deltaP `4.8742` edge `0.076` maxDD `-3.7119`
- `market_context_high->metal_1h` score `-0.0811` n `157` status `ready` deltaP `9.0917` edge `0.0016` maxDD `-2.8509`
- `market_context_high->fx_1h` score `-0.4607` n `157` status `ready` deltaP `1.5571` edge `-0.0032` maxDD `-0.3124`
- `market_context_high->commodity_1h` score `-0.7518` n `157` status `ready` deltaP `-1.1051` edge `0.0062` maxDD `-2.252`
- `market_context_high->crypto_alt_1h` score `-0.9023` n `157` status `ready` deltaP `-0.6503` edge `0.0162` maxDD `-3.6309`
- `market_context_high->crypto_major_1h` score `-1.0987` n `157` status `ready` deltaP `-3.0131` edge `-0.0187` maxDD `-5.8323`
- `market_context_high->unknown_4h` score `-1.3727` n `157` status `ready` deltaP `1.4292` edge `0.0416` maxDD `-11.1695`
- `market_context_high->crypto_alt_4h` score `-1.5385` n `157` status `ready` deltaP `8.4676` edge `0.1473` maxDD `-19.5565`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
