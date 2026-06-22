# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-22T15:52:28.697663+00:00`
- Price records: `672`
- Market context records: `4428`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11138`

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

- `risk_on_high->unknown_4h` score `123.9142` n `49` status `ready` deltaP `3.111` edge `10.4885` maxDD `-10.9781`
- `risk_on_and_context->unknown_4h` score `123.9142` n `49` status `ready` deltaP `3.111` edge `10.4885` maxDD `-10.9781`
- `market_context_high->unknown_1h` score `31.256` n `233` status `ready` deltaP `2.5514` edge `2.7382` maxDD `-9.7103`
- `market_context_high->unknown_4h` score `14.8502` n `228` status `ready` deltaP `4.033` edge `1.7571` maxDD `-36.0512`
- `risk_on_high->unknown_24h` score `4.0693` n `44` status `ready` deltaP `18.8605` edge `0.2937` maxDD `-5.0928`
- `risk_on_and_context->unknown_24h` score `4.0693` n `44` status `ready` deltaP `18.8605` edge `0.2937` maxDD `-5.0928`
- `risk_on_high->equity_4h` score `3.1999` n `49` status `ready` deltaP `35.2134` edge `0.0319` maxDD `0.0`
- `risk_on_and_context->equity_4h` score `3.1999` n `49` status `ready` deltaP `35.2134` edge `0.0319` maxDD `0.0`
- `risk_on_high->metal_24h` score `3.0717` n `44` status `ready` deltaP `-15.3567` edge `0.5576` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `3.0717` n `44` status `ready` deltaP `-15.3567` edge `0.5576` maxDD `-1.9133`
- `risk_on_high->crypto_major_4h` score `2.0416` n `49` status `ready` deltaP `19.1078` edge `0.1093` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `2.0416` n `49` status `ready` deltaP `19.1078` edge `0.1093` maxDD `-2.6576`
- `risk_on_high->index_24h` score `1.8234` n `44` status `ready` deltaP `23.4375` edge `-0.0043` maxDD `0.0`
- `risk_on_and_context->index_24h` score `1.8234` n `44` status `ready` deltaP `23.4375` edge `-0.0043` maxDD `0.0`
- `risk_on_high->metal_4h` score `1.1769` n `49` status `ready` deltaP `10.5805` edge `0.0611` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `1.1769` n `49` status `ready` deltaP `10.5805` edge `0.0611` maxDD `-1.3516`
- `risk_on_high->equity_24h` score `0.9872` n `44` status `ready` deltaP `15.625` edge `-0.0219` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `0.9872` n `44` status `ready` deltaP `15.625` edge `-0.0219` maxDD `0.0`
- `risk_on_high->equity_1h` score `0.846` n `49` status `ready` deltaP `13.1951` edge `0.0168` maxDD `-0.7415`
- `risk_on_and_context->equity_1h` score `0.846` n `49` status `ready` deltaP `13.1951` edge `0.0168` maxDD `-0.7415`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
