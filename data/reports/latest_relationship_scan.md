# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T13:22:24.330813+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5220`

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

- `market_context_high->unknown_4h` score `37.6635` n `113` status `ready` deltaP `-0.2914` edge `3.1741` maxDD `-1.016`
- `market_context_high->commodity_24h` score `0.482` n `59` status `ready` deltaP `10.9758` edge `0.0579` maxDD `-3.6055`
- `market_context_high->fx_4h` score `0.0475` n `113` status `ready` deltaP `8.221` edge `0.009` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.0739` n `113` status `ready` deltaP `3.41` edge `0.0027` maxDD `-0.1258`
- `market_context_high->commodity_1h` score `-0.5194` n `113` status `ready` deltaP `-0.3325` edge `0.009` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.662` n `113` status `ready` deltaP `-2.0362` edge `-0.0061` maxDD `-1.2155`
- `market_context_high->metal_1h` score `-0.6623` n `113` status `ready` deltaP `4.3347` edge `-0.0049` maxDD `-1.6682`
- `market_context_high->commodity_4h` score `-0.9154` n `113` status `ready` deltaP `-3.61` edge `0.0296` maxDD `-1.165`
- `market_context_high->crypto_major_24h` score `-1.102` n `59` status `ready` deltaP `-3.6664` edge `-0.0143` maxDD `-4.5369`
- `market_context_high->crypto_major_1h` score `-1.3971` n `113` status `ready` deltaP `2.0494` edge `-0.0347` maxDD `-9.3126`
- `market_context_high->unknown_1h` score `-1.6895` n `113` status `ready` deltaP `4.1704` edge `-0.1197` maxDD `-1.5781`
- `market_context_high->fx_24h` score `-1.7571` n `59` status `ready` deltaP `0.3002` edge `0.0088` maxDD `-1.2451`
- `market_context_high->metal_4h` score `-1.8856` n `113` status `ready` deltaP `4.7661` edge `-0.0179` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.1854` n `113` status `ready` deltaP `-8.3774` edge `-0.0369` maxDD `-4.3282`
- `market_context_high->index_24h` score `-2.3043` n `59` status `ready` deltaP `-4.2284` edge `-0.139` maxDD `-4.925`
- `market_context_high->crypto_alt_1h` score `-3.1846` n `113` status `ready` deltaP `-2.3091` edge `-0.0626` maxDD `-11.3243`
- `market_context_high->metal_24h` score `-3.8456` n `59` status `ready` deltaP `-11.4407` edge `0.0142` maxDD `-7.3386`
- `market_context_high->equity_1h` score `-3.8859` n `113` status `ready` deltaP `-0.5392` edge `-0.0929` maxDD `-12.1865`
- `market_context_high->crypto_alt_24h` score `-6.3523` n `59` status `ready` deltaP `-0.8063` edge `-0.2173` maxDD `-39.0042`
- `market_context_high->crypto_major_4h` score `-10.0124` n `113` status `ready` deltaP `-12.7428` edge `-0.2496` maxDD `-32.9851`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
