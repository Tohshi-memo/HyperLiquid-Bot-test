# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T09:52:27.317202+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7592`

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

- `market_context_high->unknown_4h` score `38.3869` n `111` status `ready` deltaP `-0.4738` edge `3.2356` maxDD `-1.016`
- `market_context_high->unknown_1h` score `3.828` n `114` status `ready` deltaP `4.3334` edge `0.339` maxDD `-1.5781`
- `market_context_high->commodity_24h` score `0.8498` n `46` status `ready` deltaP `17.4819` edge `0.0833` maxDD `-3.6055`
- `market_context_high->crypto_alt_24h` score `0.347` n `46` status `ready` deltaP `12.6057` edge `0.219` maxDD `-17.0169`
- `market_context_high->crypto_major_24h` score `0.1279` n `46` status `ready` deltaP `4.529` edge `0.0864` maxDD `-5.8084`
- `market_context_high->fx_4h` score `-0.0114` n `111` status `ready` deltaP `7.4078` edge `0.009` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.065` n `114` status `ready` deltaP `3.5508` edge `0.0029` maxDD `-0.1258`
- `market_context_high->commodity_1h` score `-0.4835` n `114` status `ready` deltaP `0.0867` edge `0.0092` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.5448` n `114` status `ready` deltaP `5.6676` edge `-0.004` maxDD `-1.6682`
- `market_context_high->index_1h` score `-0.6207` n `114` status `ready` deltaP `-1.392` edge `-0.0051` maxDD `-1.2155`
- `market_context_high->fx_24h` score `-0.8761` n `46` status `ready` deltaP `0.5737` edge `0.0065` maxDD `-1.145`
- `market_context_high->commodity_4h` score `-0.8873` n `111` status `ready` deltaP `-3.2492` edge `0.0308` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-1.3179` n `114` status `ready` deltaP `2.3112` edge `-0.0263` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-1.9245` n `111` status `ready` deltaP `4.385` edge `-0.0186` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.1156` n `111` status `ready` deltaP `-7.0342` edge `-0.0369` maxDD `-4.3282`
- `market_context_high->crypto_alt_1h` score `-2.9763` n `114` status `ready` deltaP `-1.5207` edge `-0.0505` maxDD `-11.3243`
- `market_context_high->metal_24h` score `-3.1204` n `46` status `ready` deltaP `-8.1295` edge `-0.0112` maxDD `-6.9044`
- `market_context_high->equity_1h` score `-3.7` n `114` status `ready` deltaP `0.5541` edge `-0.0847` maxDD `-12.1865`
- `market_context_high->index_24h` score `-5.0173` n `46` status `ready` deltaP `-17.9046` edge `-0.1686` maxDD `-5.078`
- `market_context_high->crypto_major_4h` score `-9.8701` n `111` status `ready` deltaP `-12.121` edge `-0.242` maxDD `-33.3092`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
