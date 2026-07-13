# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T11:07:29.336494+00:00`
- Price records: `672`
- Market context records: `6597`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9808`

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

- `market_context_high->unknown_24h` score `3.7918` n `163` status `ready` deltaP `4.7116` edge `0.6146` maxDD `-15.0689`
- `market_context_high->unknown_1h` score `2.0388` n `210` status `ready` deltaP `-5.1297` edge `0.2942` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `0.6532` n `163` status `ready` deltaP `9.9985` edge `0.1746` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.309` n `210` status `ready` deltaP `1.6068` edge `0.0004` maxDD `-0.7249`
- `market_context_high->crypto_major_1h` score `-0.4384` n `210` status `ready` deltaP `6.7479` edge `0.0254` maxDD `-6.7936`
- `market_context_high->index_1h` score `-0.5452` n `210` status `ready` deltaP `-0.231` edge `0.0036` maxDD `-0.7564`
- `market_context_high->commodity_1h` score `-0.5596` n `210` status `ready` deltaP `0.0399` edge `-0.0037` maxDD `-2.1314`
- `market_context_high->crypto_alt_1h` score `-0.649` n `210` status `ready` deltaP `4.3941` edge `0.0188` maxDD `-5.8368`
- `market_context_high->index_4h` score `-0.9278` n `210` status `ready` deltaP `8.9896` edge `0.0091` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-1.204` n `210` status `ready` deltaP `1.7822` edge `-0.0012` maxDD `-4.2147`
- `market_context_high->commodity_4h` score `-1.2333` n `210` status `ready` deltaP `-0.5168` edge `-0.0052` maxDD `-5.6246`
- `market_context_high->metal_1h` score `-1.3195` n `210` status `ready` deltaP `-4.0262` edge `-0.0024` maxDD `-2.1239`
- `market_context_high->fx_4h` score `-1.6531` n `210` status `ready` deltaP `1.6013` edge `-0.0014` maxDD `-3.3635`
- `market_context_high->unknown_4h` score `-1.7507` n `210` status `ready` deltaP `-17.5232` edge `0.2115` maxDD `-10.5788`
- `market_context_high->crypto_major_4h` score `-1.8995` n `210` status `ready` deltaP `6.5143` edge `0.0445` maxDD `-16.8495`
- `market_context_high->metal_4h` score `-2.1956` n `210` status `ready` deltaP `-1.8061` edge `0.0166` maxDD `-5.2172`
- `market_context_high->crypto_alt_4h` score `-2.2071` n `210` status `ready` deltaP `3.4088` edge `0.0345` maxDD `-19.2145`
- `market_context_high->fx_24h` score `-3.7993` n `163` status `ready` deltaP `-4.9642` edge `-0.0005` maxDD `-9.2795`
- `market_context_high->metal_24h` score `-4.2105` n `163` status `ready` deltaP `1.0911` edge `0.0633` maxDD `-9.7162`
- `market_context_high->equity_4h` score `-4.8545` n `210` status `ready` deltaP `6.896` edge `-0.0236` maxDD `-27.1529`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
