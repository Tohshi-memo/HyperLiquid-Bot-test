# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T11:52:21.593748+00:00`
- Price records: `672`
- Market context records: `2454`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9222`

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

- `news_risk_high->crypto_alt_24h` score `19.8052` n `41` status `ready` deltaP `43.5595` edge `1.4189` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `19.6858` n `41` status `ready` deltaP `55.0263` edge `1.3176` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.4093` n `41` status `ready` deltaP `29.6791` edge `1.1177` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `9.8203` n `41` status `ready` deltaP `17.4331` edge `0.7602` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `7.5031` n `41` status `ready` deltaP `24.8179` edge `0.4824` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.7759` n `110` status `ready` deltaP `21.8024` edge `0.3688` maxDD `-1.626`
- `news_risk_high->index_24h` score `5.76` n `41` status `ready` deltaP `12.7879` edge `0.4283` maxDD `-1.3507`
- `market_context_high->crypto_major_4h` score `4.4996` n `130` status `ready` deltaP `20.9357` edge `0.4164` maxDD `-10.1468`
- `market_context_high->crypto_alt_4h` score `4.3589` n `130` status `ready` deltaP `21.5314` edge `0.4876` maxDD `-15.4319`
- `news_risk_high->fx_24h` score `3.318` n `41` status `ready` deltaP `34.4809` edge `0.0651` maxDD `-0.1442`
- `news_risk_high->commodity_4h` score `3.1749` n `41` status `ready` deltaP `27.7439` edge `0.2892` maxDD `-3.0367`
- `market_context_high->crypto_major_24h` score `2.5146` n `110` status `ready` deltaP `12.1559` edge `0.6306` maxDD `-25.1408`
- `news_risk_high->fx_4h` score `2.081` n `41` status `ready` deltaP `26.3719` edge `0.016` maxDD `-0.1382`
- `news_risk_high->unknown_1h` score `2.0242` n `41` status `ready` deltaP `23.9631` edge `0.0521` maxDD `-1.4536`
- `news_risk_high->unknown_4h` score `1.9308` n `41` status `ready` deltaP `16.1585` edge `0.1255` maxDD `-2.7857`
- `market_context_high->unknown_4h` score `1.8006` n `130` status `ready` deltaP `10.4362` edge `0.1655` maxDD `-2.4687`
- `market_context_high->index_24h` score `1.2293` n `110` status `ready` deltaP `6.2247` edge `0.1074` maxDD `-0.7163`
- `market_context_high->crypto_major_1h` score `0.8693` n `136` status `ready` deltaP `9.233` edge `0.1303` maxDD `-4.2199`
- `market_context_high->crypto_alt_1h` score `0.7032` n `136` status `ready` deltaP `7.6259` edge `0.1265` maxDD `-6.1656`
- `news_risk_high->fx_1h` score `0.6423` n `41` status `ready` deltaP `10.2271` edge `0.011` maxDD `-0.0524`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
