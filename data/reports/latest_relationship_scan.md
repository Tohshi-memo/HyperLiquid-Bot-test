# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-22T20:07:39.136911+00:00`
- Price records: `672`
- Market context records: `4446`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11151`

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

- `risk_on_high->unknown_4h` score `124.0563` n `49` status `ready` deltaP `3.5683` edge `10.4973` maxDD `-10.9781`
- `risk_on_and_context->unknown_4h` score `124.0563` n `49` status `ready` deltaP `3.5683` edge `10.4973` maxDD `-10.9781`
- `market_context_high->unknown_1h` score `31.4083` n `233` status `ready` deltaP `2.7011` edge `2.7499` maxDD `-9.7103`
- `market_context_high->unknown_4h` score `14.2436` n `233` status `ready` deltaP `4.3566` edge `1.7044` maxDD `-36.0512`
- `risk_on_high->equity_4h` score `3.6068` n `49` status `ready` deltaP `37.1951` edge `0.0526` maxDD `0.0`
- `risk_on_and_context->equity_4h` score `3.6068` n `49` status `ready` deltaP `37.1951` edge `0.0526` maxDD `0.0`
- `risk_on_high->unknown_24h` score `3.1288` n `44` status `ready` deltaP `15.9091` edge `0.235` maxDD `-5.0928`
- `risk_on_and_context->unknown_24h` score `3.1288` n `44` status `ready` deltaP `15.9091` edge `0.235` maxDD `-5.0928`
- `risk_on_high->metal_24h` score `3.0845` n `44` status `ready` deltaP `-15.5303` edge `0.5604` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `3.0845` n `44` status `ready` deltaP `-15.5303` edge `0.5604` maxDD `-1.9133`
- `risk_on_high->crypto_major_4h` score `2.175` n `49` status `ready` deltaP `19.2602` edge `0.1194` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `2.175` n `49` status `ready` deltaP `19.2602` edge `0.1194` maxDD `-2.6576`
- `risk_on_high->index_24h` score `1.9842` n `44` status `ready` deltaP `23.4375` edge `0.0091` maxDD `0.0`
- `risk_on_and_context->index_24h` score `1.9842` n `44` status `ready` deltaP `23.4375` edge `0.0091` maxDD `0.0`
- `risk_on_high->equity_24h` score `1.5394` n `44` status `ready` deltaP `18.4028` edge `0.0056` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.5394` n `44` status `ready` deltaP `18.4028` edge `0.0056` maxDD `0.0`
- `risk_on_high->metal_4h` score `1.3673` n `49` status `ready` deltaP `12.1049` edge `0.0668` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `1.3673` n `49` status `ready` deltaP `12.1049` edge `0.0668` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `0.9167` n `49` status `ready` deltaP `13.7939` edge `0.0187` maxDD `-0.7415`
- `risk_on_and_context->equity_1h` score `0.9167` n `49` status `ready` deltaP `13.7939` edge `0.0187` maxDD `-0.7415`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
