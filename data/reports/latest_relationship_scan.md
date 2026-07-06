# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T01:07:28.710789+00:00`
- Price records: `672`
- Market context records: `5830`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10076`

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

- `market_context_high->equity_4h` score `0.5348` n `273` status `ready` deltaP `7.4316` edge `0.1408` maxDD `-6.9958`
- `market_context_high->fx_1h` score `-0.2646` n `273` status `ready` deltaP `2.1485` edge `0.0003` maxDD `-0.5499`
- `market_context_high->equity_24h` score `-0.4669` n `245` status `ready` deltaP `15.2374` edge `0.3674` maxDD `-31.6316`
- `market_context_high->equity_1h` score `-0.5287` n `273` status `ready` deltaP `3.4547` edge `0.0336` maxDD `-5.0555`
- `market_context_high->commodity_1h` score `-0.5325` n `273` status `ready` deltaP `-0.8522` edge `-0.0017` maxDD `-2.2045`
- `market_context_high->metal_1h` score `-0.5658` n `273` status `ready` deltaP `2.7665` edge `0.0015` maxDD `-2.0339`
- `market_context_high->index_1h` score `-0.5954` n `273` status `ready` deltaP `0.6356` edge `0.0042` maxDD `-0.7819`
- `market_context_high->crypto_major_1h` score `-0.9158` n `273` status `ready` deltaP `2.9831` edge `0.0359` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-1.0671` n `273` status `ready` deltaP `1.5179` edge `0.0344` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.1541` n `273` status `ready` deltaP `0.9247` edge `0.0146` maxDD `-3.165`
- `market_context_high->fx_24h` score `-1.5529` n `245` status `ready` deltaP `8.8052` edge `0.024` maxDD `-5.5435`
- `market_context_high->fx_4h` score `-1.6011` n `273` status `ready` deltaP `-1.4936` edge `-0.0004` maxDD `-2.2593`
- `market_context_high->metal_4h` score `-2.196` n `273` status `ready` deltaP `-4.9975` edge `-0.0451` maxDD `-8.9164`
- `market_context_high->commodity_4h` score `-2.6822` n `273` status `ready` deltaP `-1.2955` edge `-0.0161` maxDD `-8.5691`
- `market_context_high->index_24h` score `-2.8582` n `245` status `ready` deltaP `3.2292` edge `0.0265` maxDD `-18.1572`
- `market_context_high->crypto_major_4h` score `-3.06` n `273` status `ready` deltaP `6.7855` edge `0.137` maxDD `-25.6458`
- `market_context_high->crypto_alt_4h` score `-4.8339` n `273` status `ready` deltaP `4.0986` edge `0.0707` maxDD `-28.7346`
- `market_context_high->commodity_24h` score `-5.7364` n `245` status `ready` deltaP `-11.9523` edge `-0.0598` maxDD `-30.3426`
- `market_context_high->metal_24h` score `-6.2744` n `245` status `ready` deltaP `-1.1834` edge `-0.2177` maxDD `-13.4491`
- `market_context_high->crypto_alt_24h` score `-12.6612` n `245` status `ready` deltaP `-10.8369` edge `-0.5203` maxDD `-61.7883`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
