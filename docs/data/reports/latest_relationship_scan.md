# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-22T01:37:33.055481+00:00`
- Price records: `672`
- Market context records: `4371`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11194`

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

- `risk_on_high->unknown_4h` score `132.7244` n `44` status `ready` deltaP `-1.2888` edge `11.2508` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `132.7244` n `44` status `ready` deltaP `-1.2888` edge `11.2508` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `35.2551` n `213` status `ready` deltaP `3.9218` edge `3.0614` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `11.686` n `210` status `ready` deltaP `3.0619` edge `1.4964` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `3.2334` n `44` status `ready` deltaP `35.3797` edge `0.0383` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `3.2334` n `44` status `ready` deltaP `35.3797` edge `0.0383` maxDD `-0.044`
- `risk_on_high->metal_24h` score `2.9138` n `44` status `ready` deltaP `-15.183` edge `0.5362` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `2.9138` n `44` status `ready` deltaP `-15.183` edge `0.5362` maxDD `-1.9133`
- `risk_on_high->crypto_major_4h` score `1.8271` n `44` status `ready` deltaP `18.0017` edge `0.0988` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.8271` n `44` status `ready` deltaP `18.0017` edge `0.0988` maxDD `-2.6576`
- `risk_on_high->equity_24h` score `1.7002` n `44` status `ready` deltaP `19.6181` edge `0.0109` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.7002` n `44` status `ready` deltaP `19.6181` edge `0.0109` maxDD `0.0`
- `risk_on_high->index_24h` score `0.8618` n `44` status `ready` deltaP `21.5278` edge `-0.0717` maxDD `0.0`
- `risk_on_and_context->index_24h` score `0.8618` n `44` status `ready` deltaP `21.5278` edge `-0.0717` maxDD `0.0`
- `risk_on_high->fx_1h` score `0.544` n `44` status `ready` deltaP `9.6897` edge `0.0037` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.544` n `44` status `ready` deltaP `9.6897` edge `0.0037` maxDD `-0.1704`
- `risk_on_high->equity_1h` score `0.4534` n `44` status `ready` deltaP `9.7714` edge `0.0116` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.4534` n `44` status `ready` deltaP `9.7714` edge `0.0116` maxDD `-0.7834`
- `risk_on_high->metal_4h` score `0.3491` n `44` status `ready` deltaP `6.3331` edge `0.0361` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.3491` n `44` status `ready` deltaP `6.3331` edge `0.0361` maxDD `-1.3516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
