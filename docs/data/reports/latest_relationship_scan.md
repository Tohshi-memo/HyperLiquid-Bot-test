# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T16:52:27.514643+00:00`
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

- `news_risk_high->unknown_1h` score `3277.2049` n `31` status `ready` deltaP `1.6322` edge `273.1071` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3180.0605` n `31` status `ready` deltaP `3.3291` edge `264.9885` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `16.1298` n `31` status `ready` deltaP `25.8681` edge `1.1717` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.2135` n `31` status `ready` deltaP `23.9583` edge `0.9414` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `11.7812` n `31` status `ready` deltaP `25.0` edge `0.8151` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `7.7973` n `31` status `ready` deltaP `20.2055` edge `0.6021` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.6289` n `31` status `ready` deltaP `30.3649` edge `0.3147` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `4.8246` n `31` status `ready` deltaP `13.1196` edge `0.6728` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.637` n `31` status `ready` deltaP `38.5865` edge `0.142` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.904` n `31` status `ready` deltaP `12.2424` edge `0.2712` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.4438` n `31` status `ready` deltaP `29.7551` edge `0.0313` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.3657` n `31` status `ready` deltaP `25.5208` edge `0.027` maxDD `0.0`
- `news_risk_high->index_1h` score `2.2864` n `31` status `ready` deltaP `27.9506` edge `0.0127` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.2778` n `31` status `ready` deltaP `15.197` edge `0.1072` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `1.8523` n `31` status `ready` deltaP `5.6693` edge `0.2458` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.6439` n `31` status `ready` deltaP `8.5136` edge `0.1897` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1893` n `31` status `ready` deltaP `25.5408` edge `0.0101` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.3435` n `31` status `ready` deltaP `11.2903` edge `0.0245` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.2768` n `31` status `ready` deltaP `8.9791` edge `0.0154` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.4203` n `31` status `ready` deltaP `-2.6608` edge `0.0089` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
