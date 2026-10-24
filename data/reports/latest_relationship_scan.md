# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-24T21:07:33.545970+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7816`

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

- `market_context_high->unknown_4h` score `17.533` n `102` status `ready` deltaP `-2.1431` edge `1.5089` maxDD `-1.016`
- `market_context_high->commodity_24h` score `1.6017` n `70` status `ready` deltaP `22.2421` edge `0.0761` maxDD `-3.6055`
- `market_context_high->commodity_4h` score `0.9633` n `102` status `ready` deltaP `12.9453` edge `0.0502` maxDD `-1.165`
- `market_context_high->commodity_1h` score `-0.1042` n `108` status `ready` deltaP `4.918` edge `0.0086` maxDD `-1.0053`
- `market_context_high->fx_1h` score `-0.1822` n `108` status `ready` deltaP `1.4415` edge `0.0025` maxDD `-0.1712`
- `market_context_high->fx_4h` score `-0.3541` n `102` status `ready` deltaP `1.4138` edge `0.0058` maxDD `-0.5168`
- `market_context_high->index_1h` score `-1.1214` n `108` status `ready` deltaP `-3.1881` edge `-0.007` maxDD `-1.2155`
- `market_context_high->metal_1h` score `-1.2748` n `108` status `ready` deltaP `-3.1216` edge `-0.006` maxDD `-1.6873`
- `market_context_high->fx_24h` score `-2.9631` n `70` status `ready` deltaP `-10.2083` edge `-0.0054` maxDD `-2.2108`
- `market_context_high->crypto_major_1h` score `-3.0679` n `108` status `ready` deltaP `-2.8998` edge `-0.0564` maxDD `-11.0607`
- `market_context_high->metal_4h` score `-3.6029` n `102` status `ready` deltaP `-12.4253` edge `-0.03` maxDD `-5.9927`
- `market_context_high->equity_1h` score `-4.2218` n `108` status `ready` deltaP `-3.0938` edge `-0.0983` maxDD `-12.6316`
- `market_context_high->metal_24h` score `-4.3323` n `70` status `ready` deltaP `-14.0922` edge `0.0211` maxDD `-8.0543`
- `market_context_high->crypto_alt_1h` score `-4.898` n `108` status `ready` deltaP `-8.472` edge `-0.0902` maxDD `-16.2522`
- `market_context_high->index_4h` score `-4.9258` n `102` status `ready` deltaP `-23.924` edge `-0.0507` maxDD `-5.3565`
- `market_context_high->crypto_major_24h` score `-5.9303` n `70` status `ready` deltaP `-11.3492` edge `-0.2428` maxDD `-27.3465`
- `market_context_high->index_24h` score `-8.6243` n `70` status `ready` deltaP `-38.7847` edge `-0.1681` maxDD `-8.0288`
- `market_context_high->crypto_alt_24h` score `-15.9272` n `70` status `ready` deltaP `-8.2639` edge `-0.7216` maxDD `-88.8874`
- `market_context_high->crypto_major_4h` score `-16.2066` n `102` status `ready` deltaP `-30.7` edge `-0.396` maxDD `-47.9909`
- `market_context_high->equity_4h` score `-17.142` n `102` status `ready` deltaP `-23.9898` edge `-0.4732` maxDD `-51.2958`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
