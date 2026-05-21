# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T02:37:15.096550+00:00`
- Price records: `672`
- Market context records: `1381`
- Flow alert records: `5889`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8804`

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

- `market_context_high->crypto_major_24h` score `13.3996` n `152` status `ready` deltaP `29.9433` edge `1.0302` maxDD `-8.0553`
- `market_context_high->metal_24h` score `11.9501` n `152` status `ready` deltaP `13.1488` edge `1.0749` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.4033` n `152` status `ready` deltaP `28.7555` edge `0.9602` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.2073` n `152` status `ready` deltaP `21.1714` edge `0.3181` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.7138` n `152` status `ready` deltaP `14.3001` edge `0.3635` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.6366` n `178` status `ready` deltaP `8.7867` edge `0.1608` maxDD `-3.6396`
- `market_context_high->metal_4h` score `0.0515` n `178` status `ready` deltaP `11.6538` edge `0.0697` maxDD `-6.4478`
- `market_context_high->index_1h` score `-0.0157` n `190` status `ready` deltaP `4.3351` edge `0.0163` maxDD `-1.7205`
- `market_context_high->fx_24h` score `-0.0265` n `152` status `ready` deltaP `9.0003` edge `0.0427` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.0362` n `190` status `ready` deltaP `3.0649` edge `0.0324` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.3535` n `190` status `ready` deltaP `2.9404` edge `-0.0025` maxDD `-0.3914`
- `market_context_high->index_4h` score `-0.5257` n `178` status `ready` deltaP `0.7039` edge `0.0604` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `-0.5831` n `190` status `ready` deltaP `1.1488` edge `0.0308` maxDD `-3.6309`
- `market_context_high->metal_1h` score `-0.6064` n `190` status `ready` deltaP `6.185` edge `0.0071` maxDD `-3.5762`
- `market_context_high->commodity_1h` score `-0.8446` n `190` status `ready` deltaP `-1.4245` edge `0.0006` maxDD `-2.252`
- `market_context_high->crypto_alt_4h` score `-1.3032` n `178` status `ready` deltaP `8.0039` edge `0.17` maxDD `-19.5565`
- `market_context_high->crypto_major_1h` score `-1.3722` n `190` status `ready` deltaP `-1.5648` edge `0.0026` maxDD `-6.1883`
- `market_context_high->crypto_major_4h` score `-1.4002` n `178` status `ready` deltaP `4.246` edge `0.1259` maxDD `-13.3376`
- `market_context_high->fx_4h` score `-1.9024` n `178` status `ready` deltaP `-7.2863` edge `-0.0129` maxDD `-1.4313`
- `market_context_high->unknown_4h` score `-3.2525` n `178` status `ready` deltaP `3.7544` edge `-0.2149` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
