# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T00:22:29.184133+00:00`
- Price records: `672`
- Market context records: `4673`
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

- `market_context_high->unknown_1h` score `73.9947` n `141` status `ready` deltaP `10.3474` edge `6.139` maxDD `-1.674`
- `market_context_high->unknown_4h` score `4.4321` n `141` status `ready` deltaP `9.9128` edge `0.4243` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `1.441` n `141` status `ready` deltaP `9.4082` edge `0.1497` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.4597` n `141` status `ready` deltaP `2.1584` edge `0.0269` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.5549` n `141` status `ready` deltaP `-1.7656` edge `-0.0039` maxDD `-1.1038`
- `market_context_high->index_4h` score `-0.7631` n `141` status `ready` deltaP `3.7418` edge `-0.0105` maxDD `-5.9823`
- `market_context_high->fx_4h` score `-0.7789` n `141` status `ready` deltaP `1.1233` edge `0.0009` maxDD `-1.9927`
- `market_context_high->equity_1h` score `-0.8908` n `141` status `ready` deltaP `-2.6712` edge `0.0023` maxDD `-5.5624`
- `market_context_high->commodity_4h` score `-1.3062` n `141` status `ready` deltaP `4.185` edge `0.0154` maxDD `-9.1941`
- `market_context_high->equity_4h` score `-1.3806` n `141` status `ready` deltaP `0.7525` edge `-0.0051` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.731` n `141` status `ready` deltaP `-4.6173` edge `-0.0126` maxDD `-2.7358`
- `market_context_high->metal_1h` score `-2.8615` n `141` status `ready` deltaP `-4.4135` edge `-0.0773` maxDD `-17.4778`
- `market_context_high->commodity_24h` score `-4.8439` n `141` status `ready` deltaP `13.3312` edge `0.0579` maxDD `-30.7016`
- `market_context_high->fx_24h` score `-4.8863` n `141` status `ready` deltaP `-10.5645` edge `-0.0107` maxDD `-5.7516`
- `market_context_high->crypto_alt_1h` score `-5.5192` n `141` status `ready` deltaP `-2.6712` edge `-0.1134` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.6617` n `141` status `ready` deltaP `-5.4688` edge `-0.1434` maxDD `-27.356`
- `market_context_high->index_24h` score `-7.7955` n `141` status `ready` deltaP `-8.241` edge `-0.0572` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-8.3947` n `141` status `ready` deltaP `-1.773` edge `-0.1987` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-9.4791` n `141` status `ready` deltaP `-3.3709` edge `-0.2879` maxDD `-66.0587`
- `market_context_high->crypto_major_4h` score `-11.5127` n `141` status `ready` deltaP `-3.5428` edge `-0.358` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
