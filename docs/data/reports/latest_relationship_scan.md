# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T15:52:29.011061+00:00`
- Price records: `672`
- Market context records: `7683`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14676`

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

- `market_context_high->crypto_major_1h` score `0.3099` n `140` status `ready` deltaP `10.0` edge `0.0298` maxDD `-3.3181`
- `market_context_high->crypto_major_4h` score `0.2517` n `140` status `ready` deltaP `12.2953` edge `0.1158` maxDD `-7.1435`
- `market_context_high->equity_24h` score `0.23` n `139` status `ready` deltaP `15.1994` edge `0.1648` maxDD `-14.2652`
- `market_context_high->equity_1h` score `0.1157` n `140` status `ready` deltaP `6.4651` edge `0.0695` maxDD `-5.1551`
- `market_context_high->index_1h` score `0.082` n `140` status `ready` deltaP `6.6881` edge `0.0131` maxDD `-0.7743`
- `market_context_high->fx_24h` score `-0.136` n `139` status `ready` deltaP `11.4193` edge `0.0213` maxDD `-3.0343`
- `market_context_high->crypto_alt_1h` score `-0.1692` n `140` status `ready` deltaP `2.4765` edge `0.0245` maxDD `-2.6829`
- `market_context_high->crypto_alt_4h` score `-0.2496` n `140` status `ready` deltaP `5.4573` edge `0.0849` maxDD `-6.3666`
- `market_context_high->commodity_1h` score `-0.3467` n `140` status `ready` deltaP `2.1922` edge `0.0024` maxDD `-0.6722`
- `market_context_high->equity_4h` score `-0.4081` n `140` status `ready` deltaP `1.481` edge `0.2298` maxDD `-12.6931`
- `market_context_high->index_4h` score `-0.4254` n `140` status `ready` deltaP `9.8471` edge `0.0371` maxDD `-2.2492`
- `market_context_high->commodity_4h` score `-0.4535` n `140` status `ready` deltaP `1.8545` edge `0.0092` maxDD `-1.0817`
- `market_context_high->fx_1h` score `-0.507` n `140` status `ready` deltaP `-0.1909` edge `-0.0013` maxDD `-0.5075`
- `market_context_high->metal_1h` score `-0.6454` n `140` status `ready` deltaP `0.8854` edge `0.0159` maxDD `-1.0307`
- `market_context_high->metal_4h` score `-1.3517` n `140` status `ready` deltaP `-0.6185` edge `0.0598` maxDD `-3.3178`
- `market_context_high->metal_24h` score `-1.3909` n `140` status `ready` deltaP `-0.6647` edge `0.0899` maxDD `-4.4368`
- `market_context_high->unknown_1h` score `-1.4187` n `140` status `ready` deltaP `-1.1634` edge `-0.051` maxDD `-1.0907`
- `market_context_high->commodity_24h` score `-1.4417` n `139` status `ready` deltaP `6.6014` edge `-0.0058` maxDD `-7.0012`
- `market_context_high->fx_4h` score `-2.4878` n `140` status `ready` deltaP `-5.9261` edge `-0.0037` maxDD `-1.7951`
- `market_context_high->index_24h` score `-3.1417` n `139` status `ready` deltaP `-20.3231` edge `-0.0236` maxDD `-4.8291`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
