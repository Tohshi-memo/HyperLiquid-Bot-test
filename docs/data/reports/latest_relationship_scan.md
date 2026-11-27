# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T17:22:27.118893+00:00`
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

- `news_risk_high->unknown_1h` score `3279.9973` n `31` status `ready` deltaP `1.6322` edge `273.3398` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3184.4429` n `31` status `ready` deltaP `3.3291` edge `265.3537` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `16.167` n `31` status `ready` deltaP `25.8681` edge `1.1748` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.1091` n `31` status `ready` deltaP `23.9583` edge `0.9327` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `11.8244` n `31` status `ready` deltaP `25.0` edge `0.8187` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `7.8465` n `31` status `ready` deltaP `20.2055` edge `0.6062` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.6241` n `31` status `ready` deltaP `30.3649` edge `0.3143` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `4.8418` n `31` status `ready` deltaP `13.1196` edge `0.675` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.6382` n `31` status `ready` deltaP `38.5865` edge `0.1421` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.8812` n `31` status `ready` deltaP `12.2424` edge `0.2693` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.4378` n `31` status `ready` deltaP `29.7551` edge `0.0308` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.3398` n `31` status `ready` deltaP `25.3472` edge `0.026` maxDD `0.0`
- `news_risk_high->index_1h` score `2.2852` n `31` status `ready` deltaP `27.9506` edge `0.0126` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.2826` n `31` status `ready` deltaP `15.197` edge `0.1076` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `1.8772` n `31` status `ready` deltaP `5.9687` edge `0.247` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.6602` n `31` status `ready` deltaP `8.5136` edge `0.1918` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.18` n `31` status `ready` deltaP `25.3911` edge `0.0099` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.3474` n `31` status `ready` deltaP `11.2903` edge `0.025` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.3098` n `31` status `ready` deltaP `9.284` edge `0.0176` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.4191` n `31` status `ready` deltaP `-2.6608` edge `0.009` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
