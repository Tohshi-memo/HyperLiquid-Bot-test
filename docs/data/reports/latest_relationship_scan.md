# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T06:52:19.784976+00:00`
- Price records: `672`
- Market context records: `2117`
- Flow alert records: `7991`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9149`

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

- `market_context_high->crypto_alt_4h` score `12.8516` n `164` status `ready` deltaP `36.5853` edge `0.9207` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.7807` n `164` status `ready` deltaP `41.4634` edge `0.7583` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `6.1756` n `164` status `ready` deltaP `24.8476` edge `0.4239` maxDD `-2.6599`
- `market_context_high->equity_4h` score `4.9642` n `164` status `ready` deltaP `25.6097` edge `0.3524` maxDD `-5.0894`
- `market_context_high->metal_4h` score `3.0442` n `164` status `ready` deltaP `20.8841` edge `0.2532` maxDD `-4.7664`
- `market_context_high->index_4h` score `2.9982` n `164` status `ready` deltaP `21.6464` edge `0.1739` maxDD `-1.8022`
- `market_context_high->index_24h` score `2.7821` n `163` status `ready` deltaP `12.3272` edge `0.2725` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `2.4895` n `164` status `ready` deltaP `15.7989` edge `0.19` maxDD `-3.0294`
- `market_context_high->crypto_alt_1h` score `2.4383` n `164` status `ready` deltaP `13.1043` edge `0.2147` maxDD `-4.9097`
- `market_context_high->equity_24h` score `1.9253` n `163` status `ready` deltaP `23.6833` edge `0.4924` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `1.7133` n `163` status `ready` deltaP `24.0771` edge `0.5143` maxDD `-35.8966`
- `market_context_high->crypto_major_24h` score `1.2704` n `163` status `ready` deltaP `20.6923` edge `0.8265` maxDD `-62.3533`
- `market_context_high->equity_1h` score `0.7337` n `164` status `ready` deltaP `9.5663` edge `0.0762` maxDD `-2.6402`
- `market_context_high->metal_1h` score `0.424` n `164` status `ready` deltaP `7.9049` edge `0.0497` maxDD `-2.3654`
- `market_context_high->unknown_1h` score `0.0906` n `164` status `ready` deltaP `5.371` edge `0.0437` maxDD `-3.0902`
- `market_context_high->metal_24h` score `-0.0286` n `163` status `ready` deltaP `11.0185` edge `0.313` maxDD `-23.2095`
- `market_context_high->index_1h` score `-0.0317` n `164` status `ready` deltaP `4.0346` edge `0.0295` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.0829` n `163` status `ready` deltaP `14.6061` edge `0.0313` maxDD `-2.811`
- `market_context_high->fx_1h` score `-0.6518` n `164` status `ready` deltaP `-3.2094` edge `0.0006` maxDD `-0.3548`
- `market_context_high->fx_4h` score `-1.0897` n `164` status `ready` deltaP `-7.4695` edge `-0.0027` maxDD `-0.9762`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
