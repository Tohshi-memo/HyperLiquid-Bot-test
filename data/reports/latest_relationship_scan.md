# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T01:22:27.557441+00:00`
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

- `market_context_high->unknown_24h` score `15.4762` n `88` status `ready` deltaP `16.5719` edge `1.1835` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.5825` n `90` status `ready` deltaP `1.7479` edge `0.5531` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.6016` n `90` status `ready` deltaP `17.3849` edge `0.1022` maxDD `-2.7703`
- `market_context_high->metal_24h` score `1.458` n `88` status `ready` deltaP `3.488` edge `0.2805` maxDD `-2.6802`
- `market_context_high->fx_24h` score `1.0773` n `88` status `ready` deltaP `25.9943` edge `0.0854` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.3085` n `90` status `ready` deltaP `5.9414` edge `0.0277` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.1159` n `90` status `ready` deltaP `7.1557` edge `-0.0032` maxDD `-0.7878`
- `market_context_high->fx_4h` score `0.0577` n `90` status `ready` deltaP `13.0048` edge `0.0067` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5332` n `90` status `ready` deltaP `-1.4571` edge `-0.0092` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.6024` n `90` status `ready` deltaP `-0.6054` edge `-0.0198` maxDD `-1.6054`
- `market_context_high->crypto_alt_24h` score `-0.6402` n `88` status `ready` deltaP `7.0392` edge `0.0153` maxDD `-4.5445`
- `market_context_high->metal_4h` score `-0.6871` n `90` status `ready` deltaP `3.6416` edge `0.0111` maxDD `-3.211`
- `market_context_high->crypto_alt_1h` score `-0.7445` n `90` status `ready` deltaP `-2.3087` edge `-0.009` maxDD `-3.0178`
- `market_context_high->crypto_alt_4h` score `-1.1419` n `90` status `ready` deltaP `3.0284` edge `-0.0276` maxDD `-5.7857`
- `market_context_high->index_24h` score `-1.6233` n `88` status `ready` deltaP `-4.94` edge `0.0443` maxDD `-7.8922`
- `market_context_high->equity_1h` score `-1.7453` n `90` status `ready` deltaP `3.9022` edge `-0.0962` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.1322` n `90` status `ready` deltaP `-12.5881` edge `-0.064` maxDD `-4.7021`
- `market_context_high->crypto_major_1h` score `-3.3565` n `90` status `ready` deltaP `-11.1111` edge `-0.0683` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.3952` n `90` status `ready` deltaP `2.0492` edge `-0.2519` maxDD `-1.2421`
- `market_context_high->commodity_24h` score `-7.2616` n `88` status `ready` deltaP `3.8826` edge `-0.1607` maxDD `-49.6923`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
