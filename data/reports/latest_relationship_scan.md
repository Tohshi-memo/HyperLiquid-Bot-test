# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-14T16:52:35.479649+00:00`
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

- `market_context_high->unknown_24h` score `131.2336` n `130` status `ready` deltaP `-33.0182` edge `11.4475` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `32.7591` n `32` status `ready` deltaP `-46.5278` edge `4.5851` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `32.7591` n `32` status `ready` deltaP `-46.5278` edge `4.5851` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `9.9552` n `36` status `ready` deltaP `11.6319` edge `0.79` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.3746` n `36` status `ready` deltaP `38.872` edge `0.3554` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.8246` n `130` status `ready` deltaP `28.0982` edge `0.2279` maxDD `-0.387`
- `risk_on_high->commodity_24h` score `4.7252` n `32` status `ready` deltaP `31.9444` edge `0.1808` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.7252` n `32` status `ready` deltaP `31.9444` edge `0.1808` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.8376` n `32` status `ready` deltaP `19.7409` edge `0.1231` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.8376` n `32` status `ready` deltaP `19.7409` edge `0.1231` maxDD `-0.1258`
- `risk_on_high->crypto_major_24h` score `2.3065` n `32` status `ready` deltaP `17.8819` edge `0.2921` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `2.3065` n `32` status `ready` deltaP `17.8819` edge `0.2921` maxDD `-6.2481`
- `news_risk_high->index_24h` score `2.2069` n `36` status `ready` deltaP `15.4514` edge `0.0809` maxDD `0.0`
- `news_risk_high->index_4h` score `1.7771` n `36` status `ready` deltaP `20.6809` edge `0.0234` maxDD `-0.0546`
- `market_context_high->commodity_4h` score `1.7307` n `130` status `ready` deltaP `17.0005` edge `0.078` maxDD `-0.7687`
- `news_risk_high->equity_1h` score `1.725` n `36` status `ready` deltaP `8.5829` edge `0.1184` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.3078` n `32` status `ready` deltaP `13.8099` edge `0.0402` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.3078` n `32` status `ready` deltaP `13.8099` edge `0.0402` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `1.1079` n `32` status `ready` deltaP `13.1944` edge `0.0228` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.1079` n `32` status `ready` deltaP `13.1944` edge `0.0228` maxDD `-0.1418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
