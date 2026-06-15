# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T08:22:39.368211+00:00`
- Price records: `672`
- Market context records: `3974`
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

- `risk_on_high->unknown_4h` score `148.0385` n `40` status `ready` deltaP `0.4878` edge `12.5145` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `148.0385` n `40` status `ready` deltaP `0.4878` edge `12.5145` maxDD `-10.8303`
- `market_context_high->unknown_24h` score `29.9033` n `153` status `ready` deltaP `-6.3317` edge `3.1084` maxDD `-37.9399`
- `market_context_high->unknown_4h` score `19.5849` n `166` status `ready` deltaP `1.4215` edge `2.1635` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `9.1739` n `40` status `ready` deltaP `42.0139` edge `0.4844` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.1739` n `40` status `ready` deltaP `42.0139` edge `0.4844` maxDD `0.0`
- `market_context_high->metal_24h` score `3.8514` n `153` status `ready` deltaP `17.2284` edge `0.3576` maxDD `-9.1203`
- `risk_on_high->equity_4h` score `3.5743` n `40` status `ready` deltaP `37.439` edge `0.053` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `3.5743` n `40` status `ready` deltaP `37.439` edge `0.053` maxDD `-0.0458`
- `market_context_high->index_24h` score `3.4138` n `153` status `ready` deltaP `25.9395` edge `0.2255` maxDD `-7.1159`
- `market_context_high->equity_24h` score `3.0709` n `153` status `ready` deltaP `19.1381` edge `0.4313` maxDD `-14.5715`
- `risk_on_high->index_24h` score `2.7633` n `40` status `ready` deltaP `29.8611` edge `0.0312` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.7633` n `40` status `ready` deltaP `29.8611` edge `0.0312` maxDD `0.0`
- `market_context_high->equity_4h` score `2.4514` n `166` status `ready` deltaP `20.6619` edge `0.1968` maxDD `-7.0879`
- `market_context_high->crypto_major_4h` score `2.1663` n `166` status `ready` deltaP `19.4075` edge `0.2078` maxDD `-7.8662`
- `risk_on_high->crypto_major_4h` score `1.7828` n `40` status `ready` deltaP `20.8232` edge `0.0763` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.7828` n `40` status `ready` deltaP `20.8232` edge `0.0763` maxDD `-2.6576`
- `market_context_high->crypto_major_1h` score `1.5993` n `166` status `ready` deltaP `12.5081` edge `0.1041` maxDD `-2.3372`
- `market_context_high->equity_1h` score `1.1607` n `166` status `ready` deltaP `9.8316` edge `0.0876` maxDD `-2.1799`
- `market_context_high->metal_1h` score `1.0534` n `166` status `ready` deltaP `12.3404` edge `0.0649` maxDD `-2.751`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
