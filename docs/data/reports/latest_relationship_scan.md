# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T05:07:15.893887+00:00`
- Price records: `672`
- Market context records: `1289`
- Flow alert records: `5622`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8820`

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

- `market_context_high->crypto_major_24h` score `17.5261` n `128` status `ready` deltaP `41.5798` edge `1.2965` maxDD `-8.0553`
- `market_context_high->metal_24h` score `11.8813` n `128` status `ready` deltaP `8.8542` edge `1.0978` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.2446` n `128` status `ready` deltaP `26.8229` edge `0.7932` maxDD `-15.1306`
- `market_context_high->index_24h` score `5.683` n `128` status `ready` deltaP `29.6875` edge `0.3843` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.9382` n `128` status `ready` deltaP `25.3472` edge `0.5686` maxDD `-14.2815`
- `market_context_high->equity_4h` score `2.3993` n `147` status `ready` deltaP `12.4254` edge `0.1876` maxDD `-3.6396`
- `market_context_high->unknown_24h` score `2.397` n `128` status `ready` deltaP `1.5625` edge `0.4623` maxDD `-10.1706`
- `market_context_high->commodity_24h` score `1.2236` n `128` status `ready` deltaP `-14.4097` edge `0.3462` maxDD `-6.8535`
- `market_context_high->unknown_4h` score `1.1722` n `147` status `ready` deltaP `2.52` edge `0.308` maxDD `-11.1695`
- `market_context_high->fx_24h` score `0.4086` n `128` status `ready` deltaP `6.5105` edge `0.0371` maxDD `-0.3831`
- `market_context_high->equity_1h` score `0.2228` n `156` status `ready` deltaP `3.9421` edge `0.035` maxDD `-1.7505`
- `market_context_high->index_4h` score `0.1593` n `147` status `ready` deltaP `6.1027` edge `0.0869` maxDD `-3.573`
- `market_context_high->index_1h` score `0.129` n `156` status `ready` deltaP `6.6368` edge `0.0177` maxDD `-1.6329`
- `market_context_high->metal_1h` score `0.0456` n `156` status `ready` deltaP `9.911` edge `0.0067` maxDD `-2.8509`
- `market_context_high->metal_4h` score `0.0238` n `147` status `ready` deltaP `12.8671` edge `0.0593` maxDD `-6.4478`
- `market_context_high->fx_1h` score `-0.5087` n `156` status `ready` deltaP `1.0019` edge `-0.0035` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.5901` n `156` status `ready` deltaP `0.8522` edge `0.0322` maxDD `-3.6309`
- `market_context_high->crypto_major_1h` score `-0.8085` n `156` status `ready` deltaP `-0.1919` edge `-0.0003` maxDD `-5.8323`
- `market_context_high->crypto_alt_4h` score `-0.8642` n `147` status `ready` deltaP `9.22` edge `0.1597` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-0.9487` n `147` status `ready` deltaP `4.8542` edge `0.1169` maxDD `-13.3376`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
