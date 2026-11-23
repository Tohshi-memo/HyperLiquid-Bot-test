# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T19:22:39.350138+00:00`
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

- `market_context_high->unknown_1h` score `32458.1413` n `45` status `ready` deltaP `2.6147` edge `2704.8371` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22298.5002` n `45` status `ready` deltaP `3.4824` edge `1858.199` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1248.6119` n `31` status `ready` deltaP `2.8298` edge `104.0497` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1063.147` n `31` status `ready` deltaP `4.701` edge `88.5699` maxDD `-0.119`
- `news_risk_high->equity_24h` score `40.6889` n `31` status `ready` deltaP `45.4861` edge `3.0875` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `35.4089` n `31` status `ready` deltaP `46.7014` edge `2.6394` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `31.284` n `31` status `ready` deltaP `46.875` edge `2.2945` maxDD `0.0`
- `news_risk_high->metal_24h` score `12.683` n `31` status `ready` deltaP `46.9646` edge `0.7713` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `9.8868` n `31` status `ready` deltaP `22.3397` edge `0.762` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.5599` n `31` status `ready` deltaP `30.5173` edge `0.5581` maxDD `-2.1911`
- `news_risk_high->index_24h` score `6.3248` n `31` status `ready` deltaP `43.75` edge `0.2354` maxDD `0.0`
- `news_risk_high->fx_24h` score `6.2951` n `31` status `ready` deltaP `53.3434` edge `0.1818` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.0249` n `31` status `ready` deltaP `12.0525` edge `0.8338` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.2672` n `31` status `ready` deltaP `18.191` edge `0.1697` maxDD `-0.163`
- `market_context_high->fx_4h` score `3.1844` n `45` status `ready` deltaP `38.0149` edge `0.0404` maxDD `-0.2774`
- `news_risk_high->index_4h` score `2.9089` n `31` status `ready` deltaP `32.1942` edge `0.0538` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.532` n `31` status `ready` deltaP `30.1961` edge `0.0182` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.3947` n `31` status `ready` deltaP `10.4597` edge `0.2834` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0111` n `31` status `ready` deltaP `9.4118` edge `0.2308` maxDD `-1.5232`
- `market_context_high->commodity_24h` score `2.0015` n `38` status `ready` deltaP `5.0622` edge `0.3049` maxDD `-2.5636`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
