# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T06:22:31.114740+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9656`

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

- `market_context_high->unknown_4h` score `71.8997` n `142` status `ready` deltaP `3.1197` edge `6.0044` maxDD `-1.0178`
- `market_context_high->unknown_1h` score `20.9251` n `142` status `ready` deltaP `0.8076` edge `1.7873` maxDD `-1.5807`
- `market_context_high->index_24h` score `0.5491` n `120` status `ready` deltaP `21.7938` edge `0.0259` maxDD `-2.7307`
- `market_context_high->fx_4h` score `0.4262` n `142` status `ready` deltaP `12.85` edge `0.0097` maxDD `-0.4545`
- `market_context_high->fx_1h` score `0.4164` n `142` status `ready` deltaP `10.0974` edge `0.0032` maxDD `-0.1986`
- `market_context_high->metal_1h` score `0.05` n `142` status `ready` deltaP `10.6182` edge `0.0103` maxDD `-1.3073`
- `market_context_high->metal_24h` score `0.0224` n `120` status `ready` deltaP `19.9841` edge `0.1222` maxDD `-6.204`
- `market_context_high->commodity_1h` score `-0.0514` n `142` status `ready` deltaP `4.2422` edge `0.0175` maxDD `-1.0053`
- `market_context_high->fx_24h` score `-0.3056` n `120` status `ready` deltaP `14.2128` edge `0.0233` maxDD `-1.2451`
- `market_context_high->commodity_4h` score `-0.548` n `142` status `ready` deltaP `5.5544` edge `0.0402` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-0.6166` n `142` status `ready` deltaP `5.1067` edge `0.0233` maxDD `-7.5779`
- `market_context_high->index_1h` score `-0.6865` n `142` status `ready` deltaP `-1.575` edge `-0.0038` maxDD `-1.8971`
- `market_context_high->metal_4h` score `-0.7903` n `142` status `ready` deltaP `9.3568` edge `0.0005` maxDD `-4.8031`
- `market_context_high->equity_1h` score `-1.7819` n `142` status `ready` deltaP `1.419` edge `-0.0103` maxDD `-12.2088`
- `market_context_high->crypto_alt_1h` score `-2.0137` n `142` status `ready` deltaP `-1.01` edge `-0.007` maxDD `-12.8878`
- `market_context_high->equity_24h` score `-3.0509` n `120` status `ready` deltaP `-0.286` edge `-0.0478` maxDD `-19.3152`
- `market_context_high->index_4h` score `-3.1413` n `142` status `ready` deltaP `-5.3075` edge `-0.0261` maxDD `-6.3569`
- `market_context_high->crypto_major_4h` score `-3.9545` n `142` status `ready` deltaP `1.9237` edge `-0.0684` maxDD `-28.7799`
- `market_context_high->crypto_major_24h` score `-4.3122` n `120` status `ready` deltaP `0.8203` edge `-0.0726` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-5.8349` n `142` status `ready` deltaP `1.5094` edge `-0.1409` maxDD `-40.3781`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
