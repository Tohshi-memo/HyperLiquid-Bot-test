# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T11:37:32.398432+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11781`

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

- `market_context_high->unknown_24h` score `8.4913` n `98` status `ready` deltaP `3.8407` edge `0.6863` maxDD `-0.0104`
- `market_context_high->metal_24h` score `1.4944` n `98` status `ready` deltaP `4.8256` edge `0.2092` maxDD `-2.6802`
- `market_context_high->commodity_4h` score `1.0152` n `109` status `ready` deltaP `12.3798` edge `0.0867` maxDD `-2.7703`
- `market_context_high->fx_24h` score `0.4899` n `98` status `ready` deltaP `20.5321` edge `0.0465` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.3582` n `112` status `ready` deltaP `7.1482` edge `0.0238` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0825` n `112` status `ready` deltaP `6.6884` edge `-0.0027` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.3166` n `109` status `ready` deltaP `6.5703` edge `0.0016` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5844` n `112` status `ready` deltaP `-2.5609` edge `-0.0084` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.7493` n `109` status `ready` deltaP `3.2418` edge `0.0058` maxDD `-3.211`
- `market_context_high->index_1h` score `-1.1587` n `112` status `ready` deltaP `-3.6088` edge `-0.0191` maxDD `-1.6054`
- `market_context_high->index_24h` score `-1.3037` n `98` status `ready` deltaP `-4.358` edge `0.0814` maxDD `-7.8922`
- `market_context_high->crypto_alt_1h` score `-1.3935` n `112` status `ready` deltaP `-4.1809` edge `-0.0172` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.8001` n `112` status `ready` deltaP `1.5879` edge `-0.0849` maxDD `-10.5179`
- `market_context_high->index_4h` score `-1.9052` n `109` status `ready` deltaP `-10.3813` edge `-0.0496` maxDD `-4.7021`
- `market_context_high->crypto_alt_4h` score `-1.9857` n `109` status `ready` deltaP `2.1467` edge `-0.0408` maxDD `-5.7857`
- `market_context_high->crypto_alt_24h` score `-2.4114` n `98` status `ready` deltaP `-2.7069` edge `-0.0386` maxDD `-4.5445`
- `market_context_high->crypto_major_1h` score `-3.0889` n `112` status `ready` deltaP `-9.8214` edge `-0.0546` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.757` n `98` status `ready` deltaP `5.8992` edge `-0.0291` maxDD `-52.7876`
- `market_context_high->equity_4h` score `-7.0201` n `109` status `ready` deltaP `-2.2712` edge `-0.356` maxDD `-34.9766`
- `market_context_high->crypto_major_24h` score `-7.619` n `98` status `ready` deltaP `-7.4653` edge `-0.2539` maxDD `-40.8499`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
