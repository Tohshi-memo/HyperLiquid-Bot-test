# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T07:22:28.294096+00:00`
- Price records: `672`
- Market context records: `5857`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10104`

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

- `news_risk_high->fx_4h` score `3.7011` n `30` status `ready` deltaP `38.628` edge `0.0555` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `1.9747` n `30` status `ready` deltaP `23.9321` edge `0.0189` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.8932` n `30` status `ready` deltaP `11.8363` edge `0.0823` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.6812` n `251` status `ready` deltaP `7.4465` edge `0.1529` maxDD `-6.9958`
- `news_risk_high->crypto_alt_1h` score `0.2738` n `30` status `ready` deltaP `5.4691` edge `0.0448` maxDD `-1.6923`
- `market_context_high->fx_1h` score `-0.3602` n `251` status `ready` deltaP `0.3996` edge `-0.0003` maxDD `-0.5499`
- `news_risk_high->metal_1h` score `-0.397` n `30` status `ready` deltaP `1.8363` edge `-0.0265` maxDD `-1.2643`
- `market_context_high->equity_1h` score `-0.4733` n `251` status `ready` deltaP `4.1183` edge `0.0338` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5271` n `251` status `ready` deltaP `3.0847` edge `0.0026` maxDD `-2.0339`
- `market_context_high->commodity_1h` score `-0.5401` n `251` status `ready` deltaP `-1.0419` edge `-0.0022` maxDD `-2.1412`
- `market_context_high->index_1h` score `-0.6137` n `251` status `ready` deltaP `0.3441` edge `0.0038` maxDD `-0.7819`
- `market_context_high->crypto_major_1h` score `-0.7911` n `251` status `ready` deltaP `3.8815` edge `0.0403` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-0.948` n `251` status `ready` deltaP `2.5873` edge `0.0372` maxDD `-6.6758`
- `market_context_high->equity_24h` score `-1.1646` n `228` status `ready` deltaP `16.2372` edge `0.3026` maxDD `-31.6316`
- `news_risk_high->index_1h` score `-1.2237` n `30` status `ready` deltaP `-12.2455` edge `-0.0238` maxDD `-1.1161`
- `market_context_high->index_4h` score `-1.2309` n `251` status `ready` deltaP `-0.2963` edge `0.0129` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.7673` n `251` status `ready` deltaP `-4.36` edge `-0.0026` maxDD `-2.2593`
- `news_risk_high->commodity_4h` score `-1.7842` n `30` status `ready` deltaP `-13.4248` edge `-0.0517` maxDD `-2.3372`
- `market_context_high->fx_24h` score `-1.8156` n `228` status `ready` deltaP `4.8794` edge `0.0165` maxDD `-5.5435`
- `market_context_high->metal_4h` score `-1.8997` n `251` status `ready` deltaP `-3.7539` edge `-0.0351` maxDD `-7.3409`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
