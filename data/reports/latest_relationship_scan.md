# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T03:22:31.321779+00:00`
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

- `market_context_high->unknown_24h` score `15.2139` n `88` status `ready` deltaP `15.183` edge `1.1709` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.6467` n `90` status `ready` deltaP `2.2053` edge `0.5554` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.5495` n `90` status `ready` deltaP `16.9276` edge `0.1009` maxDD `-2.7703`
- `market_context_high->metal_24h` score `1.387` n `88` status `ready` deltaP `3.488` edge `0.2714` maxDD `-2.6802`
- `market_context_high->fx_24h` score `1.0962` n `88` status `ready` deltaP `26.3415` edge `0.0855` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.3444` n `90` status `ready` deltaP `6.2408` edge `0.0287` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.141` n `90` status `ready` deltaP `7.4551` edge `-0.0031` maxDD `-0.7878`
- `market_context_high->fx_4h` score `0.0585` n `90` status `ready` deltaP `13.0048` edge `0.0068` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5753` n `90` status `ready` deltaP `-1.9062` edge `-0.0116` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.65` n `90` status `ready` deltaP `-1.2042` edge `-0.0219` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.7186` n `90` status `ready` deltaP `3.3367` edge `0.0091` maxDD `-3.211`
- `market_context_high->crypto_alt_24h` score `-0.8365` n `88` status `ready` deltaP `5.6503` edge `-0.0006` maxDD `-4.5445`
- `market_context_high->crypto_alt_1h` score `-0.8723` n `90` status `ready` deltaP `-3.3566` edge `-0.0184` maxDD `-3.0178`
- `market_context_high->crypto_alt_4h` score `-1.2933` n `90` status `ready` deltaP `1.9613` edge `-0.0399` maxDD `-5.7857`
- `market_context_high->index_24h` score `-1.7773` n `88` status `ready` deltaP `-5.9817` edge `0.0315` maxDD `-7.8922`
- `market_context_high->equity_1h` score `-1.8677` n `90` status `ready` deltaP `3.004` edge `-0.1059` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.1851` n `90` status `ready` deltaP `-13.3502` edge `-0.0657` maxDD `-4.7021`
- `market_context_high->unknown_1h` score `-3.2512` n `90` status `ready` deltaP `2.3486` edge `-0.2419` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.4608` n `90` status `ready` deltaP `-11.5602` edge `-0.074` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.9904` n `88` status `ready` deltaP `5.2715` edge `-0.1352` maxDD `-49.6923`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
