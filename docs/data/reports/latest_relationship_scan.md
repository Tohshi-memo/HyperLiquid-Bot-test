# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T12:07:24.707202+00:00`
- Price records: `672`
- Market context records: `1524`
- Flow alert records: `6301`
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

- `market_context_high->metal_24h` score `13.772` n `165` status `ready` deltaP `23.4469` edge `1.0914` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.5033` n `165` status `ready` deltaP `28.911` edge `0.9675` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.5151` n `165` status `ready` deltaP `28.2229` edge `0.8013` maxDD `-8.0553`
- `market_context_high->index_24h` score `3.7802` n `165` status `ready` deltaP `19.9874` edge `0.2904` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.511` n `165` status `ready` deltaP `13.2197` edge `0.3538` maxDD `-14.2815`
- `market_context_high->fx_24h` score `0.9523` n `165` status `ready` deltaP `18.6995` edge `0.0596` maxDD `-1.3925`
- `market_context_high->equity_4h` score `0.4427` n `190` status `ready` deltaP `4.1865` edge `0.0997` maxDD `-4.2577`
- `market_context_high->fx_1h` score `-0.5743` n `199` status `ready` deltaP `-1.096` edge `-0.0031` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.6169` n `199` status `ready` deltaP `-0.5296` edge `0.0268` maxDD `-4.1892`
- `market_context_high->index_1h` score `-0.7249` n `199` status `ready` deltaP `0.1753` edge `0.0016` maxDD `-1.7205`
- `market_context_high->commodity_1h` score `-0.7733` n `199` status `ready` deltaP `-0.6469` edge `-0.0027` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-0.7758` n `199` status `ready` deltaP `4.8484` edge `0.0018` maxDD `-6.3532`
- `market_context_high->crypto_alt_4h` score `-0.784` n `190` status `ready` deltaP `9.6518` edge `0.1671` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-0.8225` n `190` status `ready` deltaP `5.1364` edge `0.1312` maxDD `-13.3376`
- `market_context_high->equity_1h` score `-0.8967` n `199` status `ready` deltaP `-1.7813` edge `0.018` maxDD `-2.8014`
- `market_context_high->crypto_major_1h` score `-1.1031` n `199` status `ready` deltaP `-1.9408` edge `0.0072` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.2292` n `190` status `ready` deltaP `10.7477` edge `0.0951` maxDD `-12.5349`
- `market_context_high->index_4h` score `-1.4654` n `190` status `ready` deltaP `-5.3274` edge `0.0223` maxDD `-3.7119`
- `market_context_high->fx_4h` score `-1.8164` n `190` status `ready` deltaP `-7.1068` edge `-0.0111` maxDD `-1.4313`
- `market_context_high->unknown_24h` score `-3.4931` n `165` status `ready` deltaP `-1.4741` edge `-0.0083` maxDD `-10.1706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
