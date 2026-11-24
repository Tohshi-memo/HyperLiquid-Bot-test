# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T01:37:26.431353+00:00`
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

- `market_context_high->unknown_1h` score `32393.7517` n `45` status `ready` deltaP `2.6147` edge `2699.4713` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22235.582` n `45` status `ready` deltaP `3.6349` edge `1852.9548` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1184.2223` n `31` status `ready` deltaP `2.8298` edge `98.6839` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1000.2288` n `31` status `ready` deltaP `4.8535` edge `83.3257` maxDD `-0.119`
- `news_risk_high->equity_24h` score `37.5716` n `31` status `ready` deltaP `43.75` edge `2.8393` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `34.9469` n `31` status `ready` deltaP `45.4861` edge `2.609` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.9024` n `31` status `ready` deltaP `45.6597` edge `2.2708` maxDD `0.0`
- `news_risk_high->metal_24h` score `12.0992` n `31` status `ready` deltaP `43.4924` edge `0.7458` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.658` n `31` status `ready` deltaP `23.864` edge `0.8161` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.6769` n `31` status `ready` deltaP `30.9747` edge `0.5648` maxDD `-2.1911`
- `news_risk_high->fx_24h` score `6.6171` n `31` status `ready` deltaP `56.4684` edge `0.1878` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.505` n `31` status `ready` deltaP `13.4244` edge `0.8862` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.822` n `31` status `ready` deltaP `41.3194` edge `0.2097` maxDD `0.0`
- `market_context_high->fx_4h` score `3.2782` n `45` status `ready` deltaP `39.082` edge `0.0411` maxDD `-0.2774`
- `news_risk_high->equity_1h` score `3.1509` n `31` status `ready` deltaP `17.5922` edge `0.164` maxDD `-0.163`
- `news_risk_high->index_4h` score `2.8762` n `31` status `ready` deltaP `31.8893` edge `0.0531` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.4602` n `31` status `ready` deltaP `29.4476` edge `0.0172` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4477` n `31` status `ready` deltaP `10.7591` edge `0.2882` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0657` n `31` status `ready` deltaP `9.8609` edge `0.2348` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5446` n `31` status `ready` deltaP `29.8821` edge `0.0267` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
