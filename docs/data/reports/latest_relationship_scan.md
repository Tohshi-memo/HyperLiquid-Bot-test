# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T00:37:25.875002+00:00`
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

- `market_context_high->unknown_1h` score `13809.2488` n `95` status `ready` deltaP `0.7059` edge `1150.7822` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `8948.2289` n `94` status `ready` deltaP `-0.8886` edge `745.7222` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1363.4026` n `31` status `ready` deltaP `3.728` edge `113.6096` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1198.545` n `31` status `ready` deltaP `4.3962` edge `99.8551` maxDD `-0.119`
- `news_risk_high->equity_4h` score `12.0142` n `31` status `ready` deltaP `39.5112` edge `0.786` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `11.0201` n `31` status `ready` deltaP `25.5409` edge `0.8351` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.686` n `31` status `ready` deltaP `14.4915` edge `0.9023` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `4.0601` n `31` status `ready` deltaP `19.9874` edge `0.2238` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.6058` n `31` status `ready` deltaP `37.5295` edge `0.0763` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7525` n `31` status `ready` deltaP `32.1422` edge `0.0236` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4915` n `31` status `ready` deltaP `9.8609` edge `0.2998` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0947` n `31` status `ready` deltaP `8.5136` edge `0.2475` maxDD `-1.5232`
- `news_risk_high->metal_4h` score `1.6325` n `31` status `ready` deltaP `22.1135` edge `0.1176` maxDD `-0.7918`
- `news_risk_high->metal_1h` score `1.5921` n `31` status `ready` deltaP `29.8821` edge `0.0328` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.7669` n `31` status `ready` deltaP `17.6682` edge `0.0203` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.0465` n `31` status `ready` deltaP `1.5308` edge `0.0121` maxDD `-0.0947`
- `market_context_high->index_1h` score `-0.4784` n `95` status `ready` deltaP `-1.1346` edge `-0.0056` maxDD `-1.1868`
- `market_context_high->fx_4h` score `-0.7081` n `94` status `ready` deltaP `5.1926` edge `0.0089` maxDD `-1.0768`
- `market_context_high->metal_1h` score `-0.8861` n `95` status `ready` deltaP `-0.1009` edge `-0.0073` maxDD `-2.6026`
- `market_context_high->fx_1h` score `-1.2276` n `95` status `ready` deltaP `-8.9568` edge `-0.0009` maxDD `-0.3349`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
