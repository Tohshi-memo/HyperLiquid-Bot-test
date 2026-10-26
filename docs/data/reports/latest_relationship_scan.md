# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T22:52:29.995211+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7985`

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

- `market_context_high->unknown_4h` score `91.5087` n `153` status `ready` deltaP `1.0172` edge `7.6525` maxDD `-1.0178`
- `market_context_high->unknown_1h` score `21.6889` n `153` status `ready` deltaP `1.4745` edge `1.8465` maxDD `-1.5807`
- `market_context_high->fx_1h` score `0.2518` n `153` status `ready` deltaP `8.1151` edge `0.0027` maxDD `-0.1986`
- `market_context_high->metal_24h` score `0.2381` n `112` status `ready` deltaP `23.5887` edge `0.1359` maxDD `-7.0108`
- `market_context_high->fx_4h` score `0.1396` n `153` status `ready` deltaP `9.4771` edge `0.0083` maxDD `-0.4545`
- `market_context_high->index_24h` score `-0.03` n `112` status `ready` deltaP `16.3051` edge `0.0113` maxDD `-4.5747`
- `market_context_high->metal_1h` score `-0.1416` n `153` status `ready` deltaP `8.1807` edge `0.0065` maxDD `-1.6682`
- `market_context_high->fx_24h` score `-0.1755` n `112` status `ready` deltaP `16.2788` edge `0.0262` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.2582` n `153` status `ready` deltaP `2.3023` edge `0.0132` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.477` n `153` status `ready` deltaP `5.6014` edge `0.0458` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.5915` n `153` status `ready` deltaP `-0.137` edge `-0.0012` maxDD `-1.8971`
- `market_context_high->crypto_major_1h` score `-0.8421` n `153` status `ready` deltaP `4.6828` edge `0.0189` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-0.9289` n `153` status `ready` deltaP `7.8172` edge `-0.0002` maxDD `-5.3474`
- `market_context_high->equity_1h` score `-1.8245` n `153` status `ready` deltaP `1.0058` edge `-0.013` maxDD `-12.2088`
- `market_context_high->crypto_alt_1h` score `-1.9274` n `153` status `ready` deltaP `0.1732` edge `0.0002` maxDD `-13.2099`
- `market_context_high->index_4h` score `-3.3655` n `153` status `ready` deltaP `-5.9272` edge `-0.0233` maxDD `-6.7447`
- `market_context_high->crypto_major_24h` score `-4.4793` n `112` status `ready` deltaP `-2.6182` edge `-0.0711` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-4.4883` n `153` status `ready` deltaP `0.6087` edge `-0.0755` maxDD `-32.9851`
- `market_context_high->commodity_24h` score `-6.0312` n `112` status `ready` deltaP `-13.7843` edge `-0.1224` maxDD `-24.0477`
- `market_context_high->equity_24h` score `-6.7037` n `112` status `ready` deltaP `-6.6833` edge `-0.2716` maxDD `-35.4638`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
