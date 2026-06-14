# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T23:07:30.670213+00:00`
- Price records: `672`
- Market context records: `3937`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11443`

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

- `risk_on_high->unknown_4h` score `83.7332` n `45` status `ready` deltaP `-0.7826` edge `10.9397` maxDD `-12.2899`
- `risk_on_and_context->unknown_4h` score `83.7332` n `45` status `ready` deltaP `-0.7826` edge `10.9397` maxDD `-12.2899`
- `market_context_high->unknown_4h` score `15.2748` n `181` status `ready` deltaP `-3.8397` edge `1.8394` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `9.9011` n `40` status `ready` deltaP `42.0139` edge `0.545` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.9011` n `40` status `ready` deltaP `42.0139` edge `0.545` maxDD `0.0`
- `risk_on_high->equity_4h` score `4.7192` n `45` status `ready` deltaP `38.0861` edge `0.1441` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `4.7192` n `45` status `ready` deltaP `38.0861` edge `0.1441` maxDD `-0.0458`
- `market_context_high->unknown_24h` score `4.205` n `165` status `ready` deltaP `-12.5284` edge `2.1072` maxDD `-118.1945`
- `market_context_high->equity_24h` score `3.7272` n `165` status `ready` deltaP `20.8018` edge `0.4749` maxDD `-14.5715`
- `market_context_high->index_24h` score `3.5364` n `165` status `ready` deltaP `25.7923` edge `0.2367` maxDD `-7.1159`
- `risk_on_high->index_24h` score `3.4516` n `40` status `ready` deltaP `30.0347` edge `0.0874` maxDD `0.0`
- `risk_on_and_context->index_24h` score `3.4516` n `40` status `ready` deltaP `30.0347` edge `0.0874` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `3.3052` n `45` status `ready` deltaP `25.708` edge `0.1706` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `3.3052` n `45` status `ready` deltaP `25.708` edge `0.1706` maxDD `-2.6576`
- `market_context_high->metal_24h` score `2.695` n `165` status `ready` deltaP `15.4325` edge `0.2732` maxDD `-9.1203`
- `market_context_high->crypto_major_4h` score `1.6979` n `181` status `ready` deltaP `17.5557` edge `0.2009` maxDD `-9.4488`
- `risk_on_high->commodity_24h` score `1.5667` n `40` status `ready` deltaP `4.1667` edge `0.3005` maxDD `-12.1509`
- `risk_on_and_context->commodity_24h` score `1.5667` n `40` status `ready` deltaP `4.1667` edge `0.3005` maxDD `-12.1509`
- `risk_on_high->equity_1h` score `1.4719` n `45` status `ready` deltaP `12.4518` edge `0.079` maxDD `-0.8151`
- `risk_on_and_context->equity_1h` score `1.4719` n `45` status `ready` deltaP `12.4518` edge `0.079` maxDD `-0.8151`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
