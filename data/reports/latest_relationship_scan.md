# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T23:07:28.395679+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11765`

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

- `market_context_high->unknown_24h` score `39.0246` n `109` status `ready` deltaP `3.7571` edge `3.2313` maxDD `-0.0104`
- `market_context_high->commodity_4h` score `1.1533` n `119` status `ready` deltaP `13.0252` edge `0.0939` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.9112` n `109` status `ready` deltaP `3.7004` edge `0.1681` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.541` n `109` status `ready` deltaP `21.4854` edge `0.0467` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4931` n `120` status `ready` deltaP `7.9491` edge `0.0297` maxDD `-1.3282`
- `market_context_high->fx_1h` score `-0.0186` n `120` status `ready` deltaP `5.5539` edge `-0.0044` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.3961` n `119` status `ready` deltaP `5.4622` edge `-0.0012` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5537` n `120` status `ready` deltaP `-2.2255` edge `-0.0067` maxDD `-1.6224`
- `market_context_high->crypto_alt_1h` score `-0.7762` n `120` status `ready` deltaP `-2.994` edge `-0.0085` maxDD `-3.0178`
- `market_context_high->index_1h` score `-1.0971` n `120` status `ready` deltaP `-3.4231` edge `-0.0152` maxDD `-1.6054`
- `market_context_high->crypto_alt_4h` score `-1.2146` n `119` status `ready` deltaP `2.1249` edge `-0.0309` maxDD `-5.7857`
- `market_context_high->metal_4h` score `-1.2903` n `119` status `ready` deltaP `1.5073` edge `0.0059` maxDD `-3.211`
- `market_context_high->index_24h` score `-1.3486` n `109` status `ready` deltaP `-4.0511` edge `0.0736` maxDD `-7.8922`
- `market_context_high->equity_1h` score `-1.3732` n `120` status `ready` deltaP `3.498` edge `-0.0429` maxDD `-10.5179`
- `market_context_high->index_4h` score `-1.7235` n `119` status `ready` deltaP `-8.3869` edge `-0.0396` maxDD `-4.7021`
- `market_context_high->crypto_major_1h` score `-2.6225` n `120` status `ready` deltaP `-6.6018` edge `-0.0372` maxDD `-7.6533`
- `market_context_high->crypto_alt_24h` score `-2.9996` n `109` status `ready` deltaP `-5.9793` edge `-0.0658` maxDD `-4.5445`
- `market_context_high->equity_4h` score `-6.1934` n `119` status `ready` deltaP `-0.5619` edge `-0.2614` maxDD `-34.9766`
- `market_context_high->commodity_24h` score `-6.2729` n `109` status `ready` deltaP `9.8099` edge `0.0069` maxDD `-52.7876`
- `market_context_high->crypto_major_4h` score `-7.2808` n `119` status `ready` deltaP `-6.3506` edge `-0.1432` maxDD `-27.3622`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
