# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T21:37:31.345339+00:00`
- Price records: `672`
- Market context records: `6960`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11735`

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

- `market_context_high->fx_1h` score `-0.2515` n `237` status `ready` deltaP `2.1842` edge `0.0017` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.3903` n `237` status `ready` deltaP `2.2803` edge `0.0212` maxDD `-4.5815`
- `market_context_high->metal_1h` score `-0.7271` n `237` status `ready` deltaP `-2.0901` edge `-0.0025` maxDD `-2.1427`
- `market_context_high->index_1h` score `-0.7582` n `237` status `ready` deltaP `-0.8376` edge `-0.0005` maxDD `-2.2895`
- `market_context_high->fx_4h` score `-0.9394` n `237` status `ready` deltaP `11.6304` edge `0.0084` maxDD `-2.1765`
- `market_context_high->crypto_major_1h` score `-1.2077` n `237` status `ready` deltaP `3.0288` edge `0.0144` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-1.3077` n `237` status `ready` deltaP `-3.1235` edge `-0.016` maxDD `-2.4388`
- `market_context_high->unknown_1h` score `-1.5961` n `237` status `ready` deltaP `-1.9809` edge `-0.0297` maxDD `-3.2083`
- `market_context_high->commodity_4h` score `-1.6483` n `237` status `ready` deltaP `-4.2805` edge `-0.0338` maxDD `-5.5853`
- `market_context_high->unknown_24h` score `-1.6617` n `224` status `ready` deltaP `-9.1096` edge `0.3027` maxDD `-18.7342`
- `market_context_high->index_4h` score `-1.8387` n `237` status `ready` deltaP `7.3621` edge `-0.0149` maxDD `-12.2591`
- `market_context_high->equity_1h` score `-2.0357` n `237` status `ready` deltaP `1.9391` edge `-0.0185` maxDD `-15.7664`
- `market_context_high->metal_4h` score `-2.1034` n `237` status `ready` deltaP `3.8039` edge `0.0033` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-3.1809` n `237` status `ready` deltaP `-0.5512` edge `-0.0256` maxDD `-22.2831`
- `market_context_high->unknown_4h` score `-3.3573` n `237` status `ready` deltaP `-8.8679` edge `0.0159` maxDD `-10.2579`
- `market_context_high->commodity_24h` score `-3.7435` n `224` status `ready` deltaP `-6.3359` edge `-0.0829` maxDD `-5.2791`
- `market_context_high->crypto_major_4h` score `-3.8547` n `237` status `ready` deltaP `-1.8061` edge `-0.0537` maxDD `-24.6094`
- `market_context_high->fx_24h` score `-4.4166` n `224` status `ready` deltaP `-7.2822` edge `-0.0148` maxDD `-5.7093`
- `market_context_high->equity_4h` score `-7.747` n `237` status `ready` deltaP `3.7061` edge `-0.0962` maxDD `-66.7371`
- `market_context_high->index_24h` score `-12.3483` n `224` status `ready` deltaP `-6.8573` edge `-0.1304` maxDD `-59.5597`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
