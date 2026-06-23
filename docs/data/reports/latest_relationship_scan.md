# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T03:52:31.021715+00:00`
- Price records: `672`
- Market context records: `4479`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11059`

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

- `risk_on_high->unknown_4h` score `124.0788` n `49` status `ready` deltaP `3.2634` edge `10.5012` maxDD `-10.9781`
- `risk_on_and_context->unknown_4h` score `124.0788` n `49` status `ready` deltaP `3.2634` edge `10.5012` maxDD `-10.9781`
- `market_context_high->unknown_1h` score `32.9882` n `228` status `ready` deltaP `3.8345` edge `2.874` maxDD `-9.7103`
- `market_context_high->unknown_4h` score `14.9725` n `228` status `ready` deltaP `3.7468` edge `1.7692` maxDD `-36.0512`
- `risk_on_high->equity_4h` score `4.1552` n `49` status `ready` deltaP `39.0244` edge `0.0861` maxDD `0.0`
- `risk_on_and_context->equity_4h` score `4.1552` n `49` status `ready` deltaP `39.0244` edge `0.0861` maxDD `0.0`
- `risk_on_high->metal_24h` score `3.365` n `44` status `ready` deltaP `-12.9261` edge `0.579` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `3.365` n `44` status `ready` deltaP `-12.9261` edge `0.579` maxDD `-1.9133`
- `risk_on_high->equity_24h` score `2.9468` n `44` status `ready` deltaP `23.7847` edge `0.087` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `2.9468` n `44` status `ready` deltaP `23.7847` edge `0.087` maxDD `0.0`
- `risk_on_high->unknown_24h` score `2.6796` n `44` status `ready` deltaP `13.9994` edge `0.2103` maxDD `-5.0928`
- `risk_on_and_context->unknown_24h` score `2.6796` n `44` status `ready` deltaP `13.9994` edge `0.2103` maxDD `-5.0928`
- `risk_on_high->crypto_major_4h` score `2.5899` n `49` status `ready` deltaP `20.937` edge `0.1428` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `2.5899` n `49` status `ready` deltaP `20.937` edge `0.1428` maxDD `-2.6576`
- `risk_on_high->index_24h` score `2.415` n `44` status `ready` deltaP `25.8681` edge `0.0288` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.415` n `44` status `ready` deltaP `25.8681` edge `0.0288` maxDD `0.0`
- `risk_on_high->metal_4h` score `1.5506` n `49` status `ready` deltaP `12.8671` edge `0.077` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `1.5506` n `49` status `ready` deltaP `12.8671` edge `0.077` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `1.1397` n `49` status `ready` deltaP `14.8418` edge `0.0303` maxDD `-0.7415`
- `risk_on_and_context->equity_1h` score `1.1397` n `49` status `ready` deltaP `14.8418` edge `0.0303` maxDD `-0.7415`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
