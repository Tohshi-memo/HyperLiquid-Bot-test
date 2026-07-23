# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T13:37:26.030094+00:00`
- Price records: `672`
- Market context records: `7673`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14690`

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

- `market_context_high->index_1h` score `0.032` n `146` status `ready` deltaP `6.0616` edge `0.0116` maxDD `-0.8324`
- `market_context_high->crypto_major_1h` score `-0.1362` n `146` status `ready` deltaP `8.3053` edge `0.0232` maxDD `-4.0162`
- `market_context_high->crypto_alt_1h` score `-0.1991` n `146` status `ready` deltaP `2.5039` edge `0.021` maxDD `-2.7243`
- `market_context_high->fx_24h` score `-0.3196` n `145` status `ready` deltaP `9.4545` edge `0.0191` maxDD `-3.0343`
- `market_context_high->commodity_1h` score `-0.4327` n `146` status `ready` deltaP `0.7774` edge `-0.0036` maxDD `-1.5641`
- `market_context_high->equity_1h` score `-0.5275` n `146` status `ready` deltaP `4.7761` edge `0.0519` maxDD `-7.7764`
- `market_context_high->metal_1h` score `-0.6395` n `146` status `ready` deltaP `1.0889` edge `0.0153` maxDD `-1.0307`
- `market_context_high->index_4h` score `-0.7389` n `146` status `ready` deltaP `7.3813` edge `0.0262` maxDD `-3.2774`
- `market_context_high->fx_1h` score `-0.7531` n `146` status `ready` deltaP `-1.6229` edge `-0.002` maxDD `-0.6615`
- `market_context_high->commodity_4h` score `-0.8671` n `146` status `ready` deltaP `0.3834` edge `-0.0003` maxDD `-2.2943`
- `market_context_high->crypto_alt_4h` score `-0.9645` n `146` status `ready` deltaP `2.8921` edge `0.056` maxDD `-9.5815`
- `market_context_high->crypto_major_4h` score `-1.1312` n `146` status `ready` deltaP `9.589` edge `0.0588` maxDD `-14.4206`
- `market_context_high->commodity_24h` score `-1.2662` n `145` status `ready` deltaP `7.4901` edge `0.0029` maxDD `-7.0012`
- `market_context_high->unknown_1h` score `-1.5385` n `146` status `ready` deltaP `-1.5831` edge `-0.0553` maxDD `-1.3217`
- `market_context_high->metal_4h` score `-1.7029` n `146` status `ready` deltaP `-2.7376` edge `0.0456` maxDD `-4.6535`
- `market_context_high->equity_4h` score `-1.9459` n `146` status `ready` deltaP `-0.6912` edge `0.1695` maxDD `-20.4824`
- `market_context_high->metal_24h` score `-2.2964` n `146` status `ready` deltaP `-3.2772` edge `0.0531` maxDD `-7.3868`
- `market_context_high->fx_4h` score `-2.6642` n `146` status `ready` deltaP `-7.2703` edge `-0.0051` maxDD `-2.1425`
- `market_context_high->equity_24h` score `-2.9325` n `145` status `ready` deltaP `11.9248` edge `0.0351` maxDD `-34.5784`
- `market_context_high->index_24h` score `-3.6977` n `145` status `ready` deltaP `-21.7818` edge `-0.0441` maxDD `-8.114`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
