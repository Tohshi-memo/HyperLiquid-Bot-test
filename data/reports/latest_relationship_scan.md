# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T12:07:33.319825+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9833`

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

- `market_context_high->unknown_24h` score `36.5451` n `46` status `ready` deltaP `22.6525` edge `2.8987` maxDD `-0.0103`
- `market_context_high->commodity_24h` score `8.0102` n `46` status `ready` deltaP `37.2207` edge `0.4373` maxDD `-0.434`
- `market_context_high->crypto_alt_24h` score `7.7145` n `46` status `ready` deltaP `40.7005` edge `0.3889` maxDD `-0.3889`
- `market_context_high->unknown_4h` score `5.4981` n `88` status `ready` deltaP `1.0532` edge `0.5507` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.1846` n `88` status `ready` deltaP `15.2162` edge `0.0819` maxDD `-2.7703`
- `market_context_high->commodity_1h` score `0.2399` n `89` status `ready` deltaP `5.8047` edge `0.0229` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.2385` n `88` status `ready` deltaP `16.2555` edge `0.0082` maxDD `-1.8797`
- `market_context_high->fx_1h` score `0.1626` n `89` status `ready` deltaP `7.7542` edge `-0.0033` maxDD `-0.7878`
- `market_context_high->index_1h` score `-0.4613` n `89` status `ready` deltaP `1.6148` edge `-0.0165` maxDD `-1.6054`
- `market_context_high->metal_1h` score `-0.5293` n `89` status `ready` deltaP `-1.3826` edge `-0.0092` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.6246` n `88` status `ready` deltaP `3.8249` edge `0.0179` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.9309` n `88` status `ready` deltaP `3.5615` edge `-0.0041` maxDD `-5.7857`
- `market_context_high->crypto_alt_1h` score `-1.1961` n `89` status `ready` deltaP `-2.7333` edge `-0.0104` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.5984` n `89` status `ready` deltaP `4.9872` edge `-0.0846` maxDD `-10.619`
- `market_context_high->index_4h` score `-1.9013` n `88` status `ready` deltaP `-10.7262` edge `-0.0468` maxDD `-4.7021`
- `market_context_high->fx_24h` score `-2.0817` n `46` status `ready` deltaP `-8.2201` edge `0.0019` maxDD `-4.3126`
- `market_context_high->unknown_1h` score `-3.5057` n `89` status `ready` deltaP `1.9125` edge `-0.2602` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.6009` n `89` status `ready` deltaP `-12.8457` edge `-0.0771` maxDD `-7.6533`
- `market_context_high->metal_24h` score `-5.0491` n `46` status `ready` deltaP `-25.2038` edge `-0.1359` maxDD `-2.6802`
- `market_context_high->equity_4h` score `-7.0854` n `88` status `ready` deltaP `-1.8016` edge `-0.3633` maxDD `-35.3129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
