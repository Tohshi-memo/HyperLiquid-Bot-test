# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T14:07:37.344548+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4950`

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

- `market_context_high->unknown_1h` score `359.0085` n `50` status `ready` deltaP `11.1737` edge `29.8478` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `292.369` n `50` status `ready` deltaP `11.128` edge `24.2899` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.3024` n `73` status `ready` deltaP `39.795` edge `1.0308` maxDD `-1.005`
- `news_risk_high->equity_24h` score `9.6254` n `73` status `ready` deltaP `33.7947` edge `0.6253` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `9.3787` n `50` status `ready` deltaP `33.0417` edge `0.7029` maxDD `-9.3299`
- `market_context_high->crypto_alt_24h` score `8.9771` n `50` status `ready` deltaP `16.5347` edge `0.8082` maxDD `-11.6271`
- `market_context_high->crypto_major_4h` score `6.5258` n `50` status `ready` deltaP `15.7134` edge `0.5094` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.5714` n `50` status `ready` deltaP `13.75` edge `0.4182` maxDD `-7.6465`
- `news_risk_high->crypto_alt_4h` score `4.3337` n `115` status `ready` deltaP `19.4022` edge `0.3662` maxDD `-6.4195`
- `market_context_high->fx_4h` score `2.9443` n `50` status `ready` deltaP `32.8415` edge `0.0399` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `2.8201` n `50` status `ready` deltaP `13.5509` edge `0.1897` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.8176` n `50` status `ready` deltaP `13.4551` edge `0.2114` maxDD `-3.6376`
- `news_risk_high->equity_4h` score `2.3911` n `115` status `ready` deltaP `22.2084` edge `0.1208` maxDD `-2.9013`
- `market_context_high->equity_24h` score `2.0831` n `50` status `ready` deltaP `10.0139` edge `0.3865` maxDD `-11.8957`
- `news_risk_high->crypto_major_24h` score `1.7609` n `73` status `ready` deltaP `7.2061` edge `0.4931` maxDD `-15.8971`
- `market_context_high->fx_1h` score `1.4999` n `50` status `ready` deltaP `20.9401` edge `0.0118` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.2385` n `73` status `ready` deltaP `11.9673` edge `0.2064` maxDD `-2.192`
- `market_context_high->index_24h` score `0.8323` n `50` status `ready` deltaP `14.4444` edge `0.0675` maxDD `-1.2338`
- `news_risk_high->crypto_major_4h` score `0.8061` n `115` status `ready` deltaP `12.0612` edge `0.2539` maxDD `-10.477`
- `news_risk_high->index_24h` score `0.733` n `73` status `ready` deltaP `14.3074` edge `0.0464` maxDD `-0.4916`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
