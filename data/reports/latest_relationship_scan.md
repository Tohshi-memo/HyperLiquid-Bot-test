# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T20:37:28.836446+00:00`
- Price records: `672`
- Market context records: `6745`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11724`

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

- `market_context_high->unknown_24h` score `1.2185` n `176` status `ready` deltaP `1.9255` edge `0.5186` maxDD `-12.3511`
- `market_context_high->crypto_major_1h` score `0.0703` n `176` status `ready` deltaP `8.2506` edge `0.04` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `0.0483` n `176` status `ready` deltaP `6.3963` edge `0.0378` maxDD `-3.7803`
- `market_context_high->commodity_24h` score `-0.1534` n `176` status `ready` deltaP `7.9704` edge `0.1209` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.3641` n `176` status `ready` deltaP `0.1837` edge `0.0006` maxDD `-0.5468`
- `market_context_high->index_1h` score `-0.5749` n `176` status `ready` deltaP `-0.5682` edge `0.0015` maxDD `-0.7136`
- `market_context_high->commodity_1h` score `-0.6289` n `176` status `ready` deltaP `-0.3028` edge `-0.0103` maxDD `-2.1314`
- `market_context_high->metal_1h` score `-0.6731` n `176` status `ready` deltaP `-4.8415` edge `-0.0015` maxDD `-1.2017`
- `market_context_high->equity_1h` score `-0.9997` n `176` status `ready` deltaP `4.1542` edge `-0.0083` maxDD `-3.8827`
- `market_context_high->index_4h` score `-1.2011` n `176` status `ready` deltaP `6.7489` edge `-0.011` maxDD `-5.7046`
- `market_context_high->fx_4h` score `-1.2011` n `176` status `ready` deltaP `7.8437` edge `0.0001` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.4571` n `176` status `ready` deltaP `-1.7738` edge `-0.026` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.7824` n `176` status `ready` deltaP `-7.4748` edge `-0.0086` maxDD `-3.2083`
- `market_context_high->crypto_major_4h` score `-2.2603` n `176` status `ready` deltaP `5.3354` edge `0.0061` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-2.4049` n `176` status `ready` deltaP `3.8941` edge `0.0059` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.6214` n `176` status `ready` deltaP `-6.3193` edge `-0.0079` maxDD `-5.2172`
- `market_context_high->unknown_4h` score `-3.8201` n `176` status `ready` deltaP `-16.7822` edge `0.0301` maxDD `-10.2579`
- `market_context_high->equity_4h` score `-3.9896` n `176` status `ready` deltaP `4.6841` edge `-0.1158` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-4.3206` n `176` status `ready` deltaP `-8.2228` edge `-0.0016` maxDD `-5.6237`
- `market_context_high->metal_24h` score `-8.0845` n `176` status `ready` deltaP `-11.3795` edge `-0.1121` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
