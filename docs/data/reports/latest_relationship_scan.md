# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T11:37:17.247548+00:00`
- Price records: `672`
- Market context records: `1216`
- Flow alert records: `5406`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8777`

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

- `market_context_high->crypto_major_24h` score `18.8281` n `128` status `ready` deltaP `44.0104` edge `1.3888` maxDD `-8.0553`
- `market_context_high->unknown_4h` score `7.6681` n `128` status `ready` deltaP `2.9345` edge `0.7411` maxDD `-6.7322`
- `market_context_high->crypto_alt_24h` score `7.0738` n `128` status `ready` deltaP `21.9618` edge `0.6447` maxDD `-15.1306`
- `market_context_high->commodity_24h` score `5.9191` n `128` status `ready` deltaP `-2.9514` edge `0.6611` maxDD `-6.8535`
- `market_context_high->metal_24h` score `4.5227` n `128` status `ready` deltaP `-3.2986` edge `0.5656` maxDD `-6.3373`
- `market_context_high->equity_4h` score `2.9909` n `128` status `ready` deltaP `15.4153` edge `0.2128` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.2827` n `128` status `ready` deltaP `18.9236` edge `0.1727` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.0056` n `128` status `ready` deltaP `19.0972` edge `0.3625` maxDD `-14.2815`
- `market_context_high->index_4h` score `1.0681` n `128` status `ready` deltaP `11.1471` edge `0.083` maxDD `-2.1308`
- `market_context_high->fx_24h` score `1.0056` n `128` status `ready` deltaP `9.9827` edge `0.0637` maxDD `-0.3831`
- `market_context_high->index_1h` score `0.5941` n `128` status `ready` deltaP `9.3001` edge `0.0192` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.5056` n `128` status `ready` deltaP `4.5611` edge `0.0486` maxDD `-1.2834`
- `market_context_high->metal_1h` score `-0.0525` n `128` status `ready` deltaP `9.6697` edge `-0.0078` maxDD `-2.2164`
- `market_context_high->fx_1h` score `-0.1037` n `128` status `ready` deltaP `5.4501` edge `0.0006` maxDD `-0.3124`
- `market_context_high->unknown_24h` score `-0.1589` n `128` status `ready` deltaP `-0.5208` edge `0.2632` maxDD `-10.1706`
- `market_context_high->crypto_major_4h` score `-0.1798` n `128` status `ready` deltaP `5.545` edge `0.1321` maxDD `-8.3693`
- `market_context_high->crypto_alt_1h` score `-0.364` n `128` status `ready` deltaP `0.4959` edge `0.0343` maxDD `-3.4088`
- `market_context_high->crypto_major_1h` score `-0.4183` n `128` status `ready` deltaP `2.5262` edge `0.0061` maxDD `-4.1256`
- `market_context_high->commodity_1h` score `-0.8038` n `128` status `ready` deltaP `-2.6104` edge `0.0119` maxDD `-2.252`
- `market_context_high->metal_4h` score `-0.9726` n `128` status `ready` deltaP `11.9475` edge `-0.0176` maxDD `-6.4478`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
