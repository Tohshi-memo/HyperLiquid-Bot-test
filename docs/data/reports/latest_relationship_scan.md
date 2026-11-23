# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T22:07:37.511972+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4560`

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

- `market_context_high->unknown_1h` score `32432.2381` n `45` status `ready` deltaP `2.6147` edge `2702.6785` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22262.559` n `45` status `ready` deltaP `3.4824` edge `1855.2039` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1222.7087` n `31` status `ready` deltaP `2.8298` edge `101.8911` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1027.2058` n `31` status `ready` deltaP `4.701` edge `85.5748` maxDD `-0.119`
- `news_risk_high->equity_24h` score `38.9775` n `31` status `ready` deltaP `43.9236` edge `2.9553` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `34.9692` n `31` status `ready` deltaP `45.6597` edge `2.6097` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.888` n `31` status `ready` deltaP `45.6597` edge `2.2696` maxDD `0.0`
- `news_risk_high->metal_24h` score `12.3965` n `31` status `ready` deltaP `45.2285` edge `0.759` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.2194` n `31` status `ready` deltaP `22.4921` edge `0.7887` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.6769` n `31` status `ready` deltaP `30.9747` edge `0.5648` maxDD `-2.1911`
- `news_risk_high->fx_24h` score `6.4779` n `31` status `ready` deltaP `55.2532` edge `0.1843` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.2872` n `31` status `ready` deltaP `12.3574` edge `0.8654` maxDD `-7.6714`
- `news_risk_high->index_24h` score `6.0148` n `31` status `ready` deltaP `41.8403` edge `0.2223` maxDD `0.0`
- `market_context_high->fx_4h` score `3.2927` n `45` status `ready` deltaP `39.2344` edge `0.0413` maxDD `-0.2774`
- `news_risk_high->equity_1h` score `3.2169` n `31` status `ready` deltaP `17.8916` edge `0.1675` maxDD `-0.163`
- `news_risk_high->index_4h` score `2.9405` n `31` status `ready` deltaP `32.499` edge `0.0544` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.5177` n `31` status `ready` deltaP `30.0464` edge `0.018` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.5007` n `31` status `ready` deltaP `11.0585` edge `0.293` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.1312` n `31` status `ready` deltaP `10.4597` edge `0.2392` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5625` n `31` status `ready` deltaP `30.1815` edge `0.027` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
