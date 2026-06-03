# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T14:52:26.962415+00:00`
- Price records: `672`
- Market context records: `2773`
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

- `market_context_high->unknown_24h` score `3.9772` n `137` status `ready` deltaP `8.2509` edge `0.3229` maxDD `-1.7175`
- `market_context_high->crypto_alt_24h` score `2.4064` n `137` status `ready` deltaP `4.4683` edge `0.6704` maxDD `-22.6673`
- `market_context_high->unknown_4h` score `1.0026` n `142` status `ready` deltaP `6.6429` edge `0.1446` maxDD `-3.7602`
- `market_context_high->commodity_24h` score `0.2343` n `137` status `ready` deltaP `9.9325` edge `0.2732` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.0904` n `142` status `ready` deltaP `11.1667` edge `0.0213` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.0241` n `142` status `ready` deltaP `4.0314` edge `0.0442` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.1521` n `142` status `ready` deltaP `3.4495` edge `0.0069` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.5759` n `142` status `ready` deltaP `0.466` edge `-0.0016` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.5993` n `142` status `ready` deltaP `-1.2861` edge `0.003` maxDD `-0.2164`
- `market_context_high->crypto_alt_1h` score `-0.6999` n `142` status `ready` deltaP `5.2459` edge `0.0513` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.7105` n `142` status `ready` deltaP `-0.3163` edge `-0.0044` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.9373` n `142` status `ready` deltaP `3.7763` edge `0.0416` maxDD `-9.622`
- `market_context_high->equity_1h` score `-1.1713` n `142` status `ready` deltaP `-3.947` edge `0.012` maxDD `-2.6634`
- `market_context_high->fx_4h` score `-1.1873` n `142` status `ready` deltaP `-4.2103` edge `0.007` maxDD `-0.5631`
- `market_context_high->crypto_alt_4h` score `-1.3875` n `142` status `ready` deltaP `14.0329` edge `0.2249` maxDD `-28.7261`
- `market_context_high->fx_24h` score `-1.4149` n `137` status `ready` deltaP `-1.5182` edge `-0.0206` maxDD `-0.6418`
- `market_context_high->commodity_4h` score `-1.5478` n `142` status `ready` deltaP `0.161` edge `-0.0075` maxDD `-10.0279`
- `market_context_high->equity_4h` score `-1.9489` n `142` status `ready` deltaP `-0.1718` edge `-0.0233` maxDD `-5.7037`
- `market_context_high->metal_4h` score `-2.3825` n `142` status `ready` deltaP `-2.2951` edge `-0.0351` maxDD `-11.4038`
- `market_context_high->crypto_major_4h` score `-2.6178` n `142` status `ready` deltaP `5.1249` edge `0.1208` maxDD `-32.2466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
