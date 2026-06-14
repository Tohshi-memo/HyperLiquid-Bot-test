# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T23:22:51.215240+00:00`
- Price records: `672`
- Market context records: `3938`
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

- `risk_on_high->unknown_4h` score `86.0991` n `44` status `ready` deltaP `0.2772` edge `11.2316` maxDD `-11.9418`
- `risk_on_and_context->unknown_4h` score `86.0991` n `44` status `ready` deltaP `0.2772` edge `11.2316` maxDD `-11.9418`
- `market_context_high->unknown_4h` score `15.489` n `180` status `ready` deltaP `-3.7127` edge `1.8564` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `9.6587` n `40` status `ready` deltaP `42.0139` edge `0.5248` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.6587` n `40` status `ready` deltaP `42.0139` edge `0.5248` maxDD `0.0`
- `market_context_high->unknown_24h` score `4.9065` n `165` status `ready` deltaP `-12.0959` edge `2.1229` maxDD `-115.3378`
- `risk_on_high->equity_4h` score `4.4783` n `44` status `ready` deltaP `37.985` edge `0.1247` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `4.4783` n `44` status `ready` deltaP `37.985` edge `0.1247` maxDD `-0.0458`
- `market_context_high->equity_24h` score `3.6828` n `165` status `ready` deltaP `20.8018` edge `0.4712` maxDD `-14.5715`
- `market_context_high->index_24h` score `3.5016` n `165` status `ready` deltaP `25.7923` edge `0.2338` maxDD `-7.1159`
- `risk_on_high->index_24h` score `3.2632` n `40` status `ready` deltaP `30.0347` edge `0.0717` maxDD `0.0`
- `risk_on_and_context->index_24h` score `3.2632` n `40` status `ready` deltaP `30.0347` edge `0.0717` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `3.0832` n `44` status `ready` deltaP `25.1524` edge `0.1558` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `3.0832` n `44` status `ready` deltaP `25.1524` edge `0.1558` maxDD `-2.6576`
- `market_context_high->metal_24h` score `2.755` n `165` status `ready` deltaP `15.4325` edge `0.2782` maxDD `-9.1203`
- `market_context_high->crypto_major_4h` score `1.6138` n `180` status `ready` deltaP `17.3746` edge `0.1951` maxDD `-9.4488`
- `risk_on_high->commodity_24h` score `1.4461` n `40` status `ready` deltaP `4.1667` edge `0.2967` maxDD `-12.3174`
- `risk_on_and_context->commodity_24h` score `1.4461` n `40` status `ready` deltaP `4.1667` edge `0.2967` maxDD `-12.3174`
- `risk_on_high->equity_1h` score `1.3769` n `44` status `ready` deltaP `11.8944` edge `0.0748` maxDD `-0.8151`
- `risk_on_and_context->equity_1h` score `1.3769` n `44` status `ready` deltaP `11.8944` edge `0.0748` maxDD `-0.8151`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
