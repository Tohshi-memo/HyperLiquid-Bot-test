# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T19:07:32.704366+00:00`
- Price records: `672`
- Market context records: `6948`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11728`

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

- `market_context_high->fx_1h` score `-0.2359` n `237` status `ready` deltaP `2.4836` edge `0.0017` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.3692` n `237` status `ready` deltaP `2.5797` edge `0.0219` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.7263` n `237` status `ready` deltaP `-0.2388` edge `-0.0004` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.7395` n `237` status `ready` deltaP `-2.3895` edge `-0.0021` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.9219` n `231` status `ready` deltaP `11.9662` edge `0.0084` maxDD `-2.1765`
- `market_context_high->crypto_major_1h` score `-1.2185` n `237` status `ready` deltaP `2.8791` edge `0.0145` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-1.2598` n `237` status `ready` deltaP `-2.6744` edge `-0.015` maxDD `-2.4388`
- `market_context_high->unknown_1h` score `-1.5949` n `237` status `ready` deltaP `-1.9809` edge `-0.0296` maxDD `-3.2083`
- `market_context_high->unknown_24h` score `-1.5967` n `223` status `ready` deltaP `-8.9134` edge `0.3045` maxDD `-18.3163`
- `market_context_high->commodity_4h` score `-1.6548` n `231` status `ready` deltaP `-4.4055` edge `-0.0338` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.6951` n `231` status `ready` deltaP `8.0028` edge `-0.0127` maxDD `-11.3047`
- `market_context_high->equity_1h` score `-2.0248` n `237` status `ready` deltaP `2.0888` edge `-0.0181` maxDD `-15.7664`
- `market_context_high->metal_4h` score `-2.0656` n `231` status `ready` deltaP `3.9304` edge `0.0073` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-2.865` n `231` status `ready` deltaP `0.9054` edge `-0.015` maxDD `-20.6678`
- `market_context_high->crypto_major_4h` score `-3.1314` n `231` status `ready` deltaP `-0.6434` edge `-0.0395` maxDD `-18.9471`
- `market_context_high->unknown_4h` score `-3.1412` n `231` status `ready` deltaP `-8.0569` edge `0.0285` maxDD `-10.2579`
- `market_context_high->commodity_24h` score `-3.7142` n `223` status `ready` deltaP `-6.0736` edge `-0.0822` maxDD `-5.2791`
- `market_context_high->fx_24h` score `-4.383` n `223` status `ready` deltaP `-7.098` edge `-0.0143` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.1865` n `231` status `ready` deltaP `4.6615` edge `-0.09` maxDD `-61.9938`
- `market_context_high->metal_24h` score `-9.4171` n `223` status `ready` deltaP `-14.1796` edge `-0.1268` maxDD `-38.546`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
