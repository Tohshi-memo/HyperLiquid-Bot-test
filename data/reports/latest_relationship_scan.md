# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T07:52:26.313865+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11632`

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

- `market_context_high->unknown_24h` score `14.6111` n `88` status `ready` deltaP `12.058` edge `1.1415` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.5907` n `90` status `ready` deltaP `1.5955` edge `0.5548` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.586` n `90` status `ready` deltaP `17.3849` edge `0.1009` maxDD `-2.7703`
- `market_context_high->fx_24h` score `1.177` n `88` status `ready` deltaP `27.7304` edge `0.0866` maxDD `-4.3126`
- `market_context_high->metal_24h` score `1.0006` n `88` status `ready` deltaP `1.5783` edge `0.2346` maxDD `-2.6802`
- `market_context_high->commodity_1h` score `0.2595` n `92` status `ready` deltaP `5.5845` edge `0.026` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.0727` n `90` status `ready` deltaP `13.1572` edge `0.0076` maxDD `-1.8797`
- `market_context_high->fx_1h` score `0.0005` n `92` status `ready` deltaP `5.8514` edge `-0.004` maxDD `-0.7973`
- `market_context_high->metal_1h` score `-0.475` n `92` status `ready` deltaP `-0.5923` edge `-0.0075` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.6175` n `92` status `ready` deltaP `-0.9242` edge `-0.0196` maxDD `-1.6054`
- `market_context_high->crypto_alt_1h` score `-0.8523` n `92` status `ready` deltaP `-3.1828` edge `-0.017` maxDD `-3.0178`
- `market_context_high->metal_4h` score `-0.8742` n `90` status `ready` deltaP `1.9648` edge `-0.0017` maxDD `-3.211`
- `market_context_high->crypto_alt_24h` score `-1.1521` n `88` status `ready` deltaP `3.0461` edge `-0.0237` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-1.3799` n `90` status `ready` deltaP `1.0467` edge `-0.0449` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.8126` n `92` status `ready` deltaP `3.0136` edge `-0.0989` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.0965` n `90` status `ready` deltaP `-12.7405` edge `-0.0584` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.1287` n `88` status `ready` deltaP `-8.2386` edge `0.0015` maxDD `-7.8922`
- `market_context_high->unknown_1h` score `-3.2931` n `92` status `ready` deltaP `2.8899` edge `-0.249` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.3132` n `92` status `ready` deltaP `-10.7199` edge `-0.0673` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.3202` n `88` status `ready` deltaP `8.3965` edge `-0.0701` maxDD `-49.6923`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
