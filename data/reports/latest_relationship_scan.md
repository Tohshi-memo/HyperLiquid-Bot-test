# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T14:37:33.661196+00:00`
- Price records: `672`
- Market context records: `6826`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11748`

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

- `market_context_high->unknown_24h` score `0.9022` n `176` status `ready` deltaP `-1.5467` edge `0.5012` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.2606` n `176` status `ready` deltaP `10.4009` edge `0.1392` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.1815` n `204` status `ready` deltaP `6.1436` edge `0.0299` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.2992` n `204` status `ready` deltaP `3.8834` edge `0.0256` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.3548` n `204` status `ready` deltaP `0.408` edge `0.0003` maxDD `-0.5468`
- `market_context_high->index_1h` score `-0.8113` n `204` status `ready` deltaP `-3.1995` edge `-0.0042` maxDD `-1.2783`
- `market_context_high->metal_1h` score `-0.9268` n `204` status `ready` deltaP `-5.5565` edge `-0.0079` maxDD `-1.9098`
- `market_context_high->commodity_1h` score `-1.0923` n `204` status `ready` deltaP `-2.4774` edge `-0.0062` maxDD `-2.1314`
- `market_context_high->fx_4h` score `-1.2486` n `194` status `ready` deltaP `7.0342` edge `-0.0006` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.4569` n `194` status `ready` deltaP `-3.6004` edge `-0.0138` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.6693` n `204` status `ready` deltaP `-4.5761` edge `-0.0185` maxDD `-3.2083`
- `market_context_high->index_4h` score `-1.7476` n `194` status `ready` deltaP `1.6925` edge `-0.0276` maxDD `-7.2854`
- `market_context_high->equity_1h` score `-1.9329` n `204` status `ready` deltaP `0.4785` edge `-0.0313` maxDD `-6.304`
- `market_context_high->metal_4h` score `-2.6925` n `194` status `ready` deltaP `-3.3552` edge `-0.0245` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-2.9956` n `194` status `ready` deltaP `0.2043` edge `-0.0527` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.1577` n `194` status `ready` deltaP `0.1823` edge `-0.0477` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.3141` n `194` status `ready` deltaP `-11.2978` edge `0.0357` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.454` n `176` status `ready` deltaP `-9.7853` edge `-0.0023` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-5.3391` n `194` status `ready` deltaP `-0.7543` edge `-0.1756` maxDD `-33.3097`
- `market_context_high->metal_24h` score `-9.537` n `176` status `ready` deltaP `-21.1017` edge `-0.2335` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
