# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T03:37:25.875730+00:00`
- Price records: `672`
- Market context records: `5623`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8743`

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

- `market_context_high->equity_24h` score `3.0391` n `174` status `ready` deltaP `15.0084` edge `0.6611` maxDD `-31.6316`
- `market_context_high->fx_24h` score `1.3352` n `174` status `ready` deltaP `22.1325` edge `0.0611` maxDD `-1.457`
- `market_context_high->crypto_major_4h` score `0.9316` n `235` status `ready` deltaP `11.6067` edge `0.2295` maxDD `-14.0065`
- `market_context_high->equity_4h` score `0.4421` n `235` status `ready` deltaP `7.0654` edge `0.1536` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `0.0426` n `235` status `ready` deltaP `6.1255` edge `0.1393` maxDD `-9.46`
- `market_context_high->fx_1h` score `-0.2797` n `237` status `ready` deltaP `1.5993` edge `0.0011` maxDD `-0.4764`
- `market_context_high->equity_1h` score `-0.3679` n `237` status `ready` deltaP `5.4657` edge `0.0336` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5161` n `237` status `ready` deltaP `0.1427` edge `0.0004` maxDD `-2.0682`
- `market_context_high->crypto_major_1h` score `-0.5498` n `237` status `ready` deltaP `4.7298` edge `0.0472` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `-0.6261` n `237` status `ready` deltaP `1.137` edge `0.0364` maxDD `-5.0257`
- `market_context_high->index_1h` score `-0.9298` n `237` status `ready` deltaP `0.5786` edge `0.0055` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-1.0704` n `237` status `ready` deltaP `-1.0277` edge `-0.0058` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.3388` n `235` status `ready` deltaP `0.7843` edge `0.0064` maxDD `-1.3281`
- `market_context_high->index_4h` score `-1.8661` n `235` status `ready` deltaP `-0.3399` edge `0.0095` maxDD `-3.0194`
- `market_context_high->index_24h` score `-2.3793` n `174` status `ready` deltaP `10.0874` edge `0.0264` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.8765` n `235` status `ready` deltaP `-11.4797` edge `-0.0539` maxDD `-11.7351`
- `market_context_high->crypto_major_24h` score `-2.903` n `174` status `ready` deltaP `7.2019` edge `0.1641` maxDD `-29.6555`
- `market_context_high->commodity_4h` score `-4.0565` n `235` status `ready` deltaP `-4.7535` edge `-0.0388` maxDD `-14.071`
- `market_context_high->metal_24h` score `-8.2693` n `174` status `ready` deltaP `-10.9315` edge `-0.2512` maxDD `-32.8874`
- `market_context_high->crypto_alt_24h` score `-12.6623` n `174` status `ready` deltaP `-3.0112` edge `-0.1654` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
