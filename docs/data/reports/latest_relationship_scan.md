# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T16:07:17.418196+00:00`
- Price records: `672`
- Market context records: `1438`
- Flow alert records: `6053`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8797`

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

- `market_context_high->crypto_alt_24h` score `12.2729` n `154` status `ready` deltaP `28.7811` edge `1.0325` maxDD `-15.1306`
- `market_context_high->metal_24h` score `12.1131` n `154` status `ready` deltaP `13.5507` edge `1.0858` maxDD `-6.3373`
- `market_context_high->crypto_major_24h` score `11.6216` n `154` status `ready` deltaP `27.3539` edge `0.8993` maxDD `-8.0553`
- `market_context_high->index_24h` score `4.1205` n `154` status `ready` deltaP `19.3813` edge `0.3228` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.4527` n `154` status `ready` deltaP `12.5271` edge `0.4369` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.2347` n `211` status `ready` deltaP `6.4335` edge `0.143` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.1869` n `154` status `ready` deltaP `10.2273` edge `0.0523` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.1069` n `223` status `ready` deltaP `2.2958` edge `0.0358` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.1799` n `223` status `ready` deltaP `3.1968` edge `0.0102` maxDD `-1.7205`
- `market_context_high->commodity_1h` score `-0.6358` n `223` status `ready` deltaP `-0.3746` edge `0.011` maxDD `-2.252`
- `market_context_high->crypto_alt_1h` score `-0.6426` n `223` status `ready` deltaP `1.8622` edge `0.0364` maxDD `-4.1892`
- `market_context_high->index_4h` score `-0.7076` n `211` status `ready` deltaP `-0.5202` edge `0.0534` maxDD `-3.7119`
- `market_context_high->fx_1h` score `-0.7351` n `223` status `ready` deltaP `0.67` edge `-0.0025` maxDD `-0.3914`
- `market_context_high->crypto_alt_4h` score `-0.9884` n `211` status `ready` deltaP `8.9838` edge `0.1897` maxDD `-19.5565`
- `market_context_high->fx_4h` score `-1.0633` n `211` status `ready` deltaP `-4.4193` edge `-0.0098` maxDD `-1.4313`
- `market_context_high->crypto_major_4h` score `-1.2313` n `211` status `ready` deltaP `5.0067` edge `0.1349` maxDD `-13.3376`
- `market_context_high->metal_1h` score `-1.2987` n `223` status `ready` deltaP `4.4031` edge `-0.004` maxDD `-6.3532`
- `market_context_high->crypto_major_1h` score `-1.6321` n `223` status `ready` deltaP `-0.8277` edge `0.0052` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.6677` n `211` status `ready` deltaP `5.6525` edge `0.0177` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-4.0811` n `211` status `ready` deltaP `-10.0537` edge `-0.0184` maxDD `-8.04`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
