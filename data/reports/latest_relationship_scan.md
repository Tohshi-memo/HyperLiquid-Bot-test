# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T08:53:05.882575+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3712`

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

- `news_risk_high->unknown_1h` score `3371.568` n `31` status `ready` deltaP `1.7819` edge `280.9697` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3241.2502` n `31` status `ready` deltaP `3.7864` edge `270.0846` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `21.2636` n `31` status `ready` deltaP `32.7556` edge `1.5536` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.1717` n `31` status `ready` deltaP `30.6759` edge `1.0598` maxDD `0.0`
- `news_risk_high->equity_24h` score `12.0008` n `31` status `ready` deltaP `26.1698` edge `0.8256` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.2044` n `31` status `ready` deltaP `21.425` edge `0.6279` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.2929` n `31` status `ready` deltaP `29.4503` edge `0.2928` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.0706` n `31` status `ready` deltaP `15.4062` edge `0.6891` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.9093` n `31` status `ready` deltaP `40.2359` edge `0.1537` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.6557` n `31` status `ready` deltaP `14.614` edge `0.2347` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.3382` n `31` status `ready` deltaP `28.8405` edge `0.0286` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.2925` n `31` status `ready` deltaP `25.4766` edge `0.0212` maxDD `0.0`
- `news_risk_high->index_1h` score `2.2744` n `31` status `ready` deltaP `27.9506` edge `0.0117` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.1076` n `31` status `ready` deltaP `13.9994` edge `0.101` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `1.8344` n `31` status `ready` deltaP `5.6693` edge `0.2435` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.6805` n `31` status `ready` deltaP `8.6633` edge `0.1934` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1146` n `31` status `ready` deltaP `24.3432` edge `0.0085` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.3413` n `31` status `ready` deltaP `8.6743` edge `0.0257` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.3311` n `31` status `ready` deltaP `11.4427` edge `0.0219` maxDD `-0.7918`
- `market_context_high->equity_1h` score `0.2631` n `40` status `ready` deltaP `8.7575` edge `0.0162` maxDD `-1.2685`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
