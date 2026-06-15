# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T03:52:30.108596+00:00`
- Price records: `672`
- Market context records: `3956`
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

- `risk_on_high->unknown_4h` score `144.0596` n `41` status `ready` deltaP `2.5915` edge `12.1689` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `144.0596` n `41` status `ready` deltaP `2.5915` edge `12.1689` maxDD `-10.8303`
- `market_context_high->unknown_24h` score `26.819` n `151` status `ready` deltaP `-8.4138` edge `3.1534` maxDD `-59.6577`
- `market_context_high->unknown_4h` score `20.5514` n `162` status `ready` deltaP `0.2277` edge `2.252` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `9.1787` n `41` status `ready` deltaP `42.0139` edge `0.4848` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.1787` n `41` status `ready` deltaP `42.0139` edge `0.4848` maxDD `0.0`
- `market_context_high->index_24h` score `3.2608` n `151` status `ready` deltaP `25.8876` edge `0.2131` maxDD `-7.1159`
- `risk_on_high->equity_4h` score `3.2154` n `41` status `ready` deltaP `35.5183` edge `0.0359` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `3.2154` n `41` status `ready` deltaP `35.5183` edge `0.0359` maxDD `-0.0458`
- `market_context_high->metal_24h` score `3.2056` n `151` status `ready` deltaP `16.9254` edge `0.3058` maxDD `-9.1203`
- `risk_on_high->index_24h` score `2.8341` n `41` status `ready` deltaP `29.8611` edge `0.0371` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.8341` n `41` status `ready` deltaP `29.8611` edge `0.0371` maxDD `0.0`
- `market_context_high->equity_24h` score `2.7635` n `151` status `ready` deltaP `18.8351` edge `0.4077` maxDD `-14.5715`
- `market_context_high->crypto_major_4h` score `2.2977` n `162` status `ready` deltaP `20.2405` edge `0.2132` maxDD `-7.8662`
- `market_context_high->equity_4h` score `2.2033` n `162` status `ready` deltaP `18.7914` edge `0.1886` maxDD `-7.0879`
- `risk_on_high->crypto_major_4h` score `1.7917` n `41` status `ready` deltaP `21.189` edge `0.0746` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.7917` n `41` status `ready` deltaP `21.189` edge `0.0746` maxDD `-2.6576`
- `market_context_high->crypto_major_1h` score `1.4653` n `168` status `ready` deltaP `11.7479` edge `0.098` maxDD `-2.3372`
- `market_context_high->metal_1h` score `0.6885` n `168` status `ready` deltaP `10.5788` edge `0.0504` maxDD `-2.751`
- `market_context_high->crypto_alt_4h` score `0.6691` n `162` status `ready` deltaP `12.5734` edge `0.1024` maxDD `-7.1038`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
