# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T20:52:33.319875+00:00`
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

- `market_context_high->unknown_24h` score `20.9764` n `72` status `ready` deltaP `19.4444` edge `1.6227` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.3651` n `90` status `ready` deltaP `1.5955` edge `0.536` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.4663` n `90` status `ready` deltaP `16.6227` edge `0.096` maxDD `-2.7703`
- `market_context_high->fx_24h` score `0.4531` n `72` status `ready` deltaP `16.8402` edge `0.0664` maxDD `-4.3126`
- `market_context_high->metal_24h` score `0.4479` n `72` status `ready` deltaP `-4.3403` edge `0.2032` maxDD `-2.6802`
- `market_context_high->commodity_1h` score `0.2198` n `90` status `ready` deltaP `5.3426` edge `0.0243` maxDD `-1.3282`
- `market_context_high->crypto_alt_24h` score `0.1576` n `72` status `ready` deltaP `8.1597` edge `0.1062` maxDD `-4.2311`
- `market_context_high->fx_4h` score `0.1377` n `90` status `ready` deltaP `14.3767` edge `0.0078` maxDD `-1.8797`
- `market_context_high->fx_1h` score `0.1362` n `90` status `ready` deltaP `7.4551` edge `-0.0035` maxDD `-0.7878`
- `market_context_high->metal_1h` score `-0.5239` n `90` status `ready` deltaP `-1.3074` edge `-0.009` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.5549` n `90` status `ready` deltaP `0.1431` edge `-0.0187` maxDD `-1.6054`
- `market_context_high->crypto_alt_1h` score `-0.7149` n `90` status `ready` deltaP `-2.159` edge `-0.0062` maxDD `-3.0178`
- `market_context_high->metal_4h` score `-0.7472` n `90` status `ready` deltaP `2.727` edge `0.0095` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.8539` n `90` status `ready` deltaP `4.2479` edge `0.0012` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.6323` n `90` status `ready` deltaP `5.0998` edge `-0.0897` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.0051` n `90` status `ready` deltaP `-11.6734` edge `-0.0538` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.3163` n `72` status `ready` deltaP `-9.8958` edge `-0.0115` maxDD `-7.8922`
- `market_context_high->commodity_24h` score `-3.2413` n `72` status `ready` deltaP `11.1111` edge `-0.0129` maxDD `-29.4718`
- `market_context_high->unknown_1h` score `-3.4` n `90` status `ready` deltaP `2.3486` edge `-0.2543` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.402` n `90` status `ready` deltaP `-11.5602` edge `-0.0691` maxDD `-7.6533`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
