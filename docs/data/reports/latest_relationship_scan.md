# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T17:07:29.346850+00:00`
- Price records: `672`
- Market context records: `6623`
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

- `market_context_high->unknown_24h` score `2.7352` n `179` status `ready` deltaP `-0.3335` edge `0.5048` maxDD `-12.3047`
- `market_context_high->unknown_1h` score `2.1432` n `203` status `ready` deltaP `-6.3892` edge `0.3113` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `0.2376` n `179` status `ready` deltaP `8.3886` edge `0.1507` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.0526` n `203` status `ready` deltaP `7.9157` edge `0.0348` maxDD `-4.2122`
- `market_context_high->fx_1h` score `-0.2555` n `203` status `ready` deltaP `2.6363` edge `0.0004` maxDD `-0.7249`
- `market_context_high->crypto_alt_1h` score `-0.3916` n `203` status `ready` deltaP `5.1532` edge `0.0261` maxDD `-3.7803`
- `market_context_high->index_1h` score `-0.5287` n `203` status `ready` deltaP `-0.0774` edge `0.0045` maxDD `-0.7417`
- `market_context_high->commodity_1h` score `-0.6108` n `203` status `ready` deltaP `-0.6902` edge `-0.0054` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.8404` n `203` status `ready` deltaP `10.4739` edge `0.0104` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-0.9377` n `203` status `ready` deltaP `2.6032` edge `0.0072` maxDD `-3.8827`
- `market_context_high->metal_1h` score `-1.1413` n `203` status `ready` deltaP `-3.2071` edge `0.0004` maxDD `-1.5966`
- `market_context_high->unknown_4h` score `-1.2153` n `203` status `ready` deltaP `-17.1009` edge `0.2533` maxDD `-10.5788`
- `market_context_high->commodity_4h` score `-1.2718` n `203` status `ready` deltaP `-0.7022` edge `-0.0089` maxDD `-5.6246`
- `market_context_high->crypto_major_4h` score `-1.46` n `203` status `ready` deltaP `8.8903` edge `0.085` maxDD `-16.8495`
- `market_context_high->fx_4h` score `-1.5814` n `203` status `ready` deltaP `2.8603` edge `-0.0006` maxDD `-3.3635`
- `market_context_high->crypto_alt_4h` score `-1.877` n `203` status `ready` deltaP `5.7356` edge `0.0613` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.0544` n `203` status `ready` deltaP `-0.1547` edge `0.0237` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-4.5017` n `203` status `ready` deltaP `8.8309` edge `-0.0071` maxDD `-27.1529`
- `market_context_high->metal_24h` score `-4.5097` n `179` status `ready` deltaP `-1.9475` edge `0.0406` maxDD `-16.7964`
- `market_context_high->fx_24h` score `-5.8244` n `179` status `ready` deltaP `-8.3093` edge `-0.0022` maxDD `-9.5551`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
