# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T01:07:32.709975+00:00`
- Price records: `672`
- Market context records: `3945`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11355`

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

- `risk_on_high->unknown_4h` score `144.1732` n `41` status `ready` deltaP `3.2012` edge `12.1743` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `144.1732` n `41` status `ready` deltaP `3.2012` edge `12.1743` maxDD `-10.8303`
- `market_context_high->unknown_4h` score `17.0769` n `173` status `ready` deltaP `-2.7342` edge `1.9822` maxDD `-35.6052`
- `market_context_high->unknown_24h` score `11.9856` n `162` status `ready` deltaP `-10.0116` edge `2.3941` maxDD `-93.2844`
- `risk_on_high->equity_24h` score `9.2699` n `41` status `ready` deltaP `42.0139` edge `0.4924` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.2699` n `41` status `ready` deltaP `42.0139` edge `0.4924` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.5739` n `41` status `ready` deltaP `37.1952` edge `0.0546` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `3.5739` n `41` status `ready` deltaP `37.1952` edge `0.0546` maxDD `-0.0458`
- `market_context_high->equity_24h` score `3.5158` n `162` status `ready` deltaP `20.409` edge `0.4599` maxDD `-14.5715`
- `market_context_high->index_24h` score `3.4744` n `162` status `ready` deltaP `26.1574` edge `0.2291` maxDD `-7.1159`
- `market_context_high->metal_24h` score `3.4477` n `162` status `ready` deltaP `17.6119` edge `0.3214` maxDD `-9.1203`
- `risk_on_high->index_24h` score `2.8785` n `41` status `ready` deltaP `29.8611` edge `0.0408` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.8785` n `41` status `ready` deltaP `29.8611` edge `0.0408` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `2.15` n `41` status `ready` deltaP `22.7134` edge `0.0943` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `2.15` n `41` status `ready` deltaP `22.7134` edge `0.0943` maxDD `-2.6576`
- `market_context_high->crypto_major_4h` score `1.7181` n `173` status `ready` deltaP `17.7508` edge `0.1815` maxDD `-7.8662`
- `market_context_high->equity_4h` score `1.3375` n `173` status `ready` deltaP `15.4836` edge `0.151` maxDD `-7.0879`
- `market_context_high->crypto_major_1h` score `0.7208` n `173` status `ready` deltaP `11.2301` edge `0.084` maxDD `-4.904`
- `risk_on_high->metal_24h` score `0.6574` n `41` status `ready` deltaP `-15.6462` edge `0.25` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `0.6574` n `41` status `ready` deltaP `-15.6462` edge `0.25` maxDD `-1.9133`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
