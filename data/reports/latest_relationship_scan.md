# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-14T16:07:29.842781+00:00`
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

- `market_context_high->unknown_24h` score `124.1206` n `133` status `ready` deltaP `-33.2954` edge `10.8566` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `32.8065` n `32` status `ready` deltaP `-46.0069` edge `4.5877` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `32.8065` n `32` status `ready` deltaP `-46.0069` edge `4.5877` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `9.8619` n `36` status `ready` deltaP `11.1111` edge `0.7857` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.3228` n `36` status `ready` deltaP `38.7195` edge `0.3521` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.7546` n `32` status `ready` deltaP `32.1181` edge `0.1821` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.7546` n `32` status `ready` deltaP `32.1181` edge `0.1821` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.2168` n `133` status `ready` deltaP `26.1031` edge `0.2135` maxDD `-1.223`
- `risk_on_high->commodity_4h` score `2.8824` n `32` status `ready` deltaP `20.0457` edge `0.1248` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.8824` n `32` status `ready` deltaP `20.0457` edge `0.1248` maxDD `-0.1258`
- `risk_on_high->crypto_major_24h` score `2.2217` n `32` status `ready` deltaP `17.3611` edge `0.2847` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `2.2217` n `32` status `ready` deltaP `17.3611` edge `0.2847` maxDD `-6.2481`
- `news_risk_high->index_24h` score `2.158` n `36` status `ready` deltaP `14.9306` edge `0.0803` maxDD `0.0`
- `news_risk_high->equity_1h` score `1.7849` n `36` status `ready` deltaP `9.032` edge `0.1204` maxDD `-0.5496`
- `news_risk_high->index_4h` score `1.7321` n `36` status `ready` deltaP `20.2235` edge `0.0227` maxDD `-0.0546`
- `market_context_high->commodity_4h` score `1.446` n `133` status `ready` deltaP `15.6049` edge `0.0709` maxDD `-1.3543`
- `risk_on_high->commodity_1h` score `1.309` n `32` status `ready` deltaP `13.8099` edge `0.0403` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.309` n `32` status `ready` deltaP `13.8099` edge `0.0403` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `1.1417` n `32` status `ready` deltaP `13.5417` edge `0.0233` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.1417` n `32` status `ready` deltaP `13.5417` edge `0.0233` maxDD `-0.1418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
