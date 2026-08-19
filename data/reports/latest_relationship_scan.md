# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T13:07:29.268902+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11762`

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

- `market_context_high->equity_4h` score `2.0315` n `96` status `ready` deltaP `11.001` edge `0.1848` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.7361` n `96` status `ready` deltaP `14.7019` edge `0.0768` maxDD `-0.4112`
- `market_context_high->crypto_major_24h` score `1.7332` n `96` status `ready` deltaP `5.2083` edge `0.2305` maxDD `-4.9964`
- `market_context_high->metal_4h` score `1.1744` n `96` status `ready` deltaP `17.6321` edge `0.0379` maxDD `-1.273`
- `market_context_high->index_1h` score `0.9534` n `96` status `ready` deltaP `16.2113` edge `0.0101` maxDD `-0.0982`
- `market_context_high->crypto_major_4h` score `0.7624` n `96` status `ready` deltaP `9.9339` edge `0.0994` maxDD `-3.1677`
- `market_context_high->commodity_24h` score `0.7302` n `96` status `ready` deltaP `10.4167` edge `0.2075` maxDD `-4.666`
- `market_context_high->unknown_24h` score `0.312` n `96` status `ready` deltaP `18.2291` edge `-0.0449` maxDD `-1.0505`
- `market_context_high->unknown_1h` score `0.1737` n `96` status `ready` deltaP `8.009` edge `-0.0162` maxDD `-0.4843`
- `market_context_high->index_4h` score `0.1482` n `96` status `ready` deltaP `8.2571` edge `0.0228` maxDD `-0.5728`
- `market_context_high->fx_4h` score `0.1428` n `96` status `ready` deltaP `9.3242` edge `0.0064` maxDD `-0.3539`
- `market_context_high->metal_1h` score `0.1272` n `96` status `ready` deltaP `5.8196` edge `0.0105` maxDD `-0.4291`
- `market_context_high->crypto_alt_4h` score `-0.0746` n `96` status `ready` deltaP `8.2317` edge `0.0659` maxDD `-5.4926`
- `market_context_high->fx_1h` score `-0.3097` n `96` status `ready` deltaP `-1.023` edge `0.003` maxDD `-0.2043`
- `market_context_high->crypto_major_1h` score `-0.3947` n `96` status `ready` deltaP `2.9815` edge `0.014` maxDD `-2.7581`
- `market_context_high->crypto_alt_1h` score `-0.4618` n `96` status `ready` deltaP `1.628` edge `0.0101` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.6033` n `96` status `ready` deltaP `0.4319` edge `0.0048` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.8954` n `96` status `ready` deltaP `-7.7408` edge `-0.0066` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.2453` n `96` status `ready` deltaP `-3.8194` edge `0.0684` maxDD `-11.4635`
- `market_context_high->fx_24h` score `-3.8566` n `96` status `ready` deltaP `-21.7014` edge `-0.0184` maxDD `-1.9981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
