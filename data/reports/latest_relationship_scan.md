# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T03:52:24.740861+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3552`

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

- `news_risk_high->unknown_1h` score `3219.3912` n `31` status `ready` deltaP `1.7819` edge `268.2883` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3191.909` n `31` status `ready` deltaP `4.0913` edge `265.9708` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `24.691` n `31` status `ready` deltaP `33.5069` edge `1.8342` maxDD `0.0`
- `news_risk_high->equity_24h` score `21.9577` n `31` status `ready` deltaP `32.9861` edge `1.6099` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `18.8555` n `31` status `ready` deltaP `32.6389` edge `1.3537` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.269` n `31` status `ready` deltaP `23.4067` edge `0.7034` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `7.686` n `31` status `ready` deltaP `33.4137` edge `0.4658` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `6.0574` n `31` status `ready` deltaP `16.4732` edge `0.8085` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `5.9315` n `31` status `ready` deltaP `20.5758` edge `0.3846` maxDD `-0.1986`
- `news_risk_high->fx_24h` score `4.8349` n `31` status `ready` deltaP `40.6698` edge `0.1446` maxDD `-0.0262`
- `news_risk_high->index_24h` score `3.8787` n `31` status `ready` deltaP `34.5486` edge `0.0929` maxDD `0.0`
- `news_risk_high->equity_1h` score `2.8055` n `31` status `ready` deltaP `17.1431` edge `0.1382` maxDD `-0.1621`
- `news_risk_high->index_4h` score `2.7508` n `31` status `ready` deltaP `31.432` edge `0.0457` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.4374` n `31` status `ready` deltaP `29.4476` edge `0.0153` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.0604` n `31` status `ready` deltaP `6.7172` edge `0.2655` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.8426` n `31` status `ready` deltaP `9.8609` edge `0.2062` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1963` n `31` status `ready` deltaP `25.8402` edge `0.009` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.5013` n `31` status `ready` deltaP `12.5098` edge `0.0366` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.0908` n `31` status `ready` deltaP `7.6072` edge `0.0007` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.5545` n `31` status `ready` deltaP `-3.8584` edge `0.0057` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
