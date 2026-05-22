# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T10:07:19.119575+00:00`
- Price records: `672`
- Market context records: `1516`
- Flow alert records: `6276`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8791`

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

- `market_context_high->metal_24h` score `14.4838` n `157` status `ready` deltaP `24.6505` edge `1.1427` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.2403` n `157` status `ready` deltaP `28.8184` edge `0.9462` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.9322` n `157` status `ready` deltaP `28.0067` edge `0.8375` maxDD `-8.0553`
- `market_context_high->index_24h` score `3.6952` n `157` status `ready` deltaP `19.555` edge `0.2862` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.3538` n `157` status `ready` deltaP `12.7256` edge `0.344` maxDD `-14.2815`
- `market_context_high->fx_24h` score `1.069` n `157` status `ready` deltaP `19.3781` edge `0.0648` maxDD `-1.3925`
- `market_context_high->equity_4h` score `0.8197` n `183` status `ready` deltaP `5.7452` edge `0.113` maxDD `-3.6396`
- `market_context_high->index_1h` score `-0.3934` n `194` status `ready` deltaP `1.443` edge `0.0041` maxDD `-1.7205`
- `market_context_high->crypto_alt_1h` score `-0.562` n `194` status `ready` deltaP `-0.1173` edge `0.0311` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.5699` n `194` status `ready` deltaP `-1.0016` edge `0.0192` maxDD `-2.8014`
- `market_context_high->metal_1h` score `-0.7341` n `194` status `ready` deltaP `5.4695` edge `0.003` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.8518` n `194` status `ready` deltaP `-0.6991` edge `-0.0031` maxDD `-0.3914`
- `market_context_high->crypto_alt_4h` score `-0.8689` n `183` status `ready` deltaP `8.4841` edge `0.164` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-0.9021` n `183` status `ready` deltaP `4.1758` edge `0.1274` maxDD `-13.3376`
- `market_context_high->unknown_24h` score `-0.9757` n `157` status `ready` deltaP `-2.8563` edge `0.2107` maxDD `-10.1706`
- `market_context_high->crypto_major_1h` score `-1.024` n `194` status `ready` deltaP `-1.0649` edge `0.0115` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.0735` n `183` status `ready` deltaP `11.6595` edge `0.102` maxDD `-12.5349`
- `market_context_high->commodity_1h` score `-1.2051` n `194` status `ready` deltaP `-0.8982` edge `-0.0023` maxDD `-4.7041`
- `market_context_high->index_4h` score `-1.3105` n `183` status `ready` deltaP `-4.2317` edge `0.0279` maxDD `-3.7119`
- `market_context_high->fx_4h` score `-1.6947` n `183` status `ready` deltaP `-5.6602` edge `-0.0106` maxDD `-1.4313`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
