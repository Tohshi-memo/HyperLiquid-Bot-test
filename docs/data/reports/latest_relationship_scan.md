# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T23:52:17.768875+00:00`
- Price records: `672`
- Market context records: `1369`
- Flow alert records: `5855`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8804`

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

- `market_context_high->crypto_major_24h` score `13.0548` n `142` status `ready` deltaP `31.5287` edge `0.9909` maxDD `-8.0553`
- `market_context_high->metal_24h` score `12.3671` n `142` status `ready` deltaP `13.5759` edge `1.1068` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `10.4009` n `142` status `ready` deltaP `28.6165` edge `0.8776` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.0982` n `142` status `ready` deltaP `22.4325` edge `0.3006` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.5805` n `142` status `ready` deltaP `15.4685` edge `0.3446` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.6729` n `167` status `ready` deltaP `8.9309` edge `0.1587` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.5798` n `142` status `ready` deltaP `10.7688` edge `0.0483` maxDD `-1.0754`
- `market_context_high->index_1h` score `-0.0657` n `179` status `ready` deltaP `3.807` edge `0.0127` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.0759` n `167` status `ready` deltaP `11.1865` edge `0.0622` maxDD `-6.4478`
- `market_context_high->equity_1h` score `-0.146` n `179` status `ready` deltaP `2.1201` edge `0.023` maxDD `-2.8014`
- `market_context_high->index_4h` score `-0.263` n `167` status `ready` deltaP `1.6476` edge `0.0642` maxDD `-3.7119`
- `market_context_high->fx_1h` score `-0.3179` n `179` status `ready` deltaP `1.4259` edge `-0.0037` maxDD `-0.3914`
- `market_context_high->metal_1h` score `-0.4197` n `179` status `ready` deltaP `6.2933` edge `0.0031` maxDD `-3.5762`
- `market_context_high->commodity_1h` score `-0.7573` n `179` status `ready` deltaP `-0.7686` edge `0.0035` maxDD `-2.252`
- `market_context_high->crypto_alt_1h` score `-0.8543` n `179` status `ready` deltaP `-0.2609` edge `0.0176` maxDD `-3.6309`
- `market_context_high->crypto_major_1h` score `-1.0394` n `179` status `ready` deltaP `-2.3751` edge `-0.0109` maxDD `-6.1883`
- `market_context_high->fx_4h` score `-1.3781` n `167` status `ready` deltaP `-9.6191` edge `-0.0155` maxDD `-1.4311`
- `market_context_high->crypto_alt_4h` score `-1.6446` n `167` status `ready` deltaP `6.7658` edge `0.1498` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-1.9741` n `167` status `ready` deltaP `2.847` edge `0.0874` maxDD `-13.3376`
- `market_context_high->unknown_4h` score `-2.9828` n `167` status `ready` deltaP `0.6919` edge `-0.1599` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
