# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T10:07:23.662365+00:00`
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

- `news_risk_high->unknown_1h` score `3237.7825` n `31` status `ready` deltaP `1.6322` edge `269.8219` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3191.641` n `31` status `ready` deltaP `3.7864` edge `265.9505` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `19.0937` n `31` status `ready` deltaP `29.1667` edge `1.3967` maxDD `0.0`
- `news_risk_high->equity_24h` score `17.0601` n `31` status `ready` deltaP `28.6458` edge `1.2307` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `14.1835` n `31` status `ready` deltaP `28.2986` edge `0.9933` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.6335` n `31` status `ready` deltaP `20.9677` edge `0.6667` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `6.4957` n `31` status `ready` deltaP `30.6698` edge `0.3849` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.4836` n `31` status `ready` deltaP `13.8818` edge `0.7522` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `4.91` n `31` status `ready` deltaP `16.5827` edge `0.3261` maxDD `-0.1986`
- `news_risk_high->fx_24h` score `4.6322` n `31` status `ready` deltaP `38.5865` edge `0.1416` maxDD `-0.0262`
- `news_risk_high->index_24h` score `3.0887` n `31` status `ready` deltaP `30.2083` edge `0.056` maxDD `0.0`
- `news_risk_high->equity_1h` score `2.5921` n `31` status `ready` deltaP `16.2449` edge `0.1264` maxDD `-0.1621`
- `news_risk_high->index_4h` score `2.5762` n `31` status `ready` deltaP `30.06` edge `0.0403` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.411` n `31` status `ready` deltaP `29.1482` edge `0.0151` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.0379` n `31` status `ready` deltaP `6.4178` edge `0.2646` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.838` n `31` status `ready` deltaP `9.5615` edge `0.2076` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1543` n `31` status `ready` deltaP `24.942` edge `0.0096` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.3649` n `31` status `ready` deltaP `11.7476` edge `0.0242` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `-0.0147` n `31` status `ready` deltaP `6.3877` edge `-0.0047` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.6515` n `31` status `ready` deltaP `-4.7566` edge `0.0036` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
