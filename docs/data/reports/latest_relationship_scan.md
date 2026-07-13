# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T16:37:31.197292+00:00`
- Price records: `672`
- Market context records: `6621`
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

- `market_context_high->unknown_24h` score `3.0353` n `177` status `ready` deltaP `0.2473` edge `0.5176` maxDD `-12.3047`
- `market_context_high->unknown_1h` score `2.1552` n `203` status `ready` deltaP `-6.2395` edge `0.3113` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `0.2042` n `177` status `ready` deltaP `8.0162` edge `0.1504` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.09` n `203` status `ready` deltaP `7.6163` edge `0.032` maxDD `-4.2122`
- `market_context_high->fx_1h` score `-0.2469` n `203` status `ready` deltaP `2.786` edge `0.0005` maxDD `-0.7249`
- `market_context_high->crypto_alt_1h` score `-0.4587` n `203` status `ready` deltaP `4.8538` edge `0.0225` maxDD `-3.7803`
- `market_context_high->index_1h` score `-0.5474` n `203` status `ready` deltaP `-0.3768` edge `0.0041` maxDD `-0.7417`
- `market_context_high->commodity_1h` score `-0.6093` n `203` status `ready` deltaP `-0.6902` edge `-0.0052` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.8617` n `203` status `ready` deltaP `10.1691` edge `0.0097` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-1.0061` n `203` status `ready` deltaP `2.3038` edge `0.0035` maxDD `-3.8827`
- `market_context_high->metal_1h` score `-1.1724` n `203` status `ready` deltaP `-3.5065` edge `-0.0002` maxDD `-1.5966`
- `market_context_high->commodity_4h` score `-1.2545` n `203` status `ready` deltaP `-0.5497` edge `-0.0077` maxDD `-5.6246`
- `market_context_high->unknown_4h` score `-1.3585` n `203` status `ready` deltaP `-17.4058` edge `0.2434` maxDD `-10.5788`
- `market_context_high->crypto_major_4h` score `-1.5539` n `203` status `ready` deltaP `8.5854` edge `0.075` maxDD `-16.8495`
- `market_context_high->fx_4h` score `-1.5988` n `203` status `ready` deltaP `2.5554` edge `-0.0008` maxDD `-3.3635`
- `market_context_high->crypto_alt_4h` score `-1.9724` n `203` status `ready` deltaP `5.4307` edge `0.0511` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.0835` n `203` status `ready` deltaP `-0.4596` edge `0.022` maxDD `-5.2172`
- `market_context_high->metal_24h` score `-4.3135` n `177` status `ready` deltaP `-1.9148` edge `0.0432` maxDD `-15.6763`
- `market_context_high->equity_4h` score `-4.5896` n `203` status `ready` deltaP `8.5261` edge `-0.0124` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-5.7635` n `177` status `ready` deltaP `-7.9242` edge `-0.0016` maxDD `-9.4022`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
