# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T08:37:33.960238+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3348`

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

- `news_risk_high->unknown_1h` score `3224.8669` n `31` status `ready` deltaP `1.6322` edge `268.7456` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3183.199` n `31` status `ready` deltaP `3.7864` edge `265.247` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `20.3111` n `31` status `ready` deltaP `30.2083` edge `1.4912` maxDD `0.0`
- `news_risk_high->equity_24h` score `18.2234` n `31` status `ready` deltaP `29.6875` edge `1.3207` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.234` n `31` status `ready` deltaP `29.3403` edge `1.0739` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.8468` n `31` status `ready` deltaP `21.7299` edge `0.6794` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `6.6607` n `31` status `ready` deltaP `31.1271` edge `0.3956` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.6183` n `31` status `ready` deltaP `14.644` edge `0.7644` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `5.195` n `31` status `ready` deltaP `17.6244` edge `0.3429` maxDD `-0.1986`
- `news_risk_high->fx_24h` score `4.631` n `31` status `ready` deltaP `38.5865` edge `0.1415` maxDD `-0.0262`
- `news_risk_high->index_24h` score `3.2764` n `31` status `ready` deltaP `31.25` edge `0.0647` maxDD `0.0`
- `news_risk_high->equity_1h` score `2.6341` n `31` status `ready` deltaP `16.3946` edge `0.1289` maxDD `-0.1621`
- `news_risk_high->index_4h` score `2.6102` n `31` status `ready` deltaP `30.3649` edge `0.0411` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.4134` n `31` status `ready` deltaP `29.1482` edge `0.0153` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.0363` n `31` status `ready` deltaP `6.4178` edge `0.2644` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.8567` n `31` status `ready` deltaP `9.7112` edge `0.209` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1512` n `31` status `ready` deltaP `24.942` edge `0.0092` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.4137` n `31` status `ready` deltaP `12.2049` edge `0.0274` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `-0.1083` n `31` status `ready` deltaP `5.473` edge `-0.0106` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.6971` n `31` status `ready` deltaP `-5.2057` edge `0.0028` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
