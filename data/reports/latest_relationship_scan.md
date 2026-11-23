# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T01:22:27.493127+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5282`

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

- `market_context_high->unknown_1h` score `14365.1156` n `92` status `ready` deltaP `0.8461` edge `1197.1035` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `9217.5385` n `92` status `ready` deltaP `-1.0737` edge `768.1659` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1363.4769` n `31` status `ready` deltaP `4.1771` edge `113.6128` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1195.5798` n `31` status `ready` deltaP `4.3962` edge `99.608` maxDD `-0.119`
- `news_risk_high->equity_4h` score `11.8768` n `31` status `ready` deltaP `39.0539` edge `0.7776` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `11.0093` n `31` status `ready` deltaP `25.5409` edge `0.8342` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.6555` n `31` status `ready` deltaP `14.3391` edge `0.8994` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `4.0194` n `31` status `ready` deltaP `19.8377` edge `0.2214` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.55` n `31` status `ready` deltaP `37.0722` edge `0.0747` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7346` n `31` status `ready` deltaP `31.9925` edge `0.0231` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4759` n `31` status `ready` deltaP `9.8609` edge `0.2978` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0791` n `31` status `ready` deltaP `8.5136` edge `0.2455` maxDD `-1.5232`
- `news_risk_high->metal_4h` score `1.5845` n `31` status `ready` deltaP `21.6562` edge `0.1145` maxDD `-0.7918`
- `news_risk_high->metal_1h` score `1.5797` n `31` status `ready` deltaP `29.7324` edge `0.0322` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.7865` n `31` status `ready` deltaP `17.8206` edge `0.0218` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.0501` n `31` status `ready` deltaP `1.5308` edge `0.0118` maxDD `-0.0947`
- `market_context_high->fx_4h` score `-0.5008` n `92` status `ready` deltaP `6.8398` edge `0.0105` maxDD `-0.9574`
- `market_context_high->index_1h` score `-0.5551` n `92` status `ready` deltaP `0.2603` edge `-0.0024` maxDD `-0.9806`
- `market_context_high->metal_1h` score `-0.6697` n `92` status `ready` deltaP `1.1911` edge `-0.0037` maxDD `-2.1373`
- `market_context_high->fx_1h` score `-1.221` n `92` status `ready` deltaP `-8.9235` edge `-0.0007` maxDD `-0.325`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
