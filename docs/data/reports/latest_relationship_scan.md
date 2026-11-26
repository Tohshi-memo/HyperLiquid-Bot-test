# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T18:07:29.722241+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3419`

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

- `news_risk_high->unknown_1h` score `3224.3772` n `31` status `ready` deltaP `2.0813` edge `268.7018` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3218.0296` n `31` status `ready` deltaP `4.2437` edge `268.1465` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `31.0471` n `31` status `ready` deltaP `40.1042` edge `2.3199` maxDD `0.0`
- `news_risk_high->equity_24h` score `28.6317` n `31` status `ready` deltaP `39.2361` edge `2.1244` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `24.8548` n `31` status `ready` deltaP `39.4097` edge `1.8085` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.3617` n `31` status `ready` deltaP `25.8457` edge `0.7782` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `9.3823` n `31` status `ready` deltaP `37.682` edge `0.5787` maxDD `-2.178`
- `news_risk_high->metal_24h` score `7.1521` n `31` status `ready` deltaP `25.7841` edge `0.4516` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.7364` n `31` status `ready` deltaP `18.7598` edge `0.8803` maxDD `-7.6714`
- `news_risk_high->index_24h` score `4.9972` n `31` status `ready` deltaP `40.625` edge `0.1456` maxDD `0.0`
- `news_risk_high->fx_24h` score `4.8155` n `31` status `ready` deltaP `40.3226` edge `0.1453` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.525` n `31` status `ready` deltaP `20.2868` edge `0.1772` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.261` n `31` status `ready` deltaP `36.31` edge `0.0557` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7081` n `31` status `ready` deltaP `32.2919` edge `0.0189` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4455` n `31` status `ready` deltaP `9.4118` edge `0.2969` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.1832` n `31` status `ready` deltaP `12.4058` edge `0.2329` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.4394` n `31` status `ready` deltaP `28.5348` edge `0.0222` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.8805` n `31` status `ready` deltaP `14.4915` edge `0.072` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.3008` n `31` status `ready` deltaP `10.656` edge `0.0073` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.4239` n `31` status `ready` deltaP `-2.5111` edge `0.0076` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
