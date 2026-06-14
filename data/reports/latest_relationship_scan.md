# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T22:37:27.727970+00:00`
- Price records: `672`
- Market context records: `3934`
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

- `risk_on_high->unknown_4h` score `79.2515` n `47` status `ready` deltaP `-2.7472` edge `10.3897` maxDD `-13.2079`
- `risk_on_and_context->unknown_4h` score `79.2515` n `47` status `ready` deltaP `-2.7472` edge `10.3897` maxDD `-13.2079`
- `market_context_high->unknown_4h` score `14.8497` n `183` status `ready` deltaP `-4.0842` edge `1.8056` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `10.1783` n `40` status `ready` deltaP `42.0139` edge `0.5681` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `10.1783` n `40` status `ready` deltaP `42.0139` edge `0.5681` maxDD `0.0`
- `risk_on_high->equity_4h` score `5.0607` n `47` status `ready` deltaP `38.2752` edge `0.1713` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `5.0607` n `47` status `ready` deltaP `38.2752` edge `0.1713` maxDD `-0.0458`
- `risk_on_high->index_24h` score `3.7816` n `40` status `ready` deltaP `30.0347` edge `0.1149` maxDD `0.0`
- `risk_on_and_context->index_24h` score `3.7816` n `40` status `ready` deltaP `30.0347` edge `0.1149` maxDD `0.0`
- `market_context_high->equity_24h` score `3.7788` n `165` status `ready` deltaP `20.8018` edge `0.4792` maxDD `-14.5715`
- `market_context_high->index_24h` score `3.5988` n `165` status `ready` deltaP `25.7923` edge `0.2419` maxDD `-7.1159`
- `risk_on_high->crypto_major_4h` score `3.2964` n `47` status `ready` deltaP `24.773` edge `0.1761` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `3.2964` n `47` status `ready` deltaP `24.773` edge `0.1761` maxDD `-2.6576`
- `market_context_high->unknown_24h` score `2.7548` n `165` status `ready` deltaP `-13.3933` edge `2.0726` maxDD `-123.966`
- `market_context_high->metal_24h` score `2.5426` n `165` status `ready` deltaP `15.4325` edge `0.2605` maxDD `-9.1203`
- `market_context_high->crypto_major_4h` score `1.7837` n `183` status `ready` deltaP `17.518` edge `0.2083` maxDD `-9.4488`
- `risk_on_high->commodity_24h` score `1.7388` n `40` status `ready` deltaP `4.1667` edge `0.3044` maxDD `-11.9822`
- `risk_on_and_context->commodity_24h` score `1.7388` n `40` status `ready` deltaP `4.1667` edge `0.3044` maxDD `-11.9822`
- `market_context_high->equity_4h` score `1.3396` n `183` status `ready` deltaP `15.7545` edge `0.177` maxDD `-8.2982`
- `risk_on_high->equity_1h` score `1.1101` n `47` status `ready` deltaP `9.67` edge `0.0674` maxDD `-0.8151`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
