# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T22:22:34.240243+00:00`
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

- `market_context_high->unknown_24h` score `45.7974` n `109` status `ready` deltaP `3.7571` edge `3.7957` maxDD `-0.0104`
- `market_context_high->commodity_4h` score `1.1713` n `119` status `ready` deltaP `13.2501` edge `0.0939` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.9268` n `109` status `ready` deltaP `3.7004` edge `0.1694` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.5363` n `109` status `ready` deltaP `21.4854` edge `0.0461` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.511` n `120` status `ready` deltaP `8.1726` edge `0.0297` maxDD `-1.3282`
- `market_context_high->fx_1h` score `-0.0045` n `120` status `ready` deltaP `5.781` edge `-0.0041` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.3922` n `119` status `ready` deltaP `5.5372` edge `-0.0012` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.565` n `120` status `ready` deltaP `-2.4439` edge `-0.0067` maxDD `-1.6224`
- `market_context_high->crypto_alt_1h` score `-0.8079` n `120` status `ready` deltaP `-3.3632` edge `-0.0101` maxDD `-3.0178`
- `market_context_high->index_1h` score `-1.0785` n `120` status `ready` deltaP `-3.1913` edge `-0.0152` maxDD `-1.6054`
- `market_context_high->crypto_alt_4h` score `-1.2306` n `119` status `ready` deltaP `1.9074` edge `-0.0315` maxDD `-5.7857`
- `market_context_high->metal_4h` score `-1.3095` n `119` status `ready` deltaP `1.3115` edge `0.0056` maxDD `-3.211`
- `market_context_high->equity_1h` score `-1.3804` n `120` status `ready` deltaP `3.4342` edge `-0.0434` maxDD `-10.5179`
- `market_context_high->index_24h` score `-1.3941` n `109` status `ready` deltaP `-4.5519` edge `0.0711` maxDD `-7.8922`
- `market_context_high->index_4h` score `-1.7389` n `119` status `ready` deltaP `-8.5948` edge `-0.0402` maxDD `-4.7021`
- `market_context_high->crypto_major_1h` score `-2.6609` n `120` status `ready` deltaP `-6.9768` edge `-0.0379` maxDD `-7.6533`
- `market_context_high->crypto_alt_24h` score `-2.926` n `109` status `ready` deltaP `-5.4785` edge `-0.063` maxDD `-4.5445`
- `market_context_high->equity_4h` score `-6.2341` n `119` status `ready` deltaP `-0.7597` edge `-0.2653` maxDD `-34.9766`
- `market_context_high->commodity_24h` score `-6.2487` n `109` status `ready` deltaP `9.8099` edge `0.01` maxDD `-52.7876`
- `market_context_high->crypto_major_4h` score `-7.2916` n `119` status `ready` deltaP `-6.4405` edge `-0.1435` maxDD `-27.3622`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
