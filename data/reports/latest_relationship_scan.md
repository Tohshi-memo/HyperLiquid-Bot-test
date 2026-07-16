# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T02:22:28.655361+00:00`
- Price records: `672`
- Market context records: `6875`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11786`

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

- `market_context_high->unknown_24h` score `1.0926` n `176` status `ready` deltaP `-3.3599` edge `0.5377` maxDD `-12.3511`
- `market_context_high->fx_1h` score `-0.2487` n `224` status `ready` deltaP `2.2375` edge `0.0017` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.5853` n `224` status `ready` deltaP `1.9114` edge `0.0149` maxDD `-3.7803`
- `market_context_high->commodity_1h` score `-0.6143` n `224` status `ready` deltaP `-0.8982` edge `-0.0043` maxDD `-2.1443`
- `market_context_high->crypto_major_1h` score `-0.6233` n `224` status `ready` deltaP `3.5474` edge `0.0148` maxDD `-4.2314`
- `market_context_high->index_1h` score `-0.8133` n `224` status `ready` deltaP `-1.628` edge `-0.0023` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.8923` n `224` status `ready` deltaP `-4.5926` edge `-0.007` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.9767` n `224` status `ready` deltaP `11.2588` edge `0.0061` maxDD `-2.1765`
- `market_context_high->commodity_24h` score `-1.1517` n `176` status `ready` deltaP `4.4322` edge `0.0613` maxDD `-5.2791`
- `market_context_high->commodity_4h` score `-1.3565` n `224` status `ready` deltaP `-2.4935` edge `-0.0083` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.6457` n `224` status `ready` deltaP `-3.2613` edge `-0.0253` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.8557` n `224` status `ready` deltaP `1.0372` edge `-0.0268` maxDD `-13.1084`
- `market_context_high->index_4h` score `-1.9796` n `224` status `ready` deltaP `3.9417` edge `-0.0221` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.3833` n `224` status `ready` deltaP `0.49` edge `-0.0105` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-3.075` n `224` status `ready` deltaP `-1.3066` edge `-0.0528` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.1042` n `224` status `ready` deltaP `-0.2287` edge `-0.0381` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.2001` n `224` status `ready` deltaP `-9.6472` edge `0.0342` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.5654` n `176` status `ready` deltaP `-9.7083` edge `-0.0121` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.3473` n `224` status `ready` deltaP `1.3393` edge `-0.1564` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.8499` n `176` status `ready` deltaP `-17.8933` edge `-0.1668` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
