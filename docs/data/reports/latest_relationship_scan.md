# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T03:07:14.784762+00:00`
- Price records: `672`
- Market context records: `1383`
- Flow alert records: `5895`
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

- `market_context_high->crypto_major_24h` score `13.1582` n `152` status `ready` deltaP `29.5961` edge `1.0124` maxDD `-8.0553`
- `market_context_high->metal_24h` score `11.8407` n `152` status `ready` deltaP `12.8016` edge `1.0681` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.2881` n `152` status `ready` deltaP `28.7555` edge `0.9506` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.0883` n `152` status `ready` deltaP `20.8242` edge `0.3105` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.5552` n `152` status `ready` deltaP `13.9529` edge `0.3526` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.6547` n `180` status `ready` deltaP `8.7127` edge `0.1628` maxDD `-3.6396`
- `market_context_high->index_1h` score `-0.0011` n `192` status `ready` deltaP `4.5472` edge `0.0161` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.0021` n `180` status `ready` deltaP `11.2534` edge `0.0679` maxDD `-6.4478`
- `market_context_high->fx_24h` score `-0.0193` n `152` status `ready` deltaP `9.0003` edge `0.0433` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.0437` n `192` status `ready` deltaP `3.1218` edge `0.0314` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.3694` n `192` status `ready` deltaP `2.7414` edge `-0.0025` maxDD `-0.3914`
- `market_context_high->metal_1h` score `-0.4551` n `192` status `ready` deltaP `5.8539` edge `0.002` maxDD `-3.6165`
- `market_context_high->index_4h` score `-0.5077` n `180` status `ready` deltaP `0.7487` edge `0.0616` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `-0.5439` n `192` status `ready` deltaP `1.6093` edge `0.031` maxDD `-3.6309`
- `market_context_high->commodity_1h` score `-0.8312` n `192` status `ready` deltaP `-1.1976` edge `0.0002` maxDD `-2.252`
- `market_context_high->crypto_alt_4h` score `-1.2486` n `180` status `ready` deltaP `8.0861` edge `0.174` maxDD `-19.5565`
- `market_context_high->crypto_major_1h` score `-1.3223` n `192` status `ready` deltaP `-1.0604` edge `0.0034` maxDD `-6.1883`
- `market_context_high->crypto_major_4h` score `-1.3287` n `180` status `ready` deltaP `4.4343` edge `0.1306` maxDD `-13.3376`
- `market_context_high->fx_4h` score `-1.8728` n `180` status `ready` deltaP `-6.9918` edge `-0.0124` maxDD `-1.4313`
- `market_context_high->unknown_4h` score `-3.2895` n `180` status `ready` deltaP `4.0176` edge `-0.2214` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
