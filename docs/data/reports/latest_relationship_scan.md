# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T18:07:28.252909+00:00`
- Price records: `672`
- Market context records: `7276`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13791`

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

- `market_context_high->fx_1h` score `-0.2222` n `138` status `ready` deltaP `3.0226` edge `0.0003` maxDD `-0.5817`
- `market_context_high->crypto_alt_1h` score `-0.7352` n `138` status `ready` deltaP `-0.5511` edge `0.0133` maxDD `-5.9775`
- `market_context_high->crypto_major_1h` score `-0.906` n `138` status `ready` deltaP `1.8745` edge `0.0124` maxDD `-7.6171`
- `market_context_high->fx_4h` score `-0.9504` n `135` status `ready` deltaP `4.1591` edge `0.0104` maxDD `-1.4649`
- `market_context_high->commodity_1h` score `-1.1605` n `138` status `ready` deltaP `-2.8529` edge `-0.0156` maxDD `-1.9668`
- `market_context_high->unknown_4h` score `-1.1679` n `135` status `ready` deltaP `7.9257` edge `0.0857` maxDD `-6.2026`
- `market_context_high->unknown_1h` score `-1.3273` n `138` status `ready` deltaP `-1.6532` edge `-0.0968` maxDD `-1.3212`
- `market_context_high->index_1h` score `-1.4034` n `138` status `ready` deltaP `-6.0125` edge `-0.0096` maxDD `-2.3816`
- `market_context_high->commodity_4h` score `-1.5469` n `135` status `ready` deltaP `-0.7612` edge `-0.0203` maxDD `-2.9494`
- `market_context_high->fx_24h` score `-1.9737` n `126` status `ready` deltaP `-5.1429` edge `-0.0074` maxDD `-2.1564`
- `market_context_high->commodity_24h` score `-2.2165` n `126` status `ready` deltaP `-1.0711` edge `-0.0978` maxDD `-2.3815`
- `market_context_high->metal_1h` score `-2.238` n `138` status `ready` deltaP `-9.5765` edge `-0.0068` maxDD `-1.9351`
- `market_context_high->metal_4h` score `-4.2046` n `135` status `ready` deltaP `-12.5316` edge `-0.0194` maxDD `-4.795`
- `market_context_high->equity_1h` score `-4.4114` n `138` status `ready` deltaP `-7.6119` edge `-0.0642` maxDD `-15.5469`
- `market_context_high->index_4h` score `-5.5806` n `135` status `ready` deltaP `-16.9691` edge `-0.0644` maxDD `-12.6686`
- `market_context_high->crypto_alt_4h` score `-5.688` n `135` status `ready` deltaP `-3.2712` edge `-0.0606` maxDD `-23.6607`
- `market_context_high->crypto_major_4h` score `-5.959` n `135` status `ready` deltaP `-3.5739` edge `-0.0672` maxDD `-24.7779`
- `market_context_high->unknown_24h` score `-6.5799` n `127` status `ready` deltaP `-14.0461` edge `-0.0678` maxDD `-18.9508`
- `market_context_high->metal_24h` score `-13.0835` n `127` status `ready` deltaP `-33.4331` edge `-0.1653` maxDD `-29.5014`
- `market_context_high->index_24h` score `-15.5873` n `126` status `ready` deltaP `-29.619` edge `-0.2023` maxDD `-42.9344`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
