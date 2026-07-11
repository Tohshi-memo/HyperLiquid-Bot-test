# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T06:52:24.972445+00:00`
- Price records: `672`
- Market context records: `6365`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11120`

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

- `news_risk_high->crypto_alt_24h` score `14.6743` n `32` status `ready` deltaP `39.9306` edge `0.9714` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.3076` n `32` status `ready` deltaP `52.4306` edge `0.1761` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.405` n `32` status `ready` deltaP `17.5347` edge `0.5258` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `4.051` n `32` status `ready` deltaP `41.997` edge `0.0622` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.9584` n `32` status `ready` deltaP `34.2014` edge `0.1224` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.35` n `32` status `ready` deltaP `28.2934` edge `0.0211` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.552` n `32` status `ready` deltaP `15.0262` edge `0.1455` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.9307` n `32` status `ready` deltaP `11.6205` edge `0.088` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.5258` n `210` status `ready` deltaP `15.7302` edge `0.0422` maxDD `-2.7056`
- `market_context_high->unknown_1h` score `0.1839` n `220` status `ready` deltaP `-6.7746` edge `0.1613` maxDD `-3.7317`
- `market_context_high->index_4h` score `0.1153` n `210` status `ready` deltaP `8.3014` edge `0.0219` maxDD `-0.4108`
- `news_risk_high->unknown_1h` score `-0.4179` n `32` status `ready` deltaP `5.7822` edge `-0.0389` maxDD `-0.7581`
- `market_context_high->metal_1h` score `-0.4191` n `220` status `ready` deltaP `3.2145` edge `0.0026` maxDD `-1.8877`
- `market_context_high->commodity_24h` score `-0.5239` n `131` status `ready` deltaP `-3.6087` edge `0.1433` maxDD `-6.2457`
- `market_context_high->metal_24h` score `-0.5715` n `131` status `ready` deltaP `15.8967` edge `0.0776` maxDD `-11.8809`
- `market_context_high->index_1h` score `-0.616` n `220` status `ready` deltaP `-1.5024` edge `0.003` maxDD `-0.7564`
- `market_context_high->fx_1h` score `-0.6861` n `220` status `ready` deltaP `-0.343` edge `-0.0015` maxDD `-0.9376`
- `news_risk_high->index_24h` score `-0.7105` n `32` status `ready` deltaP `0.5208` edge `-0.0074` maxDD `-2.3058`
- `news_risk_high->metal_1h` score `-0.7255` n `32` status `ready` deltaP `-2.6946` edge `-0.0253` maxDD `-1.6464`
- `market_context_high->crypto_alt_1h` score `-0.9584` n `220` status `ready` deltaP `5.4273` edge `0.0162` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
