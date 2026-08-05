# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T01:37:28.784072+00:00`
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

- `market_context_high->unknown_24h` score `15.4455` n `88` status `ready` deltaP `16.3983` edge `1.1821` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.6007` n `90` status `ready` deltaP `1.9004` edge `0.5536` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.5822` n `90` status `ready` deltaP `17.2324` edge `0.1016` maxDD `-2.7703`
- `market_context_high->metal_24h` score `1.4533` n `88` status `ready` deltaP `3.488` edge `0.2799` maxDD `-2.6802`
- `market_context_high->fx_24h` score `1.0766` n `88` status `ready` deltaP `25.9943` edge `0.0853` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.2929` n `90` status `ready` deltaP `5.7917` edge `0.0274` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.1159` n `90` status `ready` deltaP `7.1557` edge `-0.0032` maxDD `-0.7878`
- `market_context_high->fx_4h` score `0.057` n `90` status `ready` deltaP `13.0048` edge `0.0066` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5231` n `90` status `ready` deltaP `-1.3074` edge `-0.0089` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.6048` n `90` status `ready` deltaP `-0.6054` edge `-0.0201` maxDD `-1.6054`
- `market_context_high->crypto_alt_24h` score `-0.675` n `88` status `ready` deltaP `6.8656` edge `0.012` maxDD `-4.5445`
- `market_context_high->metal_4h` score `-0.6784` n `90` status `ready` deltaP `3.794` edge `0.0112` maxDD `-3.211`
- `market_context_high->crypto_alt_1h` score `-0.7616` n `90` status `ready` deltaP `-2.4584` edge `-0.0102` maxDD `-3.0178`
- `market_context_high->crypto_alt_4h` score `-1.1662` n `90` status `ready` deltaP `2.876` edge `-0.0297` maxDD `-5.7857`
- `market_context_high->index_24h` score `-1.6487` n `88` status `ready` deltaP `-5.1136` edge `0.0422` maxDD `-7.8922`
- `market_context_high->equity_1h` score `-1.7515` n `90` status `ready` deltaP `3.9022` edge `-0.097` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.1456` n `90` status `ready` deltaP `-12.7405` edge `-0.0647` maxDD `-4.7021`
- `market_context_high->unknown_1h` score `-3.3364` n `90` status `ready` deltaP `2.1989` edge `-0.248` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.3745` n `90` status `ready` deltaP `-11.2608` edge `-0.0688` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-7.2299` n `88` status `ready` deltaP `4.0562` edge `-0.1578` maxDD `-49.6923`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
