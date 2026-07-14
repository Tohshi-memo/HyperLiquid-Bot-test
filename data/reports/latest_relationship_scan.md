# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T12:21:03.777695+00:00`
- Price records: `672`
- Market context records: `6708`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11784`

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

- `market_context_high->unknown_24h` score `1.4277` n `177` status `ready` deltaP `2.4982` edge `0.5416` maxDD `-12.3511`
- `market_context_high->crypto_major_1h` score `0.1832` n `177` status `ready` deltaP `9.0708` edge `0.049` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `0.1304` n `177` status `ready` deltaP `6.328` edge `0.0451` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.3458` n `177` status `ready` deltaP `0.5193` edge `0.0007` maxDD `-0.5468`
- `market_context_high->commodity_24h` score `-0.4191` n `177` status `ready` deltaP `8.1598` edge `0.0975` maxDD `-5.2791`
- `market_context_high->index_1h` score `-0.5373` n `177` status `ready` deltaP `-0.099` edge `0.0032` maxDD `-0.7136`
- `market_context_high->metal_1h` score `-0.6235` n `177` status `ready` deltaP `-4.2178` edge `0.0007` maxDD `-1.2017`
- `market_context_high->commodity_1h` score `-0.6725` n `177` status `ready` deltaP `-0.9007` edge `-0.0119` maxDD `-2.1314`
- `market_context_high->equity_1h` score `-0.8323` n `177` status `ready` deltaP `4.5511` edge `0.003` maxDD `-3.8827`
- `market_context_high->index_4h` score `-0.9945` n `177` status `ready` deltaP `9.2953` edge `-0.0015` maxDD `-5.7046`
- `market_context_high->unknown_1h` score `-1.0622` n `177` status `ready` deltaP `-8.0424` edge `0.0552` maxDD `-3.2083`
- `market_context_high->fx_4h` score `-1.2027` n `177` status `ready` deltaP `7.7073` edge `0.0008` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.7473` n `177` status `ready` deltaP `-4.8195` edge `-0.0429` maxDD `-5.5853`
- `market_context_high->crypto_major_4h` score `-1.7584` n `177` status `ready` deltaP `6.542` edge `0.0624` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-1.9646` n `177` status `ready` deltaP `4.8023` edge `0.0563` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.4027` n `177` status `ready` deltaP `-4.5878` edge `0.0086` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-3.4858` n `177` status `ready` deltaP `7.4118` edge `-0.0694` maxDD `-27.1529`
- `market_context_high->unknown_4h` score `-3.8796` n `177` status `ready` deltaP `-17.2412` edge `0.0282` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.2969` n `177` status `ready` deltaP `-8.0714` edge `0.0014` maxDD `-5.7868`
- `market_context_high->metal_24h` score `-7.0022` n `177` status `ready` deltaP `-5.8204` edge `-0.0104` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
