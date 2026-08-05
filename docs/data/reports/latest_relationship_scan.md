# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T05:07:36.206981+00:00`
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

- `market_context_high->unknown_24h` score `14.9883` n `88` status `ready` deltaP `13.9678` edge `1.1602` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.74` n `90` status `ready` deltaP `2.9674` edge `0.5581` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.5447` n `90` status `ready` deltaP `16.9276` edge `0.1005` maxDD `-2.7703`
- `market_context_high->metal_24h` score `1.3012` n `88` status `ready` deltaP `3.488` edge `0.2604` maxDD `-2.6802`
- `market_context_high->fx_24h` score `1.146` n `88` status `ready` deltaP `27.2096` edge `0.0861` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.2558` n `90` status `ready` deltaP `5.3426` edge `0.0273` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0847` n `90` status `ready` deltaP `6.8563` edge `-0.0038` maxDD `-0.7878`
- `market_context_high->fx_4h` score `0.0711` n `90` status `ready` deltaP `13.1572` edge `0.0074` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5566` n `90` status `ready` deltaP `-1.6068` edge `-0.0112` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.6562` n `90` status `ready` deltaP `-1.3539` edge `-0.0217` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.7365` n `90` status `ready` deltaP `3.3367` edge `0.0068` maxDD `-3.211`
- `market_context_high->crypto_alt_1h` score `-0.863` n `90` status `ready` deltaP `-3.2069` edge `-0.0182` maxDD `-3.0178`
- `market_context_high->crypto_alt_24h` score `-0.8983` n `88` status `ready` deltaP `4.9558` edge `-0.0039` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-1.3114` n `90` status `ready` deltaP `1.8089` edge `-0.0412` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.8739` n `90` status `ready` deltaP `2.5549` edge `-0.1037` maxDD `-10.619`
- `market_context_high->index_24h` score `-1.875` n `88` status `ready` deltaP `-6.3289` edge `0.0213` maxDD `-7.8922`
- `market_context_high->index_4h` score `-2.1389` n `90` status `ready` deltaP `-13.0454` edge `-0.0618` maxDD `-4.7021`
- `market_context_high->unknown_1h` score `-3.3148` n `90` status `ready` deltaP `2.0492` edge `-0.2452` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.3733` n `90` status `ready` deltaP `-11.1111` edge `-0.0697` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.7432` n `88` status `ready` deltaP `6.4867` edge `-0.1116` maxDD `-49.6923`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
