# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T06:07:39.774251+00:00`
- Price records: `672`
- Market context records: `3965`
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

- `risk_on_high->unknown_4h` score `148.168` n `40` status `ready` deltaP `1.4024` edge `12.5192` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `148.168` n `40` status `ready` deltaP `1.4024` edge `12.5192` maxDD `-10.8303`
- `market_context_high->unknown_24h` score `36.535` n `144` status `ready` deltaP `-7.4652` edge `3.6686` maxDD `-37.9399`
- `market_context_high->unknown_4h` score `22.003` n `158` status `ready` deltaP `1.4973` edge `2.3645` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `8.9711` n `40` status `ready` deltaP `42.0139` edge `0.4675` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `8.9711` n `40` status `ready` deltaP `42.0139` edge `0.4675` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.4242` n `40` status `ready` deltaP `37.439` edge `0.0405` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `3.4242` n `40` status `ready` deltaP `37.439` edge `0.0405` maxDD `-0.0458`
- `market_context_high->metal_24h` score `2.9918` n `144` status `ready` deltaP `15.7986` edge `0.2955` maxDD `-9.1203`
- `market_context_high->index_24h` score `2.9586` n `144` status `ready` deltaP `25.6944` edge `0.1892` maxDD `-7.1159`
- `risk_on_high->index_24h` score `2.7093` n `40` status `ready` deltaP `29.8611` edge `0.0267` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.7093` n `40` status `ready` deltaP `29.8611` edge `0.0267` maxDD `0.0`
- `market_context_high->equity_4h` score `2.3409` n `158` status `ready` deltaP `19.6858` edge `0.1941` maxDD `-7.0879`
- `market_context_high->crypto_major_4h` score `2.3351` n `158` status `ready` deltaP `20.0178` edge `0.2178` maxDD `-7.8662`
- `market_context_high->equity_24h` score `1.8741` n `144` status `ready` deltaP `17.7083` edge `0.3411` maxDD `-14.5715`
- `risk_on_high->crypto_major_4h` score `1.6982` n `40` status `ready` deltaP `20.3659` edge `0.0723` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.6982` n `40` status `ready` deltaP `20.3659` edge `0.0723` maxDD `-2.6576`
- `market_context_high->crypto_major_1h` score `1.6017` n `166` status `ready` deltaP `12.3584` edge `0.1053` maxDD `-2.3372`
- `market_context_high->equity_1h` score `1.0996` n `166` status `ready` deltaP `9.6819` edge `0.0835` maxDD `-2.1799`
- `market_context_high->metal_1h` score `1.0965` n `166` status `ready` deltaP `12.7895` edge `0.0655` maxDD `-2.751`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
