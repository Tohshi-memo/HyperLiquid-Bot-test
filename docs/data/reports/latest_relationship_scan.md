# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T13:22:33.375994+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3780`

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

- `market_context_high->unknown_1h` score `32207.261` n `45` status `ready` deltaP `1.8662` edge `2683.9354` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21939.1297` n `45` status `ready` deltaP `3.1776` edge `1828.2535` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `972.306` n `31` status `ready` deltaP `2.0813` edge `81.0292` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `686.1822` n `31` status `ready` deltaP `4.3962` edge `57.1582` maxDD `-0.1191`
- `news_risk_high->unknown_24h` score `568.7303` n `31` status `ready` deltaP `5.7292` edge `47.356` maxDD `0.0`
- `news_risk_high->equity_24h` score `43.973` n `31` status `ready` deltaP `49.6528` edge `3.3334` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `41.1532` n `31` status `ready` deltaP `51.2153` edge `3.088` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `37.9068` n `31` status `ready` deltaP `53.8194` edge `2.8001` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.8337` n `31` status `ready` deltaP `27.3701` edge `0.8907` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.7638` n `31` status `ready` deltaP `41.2355` edge `0.7329` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `11.1631` n `31` status `ready` deltaP `37.682` edge `0.7271` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.4541` n `31` status `ready` deltaP `18.9123` edge `0.9713` maxDD `-7.6714`
- `news_risk_high->index_24h` score `6.9774` n `31` status `ready` deltaP `50.3472` edge `0.2458` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.2412` n `31` status `ready` deltaP `44.4893` edge `0.153` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `4.017` n `31` status `ready` deltaP `20.7359` edge `0.2152` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3856` n `31` status `ready` deltaP `36.1576` edge `0.0671` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.7479` n `31` status `ready` deltaP `11.807` edge `0.3197` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.7202` n `31` status `ready` deltaP `31.9925` edge `0.0219` maxDD `-0.0136`
- `market_context_high->fx_4h` score `2.5492` n `45` status `ready` deltaP `31.1551` edge `0.0332` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.4959` n `31` status `ready` deltaP `13.6034` edge `0.265` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
