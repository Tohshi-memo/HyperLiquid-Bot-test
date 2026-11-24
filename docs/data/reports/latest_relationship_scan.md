# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T01:07:25.050888+00:00`
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

- `market_context_high->unknown_1h` score `32401.7773` n `45` status `ready` deltaP `2.6147` edge `2700.1401` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22239.403` n `45` status `ready` deltaP `3.7873` edge `1853.2722` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1192.2479` n `31` status `ready` deltaP `2.8298` edge `99.3527` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1004.0498` n `31` status `ready` deltaP `5.0059` edge `83.6431` maxDD `-0.119`
- `news_risk_high->equity_24h` score `37.8224` n `31` status `ready` deltaP `43.75` edge `2.8602` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `34.9913` n `31` status `ready` deltaP `45.4861` edge `2.6127` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.942` n `31` status `ready` deltaP `45.6597` edge `2.2741` maxDD `0.0`
- `news_risk_high->metal_24h` score `12.1606` n `31` status `ready` deltaP `43.8396` edge `0.7486` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.6376` n `31` status `ready` deltaP `23.864` edge `0.8144` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.7069` n `31` status `ready` deltaP `30.9747` edge `0.5673` maxDD `-2.1911`
- `news_risk_high->fx_24h` score `6.6147` n `31` status `ready` deltaP `56.4684` edge `0.1876` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.4917` n `31` status `ready` deltaP `13.4244` edge `0.8845` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.8797` n `31` status `ready` deltaP `41.6667` edge `0.2122` maxDD `0.0`
- `market_context_high->fx_4h` score `3.3061` n `45` status `ready` deltaP `39.3868` edge `0.0414` maxDD `-0.2774`
- `news_risk_high->equity_1h` score `3.1905` n `31` status `ready` deltaP `17.7419` edge `0.1663` maxDD `-0.163`
- `news_risk_high->index_4h` score `2.9089` n `31` status `ready` deltaP `32.1942` edge `0.0538` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.4769` n `31` status `ready` deltaP `29.5973` edge `0.0176` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4742` n `31` status `ready` deltaP `10.9088` edge `0.2906` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0727` n `31` status `ready` deltaP `9.8609` edge `0.2357` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5438` n `31` status `ready` deltaP `29.8821` edge `0.0266` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
