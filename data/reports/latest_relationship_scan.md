# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T16:52:20.910237+00:00`
- Price records: `672`
- Market context records: `1441`
- Flow alert records: `6063`
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

- `market_context_high->crypto_alt_24h` score `12.4469` n `154` status `ready` deltaP `28.7811` edge `1.047` maxDD `-15.1306`
- `market_context_high->metal_24h` score `12.1689` n `154` status `ready` deltaP `13.7243` edge `1.0893` maxDD `-6.3373`
- `market_context_high->crypto_major_24h` score `11.6144` n `154` status `ready` deltaP `27.3539` edge `0.8987` maxDD `-8.0553`
- `market_context_high->index_24h` score `4.1961` n `154` status `ready` deltaP `19.3813` edge `0.3291` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.6267` n `154` status `ready` deltaP `12.5271` edge `0.4514` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.2869` n `214` status `ready` deltaP `6.7259` edge `0.1454` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.208` n `154` status `ready` deltaP `10.4009` edge `0.0529` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.127` n `225` status `ready` deltaP `2.3` edge `0.0341` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.1451` n `225` status `ready` deltaP `3.5117` edge `0.011` maxDD `-1.7205`
- `market_context_high->index_4h` score `-0.6715` n `214` status `ready` deltaP `-0.0684` edge `0.0534` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `-0.7077` n `225` status `ready` deltaP `1.364` edge `0.0343` maxDD `-4.1892`
- `market_context_high->commodity_1h` score `-0.7159` n `225` status `ready` deltaP `-0.821` edge `0.0073` maxDD `-2.252`
- `market_context_high->fx_1h` score `-0.7357` n `225` status `ready` deltaP `0.648` edge `-0.0024` maxDD `-0.3914`
- `market_context_high->crypto_alt_4h` score `-0.9022` n `214` status `ready` deltaP `9.4755` edge `0.1936` maxDD `-19.5565`
- `market_context_high->fx_4h` score `-1.0744` n `214` status `ready` deltaP `-4.633` edge `-0.0098` maxDD `-1.4313`
- `market_context_high->metal_1h` score `-1.213` n `225` status `ready` deltaP `4.7698` edge `0.0007` maxDD `-6.3532`
- `market_context_high->crypto_major_4h` score `-1.2256` n `214` status `ready` deltaP `5.1075` edge `0.1347` maxDD `-13.3376`
- `market_context_high->crypto_major_1h` score `-1.7153` n `225` status `ready` deltaP `-1.2981` edge `0.0014` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-2.3997` n `214` status `ready` deltaP `6.2571` edge `0.0275` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-4.1396` n `214` status `ready` deltaP `-10.2904` edge `-0.0217` maxDD `-8.04`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
