# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T20:22:18.040005+00:00`
- Price records: `672`
- Market context records: `2492`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9248`

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

- `market_context_high->unknown_24h` score `5.4859` n `124` status `ready` deltaP `19.8869` edge `0.3574` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `3.9878` n `141` status `ready` deltaP `20.8226` edge `0.4614` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.5167` n `141` status `ready` deltaP `16.6137` edge `0.3633` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `2.0627` n `124` status `ready` deltaP `11.9119` edge `0.5743` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `1.2533` n `141` status `ready` deltaP `9.0772` edge `0.1489` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `0.5282` n `153` status `ready` deltaP `6.8774` edge `0.1169` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.388` n `153` status `ready` deltaP `6.7277` edge `0.1069` maxDD `-4.2199`
- `market_context_high->crypto_alt_24h` score `0.1427` n `124` status `ready` deltaP `1.9713` edge `0.7009` maxDD `-43.6595`
- `market_context_high->index_24h` score `0.0904` n `124` status `ready` deltaP `4.3514` edge `0.0766` maxDD `-2.5127`
- `market_context_high->equity_24h` score `-0.1509` n `124` status `ready` deltaP `18.4084` edge `0.0174` maxDD `-6.8828`
- `market_context_high->index_4h` score `-0.1621` n `141` status `ready` deltaP `6.0554` edge `0.023` maxDD `-2.3986`
- `market_context_high->fx_1h` score `-0.3645` n `153` status `ready` deltaP `0.3816` edge `0.0042` maxDD `-0.278`
- `market_context_high->unknown_1h` score `-0.5177` n `153` status `ready` deltaP `2.043` edge `0.0152` maxDD `-3.0902`
- `market_context_high->commodity_1h` score `-0.5288` n `153` status `ready` deltaP `3.0508` edge `-0.0003` maxDD `-4.3601`
- `market_context_high->index_1h` score `-0.5586` n `153` status `ready` deltaP `-0.3375` edge `0.0051` maxDD `-1.2855`
- `market_context_high->fx_4h` score `-0.5755` n `141` status `ready` deltaP `0.507` edge `0.0088` maxDD `-0.8774`
- `market_context_high->metal_1h` score `-0.8012` n `153` status `ready` deltaP `0.4618` edge `0.0061` maxDD `-3.0759`
- `market_context_high->equity_1h` score `-0.8638` n `153` status `ready` deltaP `-0.0342` edge `0.0121` maxDD `-2.7085`
- `market_context_high->fx_24h` score `-0.9042` n `124` status `ready` deltaP `2.8506` edge `0.0036` maxDD `-2.7484`
- `market_context_high->metal_4h` score `-1.1044` n `141` status `ready` deltaP `1.892` edge `0.0341` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
