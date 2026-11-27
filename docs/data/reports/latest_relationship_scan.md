# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T12:22:26.031396+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `2886`

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

- `news_risk_high->unknown_1h` score `3251.3881` n `31` status `ready` deltaP `1.4825` edge `270.9567` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3183.5194` n `31` status `ready` deltaP `3.7864` edge `265.2737` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `17.3775` n `31` status `ready` deltaP `27.6042` edge `1.2641` maxDD `0.0`
- `news_risk_high->equity_24h` score `15.4267` n `31` status `ready` deltaP `27.0833` edge `1.105` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `12.7877` n `31` status `ready` deltaP `26.7361` edge `0.8874` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.2299` n `31` status `ready` deltaP `20.6628` edge `0.6351` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `6.2865` n `31` status `ready` deltaP `30.3649` edge `0.3695` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.174` n `31` status `ready` deltaP `13.1196` edge `0.7176` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.6346` n `31` status `ready` deltaP `38.5865` edge `0.1418` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `4.4742` n `31` status `ready` deltaP `15.0202` edge `0.3002` maxDD `-0.1986`
- `news_risk_high->index_24h` score `2.8173` n `31` status `ready` deltaP `28.6458` edge `0.0438` maxDD `0.0`
- `news_risk_high->index_4h` score `2.5654` n `31` status `ready` deltaP `30.06` edge `0.0394` maxDD `-0.4146`
- `news_risk_high->equity_1h` score `2.5489` n `31` status `ready` deltaP `15.9455` edge `0.1248` maxDD `-0.1621`
- `news_risk_high->index_1h` score `2.3571` n `31` status `ready` deltaP `28.5494` edge `0.0146` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `1.9747` n `31` status `ready` deltaP `6.1184` edge `0.2585` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.7803` n `31` status `ready` deltaP `9.2621` edge `0.2022` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1621` n `31` status `ready` deltaP `25.0917` edge `0.0096` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.3232` n `31` status `ready` deltaP `11.2903` edge `0.0219` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.0474` n `31` status `ready` deltaP `6.9974` edge `-0.0008` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.5509` n `31` status `ready` deltaP `-3.8584` edge `0.006` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
