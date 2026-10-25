# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T13:52:30.617884+00:00`
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

- `market_context_high->unknown_4h` score `37.3719` n `113` status `ready` deltaP `-0.2914` edge `3.1498` maxDD `-1.016`
- `market_context_high->commodity_24h` score `0.2299` n `61` status `ready` deltaP `8.9196` edge `0.0506` maxDD `-3.6055`
- `market_context_high->fx_4h` score `0.0463` n `113` status `ready` deltaP `8.221` edge `0.0089` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.0653` n `113` status `ready` deltaP `3.5597` edge `0.0028` maxDD `-0.1258`
- `market_context_high->commodity_1h` score `-0.517` n `113` status `ready` deltaP `-0.3325` edge `0.0092` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.662` n `113` status `ready` deltaP `-2.0362` edge `-0.0061` maxDD `-1.2155`
- `market_context_high->metal_1h` score `-0.6623` n `113` status `ready` deltaP `4.3347` edge `-0.0049` maxDD `-1.6682`
- `market_context_high->commodity_4h` score `-0.8972` n `113` status `ready` deltaP `-3.3051` edge `0.0299` maxDD `-1.165`
- `market_context_high->crypto_major_24h` score `-1.2292` n `61` status `ready` deltaP `-4.9864` edge `-0.0218` maxDD `-4.5369`
- `market_context_high->crypto_major_1h` score `-1.3885` n `113` status `ready` deltaP `2.1991` edge `-0.0346` maxDD `-9.3126`
- `market_context_high->fx_24h` score `-1.5792` n `61` status `ready` deltaP `2.405` edge `0.0096` maxDD `-1.2451`
- `market_context_high->metal_4h` score `-1.8868` n `113` status `ready` deltaP `4.7661` edge `-0.018` maxDD `-5.3474`
- `market_context_high->index_24h` score `-2.1836` n `61` status `ready` deltaP `-2.6724` edge `-0.1339` maxDD `-4.925`
- `market_context_high->index_4h` score `-2.1854` n `113` status `ready` deltaP `-8.3774` edge `-0.0369` maxDD `-4.3282`
- `market_context_high->crypto_alt_1h` score `-3.1534` n `113` status `ready` deltaP `-2.0097` edge `-0.062` maxDD `-11.3243`
- `market_context_high->equity_1h` score `-3.8859` n `113` status `ready` deltaP `-0.5392` edge `-0.0929` maxDD `-12.1865`
- `market_context_high->metal_24h` score `-3.903` n `61` status `ready` deltaP `-11.538` edge `0.0187` maxDD `-7.3625`
- `market_context_high->unknown_1h` score `-4.8803` n `113` status `ready` deltaP `4.0207` edge `-0.3846` maxDD `-1.5781`
- `market_context_high->crypto_alt_24h` score `-6.9679` n `61` status `ready` deltaP `-2.3623` edge `-0.2516` maxDD `-41.0773`
- `market_context_high->crypto_major_4h` score `-10.004` n `113` status `ready` deltaP `-12.7428` edge `-0.2489` maxDD `-32.9851`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
