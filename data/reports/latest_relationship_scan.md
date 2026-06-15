# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T11:22:34.737545+00:00`
- Price records: `672`
- Market context records: `3986`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10092`

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

- `risk_on_high->unknown_4h` score `147.2873` n `40` status `ready` deltaP `-1.3415` edge `12.4641` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `147.2873` n `40` status `ready` deltaP `-1.3415` edge `12.4641` maxDD `-10.8303`
- `market_context_high->unknown_24h` score `33.8288` n `150` status `ready` deltaP `-6.6111` edge `3.2955` maxDD `-26.589`
- `market_context_high->unknown_4h` score `20.61` n `162` status `ready` deltaP `1.035` edge `2.2515` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `9.3347` n `40` status `ready` deltaP `42.0139` edge `0.4978` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.3347` n `40` status `ready` deltaP `42.0139` edge `0.4978` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.8505` n `40` status `ready` deltaP `37.5915` edge `0.075` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `3.8505` n `40` status `ready` deltaP `37.5915` edge `0.075` maxDD `-0.0458`
- `market_context_high->metal_24h` score `3.4836` n `150` status `ready` deltaP `16.7709` edge `0.33` maxDD `-9.1203`
- `market_context_high->index_24h` score `3.2671` n `150` status `ready` deltaP `25.8611` edge `0.2138` maxDD `-7.1159`
- `risk_on_high->index_24h` score `2.8149` n `40` status `ready` deltaP `29.8611` edge `0.0355` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.8149` n `40` status `ready` deltaP `29.8611` edge `0.0355` maxDD `0.0`
- `market_context_high->equity_24h` score `2.7475` n `150` status `ready` deltaP `18.6806` edge `0.4074` maxDD `-14.5715`
- `market_context_high->equity_4h` score `2.4003` n `162` status `ready` deltaP `20.3384` edge `0.1947` maxDD `-7.0879`
- `market_context_high->crypto_major_4h` score `1.9809` n `162` status `ready` deltaP `18.846` edge `0.1961` maxDD `-7.8662`
- `risk_on_high->crypto_major_4h` score `1.9762` n `40` status `ready` deltaP `20.9756` edge `0.0914` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.9762` n `40` status `ready` deltaP `20.9756` edge `0.0914` maxDD `-2.6576`
- `market_context_high->crypto_major_1h` score `1.4055` n `162` status `ready` deltaP `11.466` edge `0.0949` maxDD `-2.3372`
- `market_context_high->equity_1h` score `1.022` n `162` status `ready` deltaP `9.3129` edge `0.0795` maxDD `-2.1799`
- `risk_on_high->commodity_24h` score `0.8559` n `40` status `ready` deltaP `4.1667` edge `0.2717` maxDD `-12.9187`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
