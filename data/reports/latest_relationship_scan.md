# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T03:37:24.187072+00:00`
- Price records: `672`
- Market context records: `6777`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11688`

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

- `market_context_high->unknown_24h` score `0.9747` n `176` status `ready` deltaP `-0.3315` edge `0.5024` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.0249` n `176` status `ready` deltaP `8.144` edge `0.1346` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.0505` n `176` status `ready` deltaP `7.5021` edge `0.0295` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.2071` n `176` status `ready` deltaP `4.8993` edge `0.0265` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.4038` n `176` status `ready` deltaP `-0.5648` edge `0.0005` maxDD `-0.5468`
- `market_context_high->commodity_1h` score `-0.5899` n `176` status `ready` deltaP `0.1463` edge `-0.0083` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.6481` n `176` status `ready` deltaP `-1.7658` edge `0.0001` maxDD `-0.7136`
- `market_context_high->metal_1h` score `-0.7323` n `176` status `ready` deltaP `-5.59` edge `-0.0041` maxDD `-1.2017`
- `market_context_high->index_4h` score `-1.2515` n `176` status `ready` deltaP `6.1391` edge `-0.0134` maxDD `-5.7046`
- `market_context_high->fx_4h` score `-1.2533` n `176` status `ready` deltaP `6.9291` edge `-0.0005` maxDD `-2.1765`
- `market_context_high->equity_1h` score `-1.2634` n `176` status `ready` deltaP `2.5075` edge `-0.0193` maxDD `-3.8827`
- `market_context_high->commodity_4h` score `-1.5208` n `176` status `ready` deltaP `-3.2982` edge `-0.024` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.6074` n `176` status `ready` deltaP `-6.2772` edge `-0.002` maxDD `-3.2083`
- `market_context_high->metal_4h` score `-2.6716` n `176` status `ready` deltaP `-6.6242` edge `-0.0123` maxDD `-5.2172`
- `market_context_high->crypto_major_4h` score `-2.745` n `176` status `ready` deltaP `3.0488` edge `-0.0408` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-2.9016` n `176` status `ready` deltaP `1.3026` edge `-0.0405` maxDD `-19.2145`
- `market_context_high->unknown_4h` score `-3.3745` n `176` status `ready` deltaP `-14.648` edge `0.053` maxDD `-10.2579`
- `market_context_high->equity_4h` score `-4.2213` n `176` status `ready` deltaP `2.7023` edge `-0.1323` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-4.3374` n `176` status `ready` deltaP `-8.2228` edge `-0.003` maxDD `-5.6237`
- `market_context_high->metal_24h` score `-8.8919` n `176` status `ready` deltaP `-16.2406` edge `-0.1832` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
