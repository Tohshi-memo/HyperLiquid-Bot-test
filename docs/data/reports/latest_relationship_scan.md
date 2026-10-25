# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T18:37:28.943425+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5440`

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

- `market_context_high->unknown_4h` score `30.1317` n `113` status `ready` deltaP `-0.7487` edge `2.5495` maxDD `-1.016`
- `market_context_high->fx_4h` score `-0.0427` n `113` status `ready` deltaP `7.1539` edge `0.0086` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.0817` n `113` status `ready` deltaP `3.2603` edge `0.0027` maxDD `-0.1258`
- `market_context_high->crypto_major_24h` score `-0.2269` n `69` status `ready` deltaP `-0.3699` edge `0.0861` maxDD `-4.5369`
- `market_context_high->commodity_1h` score `-0.4655` n `113` status `ready` deltaP `0.2663` edge `0.0095` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.6299` n `113` status `ready` deltaP `4.7838` edge `-0.0052` maxDD `-1.6682`
- `market_context_high->commodity_24h` score `-0.6832` n `69` status `ready` deltaP `1.8871` edge `0.0199` maxDD `-3.6055`
- `market_context_high->index_1h` score `-0.7017` n `113` status `ready` deltaP `-2.7847` edge `-0.0062` maxDD `-1.2155`
- `market_context_high->commodity_4h` score `-0.8024` n `113` status `ready` deltaP `-1.7807` edge `0.0319` maxDD `-1.165`
- `market_context_high->fx_24h` score `-1.1166` n `69` status `ready` deltaP `7.7672` edge `0.0124` maxDD `-1.2451`
- `market_context_high->crypto_major_1h` score `-1.3317` n `113` status `ready` deltaP `3.0973` edge `-0.0333` maxDD `-9.3126`
- `market_context_high->index_24h` score `-1.6518` n `69` status `ready` deltaP `2.6495` edge `-0.1012` maxDD `-4.925`
- `market_context_high->metal_4h` score `-1.9158` n `113` status `ready` deltaP `4.6137` edge `-0.0194` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.206` n `113` status `ready` deltaP `-8.6822` edge `-0.0375` maxDD `-4.3282`
- `market_context_high->metal_24h` score `-2.6831` n `69` status `ready` deltaP `-1.4644` edge `0.0532` maxDD `-7.3625`
- `market_context_high->crypto_alt_1h` score `-3.199` n `113` status `ready` deltaP `-1.86` edge `-0.0668` maxDD `-11.3243`
- `market_context_high->equity_1h` score `-3.9686` n `113` status `ready` deltaP `-1.4374` edge `-0.0938` maxDD `-12.1865`
- `market_context_high->crypto_alt_24h` score `-6.5371` n `69` status `ready` deltaP `0.2038` edge `-0.1938` maxDD `-42.3182`
- `market_context_high->crypto_major_4h` score `-10.1891` n `113` status `ready` deltaP `-13.9623` edge `-0.2562` maxDD `-32.9851`
- `market_context_high->equity_24h` score `-10.1911` n `69` status `ready` deltaP `-11.4432` edge `-0.7019` maxDD `-36.6024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
