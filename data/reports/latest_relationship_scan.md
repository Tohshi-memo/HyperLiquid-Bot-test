# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-14T13:07:25.697850+00:00`
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

- `market_context_high->unknown_24h` score `98.8418` n `145` status `ready` deltaP `-32.5263` edge `8.7449` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `32.9517` n `32` status `ready` deltaP `-44.4444` edge `4.5959` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `32.9517` n `32` status `ready` deltaP `-44.4444` edge `4.5959` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `9.5986` n `36` status `ready` deltaP `10.0694` edge `0.7707` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.1792` n `36` status `ready` deltaP `38.1098` edge `0.3442` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.8275` n `32` status `ready` deltaP `32.6389` edge `0.1847` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.8275` n `32` status `ready` deltaP `32.6389` edge `0.1847` maxDD `0.0`
- `market_context_high->commodity_24h` score `2.9508` n `145` status `ready` deltaP `22.2941` edge `0.1776` maxDD `-2.4263`
- `risk_on_high->commodity_4h` score `2.8728` n `32` status `ready` deltaP `20.0457` edge `0.124` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.8728` n `32` status `ready` deltaP `20.0457` edge `0.124` maxDD `-0.1258`
- `news_risk_high->index_24h` score `2.1164` n `36` status `ready` deltaP `14.4097` edge `0.0803` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `1.8965` n `32` status `ready` deltaP `16.1458` edge `0.2511` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.8965` n `32` status `ready` deltaP `16.1458` edge `0.2511` maxDD `-6.2481`
- `news_risk_high->equity_1h` score `1.707` n `36` status `ready` deltaP `8.5829` edge `0.1169` maxDD `-0.5496`
- `news_risk_high->index_4h` score `1.6835` n `36` status `ready` deltaP `19.7662` edge `0.0217` maxDD `-0.0546`
- `market_context_high->commodity_4h` score `1.3153` n `145` status `ready` deltaP `15.7138` edge `0.0687` maxDD `-2.1077`
- `risk_on_high->commodity_1h` score `1.2443` n `32` status `ready` deltaP `13.2111` edge `0.0389` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2443` n `32` status `ready` deltaP `13.2111` edge `0.0389` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `1.2183` n `32` status `ready` deltaP `14.4097` edge `0.0239` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.2183` n `32` status `ready` deltaP `14.4097` edge `0.0239` maxDD `-0.1418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
