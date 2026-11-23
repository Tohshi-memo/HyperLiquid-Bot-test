# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T18:52:30.418327+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4518`

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

- `market_context_high->unknown_1h` score `32452.2949` n `45` status `ready` deltaP `2.6147` edge `2704.3499` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22296.9066` n `45` status `ready` deltaP `3.4824` edge `1858.0662` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1242.7655` n `31` status `ready` deltaP `2.8298` edge `103.5625` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1061.5534` n `31` status `ready` deltaP `4.701` edge `88.4371` maxDD `-0.119`
- `news_risk_high->equity_24h` score `41.0515` n `31` status `ready` deltaP `45.8333` edge `3.1154` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `35.5459` n `31` status `ready` deltaP `47.0486` edge `2.6485` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `31.4354` n `31` status `ready` deltaP `47.2222` edge `2.3048` maxDD `0.0`
- `news_risk_high->metal_24h` score `12.7408` n `31` status `ready` deltaP `47.3119` edge `0.7738` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `9.7978` n `31` status `ready` deltaP `22.1872` edge `0.7556` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.5479` n `31` status `ready` deltaP `30.5173` edge `0.5571` maxDD `-2.1911`
- `news_risk_high->index_24h` score `6.3862` n `31` status `ready` deltaP `44.0972` edge `0.2382` maxDD `0.0`
- `news_risk_high->fx_24h` score `6.2626` n `31` status `ready` deltaP `52.9962` edge `0.1814` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `5.9225` n `31` status `ready` deltaP `11.7476` edge `0.8227` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.2624` n `31` status `ready` deltaP `18.191` edge `0.1693` maxDD `-0.163`
- `market_context_high->fx_4h` score `3.1698` n `45` status `ready` deltaP `37.8624` edge `0.0402` maxDD `-0.2774`
- `news_risk_high->index_4h` score `2.9089` n `31` status `ready` deltaP `32.1942` edge `0.0538` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.5452` n `31` status `ready` deltaP `30.3458` edge `0.0183` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.3768` n `31` status `ready` deltaP `10.31` edge `0.2821` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9917` n `31` status `ready` deltaP `9.2621` edge `0.2293` maxDD `-1.5232`
- `market_context_high->commodity_24h` score `1.9343` n `38` status `ready` deltaP `4.7149` edge `0.2986` maxDD `-2.5636`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
