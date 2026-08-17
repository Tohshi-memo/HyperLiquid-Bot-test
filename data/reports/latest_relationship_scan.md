# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-17T20:07:30.377864+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11835`

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

- `risk_on_high->unknown_1h` score `7.2401` n `35` status `ready` deltaP `1.4414` edge `0.6332` maxDD `-0.8243`
- `risk_on_and_context->unknown_1h` score `7.2401` n `35` status `ready` deltaP `1.4414` edge `0.6332` maxDD `-0.8243`
- `market_context_high->crypto_major_24h` score `5.0157` n `78` status `ready` deltaP `19.6596` edge `0.4077` maxDD `-4.9964`
- `market_context_high->equity_24h` score `3.1264` n `78` status `ready` deltaP `16.9844` edge `0.1473` maxDD `0.0`
- `market_context_high->index_24h` score `1.3217` n `78` status `ready` deltaP `18.8908` edge `-0.0158` maxDD `0.0`
- `risk_on_high->fx_4h` score `1.1977` n `35` status `ready` deltaP `16.5166` edge `0.0038` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.1977` n `35` status `ready` deltaP `16.5166` edge `0.0038` maxDD `-0.1285`
- `risk_on_high->crypto_major_1h` score `1.0012` n `35` status `ready` deltaP `11.6595` edge `0.0363` maxDD `-1.1144`
- `risk_on_and_context->crypto_major_1h` score `1.0012` n `35` status `ready` deltaP `11.6595` edge `0.0363` maxDD `-1.1144`
- `risk_on_high->index_1h` score `0.8405` n `35` status `ready` deltaP `14.243` edge `0.0126` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.8405` n `35` status `ready` deltaP `14.243` edge `0.0126` maxDD `-0.3343`
- `risk_on_high->equity_1h` score `0.7598` n `35` status `ready` deltaP `12.6091` edge `0.0336` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `0.7598` n `35` status `ready` deltaP `12.6091` edge `0.0336` maxDD `-1.6811`
- `market_context_high->commodity_4h` score `0.6448` n `127` status `ready` deltaP `13.2995` edge `0.0501` maxDD `-2.4692`
- `risk_on_high->commodity_4h` score `0.3381` n `35` status `ready` deltaP `2.2309` edge `0.0762` maxDD `-1.3651`
- `risk_on_and_context->commodity_4h` score `0.3381` n `35` status `ready` deltaP `2.2309` edge `0.0762` maxDD `-1.3651`
- `risk_on_high->fx_1h` score `0.1185` n `35` status `ready` deltaP `5.3336` edge `0.0024` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.1185` n `35` status `ready` deltaP `5.3336` edge `0.0024` maxDD `-0.1547`
- `market_context_high->commodity_24h` score `0.1025` n `78` status `ready` deltaP `15.3691` edge `0.094` maxDD `-4.666`
- `risk_on_high->crypto_major_4h` score `-0.0053` n `35` status `ready` deltaP `1.4699` edge `0.0607` maxDD `-2.0278`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
