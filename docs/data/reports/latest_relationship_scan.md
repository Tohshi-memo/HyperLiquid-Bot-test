# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T19:22:29.213749+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9318`

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

- `market_context_high->commodity_24h` score `1.8987` n `114` status `ready` deltaP `18.0855` edge `0.1228` maxDD `-1.8119`
- `market_context_high->crypto_major_4h` score `1.8472` n `114` status `ready` deltaP `20.1701` edge `0.4428` maxDD `-15.2359`
- `risk_on_high->commodity_24h` score `1.6649` n `81` status `ready` deltaP `19.7424` edge `0.0869` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `1.6649` n `81` status `ready` deltaP `19.7424` edge `0.0869` maxDD `-1.7154`
- `risk_on_high->crypto_major_4h` score `1.4994` n `81` status `ready` deltaP `21.2097` edge `0.2989` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `1.4994` n `81` status `ready` deltaP `21.2097` edge `0.2989` maxDD `-11.1788`
- `market_context_high->crypto_major_1h` score `0.5136` n `114` status `ready` deltaP `6.2901` edge `0.1128` maxDD `-3.7781`
- `risk_on_high->index_1h` score `0.2346` n `81` status `ready` deltaP `7.8245` edge `0.0058` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.2346` n `81` status `ready` deltaP `7.8245` edge `0.0058` maxDD `-0.7394`
- `risk_on_high->equity_1h` score `-0.274` n `81` status `ready` deltaP `11.5783` edge `0.0296` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.274` n `81` status `ready` deltaP `11.5783` edge `0.0296` maxDD `-5.3696`
- `market_context_high->crypto_alt_1h` score `-0.3819` n `114` status `ready` deltaP `1.7307` edge `0.0895` maxDD `-7.3329`
- `risk_on_high->fx_1h` score `-0.4351` n `81` status `ready` deltaP `-2.1522` edge `-0.0034` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.4351` n `81` status `ready` deltaP `-2.1522` edge `-0.0034` maxDD `-0.376`
- `risk_on_high->crypto_major_1h` score `-0.4767` n `81` status `ready` deltaP `0.767` edge `0.0257` maxDD `-4.6876`
- `risk_on_and_context->crypto_major_1h` score `-0.4767` n `81` status `ready` deltaP `0.767` edge `0.0257` maxDD `-4.6876`
- `market_context_high->index_1h` score `-0.5805` n `114` status `ready` deltaP `3.6984` edge `0.0018` maxDD `-1.3195`
- `risk_on_high->metal_1h` score `-0.6289` n `81` status `ready` deltaP `-1.6634` edge `0.0036` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.6289` n `81` status `ready` deltaP `-1.6634` edge `0.0036` maxDD `-0.8513`
- `market_context_high->fx_1h` score `-0.6705` n `114` status `ready` deltaP `-4.6863` edge `-0.0026` maxDD `-0.503`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
