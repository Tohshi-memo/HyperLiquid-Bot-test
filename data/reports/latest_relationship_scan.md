# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T01:52:32.292693+00:00`
- Price records: `672`
- Market context records: `8046`
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

- `market_context_high->equity_24h` score `19.4617` n `76` status `ready` deltaP `33.6359` edge `1.4886` maxDD `-4.9489`
- `market_context_high->metal_24h` score `8.3024` n `76` status `ready` deltaP `35.8752` edge `0.4527` maxDD `0.0`
- `market_context_high->equity_4h` score `7.8284` n `89` status `ready` deltaP `31.142` edge `0.5124` maxDD `-3.7448`
- `market_context_high->commodity_24h` score `5.2786` n `76` status `ready` deltaP `34.7464` edge `0.3237` maxDD `-6.2367`
- `market_context_high->index_4h` score `2.9011` n `89` status `ready` deltaP `29.3693` edge `0.0766` maxDD `-0.7842`
- `market_context_high->index_24h` score `2.3482` n `76` status `ready` deltaP `13.1419` edge `0.1751` maxDD `-1.3621`
- `market_context_high->metal_4h` score `2.3051` n `89` status `ready` deltaP `21.3346` edge `0.1121` maxDD `-0.979`
- `market_context_high->equity_1h` score `1.9339` n `89` status `ready` deltaP `15.2459` edge `0.1299` maxDD `-3.6305`
- `market_context_high->fx_24h` score `1.3972` n `76` status `ready` deltaP `29.4718` edge `0.053` maxDD `-0.6283`
- `market_context_high->index_1h` score `0.8942` n `89` status `ready` deltaP `14.0466` edge `0.019` maxDD `-0.717`
- `market_context_high->metal_1h` score `0.6917` n `89` status `ready` deltaP `10.2267` edge `0.0273` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.4011` n `89` status `ready` deltaP `9.7003` edge `0.0278` maxDD `-1.6171`
- `market_context_high->crypto_major_4h` score `0.2826` n `89` status `ready` deltaP `6.8632` edge `0.1496` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `0.1648` n `89` status `ready` deltaP `3.1875` edge `0.1042` maxDD `-3.9374`
- `market_context_high->fx_4h` score `0.0214` n `89` status `ready` deltaP `7.252` edge `0.0059` maxDD `-0.4534`
- `market_context_high->crypto_alt_1h` score `-0.2177` n `89` status `ready` deltaP `-0.3381` edge `0.0176` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.396` n `89` status `ready` deltaP `1.9125` edge `-0.0012` maxDD `-1.9855`
- `market_context_high->fx_1h` score `-0.4571` n `89` status `ready` deltaP `-3.3355` edge `0.0` maxDD `-0.2428`
- `market_context_high->commodity_4h` score `-0.8238` n `89` status `ready` deltaP `5.7396` edge `0.0063` maxDD `-5.3478`
- `market_context_high->unknown_1h` score `-2.1354` n `89` status `ready` deltaP `5.6533` edge `-0.1733` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
