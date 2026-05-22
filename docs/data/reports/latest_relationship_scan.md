# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T07:37:16.599757+00:00`
- Price records: `672`
- Market context records: `1506`
- Flow alert records: `6245`
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

- `market_context_high->metal_24h` score `13.6947` n `163` status `ready` deltaP `23.4716` edge `1.0848` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.1343` n `163` status `ready` deltaP `28.8887` edge `0.9369` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.4823` n `163` status `ready` deltaP `27.3027` edge `0.8047` maxDD `-8.0553`
- `market_context_high->index_24h` score `3.7346` n `163` status `ready` deltaP `19.8832` edge `0.2873` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.6334` n `163` status `ready` deltaP `13.1007` edge `0.3648` maxDD `-14.2815`
- `market_context_high->fx_24h` score `0.9937` n `163` status `ready` deltaP `19.0376` edge `0.0608` maxDD `-1.3925`
- `market_context_high->equity_4h` score `0.9877` n `189` status `ready` deltaP `5.8355` edge `0.1264` maxDD `-3.6396`
- `market_context_high->index_1h` score `-0.2863` n `191` status `ready` deltaP `2.3474` edge `0.007` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.2874` n `191` status `ready` deltaP `1.0` edge `0.0294` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.5349` n `191` status `ready` deltaP `-0.3386` edge `-0.0031` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.6954` n `191` status `ready` deltaP `1.0072` edge `0.0377` maxDD `-4.1892`
- `market_context_high->crypto_alt_4h` score `-0.6989` n `189` status `ready` deltaP `9.1432` edge `0.1814` maxDD `-19.5565`
- `market_context_high->metal_1h` score `-0.7064` n `191` status `ready` deltaP `5.9434` edge `0.0034` maxDD `-6.3532`
- `market_context_high->crypto_major_4h` score `-0.7564` n `189` status `ready` deltaP `5.2959` edge `0.1386` maxDD `-13.3376`
- `market_context_high->commodity_1h` score `-0.8779` n `191` status `ready` deltaP `-1.9822` edge `-0.0072` maxDD `-4.7041`
- `market_context_high->crypto_major_1h` score `-1.061` n `191` status `ready` deltaP `-1.4602` edge `0.0094` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.2036` n `189` status `ready` deltaP `10.9184` edge `0.0961` maxDD `-12.5349`
- `market_context_high->index_4h` score `-1.2253` n `189` status `ready` deltaP `-3.6617` edge `0.0312` maxDD `-3.7119`
- `market_context_high->fx_4h` score `-1.5729` n `189` status `ready` deltaP `-4.228` edge `-0.01` maxDD `-1.4313`
- `market_context_high->unknown_24h` score `-3.0271` n `163` status `ready` deltaP `-1.5433` edge `0.031` maxDD `-10.1706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
