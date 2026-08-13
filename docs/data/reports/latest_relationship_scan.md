# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-13T22:37:35.758419+00:00`
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

- `market_context_high->unknown_24h` score `91.1597` n `150` status `ready` deltaP `-27.5417` edge `8.0715` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.7131` n `32` status `ready` deltaP `-41.6667` edge `4.675` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.7131` n `32` status `ready` deltaP `-41.6667` edge `4.675` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `9.5422` n `36` status `ready` deltaP `10.0694` edge `0.766` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `6.5611` n `36` status `ready` deltaP `35.2134` edge `0.312` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.6821` n `32` status `ready` deltaP `32.2917` edge `0.1749` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.6821` n `32` status `ready` deltaP `32.2917` edge `0.1749` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.981` n `32` status `ready` deltaP `21.1128` edge `0.1259` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.981` n `32` status `ready` deltaP `21.1128` edge `0.1259` maxDD `-0.1258`
- `market_context_high->commodity_24h` score `2.755` n `150` status `ready` deltaP `22.2917` edge `0.1613` maxDD `-2.4263`
- `news_risk_high->index_24h` score `2.3403` n `36` status `ready` deltaP `14.5833` edge `0.0978` maxDD `0.0`
- `market_context_high->commodity_4h` score `1.6194` n `150` status `ready` deltaP `17.6545` edge `0.0811` maxDD `-2.1077`
- `news_risk_high->index_4h` score `1.5887` n `36` status `ready` deltaP `18.8516` edge `0.0199` maxDD `-0.0546`
- `risk_on_high->fx_24h` score `1.5573` n `32` status `ready` deltaP `17.8819` edge `0.029` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.5573` n `32` status `ready` deltaP `17.8819` edge `0.029` maxDD `-0.1418`
- `news_risk_high->equity_1h` score `1.4373` n `36` status `ready` deltaP `6.7865` edge `0.1064` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.3605` n `32` status `ready` deltaP `14.4087` edge `0.0406` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.3605` n `32` status `ready` deltaP `14.4087` edge `0.0406` maxDD `-0.1957`
- `risk_on_high->crypto_major_24h` score `1.2372` n `32` status `ready` deltaP `12.1528` edge `0.1932` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.2372` n `32` status `ready` deltaP `12.1528` edge `0.1932` maxDD `-6.2481`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
