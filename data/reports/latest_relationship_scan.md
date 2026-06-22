# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-22T22:37:27.769031+00:00`
- Price records: `672`
- Market context records: `4457`
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

- `risk_on_high->unknown_4h` score `123.9528` n `49` status `ready` deltaP `3.2634` edge `10.4907` maxDD `-10.9781`
- `risk_on_and_context->unknown_4h` score `123.9528` n `49` status `ready` deltaP `3.2634` edge `10.4907` maxDD `-10.9781`
- `market_context_high->unknown_1h` score `31.4311` n `233` status `ready` deltaP `3.0005` edge `2.7498` maxDD `-9.7103`
- `market_context_high->unknown_4h` score `14.1401` n `233` status `ready` deltaP `4.0517` edge `1.6978` maxDD `-36.0512`
- `risk_on_high->equity_4h` score `3.6334` n `49` status `ready` deltaP `37.3476` edge `0.0538` maxDD `0.0`
- `risk_on_and_context->equity_4h` score `3.6334` n `49` status `ready` deltaP `37.3476` edge `0.0538` maxDD `0.0`
- `risk_on_high->unknown_24h` score `3.166` n `44` status `ready` deltaP `15.9091` edge `0.2381` maxDD `-5.0928`
- `risk_on_and_context->unknown_24h` score `3.166` n `44` status `ready` deltaP `15.9091` edge `0.2381` maxDD `-5.0928`
- `risk_on_high->metal_24h` score `3.0712` n `44` status `ready` deltaP `-15.5303` edge `0.5587` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `3.0712` n `44` status `ready` deltaP `-15.5303` edge `0.5587` maxDD `-1.9133`
- `risk_on_high->crypto_major_4h` score `2.3016` n `49` status `ready` deltaP `19.7175` edge `0.1269` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `2.3016` n `49` status `ready` deltaP `19.7175` edge `0.1269` maxDD `-2.6576`
- `risk_on_high->index_24h` score `2.0466` n `44` status `ready` deltaP `23.4375` edge `0.0143` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.0466` n `44` status `ready` deltaP `23.4375` edge `0.0143` maxDD `0.0`
- `risk_on_high->equity_24h` score `1.8463` n `44` status `ready` deltaP `20.1389` edge `0.0196` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.8463` n `44` status `ready` deltaP `20.1389` edge `0.0196` maxDD `0.0`
- `risk_on_high->metal_4h` score `1.2955` n `49` status `ready` deltaP `11.3427` edge `0.0659` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `1.2955` n `49` status `ready` deltaP `11.3427` edge `0.0659` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `0.9143` n `49` status `ready` deltaP `13.7939` edge `0.0185` maxDD `-0.7415`
- `risk_on_and_context->equity_1h` score `0.9143` n `49` status `ready` deltaP `13.7939` edge `0.0185` maxDD `-0.7415`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
