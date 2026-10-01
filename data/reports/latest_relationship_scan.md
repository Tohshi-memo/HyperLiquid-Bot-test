# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T16:07:38.150741+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6786`

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

- `market_context_high->unknown_1h` score `334.1618` n `50` status `ready` deltaP `7.8802` edge `27.7992` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `284.0416` n `50` status `ready` deltaP `6.8598` edge `23.6244` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.85` n `111` status `ready` deltaP `33.9621` edge `1.4487` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `9.9145` n `50` status `ready` deltaP `32.0` edge `0.7545` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.4916` n `50` status `ready` deltaP `20.2866` edge `0.5594` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.2116` n `50` status `ready` deltaP `17.1037` edge `0.4496` maxDD `-7.6792`
- `news_risk_high->crypto_major_24h` score `4.9123` n `111` status `ready` deltaP `21.1712` edge `0.5836` maxDD `-15.8971`
- `market_context_high->crypto_alt_24h` score `4.5628` n `50` status `ready` deltaP `9.7639` edge `0.4861` maxDD `-11.6768`
- `market_context_high->equity_24h` score `3.9991` n `50` status `ready` deltaP `19.2153` edge `0.5708` maxDD `-11.8957`
- `news_risk_high->equity_4h` score `3.4145` n `124` status `ready` deltaP `27.0506` edge `0.1738` maxDD `-2.9013`
- `market_context_high->fx_4h` score `3.12` n `50` status `ready` deltaP `35.128` edge `0.0393` maxDD `-0.0791`
- `news_risk_high->equity_24h` score `3.1048` n `111` status `ready` deltaP `22.3865` edge `0.4837` maxDD `-9.4579`
- `market_context_high->crypto_major_1h` score `3.1019` n `50` status `ready` deltaP `15.0479` edge `0.2032` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `3.0165` n `50` status `ready` deltaP `13.9042` edge `0.225` maxDD `-3.6387`
- `news_risk_high->index_24h` score `2.4713` n `111` status `ready` deltaP `24.2774` edge `0.0919` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.251` n `111` status `ready` deltaP `26.4734` edge `0.2395` maxDD `-2.192`
- `market_context_high->fx_1h` score `1.5394` n `50` status `ready` deltaP `21.3892` edge `0.0121` maxDD `-0.113`
- `market_context_high->index_24h` score `0.8447` n `50` status `ready` deltaP `14.0972` edge `0.0714` maxDD `-1.2338`
- `news_risk_high->equity_1h` score `0.5817` n `124` status `ready` deltaP `7.6396` edge `0.0512` maxDD `-0.9592`
- `market_context_high->fx_24h` score `0.5289` n `50` status `ready` deltaP `14.4306` edge `0.0734` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
