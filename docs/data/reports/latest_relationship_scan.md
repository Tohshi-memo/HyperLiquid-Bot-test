# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T01:07:25.659612+00:00`
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

- `market_context_high->unknown_1h` score `14175.8565` n `93` status `ready` deltaP `0.8016` edge `1181.3322` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `9082.8292` n `93` status `ready` deltaP `-0.9802` edge `756.9395` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1363.453` n `31` status `ready` deltaP `4.0274` edge `113.6118` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1198.5798` n `31` status `ready` deltaP `4.3962` edge `99.858` maxDD `-0.119`
- `news_risk_high->equity_4h` score `11.9166` n `31` status `ready` deltaP `39.2064` edge `0.7799` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `11.0045` n `31` status `ready` deltaP `25.5409` edge `0.8338` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.6571` n `31` status `ready` deltaP `14.3391` edge `0.8996` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `4.0362` n `31` status `ready` deltaP `19.8377` edge `0.2228` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.5682` n `31` status `ready` deltaP `37.2247` edge `0.0752` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.737` n `31` status `ready` deltaP `31.9925` edge `0.0233` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4821` n `31` status `ready` deltaP `9.8609` edge `0.2986` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0861` n `31` status `ready` deltaP `8.5136` edge `0.2464` maxDD `-1.5232`
- `news_risk_high->metal_4h` score `1.601` n `31` status `ready` deltaP `21.8086` edge `0.1156` maxDD `-0.7918`
- `news_risk_high->metal_1h` score `1.5914` n `31` status `ready` deltaP `29.8821` edge `0.0327` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.7834` n `31` status `ready` deltaP `17.8206` edge `0.0214` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.0346` n `31` status `ready` deltaP `1.6805` edge `0.0121` maxDD `-0.0947`
- `market_context_high->fx_4h` score `-0.5567` n `93` status `ready` deltaP `6.4664` edge `0.0104` maxDD `-0.9907`
- `market_context_high->index_1h` score `-0.6169` n `93` status `ready` deltaP `-0.2656` edge `-0.004` maxDD `-0.9845`
- `market_context_high->metal_1h` score `-0.7664` n `93` status `ready` deltaP `0.8499` edge `-0.006` maxDD `-2.4158`
- `market_context_high->fx_1h` score `-1.1651` n `93` status `ready` deltaP `-8.269` edge `-0.0004` maxDD `-0.325`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
