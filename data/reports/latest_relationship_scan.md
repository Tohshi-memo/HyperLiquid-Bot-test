# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T20:37:31.477605+00:00`
- Price records: `672`
- Market context records: `4552`
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

- `market_context_high->unknown_1h` score `59.8449` n `163` status `ready` deltaP `6.1837` edge `4.9959` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `2.067` n `163` status `ready` deltaP `6.9514` edge `0.2825` maxDD `-7.5275`
- `market_context_high->fx_4h` score `-0.4755` n `163` status `ready` deltaP `6.7166` edge `0.0025` maxDD `-1.9927`
- `market_context_high->commodity_1h` score `-0.5534` n `163` status `ready` deltaP `-0.4243` edge `0.0152` maxDD `-2.3322`
- `market_context_high->fx_1h` score `-0.6961` n `163` status `ready` deltaP `0.0689` edge `-0.003` maxDD `-1.1038`
- `market_context_high->equity_4h` score `-0.7023` n `163` status `ready` deltaP `2.3371` edge `0.0713` maxDD `-8.8203`
- `market_context_high->index_4h` score `-0.7965` n `163` status `ready` deltaP `2.6345` edge `-0.0074` maxDD `-5.9823`
- `market_context_high->index_1h` score `-0.9835` n `163` status `ready` deltaP `-2.2382` edge `-0.0103` maxDD `-2.7358`
- `market_context_high->equity_1h` score `-1.0647` n `163` status `ready` deltaP `-2.0591` edge `0.0237` maxDD `-5.5624`
- `market_context_high->commodity_4h` score `-1.8937` n `163` status `ready` deltaP `3.1732` edge `0.0318` maxDD `-9.1941`
- `market_context_high->unknown_24h` score `-2.8918` n `161` status `ready` deltaP `2.2731` edge `-0.1638` maxDD `-4.7201`
- `market_context_high->metal_1h` score `-4.4812` n `163` status `ready` deltaP `-4.1815` edge `-0.0804` maxDD `-17.8795`
- `market_context_high->crypto_alt_1h` score `-5.5144` n `163` status `ready` deltaP `-3.3154` edge `-0.1087` maxDD `-22.2982`
- `market_context_high->fx_24h` score `-5.5298` n `161` status `ready` deltaP `-14.083` edge `-0.0157` maxDD `-6.0982`
- `market_context_high->index_24h` score `-5.7305` n `161` status `ready` deltaP `-9.705` edge `-0.1325` maxDD `-29.3321`
- `market_context_high->crypto_major_1h` score `-6.5406` n `163` status `ready` deltaP `-5.335` edge `-0.1342` maxDD `-27.356`
- `market_context_high->commodity_24h` score `-6.8399` n `161` status `ready` deltaP `6.6263` edge `0.0349` maxDD `-39.2589`
- `market_context_high->crypto_alt_4h` score `-8.7066` n `163` status `ready` deltaP `-1.8311` edge `-0.2383` maxDD `-63.9243`
- `market_context_high->equity_24h` score `-13.4304` n `161` status `ready` deltaP `-1.2293` edge `-0.2457` maxDD `-102.1031`
- `market_context_high->metal_4h` score `-15.6115` n `163` status `ready` deltaP `-7.9848` edge `-0.326` maxDD `-67.4051`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
