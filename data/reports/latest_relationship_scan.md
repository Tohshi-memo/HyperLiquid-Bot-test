# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T11:22:27.450615+00:00`
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

- `market_context_high->unknown_4h` score `39.8907` n `113` status `ready` deltaP `-0.2914` edge `3.3597` maxDD `-1.016`
- `market_context_high->unknown_1h` score `3.6481` n `113` status `ready` deltaP `4.0207` edge `0.3261` maxDD `-1.5781`
- `market_context_high->commodity_24h` score `0.9423` n `51` status `ready` deltaP `19.7712` edge `0.0799` maxDD `-3.6055`
- `market_context_high->fx_4h` score `0.0487` n `113` status `ready` deltaP `8.221` edge `0.0091` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.0498` n `113` status `ready` deltaP `3.8591` edge `0.0028` maxDD `-0.1258`
- `market_context_high->crypto_major_24h` score `-0.4228` n `51` status `ready` deltaP `0.5617` edge `0.0446` maxDD `-4.5369`
- `market_context_high->commodity_1h` score `-0.5601` n `113` status `ready` deltaP `-0.7816` edge `0.0086` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.6071` n `113` status `ready` deltaP `4.9335` edge `-0.0043` maxDD `-1.6682`
- `market_context_high->index_1h` score `-0.616` n `113` status `ready` deltaP `-1.2877` edge `-0.0052` maxDD `-1.2155`
- `market_context_high->commodity_4h` score `-0.9075` n `113` status `ready` deltaP `-3.4576` edge `0.0296` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-1.3308` n `113` status `ready` deltaP `2.3488` edge `-0.0282` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-1.8332` n `113` status `ready` deltaP `5.3758` edge `-0.0176` maxDD `-5.3474`
- `market_context_high->fx_24h` score `-2.016` n `51` status `ready` deltaP `-3.8501` edge `0.0065` maxDD `-1.24`
- `market_context_high->index_4h` score `-2.1498` n `113` status `ready` deltaP `-7.7676` edge `-0.0364` maxDD `-4.3282`
- `market_context_high->crypto_alt_24h` score `-2.7547` n `51` status `ready` deltaP `6.6381` edge `0.0225` maxDD `-27.9266`
- `market_context_high->crypto_alt_1h` score `-3.0466` n `113` status `ready` deltaP `-2.0097` edge `-0.0531` maxDD `-11.3243`
- `market_context_high->metal_24h` score `-3.4771` n `51` status `ready` deltaP `-9.8345` edge `-0.0015` maxDD `-7.1488`
- `market_context_high->equity_1h` score `-3.7456` n `113` status `ready` deltaP `0.2093` edge `-0.0862` maxDD `-12.1865`
- `market_context_high->index_24h` score `-4.2619` n `51` status `ready` deltaP `-10.8048` edge `-0.1549` maxDD `-4.925`
- `market_context_high->crypto_major_4h` score `-10.022` n `113` status `ready` deltaP `-12.7428` edge `-0.2504` maxDD `-32.9851`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
