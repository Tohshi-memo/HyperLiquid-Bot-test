# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T20:07:29.808563+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4652`

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

- `market_context_high->unknown_1h` score `32463.9829` n `45` status `ready` deltaP `2.6147` edge `2705.3239` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22300.4574` n `45` status `ready` deltaP `3.4824` edge `1858.3621` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1254.4535` n `31` status `ready` deltaP `2.8298` edge `104.5365` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1065.1042` n `31` status `ready` deltaP `4.701` edge `88.733` maxDD `-0.119`
- `news_risk_high->equity_24h` score `40.178` n `31` status `ready` deltaP `44.9653` edge `3.0484` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `35.2575` n `31` status `ready` deltaP `46.3542` edge `2.6291` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `31.1115` n `31` status `ready` deltaP `46.3542` edge `2.2836` maxDD `0.0`
- `news_risk_high->metal_24h` score `12.5981` n `31` status `ready` deltaP `46.4438` edge `0.7677` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.0142` n `31` status `ready` deltaP `22.4921` edge `0.7716` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.6043` n `31` status `ready` deltaP `30.5173` edge `0.5618` maxDD `-2.1911`
- `news_risk_high->fx_24h` score `6.344` n `31` status `ready` deltaP `53.8643` edge `0.1824` maxDD `-0.0262`
- `news_risk_high->index_24h` score `6.2363` n `31` status `ready` deltaP `43.2292` edge `0.2315` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `6.1562` n `31` status `ready` deltaP `12.3574` edge `0.8486` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.2696` n `31` status `ready` deltaP `18.191` edge `0.1699` maxDD `-0.163`
- `market_context_high->fx_4h` score `3.2002` n `45` status `ready` deltaP `38.1673` edge `0.0407` maxDD `-0.2774`
- `news_risk_high->index_4h` score `2.9125` n `31` status `ready` deltaP `32.1942` edge `0.0541` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.5332` n `31` status `ready` deltaP `30.1961` edge `0.0183` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4391` n `31` status `ready` deltaP `10.7591` edge `0.2871` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0548` n `31` status `ready` deltaP `9.7112` edge `0.2344` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5282` n `31` status `ready` deltaP `29.5827` edge `0.0266` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
