# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T00:07:32.151231+00:00`
- Price records: `672`
- Market context records: `4672`
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

- `market_context_high->unknown_1h` score `73.178` n `142` status `ready` deltaP `9.8929` edge `6.077` maxDD `-1.916`
- `market_context_high->unknown_4h` score `4.3495` n `142` status `ready` deltaP `10.0052` edge `0.4168` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `1.4511` n `142` status `ready` deltaP `9.3995` edge `0.1506` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.4205` n `142` status `ready` deltaP `2.528` edge `0.0277` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.5341` n `142` status `ready` deltaP `-1.3811` edge `-0.0038` maxDD `-1.1038`
- `market_context_high->fx_4h` score `-0.7576` n `142` status `ready` deltaP `1.4878` edge `0.0012` maxDD `-1.9927`
- `market_context_high->index_4h` score `-0.7811` n `142` status `ready` deltaP `3.4997` edge `-0.0112` maxDD `-5.9823`
- `market_context_high->equity_1h` score `-0.8757` n `142` status `ready` deltaP `-2.4564` edge `0.0028` maxDD `-5.5624`
- `market_context_high->commodity_4h` score `-1.2763` n `142` status `ready` deltaP `4.5796` edge `0.0166` maxDD `-9.1941`
- `market_context_high->equity_4h` score `-1.3549` n `142` status `ready` deltaP `1.0821` edge `-0.004` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.7138` n `142` status `ready` deltaP `-4.4025` edge `-0.0126` maxDD `-2.7358`
- `market_context_high->metal_1h` score `-2.906` n `142` status `ready` deltaP `-4.5585` edge `-0.0782` maxDD `-17.7845`
- `market_context_high->commodity_24h` score `-4.7795` n `142` status `ready` deltaP `13.5221` edge `0.062` maxDD `-30.7016`
- `market_context_high->fx_24h` score `-4.9488` n `142` status `ready` deltaP `-10.5756` edge `-0.0107` maxDD `-5.8293`
- `market_context_high->crypto_alt_1h` score `-5.4649` n `142` status `ready` deltaP `-2.3067` edge `-0.1113` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.6605` n `142` status `ready` deltaP `-5.6338` edge `-0.1422` maxDD `-27.356`
- `market_context_high->index_24h` score `-7.7135` n `142` status `ready` deltaP `-7.8614` edge `-0.0529` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-8.3297` n `142` status `ready` deltaP `-1.4085` edge `-0.1928` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-9.5448` n `142` status `ready` deltaP `-3.4932` edge `-0.288` maxDD `-66.6586`
- `market_context_high->crypto_major_4h` score `-11.4887` n `142` status `ready` deltaP `-3.7101` edge `-0.3538` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
