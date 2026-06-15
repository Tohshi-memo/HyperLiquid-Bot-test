# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T08:07:28.035522+00:00`
- Price records: `672`
- Market context records: `3973`
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

- `risk_on_high->unknown_4h` score `148.0675` n `40` status `ready` deltaP `0.6402` edge `12.5159` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `148.0675` n `40` status `ready` deltaP `0.6402` edge `12.5159` maxDD `-10.8303`
- `market_context_high->unknown_24h` score `30.6241` n `152` status `ready` deltaP `-6.4419` edge `3.1692` maxDD `-37.9399`
- `market_context_high->unknown_4h` score `19.6139` n `166` status `ready` deltaP `1.5739` edge `2.1649` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `9.1667` n `40` status `ready` deltaP `42.0139` edge `0.4838` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.1667` n `40` status `ready` deltaP `42.0139` edge `0.4838` maxDD `0.0`
- `market_context_high->metal_24h` score `3.7494` n `152` status `ready` deltaP `17.0779` edge `0.3501` maxDD `-9.1203`
- `risk_on_high->equity_4h` score `3.5598` n `40` status `ready` deltaP `37.439` edge `0.0518` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `3.5598` n `40` status `ready` deltaP `37.439` edge `0.0518` maxDD `-0.0458`
- `market_context_high->index_24h` score `3.3685` n `152` status `ready` deltaP `25.9137` edge `0.2219` maxDD `-7.1159`
- `market_context_high->equity_24h` score `2.9641` n `152` status `ready` deltaP `18.9876` edge `0.4234` maxDD `-14.5715`
- `risk_on_high->index_24h` score `2.7621` n `40` status `ready` deltaP `29.8611` edge `0.0311` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.7621` n `40` status `ready` deltaP `29.8611` edge `0.0311` maxDD `0.0`
- `market_context_high->equity_4h` score `2.437` n `166` status `ready` deltaP `20.6619` edge `0.1956` maxDD `-7.0879`
- `market_context_high->crypto_major_4h` score `2.1627` n `166` status `ready` deltaP `19.4075` edge `0.2075` maxDD `-7.8662`
- `risk_on_high->crypto_major_4h` score `1.7792` n `40` status `ready` deltaP `20.8232` edge `0.076` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.7792` n `40` status `ready` deltaP `20.8232` edge `0.076` maxDD `-2.6576`
- `market_context_high->crypto_major_1h` score `1.6041` n `166` status `ready` deltaP `12.5081` edge `0.1045` maxDD `-2.3372`
- `market_context_high->equity_1h` score `1.1607` n `166` status `ready` deltaP `9.8316` edge `0.0876` maxDD `-2.1799`
- `market_context_high->metal_1h` score `1.069` n `166` status `ready` deltaP `12.4901` edge `0.0652` maxDD `-2.751`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
