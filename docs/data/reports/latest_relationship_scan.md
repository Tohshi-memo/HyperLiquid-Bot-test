# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-14T04:52:25.561971+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11712`

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

- `market_context_high->unknown_24h` score `90.4111` n `150` status `ready` deltaP `-29.625` edge `8.023` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.2265` n `32` status `ready` deltaP `-43.75` edge `4.6265` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.2265` n `32` status `ready` deltaP `-43.75` edge `4.6265` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `9.9154` n `36` status `ready` deltaP `10.0694` edge `0.7971` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `6.972` n `36` status `ready` deltaP `37.5` edge `0.331` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.7745` n `32` status `ready` deltaP `32.2917` edge `0.1826` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.7745` n `32` status `ready` deltaP `32.2917` edge `0.1826` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.965` n `32` status `ready` deltaP `20.8079` edge `0.1266` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.965` n `32` status `ready` deltaP `20.8079` edge `0.1266` maxDD `-0.1258`
- `market_context_high->commodity_24h` score `2.8474` n `150` status `ready` deltaP `22.2917` edge `0.169` maxDD `-2.4263`
- `news_risk_high->index_24h` score `2.2935` n `36` status `ready` deltaP `14.5833` edge `0.0939` maxDD `0.0`
- `news_risk_high->index_4h` score `1.6703` n `36` status `ready` deltaP `19.7662` edge `0.0206` maxDD `-0.0546`
- `market_context_high->commodity_4h` score `1.6034` n `150` status `ready` deltaP `17.3496` edge `0.0818` maxDD `-2.1077`
- `news_risk_high->equity_1h` score `1.5427` n `36` status `ready` deltaP `7.6847` edge `0.1092` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.3498` n `32` status `ready` deltaP `14.259` edge `0.0407` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.3498` n `32` status `ready` deltaP `14.259` edge `0.0407` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `1.2473` n `32` status `ready` deltaP `14.7569` edge `0.024` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.2473` n `32` status `ready` deltaP `14.7569` edge `0.024` maxDD `-0.1418`
- `risk_on_high->crypto_major_24h` score `1.0753` n `32` status `ready` deltaP `10.7639` edge `0.1817` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.0753` n `32` status `ready` deltaP `10.7639` edge `0.1817` maxDD `-6.2481`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
