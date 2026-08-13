# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-13T20:22:31.862878+00:00`
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

- `market_context_high->unknown_24h` score `84.2295` n `154` status `ready` deltaP `-25.8794` edge `7.4829` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.7217` n `32` status `ready` deltaP `-41.6667` edge `4.6761` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.7217` n `32` status `ready` deltaP `-41.6667` edge `4.6761` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `9.6754` n `36` status `ready` deltaP `10.0694` edge `0.7771` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `6.6831` n `36` status `ready` deltaP `35.8232` edge `0.3181` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.4915` n `32` status `ready` deltaP `31.4236` edge `0.1648` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.4915` n `32` status `ready` deltaP `31.4236` edge `0.1648` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.8464` n `32` status `ready` deltaP `20.0457` edge `0.1218` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.8464` n `32` status `ready` deltaP `20.0457` edge `0.1218` maxDD `-0.1258`
- `market_context_high->commodity_24h` score `2.52` n `154` status `ready` deltaP `21.034` edge `0.1501` maxDD `-2.4263`
- `news_risk_high->index_24h` score `2.4745` n `36` status `ready` deltaP `15.4514` edge `0.1032` maxDD `0.0`
- `risk_on_high->fx_24h` score `1.7111` n `32` status `ready` deltaP `19.4444` edge `0.0314` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.7111` n `32` status `ready` deltaP `19.4444` edge `0.0314` maxDD `-0.1418`
- `news_risk_high->index_4h` score `1.6421` n `36` status `ready` deltaP `19.3089` edge `0.0213` maxDD `-0.0546`
- `market_context_high->commodity_4h` score `1.5939` n `154` status `ready` deltaP `17.2454` edge `0.0817` maxDD `-2.1077`
- `news_risk_high->equity_1h` score `1.55` n `36` status `ready` deltaP `7.3853` edge `0.1118` maxDD `-0.5496`
- `risk_on_high->crypto_major_24h` score `1.344` n `32` status `ready` deltaP `13.0208` edge `0.2011` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.344` n `32` status `ready` deltaP `13.0208` edge `0.2011` maxDD `-6.2481`
- `risk_on_high->commodity_1h` score `1.2719` n `32` status `ready` deltaP `13.6602` edge `0.0382` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2719` n `32` status `ready` deltaP `13.6602` edge `0.0382` maxDD `-0.1957`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
