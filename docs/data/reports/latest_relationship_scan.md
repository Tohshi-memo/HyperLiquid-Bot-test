# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T03:07:31.195492+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7162`

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

- `news_risk_high->unknown_24h` score `1221.778` n `132` status `ready` deltaP `1.9097` edge `101.8021` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.3494` n `132` status `ready` deltaP `30.9501` edge `1.5104` maxDD `-1.0093`
- `news_risk_high->crypto_major_24h` score `9.3659` n `132` status `ready` deltaP `25.9312` edge `0.923` maxDD `-15.8971`
- `news_risk_high->equity_24h` score `9.1077` n `132` status `ready` deltaP `30.4451` edge `0.7909` maxDD `-9.4579`
- `news_risk_high->index_24h` score `4.1887` n `132` status `ready` deltaP `36.8055` edge `0.1515` maxDD `-0.4916`
- `news_risk_high->equity_4h` score `2.9448` n `135` status `ready` deltaP `29.6285` edge `0.208` maxDD `-9.143`
- `news_risk_high->metal_24h` score `2.5131` n `132` status `ready` deltaP `28.4091` edge `0.2602` maxDD `-2.192`
- `news_risk_high->crypto_alt_4h` score `2.1316` n `135` status `ready` deltaP `12.1793` edge `0.3624` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `1.1306` n `135` status `ready` deltaP `9.4012` edge `0.1226` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.9379` n `135` status `ready` deltaP `9.7006` edge `0.0758` maxDD `-1.6514`
- `news_risk_high->index_1h` score `0.5209` n `135` status `ready` deltaP `9.1173` edge `0.0114` maxDD `-0.302`
- `news_risk_high->index_4h` score `-0.0615` n `135` status `ready` deltaP `7.7111` edge `0.0288` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.4826` n `135` status `ready` deltaP `1.1577` edge `0.015` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.4844` n `135` status `ready` deltaP `2.6391` edge `0.0703` maxDD `-7.2607`
- `news_risk_high->metal_4h` score `-1.2358` n `135` status `ready` deltaP `-7.2369` edge `0.0306` maxDD `-2.9297`
- `news_risk_high->crypto_major_4h` score `-1.4108` n `135` status `ready` deltaP `-3.0736` edge `0.1111` maxDD `-13.719`
- `news_risk_high->fx_4h` score `-1.4669` n `135` status `ready` deltaP `6.3132` edge `-0.0088` maxDD `-3.0414`
- `news_risk_high->commodity_1h` score `-1.8195` n `135` status `ready` deltaP `-8.5185` edge `-0.009` maxDD `-3.3986`
- `news_risk_high->fx_1h` score `-1.8781` n `135` status `ready` deltaP `-9.654` edge `-0.0041` maxDD `-1.0436`
- `news_risk_high->commodity_4h` score `-2.2466` n `135` status `ready` deltaP `-8.8449` edge `0.0128` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
