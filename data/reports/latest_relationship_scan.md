# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T12:52:29.772770+00:00`
- Price records: `672`
- Market context records: `6710`
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

- `market_context_high->unknown_24h` score `1.4121` n `177` status `ready` deltaP `2.4982` edge `0.5396` maxDD `-12.3511`
- `market_context_high->crypto_major_1h` score `0.1606` n `177` status `ready` deltaP `9.0708` edge `0.0461` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `0.1052` n `177` status `ready` deltaP `6.328` edge `0.043` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.3536` n `177` status `ready` deltaP `0.3696` edge `0.0007` maxDD `-0.5468`
- `market_context_high->commodity_24h` score `-0.4143` n `177` status `ready` deltaP `8.1598` edge `0.0979` maxDD `-5.2791`
- `market_context_high->index_1h` score `-0.5404` n `177` status `ready` deltaP `-0.099` edge `0.0028` maxDD `-0.7136`
- `market_context_high->metal_1h` score `-0.6298` n `177` status `ready` deltaP `-4.2178` edge `-0.0001` maxDD `-1.2017`
- `market_context_high->commodity_1h` score `-0.6935` n `177` status `ready` deltaP `-1.2001` edge `-0.0126` maxDD `-2.1314`
- `market_context_high->equity_1h` score `-0.8887` n `177` status `ready` deltaP `4.2517` edge `0.0003` maxDD `-3.8827`
- `market_context_high->index_4h` score `-1.0151` n `177` status `ready` deltaP `8.9904` edge `-0.0021` maxDD `-5.7046`
- `market_context_high->unknown_1h` score `-1.0742` n `177` status `ready` deltaP `-8.0424` edge `0.0542` maxDD `-3.2083`
- `market_context_high->fx_4h` score `-1.213` n `177` status `ready` deltaP `7.5548` edge `0.0005` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.7535` n `177` status `ready` deltaP `-4.8195` edge `-0.0437` maxDD `-5.5853`
- `market_context_high->crypto_major_4h` score `-1.7857` n `177` status `ready` deltaP `6.542` edge `0.0589` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-1.9786` n `177` status `ready` deltaP `4.8023` edge `0.0545` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.4027` n `177` status `ready` deltaP `-4.5878` edge `0.0086` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-3.5212` n `177` status `ready` deltaP `7.107` edge `-0.0719` maxDD `-27.1529`
- `market_context_high->unknown_4h` score `-3.9146` n `177` status `ready` deltaP `-17.3936` edge `0.0263` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.3017` n `177` status `ready` deltaP `-8.0714` edge `0.001` maxDD `-5.7868`
- `market_context_high->metal_24h` score `-7.0538` n `177` status `ready` deltaP `-6.1676` edge `-0.0147` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
