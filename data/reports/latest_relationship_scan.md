# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-13T17:22:29.995764+00:00`
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

- `market_context_high->unknown_24h` score `79.1699` n `157` status `ready` deltaP `-25.209` edge `7.0568` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.6486` n `32` status `ready` deltaP `-42.1875` edge `4.6702` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.6486` n `32` status `ready` deltaP `-42.1875` edge `4.6702` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `9.3802` n `36` status `ready` deltaP `10.0694` edge `0.7525` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `6.4399` n `36` status `ready` deltaP `35.2134` edge `0.3019` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.146` n `32` status `ready` deltaP `29.3403` edge `0.1499` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.146` n `32` status `ready` deltaP `29.3403` edge `0.1499` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.671` n `32` status `ready` deltaP `18.9787` edge `0.1143` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.671` n `32` status `ready` deltaP `18.9787` edge `0.1143` maxDD `-0.1258`
- `news_risk_high->index_24h` score `2.5244` n `36` status `ready` deltaP `15.625` edge `0.1062` maxDD `0.0`
- `market_context_high->commodity_24h` score `2.1964` n `157` status `ready` deltaP `19.1492` edge `0.1357` maxDD `-2.4263`
- `risk_on_high->fx_24h` score `1.88` n `32` status `ready` deltaP `21.1806` edge `0.0339` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.88` n `32` status `ready` deltaP `21.1806` edge `0.0339` maxDD `-0.1418`
- `news_risk_high->index_4h` score `1.6361` n `36` status `ready` deltaP `19.3089` edge `0.0208` maxDD `-0.0546`
- `market_context_high->commodity_4h` score `1.5138` n `157` status `ready` deltaP `16.6499` edge `0.079` maxDD `-2.1077`
- `news_risk_high->equity_1h` score `1.3928` n `36` status `ready` deltaP `7.0859` edge `0.1007` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.2048` n `32` status `ready` deltaP `13.0614` edge `0.0366` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2048` n `32` status `ready` deltaP `13.0614` edge `0.0366` maxDD `-0.1957`
- `risk_on_high->crypto_major_24h` score `1.2021` n `32` status `ready` deltaP `12.1528` edge `0.1887` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.2021` n `32` status `ready` deltaP `12.1528` edge `0.1887` maxDD `-6.2481`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
