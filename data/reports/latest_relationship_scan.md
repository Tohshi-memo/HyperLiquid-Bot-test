# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T13:07:42.423184+00:00`
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

- `market_context_high->unknown_4h` score `37.9863` n `113` status `ready` deltaP `-0.2914` edge `3.201` maxDD `-1.016`
- `market_context_high->commodity_24h` score `0.6129` n `58` status `ready` deltaP `12.057` edge `0.0616` maxDD `-3.6055`
- `market_context_high->fx_4h` score `0.0475` n `113` status `ready` deltaP `8.221` edge `0.009` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.0817` n `113` status `ready` deltaP `3.2603` edge `0.0027` maxDD `-0.1258`
- `market_context_high->commodity_1h` score `-0.5194` n `113` status `ready` deltaP `-0.3325` edge `0.009` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.662` n `113` status `ready` deltaP `-2.0362` edge `-0.0061` maxDD `-1.2155`
- `market_context_high->metal_1h` score `-0.6623` n `113` status `ready` deltaP `4.3347` edge `-0.0049` maxDD `-1.6682`
- `market_context_high->commodity_4h` score `-0.9162` n `113` status `ready` deltaP `-3.61` edge `0.0295` maxDD `-1.165`
- `market_context_high->crypto_major_24h` score `-1.0319` n `58` status `ready` deltaP `-2.9634` edge `-0.01` maxDD `-4.5369`
- `market_context_high->crypto_major_1h` score `-1.408` n `113` status `ready` deltaP `1.8997` edge `-0.0351` maxDD `-9.3126`
- `market_context_high->unknown_1h` score `-1.6451` n `113` status `ready` deltaP `4.1704` edge `-0.116` maxDD `-1.5781`
- `market_context_high->fx_24h` score `-1.8427` n `58` status `ready` deltaP `-0.7244` edge `0.0085` maxDD `-1.2451`
- `market_context_high->metal_4h` score `-1.8856` n `113` status `ready` deltaP `4.7661` edge `-0.0179` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.1854` n `113` status `ready` deltaP `-8.3774` edge `-0.0369` maxDD `-4.3282`
- `market_context_high->index_24h` score `-2.3663` n `58` status `ready` deltaP `-5.0467` edge `-0.1415` maxDD `-4.925`
- `market_context_high->crypto_alt_1h` score `-3.1882` n `113` status `ready` deltaP `-2.3091` edge `-0.0629` maxDD `-11.3243`
- `market_context_high->metal_24h` score `-3.8112` n `58` status `ready` deltaP `-11.3805` edge `0.0122` maxDD `-7.3145`
- `market_context_high->equity_1h` score `-3.8847` n `113` status `ready` deltaP `-0.5392` edge `-0.0928` maxDD `-12.1865`
- `market_context_high->crypto_alt_24h` score `-5.9912` n `58` status `ready` deltaP `0.012` edge `-0.1961` maxDD `-37.7664`
- `market_context_high->crypto_major_4h` score `-10.016` n `113` status `ready` deltaP `-12.7428` edge `-0.2499` maxDD `-32.9851`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
