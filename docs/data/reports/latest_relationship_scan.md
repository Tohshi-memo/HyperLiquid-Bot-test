# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T16:37:24.790899+00:00`
- Price records: `672`
- Market context records: `2781`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9237`

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

- `market_context_high->unknown_24h` score `3.6284` n `140` status `ready` deltaP `7.4752` edge `0.299` maxDD `-1.7175`
- `market_context_high->crypto_alt_24h` score `3.2302` n `140` status `ready` deltaP `4.5387` edge `0.6306` maxDD `-22.6673`
- `market_context_high->unknown_4h` score `0.9012` n `142` status `ready` deltaP `6.1856` edge `0.1392` maxDD `-3.7602`
- `market_context_high->commodity_24h` score `0.3262` n `140` status `ready` deltaP `10.6051` edge `0.2805` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.2161` n `142` status `ready` deltaP `12.2338` edge `0.0303` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.0781` n `142` status `ready` deltaP `3.732` edge `0.0417` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.1194` n `142` status `ready` deltaP `3.7489` edge `0.0091` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.5742` n `142` status `ready` deltaP `-0.9867` edge `0.0031` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.6404` n `142` status `ready` deltaP `0.4322` edge `-0.0004` maxDD `-3.0996`
- `market_context_high->commodity_1h` score `-0.6592` n `142` status `ready` deltaP `-0.5819` edge `-0.0053` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.6898` n `142` status `ready` deltaP `5.0962` edge `0.0536` maxDD `-10.747`
- `market_context_high->crypto_major_1h` score `-0.9085` n `142` status `ready` deltaP `3.926` edge `0.0443` maxDD `-9.622`
- `market_context_high->equity_1h` score `-1.0609` n `142` status `ready` deltaP `-3.4979` edge `0.0182` maxDD `-2.6634`
- `market_context_high->fx_4h` score `-1.1081` n `142` status `ready` deltaP `-3.2957` edge `0.0075` maxDD `-0.5631`
- `market_context_high->fx_24h` score `-1.3784` n `140` status `ready` deltaP `-1.002` edge `-0.021` maxDD `-0.6418`
- `market_context_high->crypto_alt_4h` score `-1.4045` n `142` status `ready` deltaP `13.8805` edge `0.2245` maxDD `-28.7261`
- `market_context_high->equity_4h` score `-1.5467` n `142` status `ready` deltaP `0.8953` edge `0.0031` maxDD `-5.7037`
- `market_context_high->commodity_4h` score `-1.5697` n `142` status `ready` deltaP `0.161` edge `-0.0103` maxDD `-10.0279`
- `market_context_high->metal_4h` score `-2.2359` n `142` status `ready` deltaP `-1.3805` edge `-0.0224` maxDD `-11.4038`
- `market_context_high->crypto_major_4h` score `-2.5138` n `142` status `ready` deltaP `5.4298` edge `0.1321` maxDD `-32.2466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
