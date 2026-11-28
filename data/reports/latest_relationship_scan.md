# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T09:22:26.779103+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3716`

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

- `news_risk_high->unknown_1h` score `3380.6592` n `31` status `ready` deltaP `1.9316` edge `281.7263` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3244.2034` n `31` status `ready` deltaP `3.7864` edge `270.3307` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `21.5458` n `31` status `ready` deltaP `33.1023` edge `1.5748` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.4382` n `31` status `ready` deltaP `31.0225` edge `1.0797` maxDD `0.0`
- `news_risk_high->equity_24h` score `12.1161` n `31` status `ready` deltaP `26.5165` edge `0.8329` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.3008` n `31` status `ready` deltaP `21.7299` edge `0.6339` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.3305` n `31` status `ready` deltaP `29.7551` edge `0.2939` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.1442` n `31` status `ready` deltaP `15.711` edge `0.6965` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.9407` n `31` status `ready` deltaP `40.5826` edge `0.154` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.7027` n `31` status `ready` deltaP `14.9606` edge `0.2363` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.365` n `31` status `ready` deltaP `29.1454` edge `0.0288` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.3287` n `31` status `ready` deltaP `25.8232` edge `0.0219` maxDD `0.0`
- `news_risk_high->index_1h` score `2.2996` n `31` status `ready` deltaP `28.25` edge `0.0118` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.1232` n `31` status `ready` deltaP `14.1491` edge `0.1013` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `1.8593` n `31` status `ready` deltaP `5.9687` edge `0.2447` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.6906` n `31` status `ready` deltaP `8.6633` edge `0.1947` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1224` n `31` status `ready` deltaP `24.4929` edge `0.0085` maxDD `-0.2315`
- `market_context_high->fx_4h` score `0.8303` n `30` status `ready` deltaP `13.1809` edge `0.0195` maxDD `-0.0545`
- `news_risk_high->commodity_4h` score `0.3587` n `31` status `ready` deltaP `8.9791` edge `0.0259` maxDD `-0.5151`
- `market_context_high->fx_1h` score `0.35` n `42` status `ready` deltaP `9.5238` edge `0.0028` maxDD `-0.0466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
