# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T04:37:26.270851+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3646`

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

- `news_risk_high->unknown_1h` score `3326.9833` n `31` status `ready` deltaP `1.4825` edge `277.2563` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3180.8817` n `31` status `ready` deltaP `3.634` edge `265.0549` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `18.8272` n `31` status `ready` deltaP `29.8094` edge `1.3702` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `13.0208` n `31` status `ready` deltaP `27.7296` edge `0.9002` maxDD `0.0`
- `news_risk_high->equity_24h` score `11.3561` n `31` status `ready` deltaP `23.9168` edge `0.7869` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `7.2573` n `31` status `ready` deltaP `19.2909` edge `0.5632` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `4.9834` n `31` status `ready` deltaP `27.621` edge `0.2792` maxDD `-2.178`
- `news_risk_high->fx_24h` score `4.7366` n `31` status `ready` deltaP `38.6762` edge `0.1497` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `4.4651` n `31` status `ready` deltaP `13.272` edge `0.6257` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `3.3512` n `31` status `ready` deltaP `12.1877` edge `0.2255` maxDD `-0.1986`
- `news_risk_high->index_1h` score `2.1954` n `31` status `ready` deltaP `27.0524` edge `0.0111` maxDD `-0.0136`
- `news_risk_high->index_24h` score `2.1764` n `31` status `ready` deltaP `24.6101` edge `0.0173` maxDD `0.0`
- `news_risk_high->index_4h` score `2.1703` n `31` status `ready` deltaP `27.0112` edge `0.0268` maxDD `-0.4146`
- `news_risk_high->equity_1h` score `2.0392` n `31` status `ready` deltaP `13.9994` edge `0.0953` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `1.6441` n `31` status `ready` deltaP `4.9208` edge `0.2241` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.5316` n `31` status `ready` deltaP `8.2142` edge `0.1773` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.0772` n `31` status `ready` deltaP `23.7444` edge `0.0077` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.3444` n `31` status `ready` deltaP `8.6743` edge `0.0261` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.215` n `31` status `ready` deltaP `9.6135` edge `0.0192` maxDD `-0.7918`
- `news_risk_high->commodity_1h` score `-0.3627` n `31` status `ready` deltaP `-2.3614` edge `0.0117` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
