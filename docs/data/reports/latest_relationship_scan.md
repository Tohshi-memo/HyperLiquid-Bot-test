# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T21:22:27.694932+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3720`

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

- `market_context_high->unknown_1h` score `32156.0042` n `45` status `ready` deltaP `1.4171` edge `2679.667` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21830.815` n `45` status `ready` deltaP `1.958` edge `1819.2354` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `921.0493` n `31` status `ready` deltaP `1.6322` edge `76.7608` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `577.8675` n `31` status `ready` deltaP `3.1766` edge `48.1401` maxDD `-0.1191`
- `news_risk_high->unknown_24h` score `299.2139` n `31` status `ready` deltaP `5.7292` edge `24.8963` maxDD `0.0`
- `news_risk_high->equity_24h` score `46.2243` n `31` status `ready` deltaP `52.0833` edge `3.5048` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `42.3042` n `31` status `ready` deltaP `53.9931` edge `3.1654` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `37.9318` n `31` status `ready` deltaP `53.4722` edge `2.8045` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.8125` n `31` status `ready` deltaP `40.1938` edge `0.7439` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.9625` n `31` status `ready` deltaP `26.4555` edge `0.8242` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.5549` n `31` status `ready` deltaP `37.8344` edge `0.6754` maxDD `-2.178`
- `news_risk_high->index_24h` score `7.4739` n `31` status `ready` deltaP `53.2986` edge `0.2675` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `6.7854` n `31` status `ready` deltaP `17.6927` edge `0.8937` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.3655` n `31` status `ready` deltaP `45.8782` edge `0.1541` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.6403` n `31` status `ready` deltaP `19.9874` edge `0.1888` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3462` n `31` status `ready` deltaP `36.31` edge `0.0628` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6554` n `31` status `ready` deltaP `31.5434` edge `0.0195` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4158` n `31` status `ready` deltaP `9.8609` edge `0.2901` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.3461` n `45` status `ready` deltaP `29.021` edge `0.0305` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.2339` n `31` status `ready` deltaP `12.5555` edge `0.2384` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
