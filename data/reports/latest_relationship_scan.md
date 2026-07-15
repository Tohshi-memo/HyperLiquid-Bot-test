# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T10:37:30.989941+00:00`
- Price records: `672`
- Market context records: `6808`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11680`

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

- `market_context_high->unknown_24h` score `0.8234` n `176` status `ready` deltaP `-1.5467` edge `0.4911` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.3554` n `176` status `ready` deltaP `10.4009` edge `0.1471` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.3378` n `190` status `ready` deltaP `6.0353` edge `0.0176` maxDD `-4.2122`
- `market_context_high->fx_1h` score `-0.4482` n `190` status `ready` deltaP `-1.2843` edge `-0.0004` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.4503` n `190` status `ready` deltaP `3.254` edge `0.0172` maxDD `-3.7803`
- `market_context_high->commodity_1h` score `-0.6338` n `190` status `ready` deltaP `-0.8163` edge `-0.0075` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.7222` n `190` status `ready` deltaP `-2.7765` edge `-0.0015` maxDD `-0.8068`
- `market_context_high->metal_1h` score `-0.8192` n `190` status `ready` deltaP `-6.2528` edge `-0.0055` maxDD `-1.6272`
- `market_context_high->fx_4h` score `-1.373` n `185` status `ready` deltaP `4.9126` edge `-0.0024` maxDD `-2.1765`
- `market_context_high->equity_1h` score `-1.381` n `190` status `ready` deltaP `1.5207` edge `-0.0194` maxDD `-4.1322`
- `market_context_high->commodity_4h` score `-1.397` n `185` status `ready` deltaP `-2.5981` edge `-0.0128` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.6516` n `185` status `ready` deltaP `1.8375` edge `-0.028` maxDD `-6.3458`
- `market_context_high->unknown_1h` score `-1.729` n `190` status `ready` deltaP `-6.4025` edge `-0.0113` maxDD `-3.2083`
- `market_context_high->metal_4h` score `-2.8235` n `185` status `ready` deltaP `-6.0094` edge `-0.0236` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-3.2776` n `185` status `ready` deltaP `-0.6576` edge `-0.0831` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.4832` n `185` status `ready` deltaP `-1.517` edge `-0.0781` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.4989` n `185` status `ready` deltaP `-14.1175` edge `0.0391` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.49` n `176` status `ready` deltaP `-9.7853` edge `-0.0053` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-5.0111` n `185` status `ready` deltaP `-0.81` edge `-0.1832` maxDD `-29.3079`
- `market_context_high->metal_24h` score `-9.5674` n `176` status `ready` deltaP `-21.1017` edge `-0.2374` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
