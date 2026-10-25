# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T10:52:27.219129+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5108`

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

- `market_context_high->unknown_4h` score `40.6541` n `113` status `ready` deltaP `-0.139` edge `3.4223` maxDD `-1.016`
- `market_context_high->unknown_1h` score `3.7093` n `113` status `ready` deltaP `4.1704` edge `0.3302` maxDD `-1.5781`
- `market_context_high->commodity_24h` score `0.9032` n `49` status `ready` deltaP `18.8244` edge `0.0812` maxDD `-3.6055`
- `market_context_high->fx_4h` score `0.0487` n `113` status `ready` deltaP `8.221` edge `0.0091` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.0498` n `113` status `ready` deltaP `3.8591` edge `0.0028` maxDD `-0.1258`
- `market_context_high->crypto_major_24h` score `-0.186` n `49` status `ready` deltaP `0.9353` edge `0.0683` maxDD `-4.5369`
- `market_context_high->commodity_1h` score `-0.5457` n `113` status `ready` deltaP `-0.6319` edge `0.0088` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.5832` n `113` status `ready` deltaP `5.2329` edge `-0.0043` maxDD `-1.6682`
- `market_context_high->index_1h` score `-0.616` n `113` status `ready` deltaP `-1.2877` edge `-0.0052` maxDD `-1.2155`
- `market_context_high->commodity_4h` score `-0.9075` n `113` status `ready` deltaP `-3.4576` edge `0.0296` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-1.3394` n `113` status `ready` deltaP `2.1991` edge `-0.0283` maxDD `-9.3126`
- `market_context_high->crypto_alt_24h` score `-1.5377` n `49` status `ready` deltaP `8.879` edge `0.1109` maxDD `-24.3789`
- `market_context_high->metal_4h` score `-1.8065` n `113` status `ready` deltaP `5.6807` edge `-0.0174` maxDD `-5.3474`
- `market_context_high->fx_24h` score `-1.838` n `49` status `ready` deltaP `-2.8097` edge `0.0059` maxDD `-1.2268`
- `market_context_high->index_4h` score `-2.1475` n `113` status `ready` deltaP `-7.7676` edge `-0.0361` maxDD `-4.3282`
- `market_context_high->crypto_alt_1h` score `-3.049` n `113` status `ready` deltaP `-2.0097` edge `-0.0533` maxDD `-11.3243`
- `market_context_high->metal_24h` score `-3.3626` n `49` status `ready` deltaP `-9.1943` edge `-0.0055` maxDD `-7.0736`
- `market_context_high->equity_1h` score `-3.7181` n `113` status `ready` deltaP `0.5087` edge `-0.0859` maxDD `-12.1865`
- `market_context_high->index_24h` score `-4.4578` n `49` status `ready` deltaP `-12.6985` edge `-0.1586` maxDD `-4.925`
- `market_context_high->crypto_major_4h` score `-10.0124` n `113` status `ready` deltaP `-12.7428` edge `-0.2496` maxDD `-32.9851`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
