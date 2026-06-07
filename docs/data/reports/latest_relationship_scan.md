# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T00:22:28.445978+00:00`
- Price records: `672`
- Market context records: `3127`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7027`

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

- `market_context_high->commodity_24h` score `14.3259` n `104` status `ready` deltaP `47.4226` edge `0.9205` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `11.8724` n `104` status `ready` deltaP `21.1004` edge `0.8975` maxDD `-1.9039`
- `market_context_high->crypto_alt_24h` score `11.0682` n `104` status `ready` deltaP `10.0962` edge `2.3146` maxDD `-68.3661`
- `market_context_high->index_24h` score `6.5172` n `104` status `ready` deltaP `31.4236` edge `0.8815` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.4665` n `104` status `ready` deltaP `11.1511` edge `1.3205` maxDD `-52.7768`
- `market_context_high->commodity_4h` score `3.0587` n `130` status `ready` deltaP `19.4536` edge `0.171` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `0.0472` n `142` status `ready` deltaP `2.9835` edge `0.0263` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.4019` n `142` status `ready` deltaP `5.3175` edge `0.0193` maxDD `-4.5023`
- `market_context_high->fx_24h` score `-0.5023` n `104` status `ready` deltaP `4.8611` edge `-0.0015` maxDD `-0.4876`
- `market_context_high->crypto_alt_1h` score `-0.5928` n `142` status `ready` deltaP `4.763` edge `0.1052` maxDD `-14.7034`
- `market_context_high->equity_1h` score `-0.8946` n `142` status `ready` deltaP `2.2624` edge `0.0188` maxDD `-8.8863`
- `market_context_high->crypto_major_1h` score `-1.1548` n `142` status `ready` deltaP `1.7015` edge `0.0669` maxDD `-15.1032`
- `market_context_high->fx_1h` score `-1.1864` n `142` status `ready` deltaP `-11.7336` edge `-0.0057` maxDD `-0.7877`
- `market_context_high->index_4h` score `-1.2402` n `130` status `ready` deltaP `11.8363` edge `0.053` maxDD `-17.6057`
- `market_context_high->fx_4h` score `-1.4773` n `130` status `ready` deltaP `-14.3245` edge `-0.0082` maxDD `-1.189`
- `market_context_high->metal_1h` score `-2.1079` n `142` status `ready` deltaP `-4.8579` edge `-0.0039` maxDD `-7.4828`
- `market_context_high->unknown_4h` score `-2.2406` n `130` status `ready` deltaP `2.8213` edge `0.0167` maxDD `-14.7778`
- `market_context_high->unknown_1h` score `-3.0795` n `142` status `ready` deltaP `1.847` edge `-0.0663` maxDD `-14.2111`
- `market_context_high->crypto_alt_4h` score `-3.3249` n `130` status `ready` deltaP `15.7223` edge `0.2734` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-3.583` n `130` status `ready` deltaP `9.3761` edge `0.0087` maxDD `-36.7784`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
