# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T13:07:26.400469+00:00`
- Price records: `672`
- Market context records: `6819`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11700`

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

- `market_context_high->unknown_24h` score `0.8554` n `176` status `ready` deltaP `-1.5467` edge `0.4952` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.3527` n `176` status `ready` deltaP `10.9217` edge `0.1434` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.319` n `200` status `ready` deltaP `5.9102` edge `0.02` maxDD `-4.2122`
- `market_context_high->fx_1h` score `-0.394` n `200` status `ready` deltaP `-0.3024` edge `0.0` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.4254` n `200` status `ready` deltaP `3.4611` edge `0.0179` maxDD `-3.7803`
- `market_context_high->index_1h` score `-0.7905` n `200` status `ready` deltaP `-3.497` edge `-0.0038` maxDD `-0.9382`
- `market_context_high->metal_1h` score `-0.9612` n `200` status `ready` deltaP `-6.0539` edge `-0.009` maxDD `-1.9098`
- `market_context_high->commodity_1h` score `-1.061` n `200` status `ready` deltaP `-2.1467` edge `-0.0058` maxDD `-2.1314`
- `market_context_high->fx_4h` score `-1.3415` n `188` status `ready` deltaP `5.4878` edge `-0.0022` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.3688` n `188` status `ready` deltaP `-2.4455` edge `-0.0102` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.6084` n `188` status `ready` deltaP `2.6369` edge `-0.0278` maxDD `-6.3458`
- `market_context_high->equity_1h` score `-1.6673` n `200` status `ready` deltaP `0.4581` edge `-0.0293` maxDD `-4.6821`
- `market_context_high->unknown_1h` score `-1.732` n `200` status `ready` deltaP `-5.4042` edge `-0.0182` maxDD `-3.2083`
- `market_context_high->metal_4h` score `-2.8197` n `188` status `ready` deltaP `-4.9916` edge `-0.0299` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-3.2285` n `188` status `ready` deltaP `-0.7038` edge `-0.0765` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.4216` n `188` status `ready` deltaP `-1.2325` edge `-0.0721` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.4517` n `188` status `ready` deltaP `-13.1973` edge `0.0369` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.4636` n `176` status `ready` deltaP `-9.7853` edge `-0.0031` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-4.955` n `188` status `ready` deltaP `0.0584` edge `-0.1818` maxDD `-29.3079`
- `market_context_high->metal_24h` score `-9.6368` n `176` status `ready` deltaP `-21.9697` edge `-0.2405` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
