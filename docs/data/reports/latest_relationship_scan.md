# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T16:06:50.840845+00:00`
- Price records: `672`
- Market context records: `6832`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11754`

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

- `market_context_high->unknown_24h` score `0.9303` n `176` status `ready` deltaP `-1.5467` edge `0.5048` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.1877` n `176` status `ready` deltaP `9.8801` edge `0.1366` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.2992` n `210` status `ready` deltaP `5.1825` edge `0.0265` maxDD `-4.2122`
- `market_context_high->fx_1h` score `-0.3495` n `210` status `ready` deltaP `0.4491` edge `0.0007` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.4076` n `210` status `ready` deltaP `2.9783` edge `0.0226` maxDD `-3.7803`
- `market_context_high->index_1h` score `-0.8707` n `210` status `ready` deltaP `-3.0068` edge `-0.0053` maxDD `-1.9022`
- `market_context_high->metal_1h` score `-0.9629` n `210` status `ready` deltaP `-6.0265` edge `-0.0094` maxDD `-1.9098`
- `market_context_high->fx_4h` score `-1.1527` n `200` status `ready` deltaP `8.4878` edge `0.002` maxDD `-2.1765`
- `market_context_high->commodity_1h` score `-1.1838` n `210` status `ready` deltaP `-3.2521` edge `-0.0085` maxDD `-2.1443`
- `market_context_high->unknown_1h` score `-1.6134` n `210` status `ready` deltaP `-3.5914` edge `-0.0204` maxDD `-3.2083`
- `market_context_high->index_4h` score `-2.0378` n `200` status `ready` deltaP `0.8598` edge `-0.033` maxDD `-9.3855`
- `market_context_high->commodity_4h` score `-2.3087` n `200` status `ready` deltaP `-4.2012` edge `-0.0154` maxDD `-5.5853`
- `market_context_high->metal_4h` score `-2.6656` n `200` status `ready` deltaP `-2.7927` edge `-0.0248` maxDD `-5.5324`
- `market_context_high->equity_1h` score `-2.7542` n `210` status `ready` deltaP `-0.3136` edge `-0.0408` maxDD `-10.5969`
- `market_context_high->crypto_major_4h` score `-2.8836` n `200` status `ready` deltaP `0.5732` edge `-0.0408` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.0595` n `200` status `ready` deltaP `0.75` edge `-0.0389` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.2119` n `200` status `ready` deltaP `-10.1402` edge `0.0365` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.4528` n `176` status `ready` deltaP `-9.7853` edge `-0.0022` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-6.6494` n `200` status `ready` deltaP `-1.4634` edge `-0.2022` maxDD `-44.2426`
- `market_context_high->metal_24h` score `-9.4049` n `176` status `ready` deltaP `-20.06` edge `-0.2235` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
