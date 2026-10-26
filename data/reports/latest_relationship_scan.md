# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T01:37:25.453157+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5070`

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

- `market_context_high->unknown_4h` score `29.9263` n `113` status `ready` deltaP `-0.9012` edge `2.5334` maxDD `-1.016`
- `market_context_high->fx_24h` score `-0.0457` n `93` status `ready` deltaP `18.7612` edge `0.0263` maxDD `-1.2451`
- `market_context_high->fx_1h` score `-0.0996` n `113` status `ready` deltaP `2.9609` edge `0.0024` maxDD `-0.1258`
- `market_context_high->fx_4h` score `-0.1022` n `113` status `ready` deltaP `6.5441` edge `0.0077` maxDD `-0.4545`
- `market_context_high->metal_24h` score `-0.1626` n `93` status `ready` deltaP `18.358` edge `0.1238` maxDD `-7.3625`
- `market_context_high->commodity_1h` score `-0.4163` n `113` status `ready` deltaP `0.5657` edge `0.0116` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.6143` n `113` status `ready` deltaP `4.9335` edge `-0.0049` maxDD `-1.6682`
- `market_context_high->index_1h` score `-0.6238` n `113` status `ready` deltaP `-1.4374` edge `-0.0052` maxDD `-1.2155`
- `market_context_high->commodity_4h` score `-0.6591` n `113` status `ready` deltaP `-0.2564` edge `0.0401` maxDD `-1.165`
- `market_context_high->crypto_major_24h` score `-0.72` n `93` status `ready` deltaP `3.4834` edge `0.0385` maxDD `-6.0711`
- `market_context_high->index_24h` score `-0.7712` n `93` status `ready` deltaP `11.3183` edge `-0.0461` maxDD `-4.925`
- `market_context_high->crypto_major_1h` score `-1.2436` n `113` status `ready` deltaP `4.1452` edge `-0.029` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-2.0156` n `113` status `ready` deltaP `3.5466` edge `-0.0206` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.1514` n `113` status `ready` deltaP `-7.7676` edge `-0.0366` maxDD `-4.3282`
- `market_context_high->crypto_alt_1h` score `-3.0924` n `113` status `ready` deltaP `-0.9618` edge `-0.0639` maxDD `-11.3243`
- `market_context_high->equity_1h` score `-3.7756` n `113` status `ready` deltaP `-0.0901` edge `-0.0867` maxDD `-12.1865`
- `market_context_high->commodity_24h` score `-3.7832` n `93` status `ready` deltaP `-11.9512` edge `-0.0805` maxDD `-11.9881`
- `market_context_high->equity_24h` score `-7.3083` n `93` status `ready` deltaP `-0.0896` edge `-0.408` maxDD `-36.6024`
- `market_context_high->crypto_alt_24h` score `-8.804` n `93` status `ready` deltaP `-7.5773` edge `-0.3237` maxDD `-51.027`
- `market_context_high->crypto_major_4h` score `-9.9944` n `113` status `ready` deltaP `-12.7428` edge `-0.2481` maxDD `-32.9851`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
