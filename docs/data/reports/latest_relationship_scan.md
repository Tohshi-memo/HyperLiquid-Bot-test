# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T19:52:34.767243+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9856`

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

- `market_context_high->unknown_24h` score `22.673` n `68` status `ready` deltaP `20.0572` edge `1.76` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.3385` n `90` status `ready` deltaP `1.4431` edge `0.5348` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.3635` n `90` status `ready` deltaP `16.0129` edge `0.0915` maxDD `-2.7703`
- `market_context_high->crypto_alt_24h` score `0.5563` n `68` status `ready` deltaP `10.5392` edge `0.1371` maxDD `-3.8833`
- `market_context_high->fx_24h` score `0.2325` n `68` status `ready` deltaP `13.8277` edge `0.0582` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.1719` n `90` status `ready` deltaP `4.8935` edge `0.0233` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.1479` n `90` status `ready` deltaP `14.5291` edge `0.0081` maxDD `-1.8797`
- `market_context_high->fx_1h` score `0.1243` n `90` status `ready` deltaP `7.3054` edge `-0.0035` maxDD `-0.7878`
- `market_context_high->metal_24h` score `0.115` n `68` status `ready` deltaP `-6.8729` edge `0.1774` maxDD `-2.6802`
- `market_context_high->metal_1h` score `-0.5418` n `90` status `ready` deltaP `-1.6068` edge `-0.0093` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.5822` n `90` status `ready` deltaP `-0.306` edge `-0.0192` maxDD `-1.6054`
- `market_context_high->crypto_alt_1h` score `-0.7359` n `90` status `ready` deltaP `-2.4584` edge `-0.0069` maxDD `-3.0178`
- `market_context_high->metal_4h` score `-0.7772` n `90` status `ready` deltaP `2.2696` edge `0.0087` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.8414` n `90` status `ready` deltaP `4.2479` edge `0.0028` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.7087` n `90` status `ready` deltaP `4.501` edge `-0.0955` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.009` n `90` status `ready` deltaP `-11.6734` edge `-0.0543` maxDD `-4.7021`
- `market_context_high->commodity_24h` score `-2.1223` n `68` status `ready` deltaP `13.7663` edge `0.0351` maxDD `-24.5839`
- `market_context_high->index_24h` score `-2.5963` n `68` status `ready` deltaP `-11.8157` edge `-0.0346` maxDD `-7.8922`
- `market_context_high->unknown_1h` score `-3.4025` n `90` status `ready` deltaP `2.4983` edge `-0.2555` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.42` n `90` status `ready` deltaP `-11.7099` edge `-0.0696` maxDD `-7.6533`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
