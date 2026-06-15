# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T13:52:39.468679+00:00`
- Price records: `672`
- Market context records: `3997`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10098`

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

- `risk_on_high->unknown_4h` score `146.968` n `40` status `ready` deltaP `-2.4085` edge `12.4446` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `146.968` n `40` status `ready` deltaP `-2.4085` edge `12.4446` maxDD `-10.8303`
- `market_context_high->unknown_24h` score `43.7452` n `140` status `ready` deltaP `-4.1568` edge `4.075` maxDD `-24.1486`
- `market_context_high->unknown_4h` score `24.3515` n `152` status `ready` deltaP `1.9336` edge `2.5573` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `9.2447` n `40` status `ready` deltaP `42.0139` edge `0.4903` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.2447` n `40` status `ready` deltaP `42.0139` edge `0.4903` maxDD `0.0`
- `risk_on_high->equity_4h` score `4.024` n `40` status `ready` deltaP `38.2012` edge `0.0854` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `4.024` n `40` status `ready` deltaP `38.2012` edge `0.0854` maxDD `-0.0458`
- `market_context_high->index_24h` score `2.9994` n `140` status `ready` deltaP `25.5754` edge `0.1934` maxDD `-7.1159`
- `market_context_high->metal_24h` score `2.9831` n `140` status `ready` deltaP `15.1042` edge `0.2994` maxDD `-9.1203`
- `risk_on_high->index_24h` score `2.7333` n `40` status `ready` deltaP `29.8611` edge `0.0287` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.7333` n `40` status `ready` deltaP `29.8611` edge `0.0287` maxDD `0.0`
- `market_context_high->equity_4h` score `2.1649` n `152` status `ready` deltaP `20.3065` edge `0.1753` maxDD `-7.0879`
- `market_context_high->equity_24h` score `1.959` n `140` status `ready` deltaP `17.0139` edge `0.3528` maxDD `-14.5715`
- `risk_on_high->crypto_major_4h` score `1.677` n `40` status `ready` deltaP `20.6707` edge `0.0685` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.677` n `40` status `ready` deltaP `20.6707` edge `0.0685` maxDD `-2.6576`
- `market_context_high->metal_1h` score `1.2379` n `152` status `ready` deltaP `12.5906` edge `0.0667` maxDD `-1.7983`
- `market_context_high->crypto_major_4h` score `1.2267` n `152` status `ready` deltaP `17.9075` edge `0.1395` maxDD `-7.8662`
- `market_context_high->crypto_major_1h` score `1.1908` n `152` status `ready` deltaP `11.0621` edge `0.0797` maxDD `-2.3372`
- `market_context_high->equity_1h` score `1.0587` n `152` status `ready` deltaP `9.7109` edge `0.0799` maxDD `-2.1799`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
