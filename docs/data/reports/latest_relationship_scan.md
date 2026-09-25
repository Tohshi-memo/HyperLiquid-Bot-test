# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T06:22:27.543480+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11162`

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

- `market_context_high->unknown_1h` score `85.0521` n `47` status `ready` deltaP `8.7687` edge `7.0363` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `49.398` n `47` status `ready` deltaP `30.5962` edge `3.9518` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `32.1316` n `47` status `ready` deltaP `24.782` edge `2.5504` maxDD `-2.7051`
- `market_context_high->equity_24h` score `26.0686` n `47` status `ready` deltaP `34.7628` edge `1.9762` maxDD `-2.1786`
- `market_context_high->index_24h` score `8.1964` n `47` status `ready` deltaP `38.2351` edge `0.4411` maxDD `-0.3705`
- `news_risk_high->unknown_1h` score `5.1068` n `116` status `ready` deltaP `2.6792` edge `0.4216` maxDD `-0.4452`
- `market_context_high->metal_24h` score `4.7677` n `47` status `ready` deltaP `40.2667` edge `0.1527` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.7767` n `54` status `ready` deltaP `30.3819` edge `0.147` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.9339` n `47` status `ready` deltaP `33.569` edge `0.0361` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.5631` n `47` status `ready` deltaP `17.1445` edge `0.1411` maxDD `-1.3444`
- `news_risk_high->crypto_alt_1h` score `1.1926` n `116` status `ready` deltaP `10.8817` edge `0.1179` maxDD `-4.2849`
- `market_context_high->crypto_alt_4h` score `1.1788` n `47` status `ready` deltaP `9.8404` edge `0.0994` maxDD `-3.3417`
- `market_context_high->equity_1h` score `0.9774` n `47` status `ready` deltaP `11.7658` edge `0.0433` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.9595` n `47` status `ready` deltaP `14.6101` edge `0.0104` maxDD `-0.2275`
- `news_risk_high->crypto_major_1h` score `0.3796` n `116` status `ready` deltaP `7.2786` edge `0.0578` maxDD `-3.3083`
- `market_context_high->fx_1h` score `0.3775` n `47` status `ready` deltaP `9.0616` edge `0.0067` maxDD `-0.1854`
- `market_context_high->metal_1h` score `0.0609` n `47` status `ready` deltaP `4.026` edge `0.0126` maxDD `-0.1976`
- `news_risk_high->metal_1h` score `0.043` n `116` status `ready` deltaP `8.5381` edge `0.0096` maxDD `-0.7016`
- `market_context_high->crypto_major_1h` score `-0.1002` n `47` status `ready` deltaP `2.6564` edge `0.0557` maxDD `-4.5405`
- `market_context_high->metal_4h` score `-0.2061` n `47` status `ready` deltaP `-2.105` edge `0.026` maxDD `-0.404`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
