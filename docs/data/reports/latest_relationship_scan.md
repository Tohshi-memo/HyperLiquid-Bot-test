# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T18:04:21.846097+00:00`
- Price records: `672`
- Market context records: `6627`
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

- `market_context_high->unknown_24h` score `2.2319` n `183` status `ready` deltaP `-0.7649` edge `0.4824` maxDD `-12.3047`
- `market_context_high->unknown_1h` score `2.2079` n `203` status `ready` deltaP `-5.9401` edge `0.3137` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `0.3517` n `183` status `ready` deltaP `9.1091` edge `0.1554` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `0.0159` n `203` status `ready` deltaP `8.5145` edge `0.0396` maxDD `-4.2122`
- `market_context_high->fx_1h` score `-0.2547` n `203` status `ready` deltaP `2.6363` edge `0.0005` maxDD `-0.7249`
- `market_context_high->crypto_alt_1h` score `-0.2681` n `203` status `ready` deltaP `5.752` edge `0.0324` maxDD `-3.7803`
- `market_context_high->index_1h` score `-0.5101` n `203` status `ready` deltaP `0.222` edge `0.0049` maxDD `-0.7417`
- `market_context_high->commodity_1h` score `-0.6373` n `203` status `ready` deltaP `-0.9896` edge `-0.0068` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.827` n `203` status `ready` deltaP `10.6264` edge `0.0111` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-0.8586` n `203` status `ready` deltaP `3.0523` edge `0.0108` maxDD `-3.8827`
- `market_context_high->unknown_4h` score `-0.9673` n `203` status `ready` deltaP `-16.4912` edge `0.2699` maxDD `-10.5788`
- `market_context_high->metal_1h` score `-1.1137` n `203` status `ready` deltaP `-2.9077` edge `0.0007` maxDD `-1.5966`
- `market_context_high->crypto_major_4h` score `-1.3027` n `203` status `ready` deltaP `9.5001` edge `0.1011` maxDD `-16.8495`
- `market_context_high->commodity_4h` score `-1.3236` n `203` status `ready` deltaP `-1.007` edge `-0.0135` maxDD `-5.6246`
- `market_context_high->fx_4h` score `-1.5473` n `203` status `ready` deltaP `3.47` edge `-0.0003` maxDD `-3.3635`
- `market_context_high->crypto_alt_4h` score `-1.7088` n `203` status `ready` deltaP `6.3453` edge `0.0788` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.0` n `203` status `ready` deltaP `0.4551` edge `0.0266` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-4.4367` n `203` status `ready` deltaP `8.9834` edge `-0.0027` maxDD `-27.1529`
- `market_context_high->metal_24h` score `-4.9109` n `183` status `ready` deltaP `-1.9882` edge `0.0347` maxDD `-19.0835`
- `market_context_high->fx_24h` score `-5.9694` n `183` status `ready` deltaP `-9.0542` edge `-0.0039` maxDD `-9.9885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
