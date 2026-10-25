# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T22:52:28.951625+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5062`

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

- `market_context_high->unknown_4h` score `29.6409` n `113` status `ready` deltaP `-0.7487` edge `2.5086` maxDD `-1.016`
- `market_context_high->crypto_major_24h` score `0.6913` n `82` status `ready` deltaP `6.9825` edge `0.1136` maxDD `-4.5369`
- `market_context_high->fx_1h` score `-0.0747` n `113` status `ready` deltaP `3.41` edge `0.0026` maxDD `-0.1258`
- `market_context_high->fx_4h` score `-0.0986` n `113` status `ready` deltaP `6.5441` edge `0.008` maxDD `-0.4545`
- `market_context_high->fx_24h` score `-0.3023` n `82` status `ready` deltaP `14.7569` edge `0.0201` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.4451` n `113` status `ready` deltaP `0.2663` edge `0.0112` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.6791` n `113` status `ready` deltaP `-2.3356` edge `-0.0063` maxDD `-1.2155`
- `market_context_high->metal_1h` score `-0.721` n `113` status `ready` deltaP `3.7359` edge `-0.0058` maxDD `-1.6682`
- `market_context_high->metal_24h` score `-0.7364` n `82` status `ready` deltaP `10.7131` edge `0.1012` maxDD `-7.3625`
- `market_context_high->commodity_4h` score `-0.7575` n `113` status `ready` deltaP `-1.3234` edge `0.0346` maxDD `-1.165`
- `market_context_high->index_24h` score `-1.0115` n `82` status `ready` deltaP `9.0829` edge `-0.062` maxDD `-4.925`
- `market_context_high->crypto_major_1h` score `-1.3457` n `113` status `ready` deltaP `3.0973` edge `-0.0351` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-2.0266` n `113` status `ready` deltaP `3.3941` edge `-0.0205` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.1791` n `113` status `ready` deltaP `-8.2249` edge `-0.0371` maxDD `-4.3282`
- `market_context_high->commodity_24h` score `-2.2748` n `82` status `ready` deltaP `-6.6141` edge `-0.0332` maxDD `-6.8148`
- `market_context_high->crypto_alt_1h` score `-3.2135` n `113` status `ready` deltaP `-1.7103` edge `-0.069` maxDD `-11.3243`
- `market_context_high->equity_1h` score `-3.9003` n `113` status `ready` deltaP `-0.6889` edge `-0.0931` maxDD `-12.1865`
- `market_context_high->crypto_alt_24h` score `-6.9262` n `82` status `ready` deltaP `-3.4849` edge `-0.2191` maxDD `-42.3182`
- `market_context_high->equity_24h` score `-7.9902` n `82` status `ready` deltaP `-2.2527` edge `-0.481` maxDD `-36.6024`
- `market_context_high->crypto_major_4h` score `-10.1022` n `113` status `ready` deltaP `-13.505` edge `-0.252` maxDD `-32.9851`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
