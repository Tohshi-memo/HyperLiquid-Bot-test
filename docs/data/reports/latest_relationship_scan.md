# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T15:07:32.470661+00:00`
- Price records: `672`
- Market context records: `6828`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11748`

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

- `market_context_high->unknown_24h` score `0.9139` n `176` status `ready` deltaP `-1.5467` edge `0.5027` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.2148` n `176` status `ready` deltaP `10.0537` edge `0.1377` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.1551` n `206` status `ready` deltaP `6.1886` edge `0.0318` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.3113` n `206` status `ready` deltaP `3.6117` edge `0.0264` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.3425` n `206` status `ready` deltaP `0.5988` edge `0.0006` maxDD `-0.5468`
- `market_context_high->index_1h` score `-0.868` n `206` status `ready` deltaP `-3.3617` edge `-0.0052` maxDD `-1.6939`
- `market_context_high->metal_1h` score `-0.9343` n `206` status `ready` deltaP `-5.6712` edge `-0.0081` maxDD `-1.9098`
- `market_context_high->commodity_1h` score `-1.1448` n `206` status `ready` deltaP `-2.9533` edge `-0.0074` maxDD `-2.1314`
- `market_context_high->fx_4h` score `-1.2151` n `196` status `ready` deltaP `7.5286` edge `0.0004` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.4757` n `196` status `ready` deltaP `-3.811` edge `-0.0148` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.656` n `206` status `ready` deltaP `-4.3646` edge `-0.0188` maxDD `-3.2083`
- `market_context_high->index_4h` score `-1.842` n `196` status `ready` deltaP `1.4031` edge `-0.0293` maxDD `-7.9638`
- `market_context_high->equity_1h` score `-2.3379` n `206` status `ready` deltaP `0.2544` edge `-0.0364` maxDD `-8.4763`
- `market_context_high->metal_4h` score `-2.6683` n `196` status `ready` deltaP `-3.0395` edge `-0.0235` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-2.9404` n `196` status `ready` deltaP `0.336` edge `-0.0465` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.1015` n `196` status `ready` deltaP `0.4822` edge `-0.0425` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.2785` n `196` status `ready` deltaP `-10.8978` edge `0.036` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.454` n `176` status `ready` deltaP `-9.7853` edge `-0.0023` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-5.7006` n `196` status `ready` deltaP `-1.0018` edge `-0.182` maxDD `-36.3737`
- `market_context_high->metal_24h` score `-9.4932` n `176` status `ready` deltaP `-20.7545` edge `-0.2302` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
