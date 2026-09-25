# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T04:37:32.830572+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11202`

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

- `market_context_high->unknown_1h` score `86.6949` n `47` status `ready` deltaP `8.7687` edge `7.1732` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `48.7829` n `47` status `ready` deltaP `30.4226` edge `3.9017` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `31.8544` n `47` status `ready` deltaP `24.782` edge `2.5273` maxDD `-2.7051`
- `market_context_high->equity_24h` score `26.1034` n `47` status `ready` deltaP `34.7628` edge `1.9791` maxDD `-2.1786`
- `market_context_high->index_24h` score `8.2815` n `47` status `ready` deltaP `39.1031` edge `0.4424` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.6882` n `47` status `ready` deltaP `39.5723` edge `0.1507` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.4191` n `54` status `ready` deltaP `30.3819` edge `0.1172` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.9643` n `47` status `ready` deltaP `33.8739` edge `0.0366` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.5655` n `47` status `ready` deltaP `17.1445` edge `0.1413` maxDD `-1.3444`
- `news_risk_high->crypto_alt_1h` score `1.201` n `116` status `ready` deltaP `10.8817` edge `0.1186` maxDD `-4.2849`
- `market_context_high->equity_1h` score `0.9738` n `47` status `ready` deltaP `11.7658` edge `0.043` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.9727` n `47` status `ready` deltaP `14.7598` edge `0.0105` maxDD `-0.2275`
- `market_context_high->crypto_alt_4h` score `0.8798` n `47` status `ready` deltaP `8.7733` edge `0.0816` maxDD `-3.3417`
- `news_risk_high->crypto_major_1h` score `0.612` n `116` status `ready` deltaP `9.4157` edge `0.0628` maxDD `-3.2991`
- `news_risk_high->metal_1h` score `0.4275` n `116` status `ready` deltaP `10.6752` edge `0.0138` maxDD `-0.6142`
- `market_context_high->fx_1h` score `0.3799` n `47` status `ready` deltaP `9.0616` edge `0.0069` maxDD `-0.1854`
- `market_context_high->metal_1h` score `0.0305` n `47` status `ready` deltaP `3.5769` edge `0.0117` maxDD `-0.1976`
- `market_context_high->crypto_major_1h` score `-0.1493` n `47` status `ready` deltaP `2.2073` edge `0.0546` maxDD `-4.5405`
- `news_risk_high->equity_1h` score `-0.2025` n `116` status `ready` deltaP `0.9808` edge `0.0255` maxDD `-2.6402`
- `market_context_high->metal_4h` score `-0.2865` n `47` status `ready` deltaP `-3.1721` edge `0.0228` maxDD `-0.404`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
