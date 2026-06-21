# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-21T22:22:25.665453+00:00`
- Price records: `672`
- Market context records: `4357`
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

- `risk_on_high->unknown_4h` score `130.9676` n `44` status `ready` deltaP `-1.2888` edge `11.1044` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `130.9676` n `44` status `ready` deltaP `-1.2888` edge `11.1044` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `32.5596` n `220` status `ready` deltaP `3.4731` edge `2.8481` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `13.1362` n `213` status `ready` deltaP `4.0143` edge `1.6109` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `3.2018` n `44` status `ready` deltaP `35.0749` edge `0.0377` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `3.2018` n `44` status `ready` deltaP `35.0749` edge `0.0377` maxDD `-0.044`
- `risk_on_high->metal_24h` score `2.7788` n `44` status `ready` deltaP `-16.3983` edge `0.527` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `2.7788` n `44` status `ready` deltaP `-16.3983` edge `0.527` maxDD `-1.9133`
- `risk_on_high->crypto_major_4h` score `1.7919` n `44` status `ready` deltaP `17.6968` edge `0.0979` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.7919` n `44` status `ready` deltaP `17.6968` edge `0.0979` maxDD `-2.6576`
- `risk_on_high->equity_24h` score `1.7254` n `44` status `ready` deltaP `19.6181` edge `0.013` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.7254` n `44` status `ready` deltaP `19.6181` edge `0.013` maxDD `0.0`
- `risk_on_high->index_24h` score `0.5333` n `44` status `ready` deltaP `19.7917` edge `-0.0875` maxDD `0.0`
- `risk_on_and_context->index_24h` score `0.5333` n `44` status `ready` deltaP `19.7917` edge `-0.0875` maxDD `0.0`
- `risk_on_high->fx_1h` score `0.5117` n `44` status `ready` deltaP `9.2406` edge `0.004` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.5117` n `44` status `ready` deltaP `9.2406` edge `0.004` maxDD `-0.1704`
- `risk_on_high->metal_4h` score `0.4747` n `44` status `ready` deltaP `7.2477` edge `0.0461` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.4747` n `44` status `ready` deltaP `7.2477` edge `0.0461` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `0.3731` n `44` status `ready` deltaP `9.1726` edge `0.0089` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.3731` n `44` status `ready` deltaP `9.1726` edge `0.0089` maxDD `-0.7834`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
