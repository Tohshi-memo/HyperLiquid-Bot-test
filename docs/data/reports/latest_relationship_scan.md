# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T04:07:30.199059+00:00`
- Price records: `672`
- Market context records: `8055`
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

- `market_context_high->equity_24h` score `20.1784` n `74` status `ready` deltaP `35.2897` edge `1.5373` maxDD `-4.9489`
- `market_context_high->equity_4h` score `8.5341` n `87` status `ready` deltaP `33.3351` edge `0.5369` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.3972` n `74` status `ready` deltaP `35.8752` edge `0.4606` maxDD `0.0`
- `market_context_high->commodity_24h` score `5.7311` n `74` status `ready` deltaP `37.0579` edge `0.346` maxDD `-6.2367`
- `market_context_high->index_4h` score `3.3039` n `87` status `ready` deltaP `31.7406` edge `0.0825` maxDD `-0.5022`
- `market_context_high->index_24h` score `2.5544` n `74` status `ready` deltaP `14.2934` edge `0.1846` maxDD `-1.3621`
- `market_context_high->equity_1h` score `2.5228` n `87` status `ready` deltaP `16.2227` edge `0.1454` maxDD `-2.1322`
- `market_context_high->metal_4h` score `2.2841` n `87` status `ready` deltaP `20.9963` edge `0.1126` maxDD `-0.979`
- `market_context_high->fx_24h` score `1.4021` n `74` status `ready` deltaP `29.4768` edge `0.0536` maxDD `-0.6283`
- `market_context_high->index_1h` score `1.1482` n `87` status `ready` deltaP `15.1215` edge `0.0216` maxDD `-0.4716`
- `market_context_high->metal_1h` score `0.8781` n `87` status `ready` deltaP `12.1223` edge `0.0302` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.6322` n `87` status `ready` deltaP `9.9198` edge `0.0276` maxDD `-1.6171`
- `market_context_high->crypto_major_4h` score `0.4368` n `87` status `ready` deltaP `7.8007` edge `0.1562` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `0.3176` n `87` status `ready` deltaP `4.0475` edge `0.1112` maxDD `-3.9374`
- `market_context_high->fx_4h` score `0.0105` n `87` status `ready` deltaP `6.9649` edge `0.0052` maxDD `-0.3563`
- `market_context_high->crypto_alt_1h` score `-0.2975` n `87` status `ready` deltaP `0.0241` edge `0.0183` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.3806` n `87` status `ready` deltaP `2.1784` edge `-0.001` maxDD `-1.9855`
- `market_context_high->fx_1h` score `-0.3993` n `87` status `ready` deltaP `-2.3281` edge `0.0007` maxDD `-0.2428`
- `market_context_high->commodity_4h` score `-0.8132` n `87` status `ready` deltaP `5.9591` edge `0.0062` maxDD `-5.3478`
- `market_context_high->unknown_1h` score `-2.3302` n `87` status `ready` deltaP `4.269` edge `-0.1803` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
