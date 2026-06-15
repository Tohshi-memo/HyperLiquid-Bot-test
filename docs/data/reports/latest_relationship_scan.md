# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T09:07:38.180295+00:00`
- Price records: `672`
- Market context records: `3977`
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

- `risk_on_high->unknown_4h` score `147.8351` n `40` status `ready` deltaP `0.0305` edge `12.5006` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `147.8351` n `40` status `ready` deltaP `0.0305` edge `12.5006` maxDD `-10.8303`
- `market_context_high->unknown_24h` score `29.5952` n `153` status `ready` deltaP `-6.8526` edge `3.0862` maxDD `-37.9399`
- `market_context_high->unknown_4h` score `19.3816` n `166` status `ready` deltaP `0.9642` edge `2.1496` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `9.2003` n `40` status `ready` deltaP `42.0139` edge `0.4866` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.2003` n `40` status `ready` deltaP `42.0139` edge `0.4866` maxDD `0.0`
- `market_context_high->metal_24h` score `3.7746` n `153` status `ready` deltaP `17.2284` edge `0.3512` maxDD `-9.1203`
- `risk_on_high->equity_4h` score `3.6295` n `40` status `ready` deltaP `37.439` edge `0.0576` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `3.6295` n `40` status `ready` deltaP `37.439` edge `0.0576` maxDD `-0.0458`
- `market_context_high->index_24h` score `3.4222` n `153` status `ready` deltaP `25.9395` edge `0.2262` maxDD `-7.1159`
- `market_context_high->equity_24h` score `3.0973` n `153` status `ready` deltaP `19.1381` edge `0.4335` maxDD `-14.5715`
- `risk_on_high->index_24h` score `2.7717` n `40` status `ready` deltaP `29.8611` edge `0.0319` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.7717` n `40` status `ready` deltaP `29.8611` edge `0.0319` maxDD `0.0`
- `market_context_high->equity_4h` score `2.5066` n `166` status `ready` deltaP `20.6619` edge `0.2014` maxDD `-7.0879`
- `market_context_high->crypto_major_4h` score `2.2059` n `166` status `ready` deltaP `19.4075` edge `0.2111` maxDD `-7.8662`
- `risk_on_high->crypto_major_4h` score `1.8224` n `40` status `ready` deltaP `20.8232` edge `0.0796` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.8224` n `40` status `ready` deltaP `20.8232` edge `0.0796` maxDD `-2.6576`
- `market_context_high->crypto_major_1h` score `1.6149` n `166` status `ready` deltaP `12.5081` edge `0.1054` maxDD `-2.3372`
- `market_context_high->equity_1h` score `1.1332` n `166` status `ready` deltaP `9.5322` edge `0.0873` maxDD `-2.1799`
- `market_context_high->metal_1h` score `1.0342` n `166` status `ready` deltaP `12.3404` edge `0.0633` maxDD `-2.751`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
