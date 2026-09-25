# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T08:22:35.608263+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11206`

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

- `market_context_high->unknown_1h` score `84.6693` n `47` status `ready` deltaP `8.4693` edge `7.0064` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `50.0569` n `47` status `ready` deltaP `30.9434` edge `4.0044` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `32.3248` n `47` status `ready` deltaP `24.782` edge `2.5665` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.8831` n `47` status `ready` deltaP `34.5892` edge `1.9619` maxDD `-2.1786`
- `news_risk_high->unknown_1h` score `9.832` n `113` status `ready` deltaP `3.875` edge `0.8074` maxDD `-0.4452`
- `market_context_high->index_24h` score `8.0421` n `47` status `ready` deltaP `36.8462` edge `0.4375` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.7418` n `47` status `ready` deltaP `40.0931` edge `0.1517` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.5994` n `49` status `ready` deltaP `29.8151` edge `0.136` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.8135` n `47` status `ready` deltaP `32.3495` edge `0.0342` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.3733` n `47` status `ready` deltaP `16.0774` edge `0.1324` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `1.1426` n `47` status `ready` deltaP `9.688` edge `0.0974` maxDD `-3.3417`
- `market_context_high->equity_1h` score `0.9762` n `47` status `ready` deltaP `11.7658` edge `0.0432` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.9463` n `47` status `ready` deltaP `14.4604` edge `0.0103` maxDD `-0.2275`
- `news_risk_high->crypto_alt_1h` score `0.8518` n `113` status `ready` deltaP `8.5873` edge `0.1048` maxDD `-4.2849`
- `market_context_high->fx_1h` score `0.4326` n `47` status `ready` deltaP `9.6604` edge `0.0073` maxDD `-0.1854`
- `market_context_high->metal_1h` score `0.0632` n `47` status `ready` deltaP `4.026` edge `0.0129` maxDD `-0.1976`
- `news_risk_high->metal_1h` score `-0.009` n `113` status `ready` deltaP `8.1871` edge `0.0072` maxDD `-0.7016`
- `market_context_high->crypto_major_1h` score `-0.0235` n `47` status `ready` deltaP `3.2552` edge `0.0581` maxDD `-4.5405`
- `news_risk_high->index_1h` score `-0.0839` n `113` status `ready` deltaP `3.3703` edge `0.0061` maxDD `-0.4797`
- `news_risk_high->crypto_major_1h` score `-0.1374` n `113` status `ready` deltaP `3.3305` edge `0.0419` maxDD `-3.3776`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
