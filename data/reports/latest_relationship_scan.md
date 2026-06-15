# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T04:07:29.291929+00:00`
- Price records: `672`
- Market context records: `3957`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11179`

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

- `risk_on_high->unknown_4h` score `144.0632` n `41` status `ready` deltaP `2.5915` edge `12.1692` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `144.0632` n `41` status `ready` deltaP `2.5915` edge `12.1692` maxDD `-10.8303`
- `market_context_high->unknown_24h` score `28.2475` n `150` status `ready` deltaP `-8.2431` edge `3.2272` maxDD `-56.4631`
- `market_context_high->unknown_4h` score `20.9021` n `161` status `ready` deltaP `0.5766` edge `2.2789` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `9.1763` n `41` status `ready` deltaP `42.0139` edge `0.4846` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.1763` n `41` status `ready` deltaP `42.0139` edge `0.4846` maxDD `0.0`
- `market_context_high->index_24h` score `3.2335` n `150` status `ready` deltaP `25.8611` edge `0.211` maxDD `-7.1159`
- `risk_on_high->equity_4h` score `3.1924` n `41` status `ready` deltaP `35.3659` edge `0.035` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `3.1924` n `41` status `ready` deltaP `35.3659` edge `0.035` maxDD `-0.0458`
- `market_context_high->metal_24h` score `3.1776` n `150` status `ready` deltaP `16.7709` edge `0.3045` maxDD `-9.1203`
- `risk_on_high->index_24h` score `2.8317` n `41` status `ready` deltaP `29.8611` edge `0.0369` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.8317` n `41` status `ready` deltaP `29.8611` edge `0.0369` maxDD `0.0`
- `market_context_high->equity_24h` score `2.6695` n `150` status `ready` deltaP `18.6806` edge `0.4009` maxDD `-14.5715`
- `market_context_high->crypto_major_4h` score `2.2947` n `161` status `ready` deltaP `20.068` edge `0.2141` maxDD `-7.8662`
- `market_context_high->equity_4h` score `2.2565` n `161` status `ready` deltaP `19.1259` edge `0.1908` maxDD `-7.0879`
- `risk_on_high->crypto_major_4h` score `1.7905` n `41` status `ready` deltaP `21.189` edge `0.0745` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.7905` n `41` status `ready` deltaP `21.189` edge `0.0745` maxDD `-2.6576`
- `market_context_high->crypto_major_1h` score `1.5453` n `168` status `ready` deltaP `12.1935` edge `0.1017` maxDD `-2.3372`
- `market_context_high->metal_1h` score `0.7361` n `168` status `ready` deltaP `10.5788` edge `0.0502` maxDD `-2.751`
- `market_context_high->crypto_alt_4h` score `0.6535` n `161` status `ready` deltaP `12.3779` edge `0.1024` maxDD `-7.1038`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
