# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T11:37:28.792099+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7054`

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

- `market_context_high->unknown_1h` score `324.5259` n `50` status `ready` deltaP `7.5808` edge `26.9982` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `280.9636` n `50` status `ready` deltaP `6.8598` edge `23.3679` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.7512` n `120` status `ready` deltaP `30.9722` edge `1.4604` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `8.8101` n `50` status `ready` deltaP `30.0903` edge `0.6752` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `6.9487` n `50` status `ready` deltaP `18.9146` edge `0.5233` maxDD `-3.294`
- `news_risk_high->equity_24h` score `5.5304` n `120` status `ready` deltaP `22.118` edge `0.5483` maxDD `-9.4579`
- `news_risk_high->equity_4h` score `4.5125` n `122` status `ready` deltaP `29.6432` edge `0.2273` maxDD `-1.2436`
- `market_context_high->crypto_alt_4h` score `4.1799` n `50` status `ready` deltaP `14.5122` edge `0.3809` maxDD `-7.6792`
- `news_risk_high->crypto_major_24h` score `3.795` n `120` status `ready` deltaP `21.4236` edge `0.6591` maxDD `-15.8971`
- `market_context_high->equity_24h` score `3.5701` n `50` status `ready` deltaP `16.7847` edge `0.532` maxDD `-11.8957`
- `market_context_high->fx_4h` score `2.9606` n `50` status `ready` deltaP `33.4512` edge `0.0372` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `2.8535` n `50` status `ready` deltaP `14.4491` edge `0.1865` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.5884` n `50` status `ready` deltaP `12.4072` edge `0.1993` maxDD `-3.6387`
- `news_risk_high->crypto_alt_4h` score `2.5801` n `122` status `ready` deltaP `11.7253` edge `0.3375` maxDD `-10.7193`
- `news_risk_high->index_24h` score `2.5252` n `120` status `ready` deltaP `24.2014` edge `0.0969` maxDD `-0.4916`
- `market_context_high->crypto_alt_24h` score `2.448` n `50` status `ready` deltaP `6.6389` edge `0.3307` maxDD `-11.6768`
- `news_risk_high->metal_24h` score `2.2869` n `120` status `ready` deltaP `26.9097` edge `0.2412` maxDD `-2.192`
- `market_context_high->fx_1h` score `1.4448` n `50` status `ready` deltaP `20.3413` edge `0.0112` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.8772` n `133` status `ready` deltaP `8.3641` edge `0.071` maxDD `-0.9592`
- `market_context_high->index_24h` score `0.701` n `50` status `ready` deltaP `12.5347` edge `0.0634` maxDD `-1.2338`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
