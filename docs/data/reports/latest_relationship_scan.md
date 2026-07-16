# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T19:37:28.677866+00:00`
- Price records: `672`
- Market context records: `6951`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11729`

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

- `market_context_high->fx_1h` score `-0.2523` n `237` status `ready` deltaP `2.1842` edge `0.0016` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.3692` n `237` status `ready` deltaP `2.5797` edge `0.0219` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.7247` n `237` status `ready` deltaP `-0.2388` edge `-0.0002` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.7427` n `237` status `ready` deltaP `-2.3895` edge `-0.0025` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.9482` n `233` status `ready` deltaP `11.4905` edge `0.0082` maxDD `-2.1765`
- `market_context_high->crypto_major_1h` score `-1.2389` n `237` status `ready` deltaP `2.7294` edge `0.0138` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-1.2897` n `237` status `ready` deltaP `-2.9738` edge `-0.0155` maxDD `-2.4388`
- `market_context_high->unknown_24h` score `-1.5905` n `223` status `ready` deltaP `-8.9134` edge `0.3053` maxDD `-18.3163`
- `market_context_high->unknown_1h` score `-1.5913` n `237` status `ready` deltaP `-1.9809` edge `-0.0293` maxDD `-3.2083`
- `market_context_high->commodity_4h` score `-1.6632` n `233` status `ready` deltaP `-4.5672` edge `-0.0338` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.7603` n `233` status `ready` deltaP `7.5271` edge `-0.0139` maxDD `-11.623`
- `market_context_high->equity_1h` score `-2.0201` n `237` status `ready` deltaP `2.0888` edge `-0.0175` maxDD `-15.7664`
- `market_context_high->metal_4h` score `-2.1027` n `233` status `ready` deltaP `3.5774` edge `0.0049` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-2.9208` n `233` status `ready` deltaP `0.4632` edge `-0.0192` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.2112` n `233` status `ready` deltaP `-8.3318` edge `0.0245` maxDD `-10.2579`
- `market_context_high->crypto_major_4h` score `-3.434` n `233` status `ready` deltaP `-1.0894` edge `-0.0461` maxDD `-21.2846`
- `market_context_high->commodity_24h` score `-3.713` n `223` status `ready` deltaP `-6.0736` edge `-0.0821` maxDD `-5.2791`
- `market_context_high->fx_24h` score `-4.383` n `223` status `ready` deltaP `-7.098` edge `-0.0143` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.4555` n `233` status `ready` deltaP `4.2342` edge `-0.0946` maxDD `-64.1569`
- `market_context_high->metal_24h` score `-9.3976` n `223` status `ready` deltaP `-14.1796` edge `-0.1243` maxDD `-38.546`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
