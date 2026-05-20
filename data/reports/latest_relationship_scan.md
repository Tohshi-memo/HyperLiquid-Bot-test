# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T08:22:20.754337+00:00`
- Price records: `672`
- Market context records: `1303`
- Flow alert records: `5662`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8780`

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

- `market_context_high->crypto_major_24h` score `17.0874` n `128` status `ready` deltaP `41.4062` edge `1.2611` maxDD `-8.0553`
- `market_context_high->metal_24h` score `12.8683` n `128` status `ready` deltaP `11.1111` edge `1.165` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.5832` n `128` status `ready` deltaP `28.3854` edge `0.811` maxDD `-15.1306`
- `market_context_high->index_24h` score `6.0614` n `128` status `ready` deltaP `31.5972` edge `0.4031` maxDD `-5.3574`
- `market_context_high->equity_24h` score `4.0192` n `128` status `ready` deltaP `25.0` edge `0.5813` maxDD `-14.2815`
- `market_context_high->equity_4h` score `2.6209` n `157` status `ready` deltaP `13.1107` edge `0.2015` maxDD `-3.6396`
- `market_context_high->unknown_24h` score `2.1978` n `128` status `ready` deltaP `0.3472` edge `0.4538` maxDD `-10.1706`
- `market_context_high->commodity_24h` score `0.7638` n `128` status `ready` deltaP `-15.9722` edge `0.3183` maxDD `-6.8535`
- `market_context_high->fx_24h` score `0.6647` n `128` status `ready` deltaP `8.7674` edge `0.0434` maxDD `-0.3831`
- `market_context_high->metal_4h` score `0.2601` n `157` status `ready` deltaP `13.5253` edge `0.0746` maxDD `-6.4478`
- `market_context_high->index_4h` score `0.2021` n `157` status `ready` deltaP `5.9413` edge `0.0952` maxDD `-3.7119`
- `market_context_high->equity_1h` score `0.202` n `157` status `ready` deltaP `3.6671` edge `0.0351` maxDD `-1.7505`
- `market_context_high->index_1h` score `0.1022` n `157` status `ready` deltaP `6.0624` edge `0.0181` maxDD `-1.6329`
- `market_context_high->metal_1h` score `-0.0511` n `157` status `ready` deltaP `9.0917` edge `0.0041` maxDD `-2.8509`
- `market_context_high->fx_1h` score `-0.4858` n `157` status `ready` deltaP `1.2577` edge `-0.0033` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.5677` n `157` status `ready` deltaP `0.9964` edge `0.0331` maxDD `-3.6309`
- `market_context_high->crypto_alt_4h` score `-0.7725` n `157` status `ready` deltaP `10.6018` edge `0.1969` maxDD `-19.5565`
- `market_context_high->crypto_major_1h` score `-0.8478` n `157` status `ready` deltaP `-0.6179` edge `-0.0025` maxDD `-5.8323`
- `market_context_high->unknown_4h` score `-0.8901` n `157` status `ready` deltaP `4.0207` edge `0.0862` maxDD `-11.1695`
- `market_context_high->commodity_1h` score `-1.0168` n `157` status `ready` deltaP `-2.3027` edge `-0.0079` maxDD `-2.252`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
