# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T15:37:22.528754+00:00`
- Price records: `672`
- Market context records: `1333`
- Flow alert records: `5751`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8783`

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

- `market_context_high->crypto_major_24h` score `15.0672` n `128` status `ready` deltaP `36.7187` edge `1.124` maxDD `-8.0553`
- `market_context_high->metal_24h` score `13.2033` n `128` status `ready` deltaP `12.6736` edge `1.1825` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.5988` n `128` status `ready` deltaP `28.3854` edge `0.8123` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.9287` n `128` status `ready` deltaP `27.0833` edge `0.3388` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.6381` n `128` status `ready` deltaP `19.9653` edge `0.4378` maxDD `-14.2815`
- `market_context_high->equity_4h` score `2.2966` n `157` status `ready` deltaP `11.8912` edge `0.1826` maxDD `-3.6396`
- `market_context_high->commodity_24h` score `1.9502` n `128` status `ready` deltaP `-10.9375` edge `0.3836` maxDD `-6.8535`
- `market_context_high->unknown_24h` score `1.2581` n `128` status `ready` deltaP `-3.2986` edge `0.3998` maxDD `-10.1706`
- `market_context_high->fx_24h` score `1.2343` n `128` status `ready` deltaP `13.8021` edge `0.0573` maxDD `-0.3831`
- `market_context_high->metal_4h` score `0.1823` n `157` status `ready` deltaP `13.6778` edge `0.0671` maxDD `-6.4478`
- `market_context_high->equity_1h` score `0.1145` n `157` status `ready` deltaP `3.0683` edge `0.0318` maxDD `-1.7505`
- `market_context_high->index_4h` score `0.0561` n `157` status `ready` deltaP `4.8742` edge `0.0836` maxDD `-3.7119`
- `market_context_high->index_1h` score `0.0126` n `157` status `ready` deltaP `4.8648` edge `0.0146` maxDD `-1.6329`
- `market_context_high->metal_1h` score `-0.0955` n `157` status `ready` deltaP `9.0917` edge `0.0004` maxDD `-2.8509`
- `market_context_high->fx_1h` score `-0.4619` n `157` status `ready` deltaP `1.5571` edge `-0.0033` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.7212` n `157` status `ready` deltaP `0.2479` edge `0.0253` maxDD `-3.6309`
- `market_context_high->commodity_1h` score `-0.801` n `157` status `ready` deltaP `-1.2548` edge `0.0031` maxDD `-2.252`
- `market_context_high->crypto_major_1h` score `-1.0091` n `157` status `ready` deltaP `-2.2646` edge `-0.0122` maxDD `-5.8323`
- `market_context_high->unknown_4h` score `-1.2048` n `157` status `ready` deltaP `2.6487` edge `0.055` maxDD `-11.1695`
- `market_context_high->crypto_alt_4h` score `-1.2605` n `157` status `ready` deltaP `9.0774` edge `0.1664` maxDD `-19.5565`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
