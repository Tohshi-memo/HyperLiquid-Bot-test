# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T15:37:28.884498+00:00`
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

- `news_risk_high->unknown_1h` score `3268.3429` n `31` status `ready` deltaP `1.4825` edge `272.3696` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3168.8801` n `31` status `ready` deltaP `3.3291` edge `264.0568` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `16.179` n `31` status `ready` deltaP `25.8681` edge `1.1758` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.6621` n `31` status `ready` deltaP `24.8264` edge `0.973` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `11.7668` n `31` status `ready` deltaP `25.0` edge `0.8139` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `7.7253` n `31` status `ready` deltaP `20.2055` edge `0.5961` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.7897` n `31` status `ready` deltaP `30.3649` edge `0.3281` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `4.823` n `31` status `ready` deltaP `13.1196` edge `0.6726` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.6334` n `31` status `ready` deltaP `38.5865` edge `0.1417` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `4.028` n `31` status `ready` deltaP `12.9369` edge `0.2769` maxDD `-0.1986`
- `news_risk_high->equity_1h` score `2.5069` n `31` status `ready` deltaP `15.9455` edge `0.1213` maxDD `-0.1621`
- `news_risk_high->index_4h` score `2.4994` n `31` status `ready` deltaP `30.06` edge `0.0339` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.4783` n `31` status `ready` deltaP `26.3889` edge `0.0306` maxDD `0.0`
- `news_risk_high->index_1h` score `2.3655` n `31` status `ready` deltaP `28.6991` edge `0.0143` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `1.956` n `31` status `ready` deltaP `6.2681` edge `0.2551` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.7265` n `31` status `ready` deltaP `9.1124` edge `0.1963` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.2026` n `31` status `ready` deltaP `25.6905` edge `0.0108` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.3326` n `31` status `ready` deltaP `11.2903` edge `0.0231` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.1849` n `31` status `ready` deltaP `8.2169` edge `0.0087` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.5029` n `31` status `ready` deltaP `-3.4093` edge `0.007` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
