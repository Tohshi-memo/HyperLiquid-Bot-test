# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T12:52:33.649470+00:00`
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

- `market_context_high->unknown_1h` score `32210.1673` n `45` status `ready` deltaP `2.0159` edge `2684.1766` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21944.8489` n `45` status `ready` deltaP `3.1776` edge `1828.7301` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `975.2124` n `31` status `ready` deltaP `2.231` edge `81.2704` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `691.9014` n `31` status `ready` deltaP `4.3962` edge `57.6348` maxDD `-0.1191`
- `news_risk_high->unknown_24h` score `587.8979` n `31` status `ready` deltaP `5.7292` edge `48.9533` maxDD `0.0`
- `news_risk_high->equity_24h` score `43.6812` n `31` status `ready` deltaP `49.3056` edge `3.3114` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `40.985` n `31` status `ready` deltaP `50.8681` edge `3.0763` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `37.777` n `31` status `ready` deltaP `53.4722` edge `2.7916` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.8193` n `31` status `ready` deltaP `27.3701` edge `0.8895` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.729` n `31` status `ready` deltaP `41.2355` edge `0.73` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `11.1715` n `31` status `ready` deltaP `37.682` edge `0.7278` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.4736` n `31` status `ready` deltaP `18.9123` edge `0.9738` maxDD `-7.6714`
- `news_risk_high->index_24h` score `6.9184` n `31` status `ready` deltaP `50.0` edge `0.2432` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.211` n `31` status `ready` deltaP `44.142` edge `0.1528` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `4.0301` n `31` status `ready` deltaP `20.8856` edge `0.2153` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3832` n `31` status `ready` deltaP `36.1576` edge `0.0669` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.758` n `31` status `ready` deltaP `11.9567` edge `0.32` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.7333` n `31` status `ready` deltaP `32.1422` edge `0.022` maxDD `-0.0136`
- `market_context_high->fx_4h` score `2.5614` n `45` status `ready` deltaP `31.3076` edge `0.0332` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.4826` n `31` status `ready` deltaP `13.4537` edge `0.2643` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
