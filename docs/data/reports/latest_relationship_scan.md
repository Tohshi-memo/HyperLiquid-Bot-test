# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T07:52:26.968785+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11760`

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

- `news_risk_high->unknown_24h` score `1591.9836` n `120` status `ready` deltaP `1.2153` edge `132.6572` maxDD `0.0`
- `market_context_high->unknown_1h` score `115.5045` n `46` status `ready` deltaP `10.8501` edge `9.5577` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `54.0474` n `42` status `ready` deltaP `30.0843` edge `4.3385` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `28.9432` n `42` status `ready` deltaP `14.8065` edge `2.3512` maxDD `-2.7051`
- `market_context_high->equity_24h` score `28.7366` n `42` status `ready` deltaP `35.9871` edge `2.1862` maxDD `-2.1786`
- `market_context_high->index_24h` score `8.0599` n `42` status `ready` deltaP `33.3829` edge `0.4579` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.2188` n `42` status `ready` deltaP `38.0705` edge `0.1216` maxDD `-0.2401`
- `market_context_high->equity_4h` score `3.1603` n `42` status `ready` deltaP `18.6048` edge `0.1728` maxDD `-1.3444`
- `market_context_high->index_4h` score `3.1233` n `42` status `ready` deltaP `34.5674` edge `0.0369` maxDD `-0.2323`
- `market_context_high->crypto_alt_4h` score `1.5679` n `42` status `ready` deltaP `10.4893` edge `0.115` maxDD `-3.3417`
- `market_context_high->equity_1h` score `1.2326` n `46` status `ready` deltaP `14.3257` edge `0.0475` maxDD `-1.5564`
- `market_context_high->crypto_major_1h` score `1.1305` n `46` status `ready` deltaP `10.0495` edge `0.113` maxDD `-4.8632`
- `market_context_high->crypto_major_4h` score `0.9425` n `42` status `ready` deltaP `7.063` edge `0.1219` maxDD `-5.2359`
- `market_context_high->crypto_alt_1h` score `0.8917` n `46` status `ready` deltaP `9.3791` edge `0.1007` maxDD `-5.7799`
- `market_context_high->index_1h` score `0.8185` n `46` status `ready` deltaP `11.8524` edge `0.0087` maxDD `-0.2275`
- `news_risk_high->index_24h` score `0.6031` n `120` status `ready` deltaP `14.0972` edge `0.0258` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `0.422` n `120` status `ready` deltaP `14.6181` edge `0.1232` maxDD `-6.8392`
- `market_context_high->fx_1h` score `0.4084` n `46` status `ready` deltaP `12.0606` edge `0.0076` maxDD `-0.1854`
- `market_context_high->metal_1h` score `-0.0386` n `46` status `ready` deltaP `2.7662` edge `0.0102` maxDD `-0.215`
- `news_risk_high->index_1h` score `-0.1498` n `139` status `ready` deltaP `2.0151` edge `0.0031` maxDD `-0.3214`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
