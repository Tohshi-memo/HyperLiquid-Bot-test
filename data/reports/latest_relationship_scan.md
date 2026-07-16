# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T16:52:25.949008+00:00`
- Price records: `672`
- Market context records: `6938`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11706`

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

- `market_context_high->fx_1h` score `-0.2542` n `234` status `ready` deltaP `2.1175` edge `0.0018` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.4799` n `234` status `ready` deltaP `2.5398` edge `0.0195` maxDD `-3.7803`
- `market_context_high->metal_1h` score `-0.7187` n `234` status `ready` deltaP `-2.1534` edge `-0.001` maxDD `-2.1427`
- `market_context_high->index_1h` score `-0.7364` n `234` status `ready` deltaP `-0.4031` edge `-0.0006` maxDD `-2.2895`
- `market_context_high->fx_4h` score `-0.821` n `224` status `ready` deltaP `13.6978` edge `0.0098` maxDD `-2.1765`
- `market_context_high->crypto_major_1h` score `-0.8752` n `234` status `ready` deltaP `2.9889` edge `0.0139` maxDD `-5.5406`
- `market_context_high->unknown_24h` score `-1.0373` n `216` status `ready` deltaP `-7.4892` edge `0.3381` maxDD `-16.026`
- `market_context_high->commodity_1h` score `-1.1793` n `234` status `ready` deltaP `-2.33` edge `-0.0139` maxDD `-2.1742`
- `market_context_high->commodity_4h` score `-1.5893` n `224` status `ready` deltaP `-3.8655` edge `-0.029` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.6102` n `234` status `ready` deltaP `-2.2622` edge `-0.029` maxDD `-3.2083`
- `market_context_high->index_4h` score `-1.6283` n `224` status `ready` deltaP `8.9722` edge `-0.0106` maxDD `-11.3047`
- `market_context_high->equity_1h` score `-1.9191` n `234` status `ready` deltaP `2.4169` edge `-0.0187` maxDD `-15.143`
- `market_context_high->metal_4h` score `-1.9371` n `224` status `ready` deltaP `5.2156` edge `0.0152` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-2.7785` n `224` status `ready` deltaP `-0.2396` edge `-0.0219` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-2.7797` n `224` status `ready` deltaP `1.6006` edge `-0.0087` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-2.9827` n `224` status `ready` deltaP `-7.6655` edge `0.0391` maxDD `-10.2579`
- `market_context_high->commodity_24h` score `-3.3831` n `216` status `ready` deltaP `-4.1699` edge `-0.0673` maxDD `-5.2791`
- `market_context_high->fx_24h` score `-4.222` n `216` status `ready` deltaP `-5.761` edge `-0.0098` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-6.4416` n `224` status `ready` deltaP `6.2173` edge `-0.0728` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.8682` n `216` status `ready` deltaP `-13.235` edge `-0.1184` maxDD `-34.0917`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
