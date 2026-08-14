# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-14T14:52:43.754346+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11796`

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

- `market_context_high->unknown_24h` score `113.0075` n `138` status `ready` deltaP `-33.1295` edge `9.9294` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `32.8668` n `32` status `ready` deltaP `-45.3125` edge `4.5908` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `32.8668` n `32` status `ready` deltaP `-45.3125` edge `4.5908` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `9.6413` n `36` status `ready` deltaP `10.243` edge `0.7731` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.1684` n `36` status `ready` deltaP `38.1098` edge `0.3433` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.7992` n `32` status `ready` deltaP `32.4653` edge `0.1835` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.7992` n `32` status `ready` deltaP `32.4653` edge `0.1835` maxDD `0.0`
- `market_context_high->commodity_24h` score `3.3162` n `138` status `ready` deltaP `23.045` edge `0.1927` maxDD `-2.2652`
- `risk_on_high->commodity_4h` score `2.9406` n `32` status `ready` deltaP `20.503` edge `0.1266` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.9406` n `32` status `ready` deltaP `20.503` edge `0.1266` maxDD `-0.1258`
- `news_risk_high->index_24h` score `2.073` n `36` status `ready` deltaP `14.0625` edge `0.079` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `2.0471` n `32` status `ready` deltaP `16.4931` edge `0.2681` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `2.0471` n `32` status `ready` deltaP `16.4931` edge `0.2681` maxDD `-6.2481`
- `news_risk_high->index_4h` score `1.6665` n `36` status `ready` deltaP `19.6138` edge `0.0213` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.6446` n `36` status `ready` deltaP `8.4332` edge `0.1127` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.2935` n `32` status `ready` deltaP `13.6602` edge `0.04` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2935` n `32` status `ready` deltaP `13.6602` edge `0.04` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `1.2183` n `32` status `ready` deltaP `14.4097` edge `0.0239` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.2183` n `32` status `ready` deltaP `14.4097` edge `0.0239` maxDD `-0.1418`
- `market_context_high->commodity_4h` score `1.2012` n `138` status `ready` deltaP `14.8418` edge `0.065` maxDD `-2.1077`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
