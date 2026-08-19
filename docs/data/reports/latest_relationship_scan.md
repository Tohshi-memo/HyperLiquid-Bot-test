# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T19:37:47.821946+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9828`

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

- `market_context_high->equity_4h` score `2.2819` n `96` status `ready` deltaP `11.6107` edge `0.2016` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.91` n `96` status `ready` deltaP `15.4504` edge `0.0863` maxDD `-0.4112`
- `market_context_high->index_1h` score `0.9881` n `96` status `ready` deltaP `16.5107` edge `0.011` maxDD `-0.0982`
- `market_context_high->metal_4h` score `0.5585` n `96` status `ready` deltaP `13.6687` edge `0.013` maxDD `-1.273`
- `market_context_high->commodity_24h` score `0.2753` n `96` status `ready` deltaP `6.4236` edge `0.1758` maxDD `-4.666`
- `market_context_high->index_4h` score `0.2248` n `96` status `ready` deltaP `9.0193` edge `0.0241` maxDD `-0.5728`
- `market_context_high->unknown_24h` score `0.2146` n `96` status `ready` deltaP `17.8819` edge `-0.0507` maxDD `-1.0505`
- `market_context_high->fx_4h` score `0.0383` n `96` status `ready` deltaP `7.4949` edge `0.0052` maxDD `-0.3539`
- `market_context_high->unknown_1h` score `-0.0145` n `96` status `ready` deltaP `6.8114` edge `-0.0239` maxDD `-0.4843`
- `market_context_high->metal_1h` score `-0.0681` n `96` status `ready` deltaP `4.1729` edge `0.0052` maxDD `-0.4291`
- `market_context_high->fx_1h` score `-0.3284` n `96` status `ready` deltaP `-1.3224` edge `0.0026` maxDD `-0.2043`
- `market_context_high->crypto_major_24h` score `-0.4693` n `96` status `ready` deltaP `2.9514` edge `0.062` maxDD `-4.9964`
- `market_context_high->commodity_4h` score `-0.684` n `96` status `ready` deltaP `-0.94` edge `0.0036` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.7128` n `96` status `ready` deltaP `-0.0187` edge `-0.0111` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.7401` n `96` status `ready` deltaP `1.6342` edge `-0.0213` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.8612` n `96` status `ready` deltaP `-7.2917` edge `-0.0052` maxDD `-1.1941`
- `market_context_high->crypto_major_4h` score `-1.0357` n `96` status `ready` deltaP `6.7327` edge `-0.0291` maxDD `-3.1677`
- `market_context_high->crypto_alt_4h` score `-1.3896` n `96` status `ready` deltaP `4.5732` edge `-0.0193` maxDD `-5.4926`
- `market_context_high->metal_24h` score `-2.8981` n `96` status `ready` deltaP `-8.3333` edge `0.0148` maxDD `-11.4635`
- `market_context_high->fx_24h` score `-3.5264` n `96` status `ready` deltaP `-18.9236` edge `-0.0094` maxDD `-1.9981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
