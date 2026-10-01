# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T14:37:34.690829+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7110`

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

- `market_context_high->unknown_1h` score `333.6915` n `50` status `ready` deltaP `7.7305` edge `27.761` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `283.0048` n `50` status `ready` deltaP `6.8598` edge `23.538` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.2544` n `114` status `ready` deltaP `32.9678` edge `1.4057` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `9.679` n `50` status `ready` deltaP `31.3056` edge `0.7395` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.2421` n `50` status `ready` deltaP `19.372` edge `0.5447` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.9224` n `50` status `ready` deltaP `16.189` edge `0.4316` maxDD `-7.6792`
- `news_risk_high->crypto_major_24h` score `4.8131` n `114` status `ready` deltaP `21.2354` edge `0.5749` maxDD `-15.8971`
- `market_context_high->crypto_alt_24h` score `4.0259` n `50` status `ready` deltaP `8.7222` edge `0.4483` maxDD `-11.6768`
- `market_context_high->equity_24h` score `3.8654` n `50` status `ready` deltaP `18.1736` edge `0.5606` maxDD `-11.8957`
- `news_risk_high->equity_4h` score `3.3905` n `127` status `ready` deltaP `26.6313` edge `0.1746` maxDD `-2.9013`
- `news_risk_high->equity_24h` score `3.1509` n `114` status `ready` deltaP `22.1034` edge `0.4915` maxDD `-9.4579`
- `market_context_high->fx_4h` score `3.0934` n `50` status `ready` deltaP `34.9756` edge `0.0381` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `2.9723` n `50` status `ready` deltaP `14.5988` edge `0.1954` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.8822` n `50` status `ready` deltaP `13.4551` edge `0.2168` maxDD `-3.6387`
- `news_risk_high->index_24h` score `2.4321` n `114` status `ready` deltaP `23.7574` edge `0.0921` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.264` n `114` status `ready` deltaP `26.4985` edge `0.241` maxDD `-2.192`
- `market_context_high->fx_1h` score `1.5094` n `50` status `ready` deltaP `21.0898` edge `0.0116` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.828` n `127` status `ready` deltaP `8.2736` edge `0.0675` maxDD `-0.9592`
- `market_context_high->index_24h` score `0.7585` n `50` status `ready` deltaP `13.0556` edge `0.0673` maxDD `-1.2338`
- `market_context_high->fx_24h` score `0.5422` n `50` status `ready` deltaP `14.4306` edge `0.0751` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
