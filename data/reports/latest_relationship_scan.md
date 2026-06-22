# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-22T02:37:30.145584+00:00`
- Price records: `672`
- Market context records: `4375`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11143`

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

- `risk_on_high->unknown_4h` score `132.6086` n `44` status `ready` deltaP `-1.7462` edge `11.2442` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `132.6086` n `44` status `ready` deltaP `-1.7462` edge `11.2442` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `35.1832` n `213` status `ready` deltaP `3.4726` edge `3.0584` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `11.2056` n `213` status `ready` deltaP `3.0874` edge `1.4562` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `3.219` n `44` status `ready` deltaP `35.3797` edge `0.0371` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `3.219` n `44` status `ready` deltaP `35.3797` edge `0.0371` maxDD `-0.044`
- `risk_on_high->metal_24h` score `2.9193` n `44` status `ready` deltaP `-15.183` edge `0.5369` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `2.9193` n `44` status `ready` deltaP `-15.183` edge `0.5369` maxDD `-1.9133`
- `risk_on_high->crypto_major_4h` score `1.6643` n `44` status `ready` deltaP `17.3919` edge `0.0893` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.6643` n `44` status `ready` deltaP `17.3919` edge `0.0893` maxDD `-2.6576`
- `risk_on_high->equity_24h` score `1.657` n `44` status `ready` deltaP `19.6181` edge `0.0073` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.657` n `44` status `ready` deltaP `19.6181` edge `0.0073` maxDD `0.0`
- `risk_on_high->index_24h` score `0.9062` n `44` status `ready` deltaP `21.5278` edge `-0.068` maxDD `0.0`
- `risk_on_and_context->index_24h` score `0.9062` n `44` status `ready` deltaP `21.5278` edge `-0.068` maxDD `0.0`
- `risk_on_high->fx_1h` score `0.5033` n `44` status `ready` deltaP `9.2406` edge `0.0033` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.5033` n `44` status `ready` deltaP `9.2406` edge `0.0033` maxDD `-0.1704`
- `risk_on_high->equity_1h` score `0.4007` n `44` status `ready` deltaP `9.472` edge `0.0092` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.4007` n `44` status `ready` deltaP `9.472` edge `0.0092` maxDD `-0.7834`
- `risk_on_high->metal_4h` score `0.3264` n `44` status `ready` deltaP `6.1807` edge `0.0342` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.3264` n `44` status `ready` deltaP `6.1807` edge `0.0342` maxDD `-1.3516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
