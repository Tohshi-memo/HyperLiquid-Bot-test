# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T21:37:34.122804+00:00`
- Price records: `672`
- Market context records: `6857`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11809`

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

- `market_context_high->unknown_24h` score `1.1463` n `176` status `ready` deltaP `-1.5467` edge `0.5325` maxDD `-12.3511`
- `market_context_high->fx_1h` score `-0.2608` n `223` status `ready` deltaP `2.0193` edge `0.0016` maxDD `-0.5468`
- `market_context_high->commodity_24h` score `-0.5887` n `176` status `ready` deltaP `6.2342` edge `0.0962` maxDD `-5.2791`
- `market_context_high->crypto_alt_1h` score `-0.6108` n `223` status `ready` deltaP `1.7125` edge `0.0141` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.6501` n `223` status `ready` deltaP `3.5062` edge `0.0126` maxDD `-4.2122`
- `market_context_high->commodity_1h` score `-0.6844` n `223` status `ready` deltaP `-2.0213` edge `-0.0058` maxDD `-2.1443`
- `market_context_high->index_1h` score `-0.8732` n `223` status `ready` deltaP `-2.6154` edge `-0.0034` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.937` n `223` status `ready` deltaP `-5.3026` edge `-0.008` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-1.0133` n `218` status `ready` deltaP `10.5392` edge `0.0062` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.4323` n `218` status `ready` deltaP `-3.5019` edge `-0.0113` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.6538` n `223` status `ready` deltaP `-2.9115` edge `-0.0283` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.9706` n `223` status `ready` deltaP `-0.2276` edge `-0.0331` maxDD `-13.1084`
- `market_context_high->index_4h` score `-2.0641` n `218` status `ready` deltaP `2.7662` edge `-0.0251` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.4581` n `218` status `ready` deltaP `-0.6321` edge `-0.0126` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-3.0892` n `218` status `ready` deltaP `-1.2041` edge `-0.0553` maxDD `-16.9508`
- `market_context_high->unknown_4h` score `-3.1422` n `218` status `ready` deltaP `-9.0443` edge `0.035` maxDD `-10.2579`
- `market_context_high->crypto_alt_4h` score `-3.1921` n `218` status `ready` deltaP `-0.7496` edge `-0.0459` maxDD `-20.6678`
- `market_context_high->fx_24h` score `-4.5128` n `176` status `ready` deltaP `-9.7853` edge `-0.0072` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.5999` n `218` status `ready` deltaP `0.007` edge `-0.1799` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-9.0476` n `176` status `ready` deltaP `-18.8447` edge `-0.1858` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
