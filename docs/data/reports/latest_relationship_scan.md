# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T19:44:58.174898+00:00`
- Price records: `672`
- Market context records: `4548`
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

- `market_context_high->unknown_1h` score `57.9679` n `167` status `ready` deltaP `7.036` edge `4.8338` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `29.3074` n `167` status `ready` deltaP `7.3317` edge `2.55` maxDD `-7.5275`
- `market_context_high->fx_4h` score `-0.4455` n `167` status `ready` deltaP `7.2787` edge `0.0026` maxDD `-1.9927`
- `market_context_high->fx_1h` score `-0.6644` n `167` status `ready` deltaP `0.4491` edge `-0.0029` maxDD `-1.1038`
- `market_context_high->commodity_1h` score `-0.6849` n `167` status `ready` deltaP `-1.1976` edge `0.0121` maxDD `-3.0206`
- `market_context_high->index_4h` score `-0.8816` n `167` status `ready` deltaP `1.2679` edge `-0.0092` maxDD `-5.9823`
- `market_context_high->index_1h` score `-1.0282` n `167` status `ready` deltaP `-2.994` edge `-0.011` maxDD `-2.7358`
- `market_context_high->equity_1h` score `-1.0496` n `167` status `ready` deltaP `-1.9461` edge `0.0242` maxDD `-5.5624`
- `market_context_high->equity_4h` score `-1.0937` n `167` status `ready` deltaP `2.7265` edge `0.0676` maxDD `-8.8203`
- `market_context_high->commodity_4h` score `-2.0283` n `167` status `ready` deltaP `2.3907` edge `0.0258` maxDD `-9.1941`
- `market_context_high->unknown_24h` score `-2.738` n `165` status `ready` deltaP `2.7399` edge `-0.1541` maxDD `-4.7201`
- `market_context_high->metal_1h` score `-4.4844` n `167` status `ready` deltaP `-4.6407` edge `-0.0776` maxDD `-17.8795`
- `market_context_high->fx_24h` score `-5.4384` n `165` status `ready` deltaP `-13.106` edge `-0.0146` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.5437` n `167` status `ready` deltaP `-3.8922` edge `-0.1073` maxDD `-22.2982`
- `market_context_high->index_24h` score `-5.6931` n `165` status `ready` deltaP `-9.255` edge `-0.1307` maxDD `-29.3321`
- `market_context_high->crypto_major_1h` score `-6.4454` n `167` status `ready` deltaP `-4.9401` edge `-0.1289` maxDD `-27.356`
- `market_context_high->commodity_24h` score `-7.6185` n `165` status `ready` deltaP `5.5271` edge `0.0225` maxDD `-42.8714`
- `market_context_high->equity_24h` score `-13.3821` n `165` status `ready` deltaP `-1.0354` edge `-0.2408` maxDD `-102.1031`
- `market_context_high->crypto_alt_4h` score `-13.4004` n `167` status `ready` deltaP `-2.4116` edge `-0.2349` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-15.4455` n `167` status `ready` deltaP `-7.1692` edge `-0.3176` maxDD `-67.4051`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
