# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T04:22:13.640632+00:00`
- Price records: `672`
- Market context records: `1388`
- Flow alert records: `5910`
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

- `market_context_high->crypto_major_24h` score `13.4533` n `157` status `ready` deltaP `28.8747` edge `1.0418` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `11.8163` n `157` status `ready` deltaP `28.8184` edge `0.9942` maxDD `-15.1306`
- `market_context_high->metal_24h` score `11.5861` n `157` status `ready` deltaP `12.6039` edge `1.0482` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.2644` n `157` status `ready` deltaP `20.2495` edge `0.329` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.7154` n `157` status `ready` deltaP `13.42` edge `0.3695` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.6525` n `185` status `ready` deltaP `8.5061` edge `0.164` maxDD `-3.6396`
- `market_context_high->index_1h` score `0.0364` n `197` status `ready` deltaP `4.9706` edge `0.0164` maxDD `-1.7205`
- `market_context_high->fx_24h` score `0.0343` n `157` status `ready` deltaP `9.8803` edge `0.0419` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.0347` n `197` status `ready` deltaP `3.3238` edge `0.0308` maxDD `-2.8014`
- `market_context_high->metal_4h` score `-0.2552` n `185` status `ready` deltaP `9.7091` edge `0.0571` maxDD `-6.4478`
- `market_context_high->fx_1h` score `-0.3408` n `197` status `ready` deltaP `3.0844` edge `-0.0024` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.4285` n `197` status `ready` deltaP `2.3618` edge `0.0356` maxDD `-3.6309`
- `market_context_high->index_4h` score `-0.4678` n `185` status `ready` deltaP `0.8273` edge `0.0644` maxDD `-3.7119`
- `market_context_high->metal_1h` score `-0.5583` n `197` status `ready` deltaP `5.2904` edge `0.001` maxDD `-4.2945`
- `market_context_high->commodity_1h` score `-0.9019` n `197` status `ready` deltaP `-1.7508` edge `-0.002` maxDD `-2.252`
- `market_context_high->crypto_alt_4h` score `-1.1451` n `185` status `ready` deltaP `8.2548` edge `0.1815` maxDD `-19.5565`
- `market_context_high->crypto_major_1h` score `-1.189` n `197` status `ready` deltaP `0.0061` edge `0.0074` maxDD `-6.1883`
- `market_context_high->crypto_major_4h` score `-1.2156` n `185` status `ready` deltaP `4.8583` edge `0.1372` maxDD `-13.3376`
- `market_context_high->fx_4h` score `-1.7395` n `185` status `ready` deltaP `-5.5504` edge `-0.0109` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-4.6189` n `185` status `ready` deltaP `-13.3265` edge `-0.0414` maxDD `-8.04`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
