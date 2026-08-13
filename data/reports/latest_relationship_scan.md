# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-13T16:22:28.955880+00:00`
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

- `market_context_high->unknown_24h` score `74.4413` n `160` status `ready` deltaP `-24.0625` edge `6.6551` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.6392` n `32` status `ready` deltaP `-42.1875` edge `4.669` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.6392` n `32` status `ready` deltaP `-42.1875` edge `4.669` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `9.3358` n `36` status `ready` deltaP `10.0694` edge `0.7488` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `6.4255` n `36` status `ready` deltaP `35.2134` edge `0.3007` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.0509` n `32` status `ready` deltaP `28.6458` edge `0.1466` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.0509` n `32` status `ready` deltaP `28.6458` edge `0.1466` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.6904` n `32` status `ready` deltaP `19.1311` edge `0.1149` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.6904` n `32` status `ready` deltaP `19.1311` edge `0.1149` maxDD `-0.1258`
- `news_risk_high->index_24h` score `2.5472` n `36` status `ready` deltaP `15.625` edge `0.1081` maxDD `0.0`
- `market_context_high->commodity_24h` score `2.0781` n `160` status `ready` deltaP `18.6458` edge `0.1292` maxDD `-2.4263`
- `risk_on_high->fx_24h` score `1.9162` n `32` status `ready` deltaP `21.5278` edge `0.0346` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.9162` n `32` status `ready` deltaP `21.5278` edge `0.0346` maxDD `-0.1418`
- `news_risk_high->index_4h` score `1.6421` n `36` status `ready` deltaP `19.3089` edge `0.0213` maxDD `-0.0546`
- `market_context_high->commodity_4h` score `1.4967` n `160` status `ready` deltaP `16.6311` edge `0.0777` maxDD `-2.1077`
- `news_risk_high->equity_1h` score `1.4084` n `36` status `ready` deltaP `7.0859` edge `0.102` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.2024` n `32` status `ready` deltaP `13.0614` edge `0.0364` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2024` n `32` status `ready` deltaP `13.0614` edge `0.0364` maxDD `-0.1957`
- `risk_on_high->crypto_major_24h` score `1.1379` n `32` status `ready` deltaP `11.4583` edge `0.1851` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.1379` n `32` status `ready` deltaP `11.4583` edge `0.1851` maxDD `-6.2481`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
