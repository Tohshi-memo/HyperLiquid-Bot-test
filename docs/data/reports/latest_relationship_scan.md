# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T06:07:13.692019+00:00`
- Price records: `672`
- Market context records: `1090`
- Flow alert records: `5043`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8686`

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

- `market_context_high->crypto_major_24h` score `16.5343` n `153` status `ready` deltaP `35.7618` edge `1.1858` maxDD `-3.3749`
- `market_context_high->equity_24h` score `5.744` n `153` status `ready` deltaP `14.8997` edge `0.429` maxDD `-3.6396`
- `market_context_high->crypto_alt_24h` score `5.733` n `153` status `ready` deltaP `12.2774` edge `0.5193` maxDD `-9.5387`
- `market_context_high->metal_24h` score `4.8923` n `153` status `ready` deltaP `-2.984` edge `0.5943` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.6865` n `153` status `ready` deltaP `15.0361` edge `0.3211` maxDD `-2.1308`
- `market_context_high->equity_4h` score `2.0989` n `163` status `ready` deltaP `11.5106` edge `0.1645` maxDD `-3.6396`
- `market_context_high->index_4h` score `1.0697` n `163` status `ready` deltaP `9.2015` edge `0.0961` maxDD `-2.1308`
- `market_context_high->crypto_major_4h` score `0.9407` n `163` status `ready` deltaP `10.9036` edge `0.1743` maxDD `-6.4882`
- `market_context_high->index_1h` score `0.6289` n `171` status `ready` deltaP `8.5644` edge `0.027` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.4806` n `171` status `ready` deltaP `3.4229` edge `0.055` maxDD `-1.3546`
- `market_context_high->crypto_major_1h` score `0.1738` n `171` status `ready` deltaP `7.4036` edge `0.0417` maxDD `-4.1256`
- `market_context_high->fx_1h` score `0.0372` n `171` status `ready` deltaP `7.0902` edge `0.0014` maxDD `-0.3124`
- `market_context_high->metal_1h` score `-0.1348` n `171` status `ready` deltaP `7.1559` edge `0.0021` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.272` n `171` status `ready` deltaP `2.7769` edge `0.0431` maxDD `-3.4088`
- `market_context_high->crypto_alt_4h` score `-0.502` n `163` status `ready` deltaP `7.2899` edge `0.16` maxDD `-13.0347`
- `market_context_high->fx_4h` score `-0.5962` n `163` status `ready` deltaP `3.0918` edge `0.0026` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.686` n `171` status `ready` deltaP `-0.9849` edge `-0.0006` maxDD `-3.7959`
- `market_context_high->metal_4h` score `-1.6504` n `163` status `ready` deltaP `6.1967` edge `-0.0575` maxDD `-9.2991`
- `market_context_high->unknown_4h` score `-2.1974` n `163` status `ready` deltaP `9.2156` edge `-0.1229` maxDD `-6.7322`
- `market_context_high->commodity_4h` score `-3.0389` n `163` status `ready` deltaP `-10.4762` edge `-0.003` maxDD `-13.0076`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
