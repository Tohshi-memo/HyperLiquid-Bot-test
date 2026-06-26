# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T16:22:32.183893+00:00`
- Price records: `672`
- Market context records: `4844`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7616`

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

- `market_context_high->unknown_1h` score `13.497` n `110` status `ready` deltaP `10.4709` edge `1.0967` maxDD `-1.674`
- `market_context_high->unknown_4h` score `11.0304` n `98` status `ready` deltaP `25.8742` edge `0.8203` maxDD `-2.5545`
- `market_context_high->unknown_24h` score `4.9214` n `91` status `ready` deltaP `23.5615` edge `0.2873` maxDD `-1.4072`
- `market_context_high->crypto_alt_4h` score `3.967` n `98` status `ready` deltaP `17.042` edge `0.3522` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `2.5587` n `98` status `ready` deltaP `13.312` edge `0.3617` maxDD `-7.1265`
- `market_context_high->metal_4h` score `1.4251` n `98` status `ready` deltaP `11.4578` edge `0.1086` maxDD `-1.9651`
- `market_context_high->crypto_major_1h` score `0.3614` n `110` status `ready` deltaP `5.411` edge `0.1141` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.3219` n `110` status `ready` deltaP `7.4115` edge `0.0941` maxDD `-5.5126`
- `market_context_high->index_4h` score `0.2616` n `98` status `ready` deltaP `7.6935` edge `0.0285` maxDD `-0.7006`
- `market_context_high->equity_1h` score `0.1705` n `110` status `ready` deltaP `4.2352` edge `0.0534` maxDD `-2.7818`
- `market_context_high->equity_4h` score `0.033` n `98` status `ready` deltaP `9.6877` edge `0.0778` maxDD `-6.3852`
- `market_context_high->metal_1h` score `-0.1484` n `110` status `ready` deltaP `1.1649` edge `0.0312` maxDD `-1.3057`
- `market_context_high->fx_4h` score `-0.1512` n `98` status `ready` deltaP `6.7322` edge `0.0107` maxDD `-0.788`
- `market_context_high->commodity_1h` score `-0.2633` n `110` status `ready` deltaP `2.6728` edge `0.0144` maxDD `-1.278`
- `market_context_high->commodity_4h` score `-0.288` n `98` status `ready` deltaP `10.3192` edge `0.0115` maxDD `-4.377`
- `market_context_high->index_1h` score `-0.5645` n `110` status `ready` deltaP `-0.8982` edge `0.0091` maxDD `-0.7054`
- `market_context_high->fx_1h` score `-1.281` n `110` status `ready` deltaP `-6.2575` edge `-0.0037` maxDD `-0.5734`
- `market_context_high->fx_24h` score `-1.8315` n `91` status `ready` deltaP `-6.1641` edge `-0.0105` maxDD `-2.749`
- `market_context_high->commodity_24h` score `-3.44` n `91` status `ready` deltaP `11.1988` edge `-0.0048` maxDD `-27.5371`
- `market_context_high->index_24h` score `-4.7764` n `91` status `ready` deltaP `-8.9401` edge `-0.1517` maxDD `-24.085`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
