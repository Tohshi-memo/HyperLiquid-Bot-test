# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T10:37:26.306510+00:00`
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

- `market_context_high->unknown_4h` score `41.0105` n `113` status `ready` deltaP `-0.139` edge `3.452` maxDD `-1.016`
- `market_context_high->unknown_1h` score `3.8353` n `113` status `ready` deltaP `4.1704` edge `0.3407` maxDD `-1.5781`
- `market_context_high->commodity_24h` score `0.8867` n `48` status `ready` deltaP `18.4027` edge `0.0819` maxDD `-3.6055`
- `market_context_high->fx_4h` score `0.0499` n `113` status `ready` deltaP `8.221` edge `0.0092` maxDD `-0.4545`
- `market_context_high->crypto_major_24h` score `0.0248` n `48` status `ready` deltaP `2.0833` edge `0.0835` maxDD `-4.5369`
- `market_context_high->fx_1h` score `-0.049` n `113` status `ready` deltaP `3.8591` edge `0.0029` maxDD `-0.1258`
- `market_context_high->commodity_1h` score `-0.5314` n `113` status `ready` deltaP `-0.4822` edge `0.009` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.5712` n `113` status `ready` deltaP `5.3826` edge `-0.0043` maxDD `-1.6682`
- `market_context_high->index_1h` score `-0.616` n `113` status `ready` deltaP `-1.2877` edge `-0.0052` maxDD `-1.2155`
- `market_context_high->crypto_alt_24h` score `-0.865` n `48` status `ready` deltaP `10.0694` edge `0.1605` maxDD `-22.4156`
- `market_context_high->commodity_4h` score `-0.9075` n `113` status `ready` deltaP `-3.4576` edge `0.0296` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-1.3503` n `113` status `ready` deltaP `2.0494` edge `-0.0287` maxDD `-9.3126`
- `market_context_high->fx_24h` score `-1.7409` n `48` status `ready` deltaP `-2.257` edge `0.0059` maxDD `-1.2074`
- `market_context_high->metal_4h` score `-1.7931` n `113` status `ready` deltaP `5.8332` edge `-0.0173` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.1459` n `113` status `ready` deltaP `-7.7676` edge `-0.0359` maxDD `-4.3282`
- `market_context_high->crypto_alt_1h` score `-3.055` n `113` status `ready` deltaP `-2.0097` edge `-0.0538` maxDD `-11.3243`
- `market_context_high->metal_24h` score `-3.3032` n `48` status `ready` deltaP `-8.8541` edge `-0.0075` maxDD `-7.0325`
- `market_context_high->equity_1h` score `-3.7049` n `113` status `ready` deltaP `0.6584` edge `-0.0858` maxDD `-12.1865`
- `market_context_high->index_24h` score `-4.562` n `48` status `ready` deltaP `-13.7152` edge `-0.1605` maxDD `-4.925`
- `market_context_high->crypto_major_4h` score `-10.0076` n `113` status `ready` deltaP `-12.7428` edge `-0.2492` maxDD `-32.9851`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
