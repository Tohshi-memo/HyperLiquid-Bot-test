# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T09:52:31.398801+00:00`
- Price records: `672`
- Market context records: `4504`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9771`

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

- `risk_on_high->unknown_4h` score `124.7441` n `49` status `ready` deltaP `4.6354` edge `10.5475` maxDD `-10.9781`
- `risk_on_and_context->unknown_4h` score `124.7441` n `49` status `ready` deltaP `4.6354` edge `10.5475` maxDD `-10.9781`
- `market_context_high->unknown_1h` score `39.9234` n `204` status `ready` deltaP `3.4637` edge `3.4544` maxDD `-9.7103`
- `market_context_high->unknown_4h` score `19.7329` n `204` status `ready` deltaP `3.0548` edge `2.0535` maxDD `-28.0229`
- `risk_on_high->equity_4h` score `5.0767` n `49` status `ready` deltaP `41.7683` edge `0.1446` maxDD `0.0`
- `risk_on_and_context->equity_4h` score `5.0767` n `49` status `ready` deltaP `41.7683` edge `0.1446` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `3.8554` n `49` status `ready` deltaP `24.2907` edge `0.2259` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `3.8554` n `49` status `ready` deltaP `24.2907` edge `0.2259` maxDD `-2.6576`
- `risk_on_high->metal_24h` score `2.5794` n `49` status `ready` deltaP `-12.7019` edge `0.5133` maxDD `-4.834`
- `risk_on_and_context->metal_24h` score `2.5794` n `49` status `ready` deltaP `-12.7019` edge `0.5133` maxDD `-4.834`
- `risk_on_high->unknown_24h` score `2.0696` n `49` status `ready` deltaP `10.9339` edge `0.1799` maxDD `-5.0928`
- `risk_on_and_context->unknown_24h` score `2.0696` n `49` status `ready` deltaP `10.9339` edge `0.1799` maxDD `-5.0928`
- `risk_on_high->metal_4h` score `2.0259` n `49` status `ready` deltaP `15.7634` edge `0.0973` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `2.0259` n `49` status `ready` deltaP `15.7634` edge `0.0973` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `1.3531` n `49` status `ready` deltaP `16.0394` edge `0.0401` maxDD `-0.7415`
- `risk_on_and_context->equity_1h` score `1.3531` n `49` status `ready` deltaP `16.0394` edge `0.0401` maxDD `-0.7415`
- `risk_on_high->index_24h` score `0.9011` n `49` status `ready` deltaP `19.8306` edge `-0.0054` maxDD `-2.4702`
- `risk_on_and_context->index_24h` score `0.9011` n `49` status `ready` deltaP `19.8306` edge `-0.0054` maxDD `-2.4702`
- `risk_on_high->fx_4h` score `0.6375` n `49` status `ready` deltaP `15.7043` edge `0.0075` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.6375` n `49` status `ready` deltaP `15.7043` edge `0.0075` maxDD `-0.3925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
