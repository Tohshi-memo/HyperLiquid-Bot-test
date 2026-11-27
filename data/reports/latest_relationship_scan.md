# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T15:52:32.974690+00:00`
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

- `news_risk_high->unknown_1h` score `3268.7029` n `31` status `ready` deltaP `1.4825` edge `272.3996` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3169.3241` n `31` status `ready` deltaP `3.3291` edge `264.0938` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `16.1802` n `31` status `ready` deltaP `25.8681` edge `1.1759` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.5714` n `31` status `ready` deltaP `24.6528` edge `0.9666` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `11.7848` n `31` status `ready` deltaP `25.0` edge `0.8154` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `7.7517` n `31` status `ready` deltaP `20.2055` edge `0.5983` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.7597` n `31` status `ready` deltaP `30.3649` edge `0.3256` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `4.8308` n `31` status `ready` deltaP `13.1196` edge `0.6736` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.6346` n `31` status `ready` deltaP `38.5865` edge `0.1418` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.9997` n `31` status `ready` deltaP `12.7633` edge `0.2757` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.4922` n `31` status `ready` deltaP `30.06` edge `0.0333` maxDD `-0.4146`
- `news_risk_high->equity_1h` score `2.4553` n `31` status `ready` deltaP `15.7958` edge `0.118` maxDD `-0.1621`
- `news_risk_high->index_24h` score `2.4548` n `31` status `ready` deltaP `26.2153` edge `0.0298` maxDD `0.0`
- `news_risk_high->index_1h` score `2.3487` n `31` status `ready` deltaP `28.5494` edge `0.0139` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `1.9513` n `31` status `ready` deltaP `6.2681` edge `0.2545` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.728` n `31` status `ready` deltaP `9.1124` edge `0.1965` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.2018` n `31` status `ready` deltaP `25.6905` edge `0.0107` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.3349` n `31` status `ready` deltaP `11.2903` edge `0.0234` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.2022` n `31` status `ready` deltaP `8.3694` edge `0.0099` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.4874` n `31` status `ready` deltaP `-3.2596` edge `0.0073` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
