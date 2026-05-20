# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T14:22:29.132544+00:00`
- Price records: `672`
- Market context records: `1328`
- Flow alert records: `5736`
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

- `market_context_high->crypto_major_24h` score `15.5218` n `128` status `ready` deltaP `37.5868` edge `1.1561` maxDD `-8.0553`
- `market_context_high->metal_24h` score `13.4347` n `128` status `ready` deltaP `13.5417` edge `1.196` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.7128` n `128` status `ready` deltaP `28.3854` edge `0.8218` maxDD `-15.1306`
- `market_context_high->index_24h` score `5.2453` n `128` status `ready` deltaP `27.9514` edge `0.3594` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.9601` n `128` status `ready` deltaP `20.8333` edge `0.4733` maxDD `-14.2815`
- `market_context_high->equity_4h` score `2.3653` n `157` status `ready` deltaP `12.1961` edge `0.1863` maxDD `-3.6396`
- `market_context_high->commodity_24h` score `1.6347` n `128` status `ready` deltaP `-11.8056` edge `0.3631` maxDD `-6.8535`
- `market_context_high->unknown_24h` score `1.5112` n `128` status `ready` deltaP `-2.4306` edge `0.4151` maxDD `-10.1706`
- `market_context_high->fx_24h` score `1.1397` n `128` status `ready` deltaP `12.9341` edge `0.0552` maxDD `-0.3831`
- `market_context_high->metal_4h` score `0.2039` n `157` status `ready` deltaP `13.6778` edge `0.0689` maxDD `-6.4478`
- `market_context_high->equity_1h` score `0.1924` n `157` status `ready` deltaP `3.3677` edge `0.0363` maxDD `-1.7505`
- `market_context_high->index_4h` score `0.0873` n `157` status `ready` deltaP `4.8742` edge `0.0876` maxDD `-3.7119`
- `market_context_high->index_1h` score `0.0454` n `157` status `ready` deltaP `5.1642` edge `0.0168` maxDD `-1.6329`
- `market_context_high->metal_1h` score `-0.0103` n `157` status `ready` deltaP `9.3911` edge `0.0055` maxDD `-2.8509`
- `market_context_high->fx_1h` score `-0.5254` n `157` status `ready` deltaP `0.8086` edge `-0.0036` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.6408` n `157` status `ready` deltaP `0.3976` edge `0.031` maxDD `-3.6309`
- `market_context_high->commodity_1h` score `-0.9233` n `157` status `ready` deltaP `-1.8536` edge `-0.0031` maxDD `-2.252`
- `market_context_high->crypto_major_1h` score `-0.9545` n `157` status `ready` deltaP `-1.8155` edge `-0.0082` maxDD `-5.8323`
- `market_context_high->crypto_alt_4h` score `-1.0327` n `157` status `ready` deltaP `9.8396` edge `0.1803` maxDD `-19.5565`
- `market_context_high->unknown_4h` score `-1.0591` n `157` status `ready` deltaP `3.4109` edge `0.0686` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
