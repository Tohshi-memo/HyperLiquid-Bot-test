# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-22T00:07:31.770519+00:00`
- Price records: `672`
- Market context records: `4365`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11234`

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

- `risk_on_high->unknown_4h` score `131.0924` n `44` status `ready` deltaP `-1.2888` edge `11.1148` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `131.0924` n `44` status `ready` deltaP `-1.2888` edge `11.1148` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `34.0315` n `216` status `ready` deltaP `3.4515` edge `2.9709` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `13.6625` n `208` status `ready` deltaP `3.213` edge `1.6601` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `3.2706` n `44` status `ready` deltaP `35.3797` edge `0.0414` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `3.2706` n `44` status `ready` deltaP `35.3797` edge `0.0414` maxDD `-0.044`
- `risk_on_high->metal_24h` score `2.9161` n `44` status `ready` deltaP `-15.183` edge `0.5365` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `2.9161` n `44` status `ready` deltaP `-15.183` edge `0.5365` maxDD `-1.9133`
- `risk_on_high->crypto_major_4h` score `2.0089` n `44` status `ready` deltaP `18.459` edge `0.1109` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `2.0089` n `44` status `ready` deltaP `18.459` edge `0.1109` maxDD `-2.6576`
- `risk_on_high->equity_24h` score `1.7062` n `44` status `ready` deltaP `19.6181` edge `0.0114` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.7062` n `44` status `ready` deltaP `19.6181` edge `0.0114` maxDD `0.0`
- `risk_on_high->index_24h` score `0.7302` n `44` status `ready` deltaP `21.0069` edge `-0.0792` maxDD `0.0`
- `risk_on_and_context->index_24h` score `0.7302` n `44` status `ready` deltaP `21.0069` edge `-0.0792` maxDD `0.0`
- `risk_on_high->fx_1h` score `0.5476` n `44` status `ready` deltaP `9.6897` edge `0.004` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.5476` n `44` status `ready` deltaP `9.6897` edge `0.004` maxDD `-0.1704`
- `risk_on_high->metal_4h` score `0.4755` n `44` status `ready` deltaP `7.2477` edge `0.0462` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.4755` n `44` status `ready` deltaP `7.2477` edge `0.0462` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `0.4642` n `44` status `ready` deltaP `9.7714` edge `0.0125` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.4642` n `44` status `ready` deltaP `9.7714` edge `0.0125` maxDD `-0.7834`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
