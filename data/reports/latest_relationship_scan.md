# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T08:52:41.726825+00:00`
- Price records: `672`
- Market context records: `3976`
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

- `risk_on_high->unknown_4h` score `147.9001` n `40` status `ready` deltaP `0.1829` edge `12.505` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `147.9001` n `40` status `ready` deltaP `0.1829` edge `12.505` maxDD `-10.8303`
- `market_context_high->unknown_24h` score `29.6979` n `153` status `ready` deltaP `-6.679` edge `3.0936` maxDD `-37.9399`
- `market_context_high->unknown_4h` score `19.4465` n `166` status `ready` deltaP `1.1166` edge `2.154` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `9.1847` n `40` status `ready` deltaP `42.0139` edge `0.4853` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.1847` n `40` status `ready` deltaP `42.0139` edge `0.4853` maxDD `0.0`
- `market_context_high->metal_24h` score `3.8034` n `153` status `ready` deltaP `17.2284` edge `0.3536` maxDD `-9.1203`
- `risk_on_high->equity_4h` score `3.6055` n `40` status `ready` deltaP `37.439` edge `0.0556` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `3.6055` n `40` status `ready` deltaP `37.439` edge `0.0556` maxDD `-0.0458`
- `market_context_high->index_24h` score `3.4186` n `153` status `ready` deltaP `25.9395` edge `0.2259` maxDD `-7.1159`
- `market_context_high->equity_24h` score `3.0817` n `153` status `ready` deltaP `19.1381` edge `0.4322` maxDD `-14.5715`
- `risk_on_high->index_24h` score `2.7681` n `40` status `ready` deltaP `29.8611` edge `0.0316` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.7681` n `40` status `ready` deltaP `29.8611` edge `0.0316` maxDD `0.0`
- `market_context_high->equity_4h` score `2.4826` n `166` status `ready` deltaP `20.6619` edge `0.1994` maxDD `-7.0879`
- `market_context_high->crypto_major_4h` score `2.1843` n `166` status `ready` deltaP `19.4075` edge `0.2093` maxDD `-7.8662`
- `risk_on_high->crypto_major_4h` score `1.8008` n `40` status `ready` deltaP `20.8232` edge `0.0778` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.8008` n `40` status `ready` deltaP `20.8232` edge `0.0778` maxDD `-2.6576`
- `market_context_high->crypto_major_1h` score `1.6041` n `166` status `ready` deltaP `12.5081` edge `0.1045` maxDD `-2.3372`
- `market_context_high->equity_1h` score `1.1284` n `166` status `ready` deltaP `9.5322` edge `0.0869` maxDD `-2.1799`
- `market_context_high->metal_1h` score `1.039` n `166` status `ready` deltaP `12.3404` edge `0.0637` maxDD `-2.751`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
