# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T18:07:32.034848+00:00`
- Price records: `672`
- Market context records: `6944`
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

- `market_context_high->fx_1h` score `-0.2273` n `237` status `ready` deltaP `2.6333` edge `0.0018` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.3879` n `237` status `ready` deltaP `2.43` edge `0.0205` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.727` n `237` status `ready` deltaP `-0.2388` edge `-0.0005` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.7349` n `237` status `ready` deltaP `-2.3895` edge `-0.0015` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.8657` n `227` status `ready` deltaP `12.9426` edge `0.0091` maxDD `-2.1765`
- `market_context_high->crypto_major_1h` score `-1.2257` n `237` status `ready` deltaP `2.8791` edge `0.0139` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-1.261` n `237` status `ready` deltaP `-2.6744` edge `-0.0151` maxDD `-2.4388`
- `market_context_high->unknown_24h` score `-1.3541` n `220` status `ready` deltaP `-8.3141` edge `0.3185` maxDD `-17.2678`
- `market_context_high->unknown_1h` score `-1.6129` n `237` status `ready` deltaP `-2.1306` edge `-0.0301` maxDD `-3.2083`
- `market_context_high->index_4h` score `-1.6311` n `227` status `ready` deltaP `8.9792` edge `-0.011` maxDD `-11.3047`
- `market_context_high->commodity_4h` score `-1.6406` n `227` status `ready` deltaP `-4.4032` edge `-0.032` maxDD `-5.5853`
- `market_context_high->metal_4h` score `-1.9951` n `227` status `ready` deltaP `4.6551` edge `0.0115` maxDD `-5.5324`
- `market_context_high->equity_1h` score `-2.003` n `237` status `ready` deltaP `2.3882` edge `-0.0173` maxDD `-15.7664`
- `market_context_high->crypto_alt_4h` score `-2.7877` n `227` status `ready` deltaP `1.5083` edge `-0.0091` maxDD `-20.6678`
- `market_context_high->crypto_major_4h` score `-2.81` n `227` status `ready` deltaP `-0.1854` edge `-0.0263` maxDD `-16.9508`
- `market_context_high->unknown_4h` score `-3.0339` n `227` status `ready` deltaP `-7.6448` edge `0.0347` maxDD `-10.2579`
- `market_context_high->commodity_24h` score `-3.5793` n `220` status `ready` deltaP `-5.2725` edge `-0.0763` maxDD `-5.2791`
- `market_context_high->fx_24h` score `-4.314` n `220` status `ready` deltaP `-6.5354` edge `-0.0123` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-6.649` n `227` status `ready` deltaP `5.5388` edge `-0.0798` maxDD `-57.7652`
- `market_context_high->metal_24h` score `-9.1156` n `220` status `ready` deltaP `-13.7821` edge `-0.122` maxDD `-36.0498`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
