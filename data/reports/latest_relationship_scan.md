# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T17:37:37.727443+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6812`

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

- `market_context_high->unknown_1h` score `334.9874` n `50` status `ready` deltaP `7.8802` edge `27.868` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `284.7556` n `50` status `ready` deltaP `6.8598` edge `23.6839` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.3209` n `111` status `ready` deltaP `35.0038` edge `1.481` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `10.1292` n `50` status `ready` deltaP `32.8681` edge `0.7666` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.4926` n `50` status `ready` deltaP `20.1341` edge `0.5605` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.2246` n `50` status `ready` deltaP `16.9512` edge `0.4517` maxDD `-7.6792`
- `news_risk_high->crypto_major_24h` score `5.127` n `111` status `ready` deltaP `22.0393` edge `0.5957` maxDD `-15.8971`
- `market_context_high->crypto_alt_24h` score `5.0337` n `50` status `ready` deltaP `10.8056` edge `0.5184` maxDD `-11.6768`
- `market_context_high->equity_24h` score `3.9827` n `50` status `ready` deltaP `19.2153` edge `0.5687` maxDD `-11.8957`
- `news_risk_high->equity_4h` score `3.3661` n `124` status `ready` deltaP `26.7457` edge `0.1718` maxDD `-2.9013`
- `market_context_high->fx_4h` score `3.16` n `50` status `ready` deltaP `35.4329` edge `0.0406` maxDD `-0.0791`
- `news_risk_high->equity_24h` score `3.0884` n `111` status `ready` deltaP `22.3865` edge `0.4816` maxDD `-9.4579`
- `market_context_high->crypto_major_1h` score `3.0395` n `50` status `ready` deltaP `14.7485` edge `0.2` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.9254` n `50` status `ready` deltaP `13.4551` edge `0.2204` maxDD `-3.6387`
- `news_risk_high->index_24h` score `2.5484` n `111` status `ready` deltaP `24.9719` edge `0.0937` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.3043` n `111` status `ready` deltaP `27.1678` edge `0.2417` maxDD `-2.192`
- `market_context_high->fx_1h` score `1.5789` n `50` status `ready` deltaP `21.8383` edge `0.0124` maxDD `-0.113`
- `market_context_high->index_24h` score `0.8948` n `50` status `ready` deltaP `14.7917` edge `0.0732` maxDD `-1.2338`
- `market_context_high->fx_24h` score `0.5188` n `50` status `ready` deltaP `14.4306` edge `0.0721` maxDD `-1.8102`
- `news_risk_high->equity_1h` score `0.457` n `124` status `ready` deltaP `6.8911` edge `0.0458` maxDD `-0.9592`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
