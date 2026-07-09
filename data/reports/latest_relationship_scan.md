# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T15:22:42.860183+00:00`
- Price records: `672`
- Market context records: `6193`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11110`

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

- `news_risk_high->crypto_alt_24h` score `12.7022` n `32` status `ready` deltaP `42.2194` edge `0.7918` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.8851` n `32` status `ready` deltaP `60.2041` edge `0.1724` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.0715` n `32` status `ready` deltaP `42.4487` edge `0.0609` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3608` n `32` status `ready` deltaP `28.4431` edge `0.021` maxDD `-0.1113`
- `news_risk_high->crypto_major_24h` score `2.1084` n `32` status `ready` deltaP `15.625` edge `0.2441` maxDD `-4.2368`
- `market_context_high->unknown_1h` score `1.8249` n `192` status `ready` deltaP `1.0635` edge `0.2458` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.3984` n `32` status `ready` deltaP `14.4274` edge `0.1298` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.7421` n `32` status `ready` deltaP `9.375` edge `0.0788` maxDD `-1.6923`
- `market_context_high->unknown_4h` score `0.3297` n `192` status `ready` deltaP `-2.1293` edge `0.2949` maxDD `-11.925`
- `news_risk_high->commodity_24h` score `0.1429` n `32` status `ready` deltaP `16.6879` edge `-0.0788` maxDD `-0.3101`
- `market_context_high->metal_24h` score `0.0661` n `192` status `ready` deltaP `19.8023` edge `0.1333` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.1704` n `32` status `ready` deltaP `9.4813` edge `0.0021` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.2824` n `192` status `ready` deltaP `1.3598` edge `-0.0007` maxDD `-0.5659`
- `market_context_high->equity_4h` score `-0.4249` n `192` status `ready` deltaP `1.4723` edge `0.0465` maxDD `-2.671`
- `market_context_high->metal_4h` score `-0.648` n `192` status `ready` deltaP `3.5351` edge `0.0121` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.7452` n `192` status `ready` deltaP `-2.3952` edge `-0.0015` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.8135` n `32` status `ready` deltaP `-3.8922` edge `-0.0286` maxDD `-1.6464`
- `market_context_high->crypto_major_1h` score `-0.9012` n `192` status `ready` deltaP `4.5316` edge `0.031` maxDD `-9.807`
- `market_context_high->metal_1h` score `-0.9108` n `192` status `ready` deltaP `1.3161` edge `-0.0048` maxDD `-2.0564`
- `market_context_high->crypto_alt_1h` score `-0.9216` n `192` status `ready` deltaP `3.6458` edge `0.0328` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
