# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T12:52:32.586248+00:00`
- Price records: `672`
- Market context records: `5982`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11220`

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

- `news_risk_high->fx_24h` score `7.3768` n `30` status `ready` deltaP `67.5347` edge `0.1645` maxDD `0.0`
- `news_risk_high->commodity_24h` score `4.6988` n `30` status `ready` deltaP `34.757` edge `0.1804` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `4.0558` n `30` status `ready` deltaP `41.9817` edge `0.0627` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.1771` n `30` status `ready` deltaP `26.1776` edge `0.0208` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.1554` n `237` status `ready` deltaP `7.9094` edge `0.153` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.7164` n `30` status `ready` deltaP `9.4411` edge `0.0756` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.0789` n `30` status `ready` deltaP `4.5709` edge `0.0258` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.0516` n `30` status `ready` deltaP `9.2361` edge `0.0322` maxDD `-2.3058`
- `market_context_high->commodity_1h` score `-0.4218` n `238` status `ready` deltaP `-0.9032` edge `0.0039` maxDD `-1.1566`
- `news_risk_high->metal_1h` score `-0.4492` n `30` status `ready` deltaP `1.0878` edge `-0.0282` maxDD `-1.2643`
- `market_context_high->equity_1h` score `-0.4655` n `238` status `ready` deltaP `3.4004` edge `0.0305` maxDD `-4.3608`
- `market_context_high->metal_1h` score `-0.5291` n `238` status `ready` deltaP `1.9562` edge `-0.001` maxDD `-2.0564`
- `market_context_high->fx_1h` score `-0.7036` n `238` status `ready` deltaP `-0.9372` edge `-0.0007` maxDD `-0.8015`
- `market_context_high->index_1h` score `-0.7296` n `238` status `ready` deltaP `-0.8693` edge `0.0036` maxDD `-1.3078`
- `market_context_high->equity_24h` score `-1.0779` n `211` status `ready` deltaP `21.0242` edge `0.3068` maxDD `-31.2762`
- `news_risk_high->index_1h` score `-1.1069` n `30` status `ready` deltaP `-10.4491` edge `-0.0208` maxDD `-1.1161`
- `market_context_high->index_4h` score `-1.1442` n `237` status `ready` deltaP `0.7256` edge `0.0172` maxDD `-3.165`
- `market_context_high->crypto_major_1h` score `-1.1629` n `238` status `ready` deltaP `1.9902` edge `0.0144` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-1.2162` n `238` status `ready` deltaP `1.2655` edge `0.0109` maxDD `-9.3536`
- `market_context_high->commodity_4h` score `-1.366` n `237` status `ready` deltaP `-0.8644` edge `-0.0044` maxDD `-5.8637`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
