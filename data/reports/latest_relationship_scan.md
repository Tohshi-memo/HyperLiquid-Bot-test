# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T01:22:25.877564+00:00`
- Price records: `672`
- Market context records: `4469`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11099`

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

- `risk_on_high->unknown_4h` score `123.989` n `49` status `ready` deltaP `3.4159` edge `10.4927` maxDD `-10.9781`
- `risk_on_and_context->unknown_4h` score `123.989` n `49` status `ready` deltaP `3.4159` edge `10.4927` maxDD `-10.9781`
- `market_context_high->unknown_1h` score `31.5246` n `233` status `ready` deltaP `3.5993` edge `2.7536` maxDD `-9.7103`
- `market_context_high->unknown_4h` score `14.1763` n `233` status `ready` deltaP `4.2042` edge `1.6998` maxDD `-36.0512`
- `risk_on_high->equity_4h` score `3.6912` n `49` status `ready` deltaP `37.5` edge `0.0576` maxDD `0.0`
- `risk_on_and_context->equity_4h` score `3.6912` n `49` status `ready` deltaP `37.5` edge `0.0576` maxDD `0.0`
- `risk_on_high->unknown_24h` score `3.1742` n `44` status `ready` deltaP `15.5619` edge `0.2411` maxDD `-5.0928`
- `risk_on_and_context->unknown_24h` score `3.1742` n `44` status `ready` deltaP `15.5619` edge `0.2411` maxDD `-5.0928`
- `risk_on_high->metal_24h` score `3.1452` n `44` status `ready` deltaP `-14.6622` edge `0.5624` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `3.1452` n `44` status `ready` deltaP `-14.6622` edge `0.5624` maxDD `-1.9133`
- `risk_on_high->crypto_major_4h` score `2.3897` n `49` status `ready` deltaP `20.1748` edge `0.1312` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `2.3897` n `49` status `ready` deltaP `20.1748` edge `0.1312` maxDD `-2.6576`
- `risk_on_high->equity_24h` score `2.2187` n `44` status `ready` deltaP `22.0486` edge `0.0379` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `2.2187` n `44` status `ready` deltaP `22.0486` edge `0.0379` maxDD `0.0`
- `risk_on_high->index_24h` score `2.155` n `44` status `ready` deltaP `24.1319` edge `0.0187` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.155` n `44` status `ready` deltaP `24.1319` edge `0.0187` maxDD `0.0`
- `risk_on_high->metal_4h` score `1.3003` n `49` status `ready` deltaP `11.3427` edge `0.0663` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `1.3003` n `49` status `ready` deltaP `11.3427` edge `0.0663` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `1.0198` n `49` status `ready` deltaP `14.5424` edge `0.0223` maxDD `-0.7415`
- `risk_on_and_context->equity_1h` score `1.0198` n `49` status `ready` deltaP `14.5424` edge `0.0223` maxDD `-0.7415`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
