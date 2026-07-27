# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T04:52:37.944386+00:00`
- Price records: `672`
- Market context records: `8058`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11848`

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

- `market_context_high->equity_24h` score `20.1832` n `74` status `ready` deltaP `35.2897` edge `1.5377` maxDD `-4.9489`
- `market_context_high->equity_4h` score `8.4917` n `87` status `ready` deltaP `33.0302` edge `0.5354` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.3912` n `74` status `ready` deltaP `35.8752` edge `0.4601` maxDD `0.0`
- `market_context_high->commodity_24h` score `5.7443` n `74` status `ready` deltaP `37.0579` edge `0.3471` maxDD `-6.2367`
- `market_context_high->index_4h` score `3.3161` n `87` status `ready` deltaP `31.893` edge `0.0825` maxDD `-0.5022`
- `market_context_high->index_24h` score `2.564` n `74` status `ready` deltaP `14.2934` edge `0.1854` maxDD `-1.3621`
- `market_context_high->equity_1h` score `2.5108` n `87` status `ready` deltaP `16.073` edge `0.1454` maxDD `-2.1322`
- `market_context_high->metal_4h` score `2.312` n `87` status `ready` deltaP `21.3011` edge `0.1129` maxDD `-0.979`
- `market_context_high->fx_24h` score `1.3673` n `74` status `ready` deltaP `28.9569` edge `0.0526` maxDD `-0.6283`
- `market_context_high->index_1h` score `1.1482` n `87` status `ready` deltaP `15.1215` edge `0.0216` maxDD `-0.4716`
- `market_context_high->metal_1h` score `0.8638` n `87` status `ready` deltaP `11.9726` edge `0.03` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.5675` n `87` status `ready` deltaP `9.4707` edge `0.0252` maxDD `-1.6171`
- `market_context_high->crypto_major_4h` score `0.3462` n `87` status `ready` deltaP `7.3434` edge `0.1517` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `0.2668` n `87` status `ready` deltaP `3.7427` edge `0.109` maxDD `-3.9374`
- `market_context_high->fx_4h` score `0.0089` n `87` status `ready` deltaP `6.9649` edge `0.005` maxDD `-0.3563`
- `market_context_high->crypto_alt_1h` score `-0.3538` n `87` status `ready` deltaP `-0.425` edge `0.0166` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.3611` n `87` status `ready` deltaP `2.4778` edge `-0.0005` maxDD `-1.9855`
- `market_context_high->fx_1h` score `-0.4148` n `87` status `ready` deltaP `-2.6275` edge `0.0007` maxDD `-0.2428`
- `market_context_high->commodity_4h` score `-0.8273` n `87` status `ready` deltaP `5.8067` edge `0.0054` maxDD `-5.3478`
- `market_context_high->unknown_1h` score `-2.3566` n `87` status `ready` deltaP `4.1193` edge `-0.1815` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
