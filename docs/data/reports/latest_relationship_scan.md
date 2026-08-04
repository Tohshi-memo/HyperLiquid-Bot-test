# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T13:37:25.071364+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9823`

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

- `market_context_high->unknown_24h` score `36.4407` n `46` status `ready` deltaP `22.6525` edge `2.89` maxDD `-0.0103`
- `market_context_high->commodity_24h` score `8.2219` n `46` status `ready` deltaP `38.2623` edge `0.448` maxDD `-0.434`
- `market_context_high->crypto_alt_24h` score `7.33` n `46` status `ready` deltaP `39.6589` edge `0.3638` maxDD `-0.3889`
- `market_context_high->unknown_4h` score `5.4289` n `88` status `ready` deltaP `0.4434` edge `0.549` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.2254` n `88` status `ready` deltaP `15.2162` edge `0.0853` maxDD `-2.7703`
- `market_context_high->commodity_1h` score `0.2807` n `89` status `ready` deltaP `5.9544` edge `0.0253` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.2519` n `88` status `ready` deltaP `16.408` edge `0.0089` maxDD `-1.8797`
- `market_context_high->fx_1h` score `0.2141` n `89` status `ready` deltaP `8.353` edge `-0.003` maxDD `-0.7878`
- `market_context_high->index_1h` score `-0.4932` n `89` status `ready` deltaP `1.1657` edge `-0.0176` maxDD `-1.6054`
- `market_context_high->metal_1h` score `-0.566` n `89` status `ready` deltaP `-1.8317` edge `-0.0109` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.6487` n `88` status `ready` deltaP `3.8249` edge `0.0148` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.8515` n `88` status `ready` deltaP `4.3237` edge `0.001` maxDD `-5.7857`
- `market_context_high->crypto_alt_1h` score `-1.2285` n `89` status `ready` deltaP `-2.7333` edge `-0.0131` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.7154` n `89` status `ready` deltaP `4.6878` edge `-0.0976` maxDD `-10.619`
- `market_context_high->index_4h` score `-1.9091` n `88` status `ready` deltaP `-10.7262` edge `-0.0478` maxDD `-4.7021`
- `market_context_high->fx_24h` score `-2.1794` n `46` status `ready` deltaP `-9.2618` edge `0.0007` maxDD `-4.3126`
- `market_context_high->unknown_1h` score `-3.4578` n `89` status `ready` deltaP `2.3616` edge `-0.2592` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.6596` n `89` status `ready` deltaP `-13.1451` edge `-0.08` maxDD `-7.6533`
- `market_context_high->metal_24h` score `-5.2638` n `46` status `ready` deltaP `-26.0719` edge `-0.148` maxDD `-2.6802`
- `market_context_high->equity_4h` score `-7.2406` n `88` status `ready` deltaP `-2.7162` edge `-0.3771` maxDD `-35.3129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
