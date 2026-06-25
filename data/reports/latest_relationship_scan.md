# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T02:07:26.340918+00:00`
- Price records: `672`
- Market context records: `4680`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9870`

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

- `market_context_high->unknown_1h` score `78.7142` n `135` status `ready` deltaP `12.1757` edge `6.5201` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.0292` n `135` status `ready` deltaP `10.612` edge `0.4694` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `1.5679` n `135` status `ready` deltaP `9.5834` edge `0.1591` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.5075` n `135` status `ready` deltaP `1.7565` edge `0.0256` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.8538` n `135` status `ready` deltaP `2.7021` edge `-0.0152` maxDD `-5.9823`
- `market_context_high->equity_1h` score `-0.8804` n `135` status `ready` deltaP `-3.0417` edge `0.0061` maxDD `-5.5624`
- `market_context_high->fx_4h` score `-0.9141` n `135` status `ready` deltaP `-1.1778` edge `-0.0011` maxDD `-1.9927`
- `market_context_high->fx_1h` score `-1.0598` n `135` status `ready` deltaP `-4.1927` edge `-0.0049` maxDD `-1.1038`
- `market_context_high->commodity_4h` score `-1.2253` n `135` status `ready` deltaP `5.2462` edge `0.0187` maxDD `-9.1941`
- `market_context_high->equity_4h` score `-1.3967` n `135` status `ready` deltaP `0.0226` edge `-0.0023` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.778` n `135` status `ready` deltaP `-5.1375` edge `-0.0135` maxDD `-2.6999`
- `market_context_high->metal_1h` score `-2.8349` n `135` status `ready` deltaP `-4.1772` edge `-0.0788` maxDD `-17.2107`
- `market_context_high->fx_24h` score `-4.5368` n `135` status `ready` deltaP `-10.6134` edge `-0.0113` maxDD `-5.3476`
- `market_context_high->commodity_24h` score `-5.1612` n `135` status `ready` deltaP `12.2453` edge `0.0387` maxDD `-30.7016`
- `market_context_high->crypto_alt_1h` score `-5.6191` n `135` status `ready` deltaP `-2.7501` edge `-0.1212` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.761` n `135` status `ready` deltaP `-5.5556` edge `-0.1511` maxDD `-27.356`
- `market_context_high->index_24h` score `-8.3543` n `135` status `ready` deltaP `-10.6366` edge `-0.0878` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-8.7257` n `135` status `ready` deltaP `-4.0741` edge `-0.2258` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-9.3231` n `135` status `ready` deltaP `-2.0732` edge `-0.2961` maxDD `-64.494`
- `market_context_high->crypto_major_4h` score `-11.7396` n `135` status `ready` deltaP `-4.3575` edge `-0.386` maxDD `-81.8692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
