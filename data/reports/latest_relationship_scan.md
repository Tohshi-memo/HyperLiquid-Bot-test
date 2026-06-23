# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T19:52:28.321678+00:00`
- Price records: `672`
- Market context records: `4549`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10045`

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

- `market_context_high->unknown_1h` score `58.4672` n `166` status `ready` deltaP `6.8267` edge `4.8768` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `29.315` n `166` status `ready` deltaP `7.1261` edge `2.552` maxDD `-7.5275`
- `market_context_high->fx_4h` score `-0.4605` n `166` status `ready` deltaP `6.9901` edge `0.0026` maxDD `-1.9927`
- `market_context_high->commodity_1h` score `-0.6647` n `166` status `ready` deltaP `-0.9343` edge `0.0123` maxDD `-2.9694`
- `market_context_high->fx_1h` score `-0.6913` n `166` status `ready` deltaP `0.128` edge `-0.003` maxDD `-1.1038`
- `market_context_high->equity_4h` score `-0.7142` n `166` status `ready` deltaP `2.6337` edge `0.0678` maxDD `-8.8203`
- `market_context_high->index_4h` score `-0.861` n `166` status `ready` deltaP `1.6034` edge `-0.0088` maxDD `-5.9823`
- `market_context_high->index_1h` score `-1.0191` n `166` status `ready` deltaP `-2.8479` edge `-0.0108` maxDD `-2.7358`
- `market_context_high->equity_1h` score `-1.0814` n `166` status `ready` deltaP `-2.2383` edge `0.0235` maxDD `-5.5624`
- `market_context_high->commodity_4h` score `-1.9913` n `166` status `ready` deltaP `2.6576` edge `0.0271` maxDD `-9.1941`
- `market_context_high->unknown_24h` score `-2.77` n `164` status `ready` deltaP `2.6254` edge `-0.156` maxDD `-4.7201`
- `market_context_high->metal_1h` score `-4.5283` n `166` status `ready` deltaP `-4.9798` edge `-0.079` maxDD `-17.8795`
- `market_context_high->fx_24h` score `-5.4609` n `164` status `ready` deltaP `-13.3426` edge `-0.0149` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.535` n `166` status `ready` deltaP `-3.7533` edge `-0.1075` maxDD `-22.2982`
- `market_context_high->index_24h` score `-5.7018` n `164` status `ready` deltaP `-9.3623` edge `-0.1311` maxDD `-29.3321`
- `market_context_high->crypto_major_1h` score `-6.4448` n `166` status `ready` deltaP `-4.8121` edge `-0.1297` maxDD `-27.356`
- `market_context_high->commodity_24h` score `-7.3977` n `164` status `ready` deltaP `5.7969` edge `0.0261` maxDD `-41.831`
- `market_context_high->crypto_alt_4h` score `-8.7116` n `166` status `ready` deltaP `-2.2719` edge `-0.236` maxDD `-63.9243`
- `market_context_high->equity_24h` score `-13.3891` n `164` status `ready` deltaP `-1.0798` edge `-0.2414` maxDD `-102.1031`
- `market_context_high->metal_4h` score `-15.4925` n `166` status `ready` deltaP `-7.3666` edge `-0.3202` maxDD `-67.4051`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
