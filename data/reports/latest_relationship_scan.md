# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T19:22:30.659668+00:00`
- Price records: `672`
- Market context records: `6949`
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

- `market_context_high->fx_1h` score `-0.2437` n `237` status `ready` deltaP `2.3339` edge `0.0017` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.3677` n `237` status `ready` deltaP `2.5797` edge `0.0221` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.7255` n `237` status `ready` deltaP `-0.2388` edge `-0.0003` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.7403` n `237` status `ready` deltaP `-2.3895` edge `-0.0022` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.9359` n `232` status `ready` deltaP `11.7273` edge `0.0082` maxDD `-2.1765`
- `market_context_high->crypto_major_1h` score `-1.2197` n `237` status `ready` deltaP `2.8791` edge `0.0144` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-1.2765` n `237` status `ready` deltaP `-2.8241` edge `-0.0154` maxDD `-2.4388`
- `market_context_high->unknown_1h` score `-1.5913` n `237` status `ready` deltaP `-1.9809` edge `-0.0293` maxDD `-3.2083`
- `market_context_high->unknown_24h` score `-1.5936` n `223` status `ready` deltaP `-8.9134` edge `0.3049` maxDD `-18.3163`
- `market_context_high->commodity_4h` score `-1.667` n `232` status `ready` deltaP `-4.6257` edge `-0.0339` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.713` n `232` status `ready` deltaP `7.7639` edge `-0.0131` maxDD `-11.3284`
- `market_context_high->equity_1h` score `-2.0209` n `237` status `ready` deltaP `2.0888` edge `-0.0176` maxDD `-15.7664`
- `market_context_high->metal_4h` score `-2.0834` n `232` status `ready` deltaP `3.7532` edge `0.0062` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-2.8883` n `232` status `ready` deltaP `0.6833` edge `-0.0165` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.1787` n `232` status `ready` deltaP `-8.1949` edge `0.0263` maxDD `-10.2579`
- `market_context_high->crypto_major_4h` score `-3.2673` n `232` status `ready` deltaP `-0.8674` edge `-0.0424` maxDD `-19.9899`
- `market_context_high->commodity_24h` score `-3.7166` n `223` status `ready` deltaP `-6.0736` edge `-0.0824` maxDD `-5.2791`
- `market_context_high->fx_24h` score `-4.383` n `223` status `ready` deltaP `-7.098` edge `-0.0143` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.3124` n `232` status `ready` deltaP `4.447` edge `-0.0922` maxDD `-62.9948`
- `market_context_high->metal_24h` score `-9.4078` n `223` status `ready` deltaP `-14.1796` edge `-0.1256` maxDD `-38.546`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
