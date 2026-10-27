# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T05:52:28.527487+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9688`

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

- `market_context_high->unknown_4h` score `71.0778` n `144` status `ready` deltaP `3.2859` edge `5.9348` maxDD `-1.0178`
- `market_context_high->unknown_1h` score `18.5639` n `144` status `ready` deltaP `0.9024` edge `1.5899` maxDD `-1.5807`
- `market_context_high->index_24h` score `0.5483` n `120` status `ready` deltaP `21.7938` edge `0.0258` maxDD `-2.7307`
- `market_context_high->fx_4h` score `0.4578` n `144` status `ready` deltaP `13.2452` edge `0.0097` maxDD `-0.4545`
- `market_context_high->fx_1h` score `0.419` n `144` status `ready` deltaP `10.1297` edge `0.0032` maxDD `-0.1986`
- `market_context_high->metal_24h` score `0.1355` n `120` status `ready` deltaP `21.3042` edge `0.1279` maxDD `-6.204`
- `market_context_high->metal_1h` score `0.0693` n `144` status `ready` deltaP `10.9448` edge `0.0106` maxDD `-1.3073`
- `market_context_high->commodity_1h` score `0.0079` n `144` status `ready` deltaP `4.8486` edge `0.0184` maxDD `-1.0053`
- `market_context_high->fx_24h` score `-0.2284` n `120` status `ready` deltaP `15.5329` edge `0.0244` maxDD `-1.2451`
- `market_context_high->commodity_4h` score `-0.491` n `144` status `ready` deltaP `6.1315` edge `0.0411` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-0.6513` n `144` status `ready` deltaP `4.9276` edge `0.0235` maxDD `-7.8544`
- `market_context_high->index_1h` score `-0.6541` n `144` status `ready` deltaP `-1.1311` edge `-0.0026` maxDD `-1.8971`
- `market_context_high->metal_4h` score `-0.7665` n `144` status `ready` deltaP `9.7561` edge `0.0009` maxDD `-4.8031`
- `market_context_high->equity_1h` score `-1.7073` n `144` status `ready` deltaP `1.8629` edge `-0.0037` maxDD `-12.2088`
- `market_context_high->crypto_alt_1h` score `-1.966` n `144` status `ready` deltaP `-0.7527` edge `-0.0026` maxDD `-12.8878`
- `market_context_high->equity_24h` score `-3.0884` n `120` status `ready` deltaP `-0.286` edge `-0.0526` maxDD `-19.3152`
- `market_context_high->index_4h` score `-3.3041` n `144` status `ready` deltaP `-5.8943` edge `-0.0263` maxDD `-6.4466`
- `market_context_high->crypto_major_4h` score `-4.0359` n `144` status `ready` deltaP `1.2195` edge `-0.0702` maxDD `-29.0949`
- `market_context_high->crypto_major_24h` score `-4.0509` n `120` status `ready` deltaP `1.4804` edge `-0.0435` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-6.0961` n `144` status `ready` deltaP `0.8638` edge `-0.148` maxDD `-41.4777`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
