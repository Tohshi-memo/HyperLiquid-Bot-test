# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T00:22:28.030885+00:00`
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

- `market_context_high->unknown_1h` score `32410.8901` n `45` status `ready` deltaP `2.6147` edge `2700.8995` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22242.9198` n `45` status `ready` deltaP `3.4824` edge `1853.5673` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1201.3607` n `31` status `ready` deltaP `2.8298` edge `100.1121` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1007.5666` n `31` status `ready` deltaP `4.701` edge `83.9382` maxDD `-0.119`
- `news_risk_high->equity_24h` score `38.0948` n `31` status `ready` deltaP `43.75` edge `2.8829` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `34.9673` n `31` status `ready` deltaP `45.4861` edge `2.6107` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.9336` n `31` status `ready` deltaP `45.6597` edge `2.2734` maxDD `0.0`
- `news_risk_high->metal_24h` score `12.249` n `31` status `ready` deltaP `44.3605` edge `0.7525` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.5362` n `31` status `ready` deltaP `23.4067` edge `0.809` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.6971` n `31` status `ready` deltaP `30.8222` edge `0.5675` maxDD `-2.1911`
- `news_risk_high->fx_24h` score `6.6099` n `31` status `ready` deltaP `56.4684` edge `0.1872` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.425` n `31` status `ready` deltaP `12.9671` edge `0.879` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.9097` n `31` status `ready` deltaP `41.6667` edge `0.2147` maxDD `0.0`
- `market_context_high->fx_4h` score `3.3341` n `45` status `ready` deltaP `39.6917` edge `0.0417` maxDD `-0.2774`
- `news_risk_high->equity_1h` score `3.2013` n `31` status `ready` deltaP `17.7419` edge `0.1672` maxDD `-0.163`
- `news_risk_high->index_4h` score `2.9271` n `31` status `ready` deltaP `32.3466` edge `0.0543` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.4949` n `31` status `ready` deltaP `29.747` edge `0.0181` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4625` n `31` status `ready` deltaP `10.7591` edge `0.2901` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.068` n `31` status `ready` deltaP `9.8609` edge `0.2351` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5461` n `31` status `ready` deltaP `29.8821` edge `0.0269` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
