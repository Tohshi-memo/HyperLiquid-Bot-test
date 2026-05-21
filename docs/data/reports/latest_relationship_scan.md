# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T05:22:17.608615+00:00`
- Price records: `672`
- Market context records: `1393`
- Flow alert records: `5922`
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

- `market_context_high->crypto_major_24h` score `12.9573` n `157` status `ready` deltaP `28.1803` edge `1.0051` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `11.5571` n `157` status `ready` deltaP `28.8184` edge `0.9726` maxDD `-15.1306`
- `market_context_high->metal_24h` score `11.3578` n `157` status `ready` deltaP `11.9095` edge `1.0338` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.0456` n `157` status `ready` deltaP `19.555` edge `0.3154` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.4126` n `157` status `ready` deltaP `12.7256` edge `0.3489` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.5416` n `189` status `ready` deltaP `8.3196` edge `0.156` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.0511` n `157` status `ready` deltaP `9.8803` edge `0.0433` maxDD `-1.3925`
- `market_context_high->index_1h` score `0.025` n `201` status `ready` deltaP `5.0385` edge `0.015` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.0317` n `201` status `ready` deltaP `3.3917` edge `0.0306` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.3202` n `201` status `ready` deltaP `3.3262` edge `-0.0023` maxDD `-0.3914`
- `market_context_high->index_4h` score `-0.4917` n `189` status `ready` deltaP `0.8582` edge `0.0622` maxDD `-3.7119`
- `market_context_high->metal_4h` score `-0.5459` n `189` status `ready` deltaP `8.4164` edge `0.0415` maxDD `-6.4478`
- `market_context_high->metal_1h` score `-0.565` n `201` status `ready` deltaP `5.3118` edge `0.0` maxDD `-4.2945`
- `market_context_high->crypto_alt_1h` score `-0.6078` n `201` status `ready` deltaP `1.2304` edge `0.0282` maxDD `-3.6309`
- `market_context_high->commodity_1h` score `-0.9727` n `201` status `ready` deltaP `-2.4414` edge `-0.0033` maxDD `-2.252`
- `market_context_high->crypto_alt_4h` score `-1.2669` n `189` status `ready` deltaP `7.9777` edge `0.1732` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-1.3434` n `189` status `ready` deltaP `4.7757` edge `0.1271` maxDD `-13.3376`
- `market_context_high->crypto_major_1h` score `-1.3578` n `201` status `ready` deltaP `-1.0546` edge `0.0004` maxDD `-6.1883`
- `market_context_high->fx_4h` score `-1.6373` n `189` status `ready` deltaP `-4.4522` edge `-0.0097` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-4.4801` n `189` status `ready` deltaP `-13.1066` edge `-0.0313` maxDD `-8.04`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
