# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T04:07:28.071373+00:00`
- Price records: `672`
- Market context records: `6779`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11714`

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

- `market_context_high->unknown_24h` score `0.9466` n `176` status `ready` deltaP `-0.6787` edge `0.5011` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.0309` n `176` status `ready` deltaP `8.144` edge `0.1351` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.0213` n `178` status `ready` deltaP `7.6432` edge `0.0323` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.1319` n `178` status `ready` deltaP `5.359` edge `0.0297` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.3881` n `178` status `ready` deltaP `-0.2641` edge `0.0005` maxDD `-0.5468`
- `market_context_high->index_1h` score `-0.6108` n `178` status `ready` deltaP `-1.1976` edge `0.0011` maxDD `-0.7136`
- `market_context_high->commodity_1h` score `-0.6271` n `178` status `ready` deltaP `-0.4474` edge `-0.0091` maxDD `-2.1314`
- `market_context_high->metal_1h` score `-0.7518` n `178` status `ready` deltaP `-5.9191` edge `-0.0044` maxDD `-1.2017`
- `market_context_high->equity_1h` score `-1.1689` n `178` status `ready` deltaP `2.9991` edge `-0.0147` maxDD `-3.8827`
- `market_context_high->index_4h` score `-1.2633` n `176` status `ready` deltaP `5.9867` edge `-0.0139` maxDD `-5.7046`
- `market_context_high->fx_4h` score `-1.2723` n `176` status `ready` deltaP `6.6242` edge `-0.0009` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.539` n `176` status `ready` deltaP `-3.6031` edge `-0.0243` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.5944` n `178` status `ready` deltaP `-5.9191` edge `-0.0033` maxDD `-3.2083`
- `market_context_high->metal_4h` score `-2.6471` n `176` status `ready` deltaP `-6.3193` edge `-0.0112` maxDD `-5.2172`
- `market_context_high->crypto_major_4h` score `-2.7873` n `176` status `ready` deltaP `2.8963` edge `-0.0452` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-2.9376` n `176` status `ready` deltaP `1.1502` edge `-0.0441` maxDD `-19.2145`
- `market_context_high->unknown_4h` score `-3.3467` n `176` status `ready` deltaP `-14.4956` edge `0.0543` maxDD `-10.2579`
- `market_context_high->equity_4h` score `-4.233` n `176` status `ready` deltaP `2.7023` edge `-0.1338` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-4.3748` n `176` status `ready` deltaP `-8.5701` edge `-0.0038` maxDD `-5.6237`
- `market_context_high->metal_24h` score `-8.938` n `176` status `ready` deltaP `-16.5878` edge `-0.1868` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
