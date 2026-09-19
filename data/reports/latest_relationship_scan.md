# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T00:07:30.553782+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8098`

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

- `news_risk_high->crypto_major_24h` score `61.9404` n `39` status `ready` deltaP `32.2783` edge `5.0357` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `56.4889` n `39` status `ready` deltaP `33.7073` edge `4.6206` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `37.8073` n `149` status `ready` deltaP `-1.2256` edge `3.1821` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `14.9691` n `39` status `ready` deltaP `52.0833` edge `0.9002` maxDD `0.0`
- `risk_on_high->unknown_4h` score `11.6859` n `52` status `ready` deltaP `-8.4662` edge `1.0528` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `11.6859` n `52` status `ready` deltaP `-8.4662` edge `1.0528` maxDD `-0.4694`
- `news_risk_high->crypto_alt_4h` score `8.8792` n `72` status `ready` deltaP `28.3706` edge `0.6634` maxDD `-7.675`
- `risk_on_high->commodity_24h` score `8.5305` n `52` status `ready` deltaP `47.3958` edge `0.3949` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.5305` n `52` status `ready` deltaP `47.3958` edge `0.3949` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.2313` n `149` status `ready` deltaP `40.6844` edge `0.3839` maxDD `-0.8682`
- `news_risk_high->crypto_major_4h` score `6.1224` n `72` status `ready` deltaP `25.1016` edge `0.4603` maxDD `-8.0625`
- `news_risk_high->metal_24h` score `4.8343` n `39` status `ready` deltaP `34.4017` edge `0.1893` maxDD `-0.2629`
- `news_risk_high->crypto_alt_1h` score `3.1636` n `72` status `ready` deltaP `17.4734` edge `0.1937` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.8905` n `72` status `ready` deltaP `21.9395` edge `0.1469` maxDD `-2.8494`
- `risk_on_high->commodity_4h` score `2.7639` n `52` status `ready` deltaP `32.235` edge `0.0504` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.7639` n `52` status `ready` deltaP `32.235` edge `0.0504` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.6636` n `149` status `ready` deltaP `28.7373` edge `0.0722` maxDD `-0.345`
- `news_risk_high->fx_24h` score `1.9016` n `39` status `ready` deltaP `9.4151` edge `0.0999` maxDD `-0.0029`
- `news_risk_high->equity_4h` score `1.5379` n `72` status `ready` deltaP `12.3984` edge `0.1355` maxDD `-4.1995`
- `news_risk_high->fx_4h` score `1.4995` n `72` status `ready` deltaP `16.311` edge `0.0381` maxDD `-0.084`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
