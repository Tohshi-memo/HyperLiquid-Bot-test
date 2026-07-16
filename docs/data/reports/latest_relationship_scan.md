# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T18:22:29.822932+00:00`
- Price records: `672`
- Market context records: `6945`
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
- `market_context_high->crypto_alt_1h` score `-0.384` n `237` status `ready` deltaP `2.43` edge `0.021` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.727` n `237` status `ready` deltaP `-0.2388` edge `-0.0005` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.7349` n `237` status `ready` deltaP `-2.3895` edge `-0.0015` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.8801` n `228` status `ready` deltaP `12.6953` edge `0.0089` maxDD `-2.1765`
- `market_context_high->crypto_major_1h` score `-1.2197` n `237` status `ready` deltaP `2.8791` edge `0.0144` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-1.2466` n `237` status `ready` deltaP `-2.5247` edge `-0.0149` maxDD `-2.4388`
- `market_context_high->unknown_24h` score `-1.4311` n `221` status `ready` deltaP `-8.5157` edge `0.3138` maxDD `-17.5734`
- `market_context_high->unknown_1h` score `-1.6165` n `237` status `ready` deltaP `-2.1306` edge `-0.0304` maxDD `-3.2083`
- `market_context_high->index_4h` score `-1.6463` n `228` status `ready` deltaP `8.7319` edge `-0.0113` maxDD `-11.3047`
- `market_context_high->commodity_4h` score `-1.6554` n `228` status `ready` deltaP `-4.4769` edge `-0.0334` maxDD `-5.5853`
- `market_context_high->metal_4h` score `-2.0101` n `228` status `ready` deltaP `4.4716` edge `0.0108` maxDD `-5.5324`
- `market_context_high->equity_1h` score `-2.0131` n `237` status `ready` deltaP `2.2385` edge `-0.0176` maxDD `-15.7664`
- `market_context_high->crypto_alt_4h` score `-2.7979` n `228` status `ready` deltaP `1.4308` edge `-0.0099` maxDD `-20.6678`
- `market_context_high->crypto_major_4h` score `-2.8352` n `228` status `ready` deltaP `-0.2647` edge `-0.029` maxDD `-16.9508`
- `market_context_high->unknown_4h` score `-3.0499` n `228` status `ready` deltaP `-7.6354` edge `0.0333` maxDD `-10.2579`
- `market_context_high->commodity_24h` score `-3.6248` n `221` status `ready` deltaP `-5.542` edge `-0.0783` maxDD `-5.2791`
- `market_context_high->fx_24h` score `-4.3363` n `221` status `ready` deltaP `-6.7246` edge `-0.0129` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-6.769` n `228` status `ready` deltaP `5.3166` edge `-0.082` maxDD `-58.7008`
- `market_context_high->metal_24h` score `-9.2071` n `221` status `ready` deltaP `-13.9158` edge `-0.1236` maxDD `-36.7889`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
