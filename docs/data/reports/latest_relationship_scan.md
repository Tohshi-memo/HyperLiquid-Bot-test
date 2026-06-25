# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T04:37:29.454631+00:00`
- Price records: `672`
- Market context records: `4690`
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

- `market_context_high->unknown_1h` score `78.725` n `135` status `ready` deltaP `12.1757` edge `6.521` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.218` n `135` status `ready` deltaP `10.9169` edge `0.4831` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `2.0511` n `135` status `ready` deltaP `11.3195` edge `0.1878` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.553` n `135` status `ready` deltaP `1.4571` edge `0.0238` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.7781` n `135` status `ready` deltaP `3.7692` edge `-0.0126` maxDD `-5.9823`
- `market_context_high->equity_1h` score `-0.8781` n `135` status `ready` deltaP `-3.0417` edge `0.0064` maxDD `-5.5624`
- `market_context_high->fx_4h` score `-0.9449` n `135` status `ready` deltaP `-1.6351` edge `-0.002` maxDD `-1.9927`
- `market_context_high->fx_1h` score `-1.061` n `135` status `ready` deltaP `-4.1927` edge `-0.005` maxDD `-1.1038`
- `market_context_high->equity_4h` score `-1.249` n `135` status `ready` deltaP `1.3946` edge `0.0075` maxDD `-8.8203`
- `market_context_high->commodity_4h` score `-1.2565` n `135` status `ready` deltaP `5.2462` edge `0.0147` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.8079` n `135` status `ready` deltaP `-5.5866` edge `-0.013` maxDD `-2.6999`
- `market_context_high->metal_1h` score `-2.8707` n `135` status `ready` deltaP `-4.4766` edge `-0.0814` maxDD `-17.2107`
- `market_context_high->fx_24h` score `-4.7141` n `135` status `ready` deltaP `-12.3495` edge `-0.0145` maxDD `-5.3476`
- `market_context_high->commodity_24h` score `-4.8603` n `135` status `ready` deltaP `13.9815` edge `0.0522` maxDD `-30.7016`
- `market_context_high->crypto_alt_1h` score `-5.5592` n `135` status `ready` deltaP `-2.301` edge `-0.1192` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.6999` n `135` status `ready` deltaP `-5.1065` edge `-0.149` maxDD `-27.356`
- `market_context_high->index_24h` score `-8.3831` n `135` status `ready` deltaP `-10.6366` edge `-0.0902` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-8.6446` n `135` status `ready` deltaP `-3.1595` edge `-0.2215` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-9.1714` n `135` status `ready` deltaP `-0.7012` edge `-0.2858` maxDD `-64.494`
- `market_context_high->crypto_major_4h` score `-11.6446` n `135` status `ready` deltaP `-3.5953` edge `-0.3789` maxDD `-81.8692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
