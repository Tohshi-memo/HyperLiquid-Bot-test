# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T21:37:34.215507+00:00`
- Price records: `672`
- Market context records: `6644`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11766`

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

- `market_context_high->unknown_1h` score `2.4046` n `203` status `ready` deltaP `-4.8922` edge `0.3231` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `0.7181` n `193` status `ready` deltaP `10.7796` edge `0.1748` maxDD `-5.2791`
- `market_context_high->unknown_24h` score `0.6493` n `193` status `ready` deltaP `-1.8126` edge `0.4283` maxDD `-12.3047`
- `market_context_high->crypto_major_1h` score `0.1274` n `203` status `ready` deltaP `8.9636` edge `0.0509` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.087` n `203` status `ready` deltaP `6.2011` edge `0.0445` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.2298` n `203` status `ready` deltaP `3.0854` edge `0.0007` maxDD `-0.7249`
- `market_context_high->index_1h` score `-0.468` n `203` status `ready` deltaP `0.9705` edge `0.0053` maxDD `-0.7417`
- `market_context_high->commodity_1h` score `-0.6638` n `203` status `ready` deltaP `-1.289` edge `-0.0082` maxDD `-2.1314`
- `market_context_high->unknown_4h` score `-0.6899` n `203` status `ready` deltaP `-15.4241` edge `0.2859` maxDD `-10.5788`
- `market_context_high->index_4h` score `-0.7743` n `203` status `ready` deltaP `11.2361` edge `0.0138` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-0.8766` n `203` status `ready` deltaP `3.0523` edge `0.0093` maxDD `-3.8827`
- `market_context_high->crypto_major_4h` score `-0.98` n `203` status `ready` deltaP `11.1769` edge `0.1313` maxDD `-16.8495`
- `market_context_high->metal_1h` score `-1.0909` n `203` status `ready` deltaP `-2.758` edge `0.0016` maxDD `-1.5966`
- `market_context_high->crypto_alt_4h` score `-1.3581` n `203` status `ready` deltaP `7.8697` edge `0.1136` maxDD `-19.2145`
- `market_context_high->commodity_4h` score `-1.4268` n `203` status `ready` deltaP `-1.3119` edge `-0.0247` maxDD `-5.6246`
- `market_context_high->fx_4h` score `-1.4808` n `203` status `ready` deltaP `4.6895` edge `0.0001` maxDD `-3.3635`
- `market_context_high->metal_4h` score `-1.8786` n `203` status `ready` deltaP `1.9795` edge `0.032` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-4.3261` n `203` status `ready` deltaP `9.1358` edge `0.0055` maxDD `-27.1529`
- `market_context_high->metal_24h` score `-5.9263` n `193` status `ready` deltaP `-3.168` edge `0.0229` maxDD `-24.5918`
- `market_context_high->fx_24h` score `-6.259` n `193` status `ready` deltaP `-10.7813` edge `-0.0081` maxDD `-10.6623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
