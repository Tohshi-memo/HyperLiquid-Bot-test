# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T09:37:24.803370+00:00`
- Price records: `672`
- Market context records: `2751`
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

- `market_context_high->unknown_24h` score `6.9809` n `121` status `ready` deltaP `14.7842` edge `0.516` maxDD `-1.6255`
- `market_context_high->crypto_alt_24h` score `5.1311` n `121` status `ready` deltaP `10.7682` edge `0.9354` maxDD `-19.9486`
- `market_context_high->unknown_4h` score `0.8833` n `143` status `ready` deltaP `6.0965` edge `0.1383` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.1823` n `143` status `ready` deltaP `11.3136` edge `0.0321` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.1448` n `143` status `ready` deltaP `3.3479` edge `0.0387` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.155` n `143` status `ready` deltaP `3.2003` edge `0.0082` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.547` n `143` status `ready` deltaP `-0.6469` edge `0.0031` maxDD `-0.2164`
- `market_context_high->crypto_alt_1h` score `-0.6438` n `143` status `ready` deltaP `5.9954` edge `0.0535` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.6936` n `143` status `ready` deltaP `-0.3518` edge `-0.002` maxDD `-3.0996`
- `market_context_high->commodity_1h` score `-0.708` n `143` status `ready` deltaP `-0.8458` edge `-0.0098` maxDD `-4.3601`
- `market_context_high->commodity_24h` score `-0.8239` n `121` status `ready` deltaP `5.7822` edge `0.1652` maxDD `-12.4171`
- `market_context_high->crypto_major_1h` score `-0.9269` n `143` status `ready` deltaP `3.9467` edge `0.0418` maxDD `-9.622`
- `market_context_high->crypto_alt_4h` score `-1.0736` n `143` status `ready` deltaP `15.6011` edge `0.2406` maxDD `-28.7261`
- `market_context_high->equity_1h` score `-1.1812` n `143` status `ready` deltaP `-3.9361` edge `0.0111` maxDD `-2.6634`
- `market_context_high->fx_4h` score `-1.2149` n `143` status `ready` deltaP `-4.5551` edge `0.007` maxDD `-0.5631`
- `market_context_high->fx_24h` score `-1.2373` n `121` status `ready` deltaP `0.2066` edge `-0.0173` maxDD `-0.6418`
- `market_context_high->commodity_4h` score `-1.6822` n `143` status `ready` deltaP `-0.7728` edge `-0.0185` maxDD `-10.0279`
- `market_context_high->equity_4h` score `-1.9627` n `143` status `ready` deltaP `-0.9444` edge `-0.0193` maxDD `-5.7037`
- `market_context_high->metal_4h` score `-2.3784` n `143` status `ready` deltaP `-2.1864` edge `-0.0353` maxDD `-11.4038`
- `market_context_high->crypto_major_4h` score `-2.469` n `143` status `ready` deltaP `6.1424` edge `0.1331` maxDD `-32.2466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
