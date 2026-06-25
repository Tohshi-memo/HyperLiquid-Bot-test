# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T04:20:55.123825+00:00`
- Price records: `672`
- Market context records: `4689`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9744`

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

- `market_context_high->unknown_1h` score `78.7334` n `135` status `ready` deltaP `12.1757` edge `6.5217` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.1964` n `135` status `ready` deltaP `10.9169` edge `0.4813` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `1.9917` n `135` status `ready` deltaP `11.1459` edge `0.184` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.535` n `135` status `ready` deltaP `1.6068` edge `0.0243` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.7788` n `135` status `ready` deltaP `3.7692` edge `-0.0127` maxDD `-5.9823`
- `market_context_high->equity_1h` score `-0.8773` n `135` status `ready` deltaP `-3.0417` edge `0.0065` maxDD `-5.5624`
- `market_context_high->fx_4h` score `-0.9449` n `135` status `ready` deltaP `-1.6351` edge `-0.002` maxDD `-1.9927`
- `market_context_high->fx_1h` score `-1.0598` n `135` status `ready` deltaP `-4.1927` edge `-0.0049` maxDD `-1.1038`
- `market_context_high->equity_4h` score `-1.2513` n `135` status `ready` deltaP `1.3946` edge `0.0072` maxDD `-8.8203`
- `market_context_high->commodity_4h` score `-1.2549` n `135` status `ready` deltaP `5.2462` edge `0.0149` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.8079` n `135` status `ready` deltaP `-5.5866` edge `-0.013` maxDD `-2.6999`
- `market_context_high->metal_1h` score `-2.8707` n `135` status `ready` deltaP `-4.4766` edge `-0.0814` maxDD `-17.2107`
- `market_context_high->fx_24h` score `-4.6954` n `135` status `ready` deltaP `-12.1759` edge `-0.0141` maxDD `-5.3476`
- `market_context_high->commodity_24h` score `-4.8958` n `135` status `ready` deltaP `13.8078` edge `0.0504` maxDD `-30.7016`
- `market_context_high->crypto_alt_1h` score `-5.5568` n `135` status `ready` deltaP `-2.301` edge `-0.119` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.6843` n `135` status `ready` deltaP `-4.9568` edge `-0.1487` maxDD `-27.356`
- `market_context_high->index_24h` score `-8.3783` n `135` status `ready` deltaP `-10.6366` edge `-0.0898` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-8.6557` n `135` status `ready` deltaP `-3.3119` edge `-0.2219` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-9.1792` n `135` status `ready` deltaP `-0.7012` edge `-0.2868` maxDD `-64.494`
- `market_context_high->crypto_major_4h` score `-11.6619` n `135` status `ready` deltaP `-3.7477` edge `-0.3801` maxDD `-81.8692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
