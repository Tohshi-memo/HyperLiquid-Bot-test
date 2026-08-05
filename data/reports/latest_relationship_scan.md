# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T05:22:30.032599+00:00`
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

- `market_context_high->unknown_24h` score `14.954` n `88` status `ready` deltaP `13.7942` edge `1.1585` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.74` n `90` status `ready` deltaP `2.9674` edge `0.5581` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.5605` n `90` status `ready` deltaP `17.08` edge `0.1008` maxDD `-2.7703`
- `market_context_high->metal_24h` score `1.2773` n `88` status `ready` deltaP `3.3144` edge `0.2585` maxDD `-2.6802`
- `market_context_high->fx_24h` score `1.146` n `88` status `ready` deltaP `27.2096` edge `0.0861` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.2582` n `90` status `ready` deltaP `5.3426` edge `0.0275` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0847` n `90` status `ready` deltaP `6.8563` edge `-0.0038` maxDD `-0.7878`
- `market_context_high->fx_4h` score `0.0719` n `90` status `ready` deltaP `13.1572` edge `0.0075` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5473` n `90` status `ready` deltaP `-1.4571` edge `-0.011` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.657` n `90` status `ready` deltaP `-1.3539` edge `-0.0218` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.7412` n `90` status `ready` deltaP `3.3367` edge `0.0062` maxDD `-3.211`
- `market_context_high->crypto_alt_1h` score `-0.8653` n `90` status `ready` deltaP `-3.2069` edge `-0.0185` maxDD `-3.0178`
- `market_context_high->crypto_alt_24h` score `-0.9214` n `88` status `ready` deltaP `4.7822` edge `-0.0057` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-1.3145` n `90` status `ready` deltaP `1.8089` edge `-0.0416` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.8793` n `90` status `ready` deltaP `2.5549` edge `-0.1044` maxDD `-10.619`
- `market_context_high->index_24h` score `-1.898` n `88` status `ready` deltaP `-6.5025` edge `0.0195` maxDD `-7.8922`
- `market_context_high->index_4h` score `-2.1357` n `90` status `ready` deltaP `-13.0454` edge `-0.0614` maxDD `-4.7021`
- `market_context_high->unknown_1h` score `-3.3004` n `90` status `ready` deltaP `2.1989` edge `-0.245` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.3793` n `90` status `ready` deltaP `-11.1111` edge `-0.0702` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.7053` n `88` status `ready` deltaP `6.6603` edge `-0.1079` maxDD `-49.6923`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
