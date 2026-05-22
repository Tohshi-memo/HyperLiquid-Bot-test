# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T14:52:21.554593+00:00`
- Price records: `672`
- Market context records: `1536`
- Flow alert records: `6335`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8802`

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

- `market_context_high->metal_24h` score `12.7958` n `176` status `ready` deltaP `22.8851` edge `1.0138` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.6994` n `176` status `ready` deltaP `28.6774` edge `0.9854` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.0212` n `176` status `ready` deltaP `28.0934` edge `0.761` maxDD `-8.0553`
- `market_context_high->index_24h` score `4.0374` n `176` status `ready` deltaP `20.5177` edge `0.3083` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.7322` n `176` status `ready` deltaP `13.8258` edge `0.3682` maxDD `-14.2815`
- `market_context_high->fx_24h` score `0.8092` n `176` status `ready` deltaP `17.661` edge `0.0546` maxDD `-1.3925`
- `market_context_high->equity_4h` score `0.1653` n `199` status `ready` deltaP `4.0239` edge `0.0964` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `-0.5211` n `199` status `ready` deltaP `11.2728` edge `0.19` maxDD `-19.5565`
- `market_context_high->crypto_alt_1h` score `-0.5655` n `199` status `ready` deltaP `-0.3799` edge `0.0324` maxDD `-4.1892`
- `market_context_high->crypto_major_4h` score `-0.5767` n `199` status `ready` deltaP `7.2979` edge `0.1483` maxDD `-13.3376`
- `market_context_high->fx_1h` score `-0.5821` n `199` status `ready` deltaP `-1.2457` edge `-0.0031` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.7345` n `199` status `ready` deltaP `0.1753` edge `0.0008` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.7508` n `199` status `ready` deltaP `4.8484` edge `0.005` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-0.7609` n `199` status `ready` deltaP `-0.6469` edge `-0.0011` maxDD `-4.7041`
- `market_context_high->equity_1h` score `-0.8703` n `199` status `ready` deltaP `-1.6316` edge `0.0192` maxDD `-2.8014`
- `market_context_high->crypto_major_1h` score `-1.0836` n `199` status `ready` deltaP `-1.7911` edge `0.0087` maxDD `-6.1883`
- `market_context_high->fx_4h` score `-1.2771` n `199` status `ready` deltaP `-8.7204` edge `-0.0127` maxDD `-1.4313`
- `market_context_high->index_4h` score `-1.3874` n `199` status `ready` deltaP `-4.5923` edge `0.0239` maxDD `-3.7119`
- `market_context_high->metal_4h` score `-1.5461` n `199` status `ready` deltaP `8.9916` edge `0.0804` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-5.3474` n `199` status `ready` deltaP `-16.2244` edge `-0.1147` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
