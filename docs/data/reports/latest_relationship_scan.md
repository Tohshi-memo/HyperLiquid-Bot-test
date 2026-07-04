# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T21:07:31.119461+00:00`
- Price records: `672`
- Market context records: `5703`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8856`

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

- `market_context_high->crypto_major_4h` score `2.0669` n `262` status `ready` deltaP `12.2207` edge `0.2279` maxDD `-6.6368`
- `market_context_high->equity_24h` score `1.0979` n `212` status `ready` deltaP `16.5521` edge `0.5383` maxDD `-31.6316`
- `market_context_high->crypto_alt_4h` score `0.9009` n `262` status `ready` deltaP `9.5524` edge `0.1723` maxDD `-7.5392`
- `market_context_high->equity_4h` score `0.2074` n `262` status `ready` deltaP `6.7271` edge `0.1363` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.262` n `274` status `ready` deltaP `2.0401` edge `0.0009` maxDD `-0.5144`
- `market_context_high->crypto_major_1h` score `-0.3755` n `274` status `ready` deltaP `3.6311` edge `0.0401` maxDD `-3.9811`
- `market_context_high->metal_1h` score `-0.4446` n `274` status `ready` deltaP `1.638` edge `-0.0004` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.5273` n `274` status `ready` deltaP `1.9658` edge `0.0373` maxDD `-3.8812`
- `market_context_high->equity_1h` score `-0.5719` n `274` status `ready` deltaP `3.6508` edge `0.0287` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.6192` n `274` status `ready` deltaP `0.4589` edge `0.0044` maxDD `-0.9472`
- `market_context_high->fx_24h` score `-1.0258` n `212` status `ready` deltaP `12.0873` edge `0.044` maxDD `-3.4876`
- `market_context_high->commodity_1h` score `-1.084` n `274` status `ready` deltaP `-0.8425` edge `-0.004` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.2237` n `262` status `ready` deltaP `3.0534` edge `0.0062` maxDD `-1.3415`
- `market_context_high->index_4h` score `-1.2987` n `262` status `ready` deltaP `-0.91` edge `0.0083` maxDD `-3.165`
- `market_context_high->metal_4h` score `-2.6974` n `262` status `ready` deltaP `-8.5436` edge `-0.0513` maxDD `-11.6719`
- `market_context_high->index_24h` score `-2.8873` n `212` status `ready` deltaP `2.2864` edge `0.0281` maxDD `-18.0809`
- `market_context_high->commodity_4h` score `-3.9475` n `262` status `ready` deltaP `-4.366` edge `-0.0323` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.1206` n `212` status `ready` deltaP `6.3319` edge `0.0601` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.9923` n `212` status `ready` deltaP `-8.1368` edge `-0.2428` maxDD `-32.5421`
- `market_context_high->commodity_24h` score `-12.1278` n `212` status `ready` deltaP `-11.0783` edge `-0.0759` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
