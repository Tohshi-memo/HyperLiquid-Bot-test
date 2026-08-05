# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T03:52:28.110019+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11824`

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

- `market_context_high->unknown_24h` score `15.1477` n `88` status `ready` deltaP `14.8358` edge `1.1677` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.6819` n `90` status `ready` deltaP `2.5101` edge `0.5563` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.5483` n `90` status `ready` deltaP `16.9276` edge `0.1008` maxDD `-2.7703`
- `market_context_high->metal_24h` score `1.3612` n `88` status `ready` deltaP `3.488` edge `0.2681` maxDD `-2.6802`
- `market_context_high->fx_24h` score `1.115` n `88` status `ready` deltaP `26.6887` edge `0.0856` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.3181` n `90` status `ready` deltaP `5.9414` edge `0.0285` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.1255` n `90` status `ready` deltaP `7.3054` edge `-0.0034` maxDD `-0.7878`
- `market_context_high->fx_4h` score `0.0593` n `90` status `ready` deltaP `13.0048` edge `0.0069` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5846` n `90` status `ready` deltaP `-2.0559` edge `-0.0118` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.6702` n `90` status `ready` deltaP `-1.5036` edge `-0.0225` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.724` n `90` status `ready` deltaP `3.3367` edge `0.0084` maxDD `-3.211`
- `market_context_high->crypto_alt_24h` score `-0.8709` n `88` status `ready` deltaP `5.3031` edge `-0.0027` maxDD `-4.5445`
- `market_context_high->crypto_alt_1h` score `-0.8832` n `90` status `ready` deltaP `-3.3566` edge `-0.0198` maxDD `-3.0178`
- `market_context_high->crypto_alt_4h` score `-1.3114` n `90` status `ready` deltaP `1.8089` edge `-0.0412` maxDD `-5.7857`
- `market_context_high->index_24h` score `-1.8211` n `88` status `ready` deltaP `-6.3289` edge `0.0282` maxDD `-7.8922`
- `market_context_high->equity_1h` score `-1.9098` n `90` status `ready` deltaP `2.7046` edge `-0.1093` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.1797` n `90` status `ready` deltaP `-13.3502` edge `-0.065` maxDD `-4.7021`
- `market_context_high->unknown_1h` score `-3.3016` n `90` status `ready` deltaP `2.0492` edge `-0.2441` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.4356` n `90` status `ready` deltaP `-11.4105` edge `-0.0729` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.9209` n `88` status `ready` deltaP `5.6187` edge `-0.1286` maxDD `-49.6923`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
