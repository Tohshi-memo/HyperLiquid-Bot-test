# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T01:52:35.085280+00:00`
- Price records: `672`
- Market context records: `3948`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11267`

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

- `risk_on_high->unknown_4h` score `144.0732` n `41` status `ready` deltaP `2.8964` edge `12.168` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `144.0732` n `41` status `ready` deltaP `2.8964` edge `12.168` maxDD `-10.8303`
- `market_context_high->unknown_4h` score `17.938` n `170` status `ready` deltaP `-2.1108` edge `2.0498` maxDD `-35.6052`
- `market_context_high->unknown_24h` score `15.9208` n `159` status `ready` deltaP `-9.624` edge `2.5925` maxDD `-84.1285`
- `risk_on_high->equity_24h` score `9.2531` n `41` status `ready` deltaP `42.0139` edge `0.491` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.2531` n `41` status `ready` deltaP `42.0139` edge `0.491` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.4894` n `41` status `ready` deltaP `36.7379` edge `0.0506` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `3.4894` n `41` status `ready` deltaP `36.7379` edge `0.0506` maxDD `-0.0458`
- `market_context_high->index_24h` score `3.4232` n `159` status `ready` deltaP `26.0875` edge `0.2253` maxDD `-7.1159`
- `market_context_high->metal_24h` score `3.4029` n `159` status `ready` deltaP `17.6363` edge `0.3175` maxDD `-9.1203`
- `market_context_high->equity_24h` score `3.3188` n `159` status `ready` deltaP `20.0013` edge `0.4462` maxDD `-14.5715`
- `risk_on_high->index_24h` score `2.8689` n `41` status `ready` deltaP `29.8611` edge `0.04` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.8689` n `41` status `ready` deltaP `29.8611` edge `0.04` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `2.0186` n `41` status `ready` deltaP `22.2561` edge `0.0864` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `2.0186` n `41` status `ready` deltaP `22.2561` edge `0.0864` maxDD `-2.6576`
- `market_context_high->crypto_major_4h` score `1.911` n `170` status `ready` deltaP `18.4972` edge `0.1926` maxDD `-7.8662`
- `market_context_high->equity_4h` score `1.6038` n `170` status `ready` deltaP `16.3218` edge `0.1551` maxDD `-7.0879`
- `market_context_high->crypto_major_1h` score `0.7268` n `170` status `ready` deltaP `11.305` edge `0.084` maxDD `-4.904`
- `market_context_high->metal_1h` score `0.6662` n `170` status `ready` deltaP `10.4808` edge `0.0492` maxDD `-2.751`
- `risk_on_high->commodity_24h` score `0.6119` n `41` status `ready` deltaP `3.5569` edge `0.2682` maxDD `-13.9406`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
