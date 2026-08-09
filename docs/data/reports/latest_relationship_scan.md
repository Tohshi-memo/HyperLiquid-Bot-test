# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T19:07:26.813982+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10842`

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

- `market_context_high->equity_24h` score `1.8117` n `113` status `ready` deltaP `2.9944` edge `0.437` maxDD `-21.1456`
- `market_context_high->metal_24h` score `1.6888` n `113` status `ready` deltaP `8.0291` edge `0.1448` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.2628` n `143` status `ready` deltaP `15.8142` edge `0.0671` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.8336` n `143` status `ready` deltaP `11.2904` edge `0.0285` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.607` n `113` status `ready` deltaP `20.3816` edge `0.0286` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.1679` n `113` status `ready` deltaP `5.9504` edge `0.135` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.4571` n `143` status `ready` deltaP `-2.1418` edge `-0.0054` maxDD `-0.7809`
- `market_context_high->fx_1h` score `-0.4582` n `143` status `ready` deltaP `2.3492` edge `-0.0043` maxDD `-0.9639`
- `market_context_high->metal_1h` score `-0.69` n `143` status `ready` deltaP `-4.8877` edge `-0.0063` maxDD `-0.9664`
- `market_context_high->fx_4h` score `-0.7172` n `143` status `ready` deltaP `3.084` edge `-0.005` maxDD `-1.6928`
- `market_context_high->index_4h` score `-0.961` n `143` status `ready` deltaP `-1.5254` edge `-0.0094` maxDD `-1.1743`
- `market_context_high->equity_1h` score `-1.0163` n `143` status `ready` deltaP `-1.2353` edge `0.0064` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-1.0256` n `143` status `ready` deltaP `-1.9657` edge `-0.0175` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-2.0906` n `143` status `ready` deltaP `-11.4809` edge `-0.0335` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.6154` n `143` status `ready` deltaP `-2.0286` edge `-0.0707` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.3089` n `143` status `ready` deltaP `-12.0347` edge `-0.0633` maxDD `-7.2436`
- `market_context_high->crypto_alt_4h` score `-4.1052` n `143` status `ready` deltaP `-9.0387` edge `-0.1162` maxDD `-6.585`
- `market_context_high->crypto_major_24h` score `-4.3817` n `113` status `ready` deltaP `0.8819` edge `-0.1216` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-6.0315` n `113` status `ready` deltaP `-17.3426` edge `-0.2427` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-7.8388` n `143` status `ready` deltaP `-6.3932` edge `-0.5659` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
