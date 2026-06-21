# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-21T18:00:17.956076+00:00`
- Price records: `672`
- Market context records: `4337`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10810`

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

- `risk_on_high->unknown_4h` score `130.9395` n `44` status `ready` deltaP `-0.6791` edge `11.098` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `130.9395` n `44` status `ready` deltaP `-0.6791` edge `11.098` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `30.3058` n `228` status `ready` deltaP `3.5456` edge `2.6598` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `11.033` n `224` status `ready` deltaP `1.3502` edge `1.4534` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `2.9293` n `44` status `ready` deltaP `33.0932` edge `0.0282` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.9293` n `44` status `ready` deltaP `33.0932` edge `0.0282` maxDD `-0.044`
- `risk_on_high->metal_24h` score `2.5307` n `44` status `ready` deltaP `-19.1761` edge `0.5137` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `2.5307` n `44` status `ready` deltaP `-19.1761` edge `0.5137` maxDD `-1.9133`
- `risk_on_high->equity_24h` score `2.1798` n `44` status `ready` deltaP `22.2222` edge `0.0335` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `2.1798` n `44` status `ready` deltaP `22.2222` edge `0.0335` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `1.6871` n `44` status `ready` deltaP `17.3919` edge `0.0912` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.6871` n `44` status `ready` deltaP `17.3919` edge `0.0912` maxDD `-2.6576`
- `risk_on_high->fx_1h` score `0.4458` n `44` status `ready` deltaP `8.4921` edge `0.0035` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.4458` n `44` status `ready` deltaP `8.4921` edge `0.0035` maxDD `-0.1704`
- `risk_on_high->metal_4h` score `0.4176` n `44` status `ready` deltaP `6.1807` edge `0.0459` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.4176` n `44` status `ready` deltaP `6.1807` edge `0.0459` maxDD `-1.3516`
- `risk_on_high->index_24h` score `0.3441` n `44` status `ready` deltaP `19.2708` edge `-0.0998` maxDD `0.0`
- `risk_on_and_context->index_24h` score `0.3441` n `44` status `ready` deltaP `19.2708` edge `-0.0998` maxDD `0.0`
- `risk_on_high->crypto_major_1h` score `0.2415` n `44` status `ready` deltaP `8.3969` edge `0.0292` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.2415` n `44` status `ready` deltaP `8.3969` edge `0.0292` maxDD `-2.3372`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
