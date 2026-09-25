# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T07:37:42.326143+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11350`

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

- `market_context_high->unknown_1h` score `84.9141` n `47` status `ready` deltaP `8.4693` edge `7.0268` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `49.821` n `47` status `ready` deltaP `30.7698` edge `3.9859` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `32.2744` n `47` status `ready` deltaP `24.782` edge `2.5623` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.9527` n `47` status `ready` deltaP `34.5892` edge `1.9677` maxDD `-2.1786`
- `market_context_high->index_24h` score `8.1018` n `47` status `ready` deltaP `37.367` edge `0.439` maxDD `-0.3705`
- `news_risk_high->unknown_1h` score `6.9595` n `115` status `ready` deltaP `4.0289` edge `0.567` maxDD `-0.4452`
- `market_context_high->metal_24h` score `4.7641` n `47` status `ready` deltaP `40.2667` edge `0.1524` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.6636` n `52` status `ready` deltaP `30.1683` edge `0.139` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.8609` n `47` status `ready` deltaP `32.8068` edge `0.0351` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.4615` n `47` status `ready` deltaP `16.5347` edge `0.1367` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `1.1858` n `47` status `ready` deltaP `9.688` edge `0.101` maxDD `-3.3417`
- `market_context_high->equity_1h` score `0.9774` n `47` status `ready` deltaP `11.7658` edge `0.0433` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.9595` n `47` status `ready` deltaP `14.6101` edge `0.0104` maxDD `-0.2275`
- `news_risk_high->crypto_alt_1h` score `0.9394` n `115` status `ready` deltaP `9.1721` edge `0.1082` maxDD `-4.2849`
- `market_context_high->fx_1h` score `0.4326` n `47` status `ready` deltaP `9.6604` edge `0.0073` maxDD `-0.1854`
- `market_context_high->metal_1h` score `0.0718` n `47` status `ready` deltaP `4.1757` edge `0.013` maxDD `-0.1976`
- `news_risk_high->metal_1h` score `-0.0014` n `115` status `ready` deltaP `8.283` edge `0.0076` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.0027` n `115` status `ready` deltaP `4.0693` edge `0.0482` maxDD `-3.3776`
- `market_context_high->crypto_major_1h` score `-0.0283` n `47` status `ready` deltaP `3.2552` edge `0.0577` maxDD `-4.5405`
- `market_context_high->metal_4h` score `-0.1799` n `47` status `ready` deltaP `-1.6477` edge `0.0263` maxDD `-0.404`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
