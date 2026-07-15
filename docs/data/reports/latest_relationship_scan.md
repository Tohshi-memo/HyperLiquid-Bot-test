# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T22:52:26.986778+00:00`
- Price records: `672`
- Market context records: `6861`
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

- `market_context_high->unknown_24h` score `1.1991` n `176` status `ready` deltaP `-1.6268` edge `0.5398` maxDD `-12.3511`
- `market_context_high->fx_1h` score `-0.2534` n `224` status `ready` deltaP `2.1614` edge `0.0016` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.6459` n `224` status `ready` deltaP `1.394` edge `0.0133` maxDD `-3.7803`
- `market_context_high->commodity_1h` score `-0.6664` n `224` status `ready` deltaP `-1.719` edge `-0.0055` maxDD `-2.1443`
- `market_context_high->crypto_major_1h` score `-0.6983` n `224` status `ready` deltaP `3.0303` edge `0.012` maxDD `-4.2314`
- `market_context_high->commodity_24h` score `-0.7385` n `176` status `ready` deltaP `5.4721` edge `0.0888` maxDD `-5.2791`
- `market_context_high->index_1h` score `-0.8554` n `224` status `ready` deltaP `-2.3029` edge `-0.0032` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.94` n `224` status `ready` deltaP `-5.4199` edge `-0.0076` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.9993` n `223` status `ready` deltaP `10.8238` edge `0.0061` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.3527` n `223` status `ready` deltaP `-2.4803` edge `-0.0079` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.6256` n `224` status `ready` deltaP `-3.1897` edge `-0.0241` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.9405` n `224` status `ready` deltaP `0.0667` edge `-0.0312` maxDD `-13.1084`
- `market_context_high->index_4h` score `-2.0433` n `223` status `ready` deltaP `3.0612` edge `-0.0244` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.4483` n `223` status `ready` deltaP `-0.4737` edge `-0.0124` maxDD `-5.5324`
- `market_context_high->unknown_4h` score `-3.1376` n `223` status `ready` deltaP `-9.1215` edge `0.0359` maxDD `-10.2579`
- `market_context_high->crypto_major_4h` score `-3.1579` n `223` status `ready` deltaP `-1.8961` edge `-0.0595` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.203` n `223` status `ready` deltaP `-0.9747` edge `-0.0458` maxDD `-20.6678`
- `market_context_high->fx_24h` score `-4.5397` n `176` status `ready` deltaP `-9.8816` edge `-0.0088` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.5667` n `223` status `ready` deltaP `-0.1809` edge `-0.1744` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-9.0179` n `176` status `ready` deltaP `-18.9332` edge `-0.1814` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
