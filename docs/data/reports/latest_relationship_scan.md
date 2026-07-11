# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T12:52:24.200230+00:00`
- Price records: `672`
- Market context records: `6392`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11074`

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

- `news_risk_high->crypto_alt_24h` score `13.9616` n `32` status `ready` deltaP `36.6319` edge `0.934` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.5338` n `32` status `ready` deltaP `54.6875` edge `0.1799` maxDD `0.0`
- `news_risk_high->commodity_24h` score `4.4201` n `32` status `ready` deltaP `38.3681` edge `0.1331` maxDD `-0.3101`
- `news_risk_high->crypto_major_24h` score `4.2653` n `32` status `ready` deltaP `17.5347` edge `0.5079` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.9974` n `32` status `ready` deltaP `41.3872` edge `0.0618` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3967` n `32` status `ready` deltaP `28.8922` edge `0.021` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4609` n `32` status `ready` deltaP `13.9783` edge `0.1408` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.8193` n `32` status `ready` deltaP `10.2732` edge `0.0827` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.4184` n `216` status `ready` deltaP `13.7986` edge `0.0413` maxDD `-2.7056`
- `market_context_high->unknown_1h` score `0.2317` n `224` status `ready` deltaP `-5.8169` edge `0.1589` maxDD `-3.7317`
- `market_context_high->index_4h` score `0.1469` n `216` status `ready` deltaP `8.7568` edge `0.0215` maxDD `-0.4108`
- `news_risk_high->unknown_1h` score `-0.1878` n `32` status `ready` deltaP `7.1295` edge `-0.0287` maxDD `-0.7581`
- `market_context_high->metal_24h` score `-0.2195` n `146` status `ready` deltaP `19.6205` edge `0.0979` maxDD `-11.8809`
- `market_context_high->metal_1h` score `-0.4466` n `224` status `ready` deltaP `2.6706` edge `0.0027` maxDD `-1.8877`
- `market_context_high->equity_4h` score `-0.4733` n `216` status `ready` deltaP `8.7003` edge `0.0512` maxDD `-8.2573`
- `news_risk_high->metal_1h` score `-0.6531` n `32` status `ready` deltaP `-1.3473` edge `-0.025` maxDD `-1.6464`
- `market_context_high->index_1h` score `-0.6882` n `224` status `ready` deltaP `-2.8309` edge `0.0026` maxDD `-0.7564`
- `market_context_high->fx_1h` score `-0.7044` n `224` status `ready` deltaP `-0.5721` edge `-0.0015` maxDD `-0.9376`
- `market_context_high->commodity_1h` score `-0.7266` n `224` status `ready` deltaP `-3.2774` edge `-0.003` maxDD `-2.1314`
- `news_risk_high->index_24h` score `-0.7424` n `32` status `ready` deltaP `0.5208` edge `-0.0115` maxDD `-2.3058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
