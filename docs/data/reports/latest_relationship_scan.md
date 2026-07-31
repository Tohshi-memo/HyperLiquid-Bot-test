# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T12:07:27.145580+00:00`
- Price records: `672`
- Market context records: `8513`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5882`

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

- `news_risk_high->unknown_24h` score `6276.9381` n `52` status `ready` deltaP `44.7383` edge `522.822` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.6214` n `64` status `ready` deltaP `21.1128` edge `0.3874` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.9867` n `64` status `ready` deltaP `16.5015` edge `0.0746` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7206` n `64` status `ready` deltaP `15.8028` edge `0.0857` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `0.8698` n `64` status `ready` deltaP `5.8308` edge `0.1502` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.7991` n `64` status `ready` deltaP `14.3293` edge `0.1461` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.5747` n `64` status `ready` deltaP `9.3095` edge `0.0643` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3392` n `64` status `ready` deltaP `6.6149` edge `0.0506` maxDD `-2.0972`
- `market_context_high->commodity_1h` score `0.1664` n `41` status `ready` deltaP `10.333` edge `0.015` maxDD `-2.0038`
- `market_context_high->equity_1h` score `0.1496` n `41` status `ready` deltaP `0.9019` edge `0.0356` maxDD `-0.9985`
- `news_risk_high->fx_1h` score `0.0932` n `64` status `ready` deltaP `5.436` edge `0.0038` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.048` n `64` status `ready` deltaP `4.3694` edge `0.0087` maxDD `-0.5338`
- `news_risk_high->fx_4h` score `-0.0038` n `64` status `ready` deltaP `11.1662` edge `0.021` maxDD `-0.6604`
- `market_context_high->index_1h` score `-0.0493` n `41` status `ready` deltaP `2.6545` edge `-0.004` maxDD `-0.2683`
- `news_risk_high->metal_4h` score `-0.0563` n `64` status `ready` deltaP `1.2576` edge `0.032` maxDD `-0.8085`
- `news_risk_high->metal_1h` score `-0.1275` n `64` status `ready` deltaP `3.256` edge `0.008` maxDD `-0.5599`
- `market_context_high->crypto_major_1h` score `-0.3279` n `41` status `ready` deltaP `2.4609` edge `-0.0087` maxDD `-1.9791`
- `market_context_high->metal_1h` score `-0.3323` n `41` status `ready` deltaP `0.6645` edge `-0.0099` maxDD `-0.6372`
- `market_context_high->fx_1h` score `-0.6216` n `41` status `ready` deltaP `-5.3491` edge `0.0025` maxDD `-0.3888`
- `market_context_high->crypto_alt_1h` score `-0.9237` n `41` status `ready` deltaP `-9.4786` edge `-0.0023` maxDD `-2.2351`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
