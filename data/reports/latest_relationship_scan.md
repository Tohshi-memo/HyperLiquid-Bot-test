# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T05:22:28.954363+00:00`
- Price records: `672`
- Market context records: `6785`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11716`

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

- `market_context_high->unknown_24h` score `0.8937` n `176` status `ready` deltaP `-1.1995` edge `0.4978` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.0657` n `176` status `ready` deltaP `8.144` edge `0.138` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.145` n `183` status `ready` deltaP `6.7635` edge `0.0223` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.3672` n `183` status `ready` deltaP `4.1286` edge `0.0183` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.3727` n `183` status `ready` deltaP `0.0335` edge `0.0005` maxDD `-0.5468`
- `market_context_high->index_1h` score `-0.6398` n `183` status `ready` deltaP `-1.6205` edge `0.0002` maxDD `-0.7136`
- `market_context_high->commodity_1h` score `-0.6733` n `183` status `ready` deltaP `-1.2761` edge `-0.0095` maxDD `-2.1314`
- `market_context_high->metal_1h` score `-0.7241` n `183` status `ready` deltaP `-5.4309` edge `-0.0041` maxDD `-1.2017`
- `market_context_high->equity_1h` score `-1.2307` n `183` status `ready` deltaP `2.5417` edge `-0.0168` maxDD `-3.8827`
- `market_context_high->fx_4h` score `-1.3189` n `176` status `ready` deltaP `5.862` edge `-0.0018` maxDD `-2.1765`
- `market_context_high->index_4h` score `-1.3232` n `176` status `ready` deltaP `5.2245` edge `-0.0165` maxDD `-5.7046`
- `market_context_high->commodity_4h` score `-1.5035` n `176` status `ready` deltaP `-3.1458` edge `-0.0228` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.6315` n `183` status `ready` deltaP `-5.8277` edge `-0.007` maxDD `-3.2083`
- `market_context_high->metal_4h` score `-2.5841` n `176` status `ready` deltaP `-5.5571` edge `-0.0082` maxDD `-5.2172`
- `market_context_high->crypto_major_4h` score `-2.9112` n `176` status `ready` deltaP `2.1341` edge `-0.056` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-2.9874` n `176` status `ready` deltaP `1.3026` edge `-0.0515` maxDD `-19.2145`
- `market_context_high->unknown_4h` score `-3.2547` n `176` status `ready` deltaP `-13.8858` edge `0.0579` maxDD `-10.2579`
- `market_context_high->equity_4h` score `-4.3373` n `176` status `ready` deltaP `2.0926` edge `-0.1431` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-4.4495` n `176` status `ready` deltaP `-9.2645` edge `-0.0054` maxDD `-5.6237`
- `market_context_high->metal_24h` score `-9.0549` n `176` status `ready` deltaP `-17.4558` edge `-0.196` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
