# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T00:52:32.797592+00:00`
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

- `market_context_high->unknown_24h` score `15.546` n `88` status `ready` deltaP `16.9192` edge `1.187` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.5657` n `90` status `ready` deltaP `1.7479` edge `0.5517` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.6344` n `90` status `ready` deltaP `17.6897` edge `0.1029` maxDD `-2.7703`
- `market_context_high->metal_24h` score `1.472` n `88` status `ready` deltaP `3.488` edge `0.2823` maxDD `-2.6802`
- `market_context_high->fx_24h` score `1.0895` n `88` status `ready` deltaP `26.1679` edge `0.0858` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.3121` n `90` status `ready` deltaP `5.9414` edge `0.028` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.1147` n `90` status `ready` deltaP `7.1557` edge `-0.0033` maxDD `-0.7878`
- `market_context_high->fx_4h` score `0.0593` n `90` status `ready` deltaP `13.0048` edge `0.0069` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.541` n `90` status `ready` deltaP `-1.6068` edge `-0.0092` maxDD `-1.6224`
- `market_context_high->crypto_alt_24h` score `-0.5559` n `88` status `ready` deltaP `7.3864` edge `0.0238` maxDD `-4.5445`
- `market_context_high->index_1h` score `-0.5954` n `90` status `ready` deltaP `-0.6054` edge `-0.0189` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.6958` n `90` status `ready` deltaP `3.4891` edge `0.011` maxDD `-3.211`
- `market_context_high->crypto_alt_1h` score `-0.7086` n `90` status `ready` deltaP `-2.0093` edge `-0.0064` maxDD `-3.0178`
- `market_context_high->crypto_alt_4h` score `-1.106` n `90` status `ready` deltaP `3.0284` edge `-0.023` maxDD `-5.7857`
- `market_context_high->index_24h` score `-1.5647` n `88` status `ready` deltaP `-4.5928` edge `0.0495` maxDD `-7.8922`
- `market_context_high->equity_1h` score `-1.7157` n `90` status `ready` deltaP `3.9022` edge `-0.0924` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.1` n `90` status `ready` deltaP `-12.2832` edge `-0.0619` maxDD `-4.7021`
- `market_context_high->crypto_major_1h` score `-3.3241` n `90` status `ready` deltaP `-10.9614` edge `-0.0666` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.4096` n `90` status `ready` deltaP `2.0492` edge `-0.2531` maxDD `-1.2421`
- `market_context_high->commodity_24h` score `-7.3272` n `88` status `ready` deltaP `3.5353` edge `-0.1668` maxDD `-49.6923`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
