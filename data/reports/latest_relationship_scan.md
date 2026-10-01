# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T13:22:29.008550+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7070`

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

- `market_context_high->unknown_1h` score `335.3271` n `50` status `ready` deltaP `7.7305` edge `27.8973` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `281.176` n `50` status `ready` deltaP `6.8598` edge `23.3856` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `18.7746` n `114` status `ready` deltaP `32.0998` edge `1.3715` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `9.4729` n `50` status `ready` deltaP `30.7847` edge `0.7258` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.1771` n `50` status `ready` deltaP `19.2195` edge `0.5403` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.7369` n `50` status `ready` deltaP `15.5793` edge `0.4202` maxDD `-7.6792`
- `news_risk_high->crypto_major_24h` score `4.607` n `114` status `ready` deltaP `20.7145` edge `0.5612` maxDD `-15.8971`
- `news_risk_high->equity_4h` score `3.9855` n `123` status `ready` deltaP `28.4553` edge `0.1913` maxDD `-1.2436`
- `market_context_high->equity_24h` score `3.7708` n `50` status `ready` deltaP `17.4792` edge `0.5531` maxDD `-11.8957`
- `market_context_high->crypto_alt_24h` score `3.546` n `50` status `ready` deltaP `7.8542` edge `0.4141` maxDD `-11.6768`
- `news_risk_high->equity_24h` score `3.0563` n `114` status `ready` deltaP `21.409` edge `0.484` maxDD `-9.4579`
- `market_context_high->fx_4h` score `3.0264` n `50` status `ready` deltaP `34.2134` edge `0.0376` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `2.9963` n `50` status `ready` deltaP `14.8982` edge `0.1954` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.8019` n `50` status `ready` deltaP `13.006` edge `0.2131` maxDD `-3.6387`
- `news_risk_high->index_24h` score `2.3664` n `114` status `ready` deltaP `23.2365` edge `0.0901` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.2237` n `114` status `ready` deltaP `25.9777` edge `0.2393` maxDD `-2.192`
- `market_context_high->fx_1h` score `1.4699` n `50` status `ready` deltaP `20.6407` edge `0.0113` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.7908` n `127` status `ready` deltaP `8.1239` edge `0.0654` maxDD `-0.9592`
- `market_context_high->index_24h` score `0.7158` n `50` status `ready` deltaP `12.5347` edge `0.0653` maxDD `-1.2338`
- `market_context_high->fx_24h` score `0.5962` n `50` status `ready` deltaP `15.125` edge `0.0774` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
