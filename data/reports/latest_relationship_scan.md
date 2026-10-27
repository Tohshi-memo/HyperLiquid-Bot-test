# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T01:37:41.467424+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8004`

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

- `market_context_high->unknown_4h` score `87.5251` n `153` status `ready` deltaP `1.3221` edge `7.3185` maxDD `-1.0178`
- `market_context_high->unknown_1h` score `20.8992` n `153` status `ready` deltaP `1.6242` edge `1.7797` maxDD `-1.5807`
- `market_context_high->fx_1h` score `0.3021` n `153` status `ready` deltaP `8.7139` edge `0.0029` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.2711` n `153` status `ready` deltaP `11.0015` edge `0.0091` maxDD `-0.4545`
- `market_context_high->metal_24h` score `0.1531` n `114` status `ready` deltaP `22.6596` edge `0.1312` maxDD `-7.0108`
- `market_context_high->index_24h` score `-0.0961` n `114` status `ready` deltaP `15.5295` edge `0.008` maxDD `-4.5747`
- `market_context_high->metal_1h` score `-0.1314` n `153` status `ready` deltaP `8.3304` edge `0.0068` maxDD `-1.6682`
- `market_context_high->fx_24h` score `-0.1644` n `114` status `ready` deltaP `16.5374` edge `0.0259` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.1647` n `153` status `ready` deltaP `3.0508` edge `0.016` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.3449` n `153` status `ready` deltaP `6.6684` edge `0.0497` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.628` n `153` status `ready` deltaP `-0.7358` edge `-0.0019` maxDD `-1.8971`
- `market_context_high->crypto_major_1h` score `-0.9044` n `153` status `ready` deltaP `4.5331` edge `0.0119` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-0.9344` n `153` status `ready` deltaP `7.8172` edge `-0.0009` maxDD `-5.3474`
- `market_context_high->equity_1h` score `-1.8486` n `153` status `ready` deltaP `0.8561` edge `-0.0151` maxDD `-12.2088`
- `market_context_high->crypto_alt_1h` score `-2.0155` n `153` status `ready` deltaP `-0.4256` edge `-0.0071` maxDD `-13.2099`
- `market_context_high->index_4h` score `-3.4225` n `153` status `ready` deltaP `-6.3845` edge `-0.025` maxDD `-6.7447`
- `market_context_high->crypto_major_4h` score `-4.6688` n `153` status `ready` deltaP `-0.7632` edge `-0.0895` maxDD `-32.9851`
- `market_context_high->crypto_major_24h` score `-4.6722` n `114` status `ready` deltaP `-3.2382` edge `-0.0917` maxDD `-29.1905`
- `market_context_high->commodity_24h` score `-5.8394` n `114` status `ready` deltaP `-11.9113` edge `-0.1103` maxDD `-24.0477`
- `market_context_high->equity_24h` score `-6.913` n `114` status `ready` deltaP `-7.6029` edge `-0.2923` maxDD `-35.4638`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
