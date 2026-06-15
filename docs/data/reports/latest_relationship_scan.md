# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T01:22:29.437089+00:00`
- Price records: `672`
- Market context records: `3946`
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

- `risk_on_high->unknown_4h` score `144.1346` n `41` status `ready` deltaP `3.0488` edge `12.1721` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `144.1346` n `41` status `ready` deltaP `3.0488` edge `12.1721` maxDD `-10.8303`
- `market_context_high->unknown_4h` score `17.3472` n `172` status `ready` deltaP `-2.5808` edge `2.0037` maxDD `-35.6052`
- `market_context_high->unknown_24h` score `13.3126` n `161` status `ready` deltaP `-9.8861` edge `2.4596` maxDD `-90.0781`
- `risk_on_high->equity_24h` score `9.2555` n `41` status `ready` deltaP `42.0139` edge `0.4912` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.2555` n `41` status `ready` deltaP `42.0139` edge `0.4912` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.5353` n `41` status `ready` deltaP `37.0427` edge `0.0524` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `3.5353` n `41` status `ready` deltaP `37.0427` edge `0.0524` maxDD `-0.0458`
- `market_context_high->equity_24h` score `3.4811` n `161` status `ready` deltaP `20.2748` edge `0.4579` maxDD `-14.5715`
- `market_context_high->metal_24h` score `3.477` n `161` status `ready` deltaP `17.9176` edge `0.3218` maxDD `-9.1203`
- `market_context_high->index_24h` score `3.4738` n `161` status `ready` deltaP `26.1344` edge `0.2292` maxDD `-7.1159`
- `risk_on_high->index_24h` score `2.8701` n `41` status `ready` deltaP `29.8611` edge `0.0401` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.8701` n `41` status `ready` deltaP `29.8611` edge `0.0401` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `2.0898` n `41` status `ready` deltaP `22.5609` edge `0.0903` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `2.0898` n `41` status `ready` deltaP `22.5609` edge `0.0903` maxDD `-2.6576`
- `market_context_high->crypto_major_4h` score `1.7893` n `172` status `ready` deltaP `17.9949` edge `0.1858` maxDD `-7.8662`
- `market_context_high->equity_4h` score `1.425` n `172` status `ready` deltaP `15.7579` edge `0.1523` maxDD `-7.0879`
- `market_context_high->crypto_major_1h` score `0.7762` n `172` status `ready` deltaP `11.5931` edge `0.0862` maxDD `-4.904`
- `market_context_high->metal_1h` score `0.6931` n `172` status `ready` deltaP `10.8167` edge `0.0492` maxDD `-2.751`
- `risk_on_high->metal_24h` score `0.621` n `41` status `ready` deltaP `-15.8198` edge `0.2465` maxDD `-1.9133`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
