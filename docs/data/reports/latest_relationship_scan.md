# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T06:52:34.436897+00:00`
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

- `market_context_high->unknown_24h` score `14.7387` n `88` status `ready` deltaP `12.7525` edge `1.1475` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.6563` n `90` status `ready` deltaP `2.2053` edge `0.5562` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.592` n `90` status `ready` deltaP `17.3849` edge `0.1014` maxDD `-2.7703`
- `market_context_high->fx_24h` score `1.186` n `88` status `ready` deltaP `27.904` edge `0.0866` maxDD `-4.3126`
- `market_context_high->metal_24h` score `1.1116` n `88` status `ready` deltaP `2.2727` edge `0.2442` maxDD `-2.6802`
- `market_context_high->commodity_1h` score `0.3087` n `92` status `ready` deltaP `6.0336` edge `0.0271` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.0735` n `90` status `ready` deltaP `13.1572` edge `0.0077` maxDD `-1.8797`
- `market_context_high->fx_1h` score `-0.0007` n `92` status `ready` deltaP `5.8514` edge `-0.0041` maxDD `-0.7973`
- `market_context_high->metal_1h` score `-0.4633` n `92` status `ready` deltaP `-0.4426` edge `-0.007` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.626` n `92` status `ready` deltaP `-1.0739` edge `-0.0197` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.8183` n `90` status `ready` deltaP `2.5745` edge `0.0014` maxDD `-3.211`
- `market_context_high->crypto_alt_1h` score `-0.8578` n `92` status `ready` deltaP `-3.1828` edge `-0.0177` maxDD `-3.0178`
- `market_context_high->crypto_alt_24h` score `-1.0567` n `88` status `ready` deltaP `3.7406` edge `-0.0161` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-1.3279` n `90` status `ready` deltaP `1.6565` edge `-0.0423` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.8352` n `92` status `ready` deltaP `2.7142` edge `-0.0998` maxDD `-10.619`
- `market_context_high->index_24h` score `-2.0286` n `88` status `ready` deltaP `-7.5442` edge `0.0097` maxDD `-7.8922`
- `market_context_high->index_4h` score `-2.1162` n `90` status `ready` deltaP `-13.0454` edge `-0.0589` maxDD `-4.7021`
- `market_context_high->unknown_1h` score `-3.2787` n `92` status `ready` deltaP `3.0396` edge `-0.2488` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.3228` n `92` status `ready` deltaP `-10.7199` edge `-0.0681` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.467` n `88` status `ready` deltaP `7.702` edge `-0.0843` maxDD `-49.6923`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
