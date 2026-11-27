# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T22:22:32.014709+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `2814`

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

- `news_risk_high->unknown_1h` score `3302.1961` n `31` status `ready` deltaP `1.6322` edge `275.1897` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3172.9937` n `31` status `ready` deltaP `3.3291` edge `264.3996` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `17.2597` n `31` status `ready` deltaP `27.5563` edge `1.2546` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `12.4416` n `31` status `ready` deltaP `27.2097` edge `0.8554` maxDD `0.0`
- `news_risk_high->equity_24h` score `12.1649` n `31` status `ready` deltaP `23.9168` edge `0.8543` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.2315` n `31` status `ready` deltaP `20.9677` edge `0.6332` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.5023` n `31` status `ready` deltaP `29.9076` edge `0.3072` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.1493` n `31` status `ready` deltaP `14.3391` edge `0.7063` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.6742` n `31` status `ready` deltaP `38.6762` edge `0.1445` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.6092` n `31` status `ready` deltaP `12.1877` edge `0.247` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.3528` n `31` status `ready` deltaP `28.993` edge `0.0288` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.2612` n `31` status `ready` deltaP `27.8009` edge `0.0116` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.2586` n `31` status `ready` deltaP `15.3467` edge `0.1046` maxDD `-0.1621`
- `news_risk_high->index_24h` score `2.204` n `31` status `ready` deltaP `24.6101` edge `0.0196` maxDD `0.0`
- `news_risk_high->crypto_major_1h` score `1.9411` n `31` status `ready` deltaP `6.4178` edge `0.2522` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.7133` n `31` status `ready` deltaP `8.6633` edge `0.1976` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1325` n `31` status `ready` deltaP `24.6426` edge `0.0088` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.4165` n `31` status `ready` deltaP `10.0462` edge `0.0262` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.3578` n `31` status `ready` deltaP `11.5952` edge `0.0243` maxDD `-0.7918`
- `news_risk_high->commodity_1h` score `-0.3376` n `31` status `ready` deltaP `-2.062` edge `0.0118` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
