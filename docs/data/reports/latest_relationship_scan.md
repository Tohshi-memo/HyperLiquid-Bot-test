# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T09:07:28.821579+00:00`
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

- `market_context_high->unknown_24h` score `11.3682` n `94` status `ready` deltaP `4.4918` edge `0.9217` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `4.1152` n `109` status `ready` deltaP `-0.8881` edge `0.4484` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.0978` n `109` status `ready` deltaP `13.142` edge `0.0885` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.9263` n `94` status `ready` deltaP `3.4796` edge `0.2124` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.55` n `94` status `ready` deltaP `21.3136` edge `0.049` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4203` n `109` status `ready` deltaP `7.7597` edge `0.0249` maxDD `-1.3282`
- `market_context_high->fx_1h` score `-0.0111` n `109` status `ready` deltaP `5.5334` edge `-0.0028` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.2355` n `109` status `ready` deltaP `7.4849` edge `0.0059` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5323` n `109` status `ready` deltaP `-1.7099` edge `-0.0074` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.7253` n `109` status `ready` deltaP `-3.0572` edge `-0.0192` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.7477` n `109` status `ready` deltaP `3.2418` edge `0.006` maxDD `-3.211`
- `market_context_high->index_24h` score `-1.2802` n `94` status `ready` deltaP `-3.5757` edge `0.0792` maxDD `-7.8922`
- `market_context_high->crypto_alt_1h` score `-1.5049` n `109` status `ready` deltaP `-5.1379` edge `-0.0201` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.7879` n `109` status `ready` deltaP `1.5685` edge `-0.0861` maxDD `-10.619`
- `market_context_high->crypto_alt_24h` score `-1.9689` n `94` status `ready` deltaP `0.6796` edge `-0.0243` maxDD `-4.5445`
- `market_context_high->index_4h` score `-2.0358` n `109` status `ready` deltaP `-11.7532` edge `-0.0572` maxDD `-4.7021`
- `market_context_high->crypto_alt_4h` score `-2.1731` n `109` status `ready` deltaP `1.0796` edge `-0.0493` maxDD `-5.7857`
- `market_context_high->unknown_1h` score `-2.2108` n `109` status `ready` deltaP `1.1344` edge `-0.1471` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.2779` n `109` status `ready` deltaP `-11.299` edge `-0.0605` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.5511` n `94` status `ready` deltaP `6.4642` edge `-0.0364` maxDD `-51.7259`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
